import json
import math
import re
import sqlite3
import sys
from pathlib import Path

BOOTSTRAP_ROOT = Path(__file__).resolve().parents[2]
if str(BOOTSTRAP_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOTSTRAP_ROOT))

from app.paths import DB_PATH

GUIDE_AUDIO_SLUGS = [
    'forbidden-city',
    'summer-palace',
    'temple-of-heaven',
    'badaling-great-wall',
    'old-summer-palace',
    'canton-tower',
    'baiyun-mountain',
    'chen-clan-academy',
    'yuexiu-park',
    'shamian-island',
    'shanghai-bund',
    'yu-garden',
    'shanghai-museum',
    'shenzhen-bay-park',
    'lianhuashan-park',
    'dapeng-fortress',
    'beihai-park',
    'yonghe-temple',
]

from app.catalog.guide_images import (
    BADALING_IMAGES,
    BAIYUN_MOUNTAIN_IMAGES,
    BEIHAI_PARK_IMAGES,
    CHEN_CLAN_ACADEMY_IMAGES,
    DAPENG_FORTRESS_IMAGES,
    FORBIDDEN_CITY_IMAGES,
    GUANGZHOU_TOWER_IMAGES,
    IMAGE_SOURCES,
    LIANHUASHAN_IMAGES,
    OLD_SUMMER_PALACE_IMAGES,
    SHAMIAN_ISLAND_IMAGES,
    SHANGHAI_BUND_IMAGES,
    SHANGHAI_MUSEUM_IMAGES,
    SHENZHEN_BAY_IMAGES,
    SUMMER_PALACE_IMAGES,
    TEMPLE_OF_HEAVEN_IMAGES,
    YONGHE_TEMPLE_IMAGES,
    YUEXIU_PARK_IMAGES,
    YU_GARDEN_IMAGES,
    GUIDE_GALLERIES,
)


def ensure_schema(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        avatar TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT DEFAULT '',
        photos TEXT,
        location TEXT,
        latitude REAL,
        longitude REAL,
        duration INTEGER,
        people INTEGER,
        author TEXT NOT NULL,
        publish_time TEXT NOT NULL,
        likes INTEGER DEFAULT 0,
        comments INTEGER DEFAULT 0,
        views INTEGER DEFAULT 0
    )''')

    cursor.execute('PRAGMA table_info(posts)')
    post_columns = [column[1] for column in cursor.fetchall()]
    migrations = {
        'content': "ALTER TABLE posts ADD COLUMN content TEXT DEFAULT ''",
        'city': "ALTER TABLE posts ADD COLUMN city TEXT DEFAULT ''",
        'audio_url': "ALTER TABLE posts ADD COLUMN audio_url TEXT DEFAULT ''",
        'audio_url_en': "ALTER TABLE posts ADD COLUMN audio_url_en TEXT DEFAULT ''",
        'guide_items': "ALTER TABLE posts ADD COLUMN guide_items TEXT DEFAULT '[]'",
        'route_map': "ALTER TABLE posts ADD COLUMN route_map TEXT DEFAULT '{}'",
        'tags': "ALTER TABLE posts ADD COLUMN tags TEXT DEFAULT '[]'",
    }

    for column, sql in migrations.items():
        if column not in post_columns:
            cursor.execute(sql)


def guide_item(title, image, latitude, longitude, map_x, map_y, time, text, detail, images=None):
    return {
        'title': title,
        'image': image,
        'images': images or [image],
        'audio': '',
        'latitude': latitude,
        'longitude': longitude,
        'map_x': map_x,
        'map_y': map_y,
        'time': time,
        'text': text,
        'detail': detail,
    }


def detail_copy(opening, route_tip):
    return f'{opening}\n\n{route_tip}'


def haversine_km(lat1, lon1, lat2, lon2):
    radius_km = 6371
    phi1 = math.radians(float(lat1))
    phi2 = math.radians(float(lat2))
    d_phi = math.radians(float(lat2) - float(lat1))
    d_lambda = math.radians(float(lon2) - float(lon1))
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    return radius_km * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def parse_stay_minutes(time_text):
    numbers = [int(value) for value in re.findall(r'\d+', time_text or '')]
    if len(numbers) >= 2:
        return (numbers[0] + numbers[1]) / 2
    if len(numbers) == 1:
        return numbers[0]
    return 20


def route_distance_km(route, guide_items):
    stops = route.get('stops') if isinstance(route, dict) else []
    valid_points = []
    for index in stops or []:
        if not isinstance(index, int) or index < 0 or index >= len(guide_items):
            continue
        item = guide_items[index]
        if item.get('latitude') is None or item.get('longitude') is None:
            continue
        valid_points.append(item)

    distance = 0
    for previous, current in zip(valid_points, valid_points[1:]):
        distance += haversine_km(previous['latitude'], previous['longitude'], current['latitude'], current['longitude'])

    # 景区步行路径通常不是直线，室内展厅/园林路线也会绕行；用温和绕行系数让显示更接近实际体感。
    detour_factor = 1.28 if distance < 5 else 1.15
    return distance * detour_factor


def route_duration_hours(route, guide_items, distance_km):
    stops = route.get('stops') if isinstance(route, dict) else []
    stay_minutes = 0
    valid_stop_count = 0
    for index in stops or []:
        if not isinstance(index, int) or index < 0 or index >= len(guide_items):
            continue
        valid_stop_count += 1
        stay_minutes += parse_stay_minutes(guide_items[index].get('time', ''))

    # 景区内步速按 3.2km/h 估算，比城市通勤步速慢；再加入排队、拍照、找路等缓冲。
    walking_minutes = distance_km / 3.2 * 60 if distance_km else max(8, valid_stop_count * 4)
    buffer_minutes = min(45, max(12, valid_stop_count * 5))
    return (walking_minutes + stay_minutes + buffer_minutes) / 60


def format_duration(hours):
    rounded = max(0.5, round(hours * 2) / 2)
    return f'约 {rounded:.1f}h'


def format_distance(distance_km):
    if distance_km < 0.05:
        return '约 0.1km'
    return f'约 {distance_km:.1f}km'


def finalize_route_map(route_map, guide_items):
    if not route_map or not isinstance(route_map, dict):
        return route_map or {}

    finalized = dict(route_map)
    finalized['subtitle'] = finalized.get('subtitle') or '建议路线，可拖动缩放并点击景点查看详情'
    routes = []
    for route in finalized.get('routes') or []:
        route = dict(route)
        distance_km = route_distance_km(route, guide_items)
        duration_hours = route_duration_hours(route, guide_items, distance_km)
        route['distance'] = format_distance(distance_km)
        route['duration'] = format_duration(duration_hours)
        route['estimate_note'] = '按点位坐标、步行速度、建议停留时间和游览缓冲估算，非官方实测。'
        routes.append(route)
    finalized['routes'] = routes
    return finalized


def max_route_hours(route_map):
    hours = []
    for route in (route_map or {}).get('routes') or []:
        match = re.search(r'(\d+(?:\.\d+)?)', route.get('duration', ''))
        if match:
            hours.append(float(match.group(1)))
    return max(hours) if hours else None


def enrich_guide_item_images(guide_items, cover_image, post_title=''):
    gallery_config = GUIDE_GALLERIES.get(post_title, {})
    if gallery_config:
        for item in guide_items:
            gallery = gallery_config.get(item.get('title'))
            if gallery:
                item['image'] = gallery[0]
                item['images'] = gallery[:3]
        return guide_items

    image_pool = []
    if cover_image:
        image_pool.append(cover_image)
    for item in guide_items:
        for image in item.get('images') or []:
            if image:
                image_pool.append(image)
        image = item.get('image')
        if image:
            image_pool.append(image)

    unique_pool = []
    for image in image_pool:
        if image not in unique_pool:
            unique_pool.append(image)

    for item in guide_items:
        item_images = []
        primary = item.get('image')
        if primary:
            item_images.append(primary)
        for image in item.get('images') or []:
            if image and image not in item_images:
                item_images.append(image)
        for image in unique_pool:
            if len(item_images) >= 3:
                break
            if image and image not in item_images:
                item_images.append(image)
        item['images'] = item_images[:3]
    return guide_items


def normalize_post_tuple(post):
    guide_items = json.loads(post[15] or '[]')
    photos = json.loads(post[2] or '[]')
    cover_image = photos[0] if photos else ''
    guide_items = enrich_guide_item_images(guide_items, cover_image, post[0])
    route_map = json.loads(post[16] or '{}')
    route_map = finalize_route_map(route_map, guide_items)
    duration_hours = max_route_hours(route_map)
    normalized = list(post)
    if duration_hours is not None:
        normalized[6] = max(1, int(math.ceil(duration_hours)))
    normalized[15] = json.dumps(guide_items, ensure_ascii=False)
    normalized[16] = json.dumps(route_map, ensure_ascii=False)
    return tuple(normalized)


def attach_audio_paths(post, slug):
    normalized = list(post)
    guide_items = json.loads(normalized[15] or '[]')
    for index, item in enumerate(guide_items, 1):
        item['audio'] = f'/assets/audio/generated-guides/{slug}/stop-{index:02d}.mp3'
        item['audio_en'] = f'/assets/audio/generated-guides-en/{slug}/stop-{index:02d}.mp3'
    normalized[14] = f'/assets/audio/generated-guides/{slug}/whole-guide.mp3'
    normalized[15] = json.dumps(guide_items, ensure_ascii=False)
    return tuple(normalized), f'/assets/audio/generated-guides-en/{slug}/whole-guide.mp3'


def build_route_map(title, subtitle, map_image, routes):
    return {
        'title': title,
        'subtitle': subtitle,
        'map_image': map_image,
        'routes': routes,
    }


def guangzhou_post(title, content, images, location, latitude, longitude, duration, people, author, likes, comments, views, guide_items, route_map):
    return (
        title,
        content,
        json.dumps([images['cover']], ensure_ascii=False),
        location,
        latitude,
        longitude,
        duration,
        people,
        author,
        '2026-06-05',
        likes,
        comments,
        views,
        '广州市',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def city_guide_post(city, title, content, images, location, latitude, longitude, duration, people, author, likes, comments, views, guide_items, route_map):
    return (
        title,
        content,
        json.dumps([images['cover']], ensure_ascii=False),
        location,
        latitude,
        longitude,
        duration,
        people,
        author,
        '2026-06-05',
        likes,
        comments,
        views,
        city,
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def forbidden_city_post():
    guide_items = [
        {
            'title': '午门',
            'image': FORBIDDEN_CITY_IMAGES['meridian_gate'],
            'images': [
                FORBIDDEN_CITY_IMAGES['meridian_gate'],
                FORBIDDEN_CITY_IMAGES['meridian_gate_2010'],
                FORBIDDEN_CITY_IMAGES['meridian_gate_2015'],
            ],
            'audio': '',
            'latitude': 39.9122,
            'longitude': 116.3907,
            'map_x': 50,
            'map_y': 88,
            'time': '建议停留 15-25 分钟',
            'text': '午门是故宫南端正门，也是整条中轴线导览的正式起点。进入前建议先观察“凹”字形城台、两侧阙楼和门洞的层次，这里会把游客从城市广场带入宫城秩序。午门适合用来建立游览方向感：南北轴线、层层递进的门禁空间，以及皇家礼仪带来的庄重感都从这里开始。',
            'detail': '午门位于紫禁城南端，是进入故宫时最有仪式感的一道门。站在午门前，可以先看它“凹”字形的城台和两侧阙楼：这种围合感会让人明显感到自己正从城市空间走入宫城秩序之中。明清时期，这里不仅是皇城正门，也承载过颁布诏令、举行重要仪式等功能。\n\n参观时建议在午门外停留几分钟，站到中轴线位置回望端门方向，再向北看午门城楼的层层屋檐。穿过门洞时，空间会从开阔广场变成较暗的通道，出来后又进入太和门前的院落，这种明暗和尺度变化正是故宫“层层递进”的第一段体验。不要急着向前走，先把太和门广场、金水河和桥梁一起看完，再继续进入外朝核心区域。'
        },
        {
            'title': '太和殿',
            'image': FORBIDDEN_CITY_IMAGES['hall_of_supreme_harmony'],
            'images': [
                FORBIDDEN_CITY_IMAGES['hall_of_supreme_harmony'],
                FORBIDDEN_CITY_IMAGES['hall_of_supreme_harmony_2010'],
            ],
            'audio': '',
            'latitude': 39.9142,
            'longitude': 116.3906,
            'map_x': 50,
            'map_y': 62,
            'time': '建议停留 25-40 分钟',
            'text': '太和殿是外朝核心建筑，也是故宫中轴线上最适合讲解皇权礼制的地点。这里的三层汉白玉台基、开阔广场、屋顶等级和殿前陈设共同构成典礼舞台。参观时不要只看大殿正面，也要留意台基、御路、铜龟铜鹤和排水螭首这些细节。',
            'detail': '太和殿是故宫外朝的核心，也是整条中轴线上最震撼的建筑之一。它坐落在三层汉白玉台基之上，前方广场非常开阔，站在远处就能感受到大殿被刻意抬高后的庄严感。明清时期，登基、大婚、册立、元旦朝贺等重大典礼都与这里相关。\n\n来到太和殿，建议先从广场远处看整体，再慢慢走近看细节。三层台基、中央御路、铜龟铜鹤、殿前螭首和屋脊上的脊兽，都在表达等级、礼制和吉祥寓意。这里不是日常办公的地方，而是皇家权力被建筑放大成可见景观的空间。看完太和殿后，再回头望一眼南侧院落，会更容易理解故宫为什么要用一条中轴线把门、院、殿一层层串联起来。'
        },
        {
            'title': '乾清宫',
            'image': FORBIDDEN_CITY_IMAGES['palace_of_heavenly_purity'],
            'images': [
                FORBIDDEN_CITY_IMAGES['palace_of_heavenly_purity'],
                FORBIDDEN_CITY_IMAGES['palace_of_heavenly_purity_exterior'],
            ],
            'audio': '',
            'latitude': 39.9180,
            'longitude': 116.3907,
            'map_x': 50,
            'map_y': 35,
            'time': '建议停留 20-35 分钟',
            'text': '乾清宫位于内廷前部，是从外朝典礼转入宫廷日常的重要节点。这里可以讲皇帝起居、召见臣工、处理政务和清代继承制度。相比太和殿的宏大广场，乾清宫的重点更接近权力如何在日常空间中运转。',
            'detail': '乾清宫位于故宫内廷前部，和太和殿的开阔典礼空间不同，这里更接近皇帝日常起居和处理政务的区域。走到这里时，参观节奏会从“看宏大的礼制建筑”转向“看宫廷生活如何运转”。殿内“正大光明”匾额很有名，也与清代秘密立储制度相关。\n\n参观乾清宫时，可以把它看作外朝和内廷之间的重要转换点。南侧是太和殿、中和殿、保和殿等面向典礼和朝会的空间；继续向北，则逐渐进入皇帝、后妃和宫廷日常生活相关的区域。这里的院落尺度比外朝更紧凑，建筑之间的关系也更贴近日常管理。停留时可以注意殿前空间、匾额位置和周边通道，它们会帮助你理解故宫不仅是宏伟建筑群，也是一个规则严密的宫廷生活系统。'
        },
        {
            'title': '珍宝馆',
            'image': FORBIDDEN_CITY_IMAGES['treasure_gallery'],
            'images': [
                FORBIDDEN_CITY_IMAGES['treasure_gallery'],
                FORBIDDEN_CITY_IMAGES['treasure_qing_jade'],
            ],
            'audio': '',
            'latitude': 39.9188,
            'longitude': 116.3938,
            'map_x': 72,
            'map_y': 32,
            'time': '建议停留 40-60 分钟',
            'text': '珍宝馆适合从宏大的宫殿空间转向具体器物，通过金银器、玉器、珐琅和陈设品理解宫廷审美。这里的导览重点不是快速打卡，而是观察材质、工艺、纹饰和用途。建议单独预留时间，把展品和宫廷生活、礼仪制度联系起来看。',
            'detail': '珍宝馆适合放慢脚步细看。这里展示了故宫院藏中的金银器、玉器、珐琅器和陈设器等宫廷珍品，和中轴线上的大殿不同，它的精彩不在“宏大”，而在材质、工艺和细节。每一件器物都能看到宫廷生活中的审美、礼仪和等级观念。\n\n参观时可以从两个角度看：一是看工艺，比如玉器的雕琢、金银器的纹饰、珐琅器的色彩；二是看用途，想象这些器物曾经摆放在怎样的宫廷空间里，用于日常陈设、礼仪活动还是赏玩收藏。珍宝馆不建议匆匆路过，最好预留一段单独时间。看完宏大的宫殿后再看这些器物，会更容易感受到故宫不仅有建筑秩序，也有细密精巧的宫廷生活。'
        },
        {
            'title': '角楼',
            'image': FORBIDDEN_CITY_IMAGES['corner_tower'],
            'images': [
                FORBIDDEN_CITY_IMAGES['corner_tower'],
                FORBIDDEN_CITY_IMAGES['corner_tower_night'],
            ],
            'audio': '',
            'latitude': 39.9215,
            'longitude': 116.3855,
            'map_x': 22,
            'map_y': 14,
            'time': '建议停留 20-35 分钟',
            'text': '角楼与护城河构成故宫外缘最具辨识度的景观，适合作为整条路线的收束。这里既是拍摄点，也是理解紫禁城边界感的好位置。城墙、护城河、角楼和城市道路共同说明，故宫不仅有内部秩序，也有清晰的外部边界。',
            'detail': '角楼位于故宫城墙四角，是故宫最经典的外景之一。红墙、金色琉璃瓦、复杂屋顶和护城河倒影组合在一起，很适合拍照，也很适合作为离开故宫后的收束点。站在护城河边看角楼，会明显感受到宫城和城市之间的边界。\n\n这里最值得看的，是城墙、护城河和角楼如何共同划定紫禁城的范围。白天可以看屋檐层次和城墙转角，傍晚则适合看水面倒影和光线变化。如果当天已经从午门进入、沿中轴线看过大殿和内廷，最后来到角楼回望，会更容易把“门、殿、城墙、护城河”这些元素串成一个完整的宫城印象。'
        },
    ]

    route_map = build_route_map('故宫路线选择', '宫城中轴与展馆导览', FORBIDDEN_CITY_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '中轴经典线', 'duration': '约 2.5h', 'distance': '约 1.6km', 'description': '午门、太和殿、乾清宫和角楼串联，适合第一次参观故宫。', 'stops': [0, 1, 2, 4]},
        {'id': 'treasure', 'title': '中轴加珍宝馆线', 'duration': '约 3.5h', 'distance': '约 2.0km', 'description': '在中轴线基础上加入珍宝馆，兼顾建筑秩序和宫廷器物。', 'stops': [0, 1, 2, 3, 4]},
        {'id': 'short', 'title': '快速核心线', 'duration': '约 1.8h', 'distance': '约 1.1km', 'description': '重点看午门、太和殿和乾清宫，适合时间有限的游客。', 'stops': [0, 1, 2]},
    ])

    content = (
        '这是一条面向第一次参观故宫博物院游客的正式语音导览路线。建议从午门进入，先建立中轴线方向感，'
        '再依次参观太和殿、乾清宫，最后根据体力和预约情况前往珍宝馆，并以角楼和护城河景观作为收束。'
        '路线会把礼制建筑、宫廷生活、院藏器物和城市景观串联起来，不只停留在“看大殿”和“拍照片”，'
        '而是帮助游客理解故宫为什么这样布局、不同空间承担什么功能，以及具体展品如何回应明清宫廷制度。'
        '如果时间充裕，可以在每个导览点停留十到二十分钟；如果行程较紧，也可以优先完成午门、太和殿、乾清宫三处核心节点。'
    )

    return (
        '故宫博物院：沿中轴线走进六百年宫城',
        content,
        json.dumps([FORBIDDEN_CITY_IMAGES['cover'], FORBIDDEN_CITY_IMAGES['meridian_gate']], ensure_ascii=False),
        '北京市东城区景山前街4号',
        39.9163,
        116.3972,
        1,
        3000,
        'palace_guide',
        '2026-06-05T09:00:00Z',
        986,
        42,
        8600,
        '北京',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def summer_palace_post():
    guide_items = [
        {
            'title': '东宫门',
            'image': SUMMER_PALACE_IMAGES['east_palace_gate'],
            'images': [SUMMER_PALACE_IMAGES['east_palace_gate']],
            'audio': '',
            'latitude': 39.9997,
            'longitude': 116.2755,
            'map_x': 70,
            'map_y': 31,
            'time': '建议停留 10-15 分钟',
            'text': '东宫门是颐和园最常用的入口，适合作为路线起点。进入后先建立方向感：万寿山在北、昆明湖在南，宫廷建筑与园林山水会从这里逐步展开。',
            'detail': '东宫门是进入颐和园最常用的入口之一。走到这里时，可以先把它当作整趟游览的起点来建立方向感：北面是万寿山，南面是昆明湖，向西会进入长廊、佛香阁、石舫等核心景观。这里不只是检票口，而是从城市道路进入皇家园林的转换点。\n\n进门后不要急着赶路，可以先看门前空间和匾额位置，再确认自己想走的路线。时间有限时，适合从东宫门进入后直奔长廊和佛香阁；时间充裕时，可以把东部宫廷区、湖区和十七孔桥一起串联。颐和园的精彩来自山、水、殿、廊、桥共同构成的空间，东宫门正是这条游览线的开场。'
        },
        {
            'title': '仁寿殿',
            'image': SUMMER_PALACE_IMAGES['renshou_hall'],
            'images': [SUMMER_PALACE_IMAGES['renshou_hall']],
            'audio': '',
            'latitude': 39.9994,
            'longitude': 116.2741,
            'map_x': 64,
            'map_y': 34,
            'time': '建议停留 15-20 分钟',
            'text': '仁寿殿是颐和园前朝区的重要建筑，适合讲清代皇室在园林中处理政务、接见臣工和举行礼仪活动的场景。',
            'detail': '仁寿殿位于东宫门内，是颐和园中带有明显“宫廷办公”属性的建筑。很多游客来到颐和园会直接想到湖山风景，但仁寿殿提醒人们：这里既是游赏园林，也是晚清皇室处理政务、接见臣工和举行仪式的空间。\n\n参观时可以先看院落尺度、殿前陈设和建筑位置。这里的氛围比湖边景观更庄重，与后面的长廊、昆明湖、佛香阁形成明显对比：仁寿殿强调礼制和秩序，后面的湖山区域则更强调游赏和休憩。建议在这里停留片刻，再继续向西进入园林部分，这样会更清楚地感受到颐和园功能的变化。'
        },
        {
            'title': '德和园',
            'image': SUMMER_PALACE_IMAGES['dehe_garden'],
            'images': [SUMMER_PALACE_IMAGES['dehe_garden'], SUMMER_PALACE_IMAGES['dehe_garden_detail']],
            'audio': '',
            'latitude': 39.9992,
            'longitude': 116.2726,
            'map_x': 58,
            'map_y': 33,
            'time': '建议停留 15-25 分钟',
            'text': '德和园以戏楼空间闻名，适合讲晚清宫廷娱乐、庆典演出和皇家园林中的生活场景。',
            'detail': '德和园是颐和园中了解晚清宫廷娱乐生活的重要地点。这里以戏楼空间闻名，院落、看台和建筑组合保留了皇家观演活动的场景感。和仁寿殿的政务礼仪氛围不同，德和园更像是进入了皇室生活中休闲、观演和庆典的一面。\n\n来到这里，可以想象当年戏曲演出、祝寿活动和宫廷观赏的场面。参观时不必只看单座建筑，而要把院落关系一起看：人从哪里进、在哪里看、戏楼如何成为视线中心。这样会发现颐和园不只是湖山风景，也包含政务、居住、娱乐和游赏等多种皇家生活功能。'
        },
        {
            'title': '长廊',
            'image': SUMMER_PALACE_IMAGES['long_gallery'],
            'images': [SUMMER_PALACE_IMAGES['long_gallery'], SUMMER_PALACE_IMAGES['long_corridor']],
            'audio': '',
            'latitude': 39.9989,
            'longitude': 116.2699,
            'map_x': 42,
            'map_y': 43,
            'time': '建议停留 20-30 分钟',
            'text': '长廊沿昆明湖北岸展开，是颐和园最适合慢走的线性空间。这里可以看彩画、湖景和万寿山前山建筑，适合把“边走边讲”的语音导览放在这里。',
            'detail': '长廊位于万寿山南麓、昆明湖北岸，是颐和园最适合慢走的地方之一。行走时，一侧能看到昆明湖水面，另一侧能望见万寿山和前山建筑群。长廊本身也很值得细看，梁枋上的彩画内容丰富，有山水、人物、历史故事和文学题材。\n\n参观长廊时，不建议只把它当作通道快速穿过。可以每隔一段停下来看看彩画，再转身望向昆明湖，感受“人在廊中走，景在两侧展开”的节奏。长廊也是路线分流点：向北可以上万寿山看佛香阁，向西可以去石舫，向东南则能转向昆明湖和十七孔桥。这里适合作为颐和园游览中最舒缓的一段。'
        },
        {
            'title': '排云殿',
            'image': SUMMER_PALACE_IMAGES['paiyun_dian'],
            'images': [SUMMER_PALACE_IMAGES['paiyun_dian']],
            'audio': '',
            'latitude': 39.9995,
            'longitude': 116.2682,
            'map_x': 41,
            'map_y': 34,
            'time': '建议停留 15-20 分钟',
            'text': '排云殿位于万寿山前山轴线上，是通往佛香阁前的重要礼仪空间，适合讲祝寿建筑群的层层递进。',
            'detail': '排云殿位于万寿山前山中轴线上，是从湖岸走向佛香阁时会经过的重要建筑。它与牌楼、台阶和上方的佛香阁一起形成一条明显的上升轴线，把人的视线从昆明湖边引向万寿山高处。\n\n参观时可以留意脚下路线的变化：从湖边到排云殿，再继续向上，空间一层层抬升，视野也逐步打开。走到排云殿附近时，建议回头看一眼昆明湖，你会发现湖面、长廊和山体建筑之间的关系变得更清楚。这里最适合感受颐和园“借山理水”的层次。'
        },
        {
            'title': '佛香阁',
            'image': SUMMER_PALACE_IMAGES['tower_buddhist_incense'],
            'images': [SUMMER_PALACE_IMAGES['tower_buddhist_incense']],
            'audio': '',
            'latitude': 39.9998,
            'longitude': 116.2676,
            'map_x': 40,
            'map_y': 28,
            'time': '建议停留 25-40 分钟',
            'text': '佛香阁位于万寿山前山中轴，是颐和园最醒目的制高点。来到这里可以俯瞰昆明湖，也能看清万寿山前山建筑层层抬升的格局。',
            'detail': '佛香阁位于万寿山前山，是颐和园最醒目的标志性建筑之一。无论从昆明湖、长廊还是远处堤岸回望，视线往往都会被它吸引。它不是孤立的一座阁楼，而是和排云殿、万寿山、昆明湖共同组成颐和园最有代表性的湖山景观。\n\n如果体力允许，建议至少走到佛香阁下方的平台区域。向南看，昆明湖会在眼前展开，十七孔桥、南湖岛和堤岸景观都能纳入视线；向北看，山体和建筑层层抬升。这里适合停留久一点，因为站在不同高度回看湖面，颐和园的山水格局会变得非常直观。'
        },
        {
            'title': '智慧海',
            'image': SUMMER_PALACE_IMAGES['sea_of_wisdom'],
            'images': [SUMMER_PALACE_IMAGES['sea_of_wisdom'], SUMMER_PALACE_IMAGES['sea_of_wisdom_detail']],
            'audio': '',
            'latitude': 40.0008,
            'longitude': 116.2675,
            'map_x': 39,
            'map_y': 20,
            'time': '建议停留 15-25 分钟',
            'text': '智慧海位于万寿山高处，是佛香阁之后继续上行的节点，适合讲山顶建筑、宗教意涵和俯瞰视野。',
            'detail': '智慧海位于万寿山较高处，是佛香阁之后继续向上的重要节点。和湖边的开阔、长廊的舒缓不同，这里更能感受到登高之后的视野变化。走到这里时，万寿山与昆明湖之间的高差关系会变得更加明显。\n\n如果体力充足，可以把智慧海加入登山段。这里适合慢一点走，边休息边回看湖面和前山建筑群。颐和园的空间层次并不是平铺展开的，而是借助山体高度不断变化：湖面提供开阔背景，山体提供高差，建筑则把视线和路线一步步组织起来。'
        },
        {
            'title': '苏州街',
            'image': SUMMER_PALACE_IMAGES['suzhou_street'],
            'images': [SUMMER_PALACE_IMAGES['suzhou_street'], SUMMER_PALACE_IMAGES['suzhou_street_detail']],
            'audio': '',
            'latitude': 40.0020,
            'longitude': 116.2670,
            'map_x': 36,
            'map_y': 14,
            'time': '建议停留 25-35 分钟',
            'text': '苏州街位于后湖区域，模拟江南水街风貌，是颐和园中很有生活气息和商业想象的景观空间。',
            'detail': '苏州街位于万寿山后湖一带，是颐和园中带有江南水街意趣的区域。这里和前山的佛香阁、排云殿气质不同，更像一段临水街巷：有水道、桥梁、店铺和岸边建筑，氛围更轻松，也更有生活感。\n\n如果时间充裕，苏州街很适合加入深度游路线。它不是普通商业街，而是皇家园林中对江南水乡景观的再创造。走在这里，可以把它和昆明湖、长廊对照着看：前者像市井水巷，后者像皇家山水画卷。半日游时间紧张时可以不深入，但如果想看到颐和园更丰富的一面，这里值得绕行。'
        },
        {
            'title': '石舫',
            'image': SUMMER_PALACE_IMAGES['marble_boat'],
            'images': [SUMMER_PALACE_IMAGES['marble_boat'], SUMMER_PALACE_IMAGES['marble_boat_detail']],
            'audio': '',
            'latitude': 40.0004,
            'longitude': 116.2637,
            'map_x': 25,
            'map_y': 42,
            'time': '建议停留 15-25 分钟',
            'text': '石舫位于昆明湖西北岸，是颐和园中很有辨识度的湖边建筑。它适合讲晚清修园、湖岸游赏和“舟”这一意象在园林中的象征意义。',
            'detail': '石舫又称清晏舫，位于昆明湖西北岸，是颐和园中很容易让人记住的景点。它看起来像一艘船，却固定在岸边，兼具建筑、装饰和观景功能。走到这里时，视野会从长廊和山体建筑转向湖岸空间，湖面也显得更加开阔。\n\n参观石舫时，可以先看它的“船形”外观，再想一想为什么皇家园林会建一艘不能航行的船。它既回应昆明湖的水景，也提供了停留、眺望和拍照的位置。轻松拍照线里，石舫是很好的湖岸节点；湖山完整线里，它则和佛香阁形成山上山下、建筑与水面的对照。'
        },
        {
            'title': '昆明湖',
            'image': SUMMER_PALACE_IMAGES['kunming_lake_wide'],
            'images': [SUMMER_PALACE_IMAGES['kunming_lake_wide']],
            'audio': '',
            'latitude': 39.9948,
            'longitude': 116.2689,
            'map_x': 45,
            'map_y': 61,
            'time': '建议停留 20-40 分钟',
            'text': '昆明湖是颐和园最大水面，也是理解整个园林格局的关键。湖面把万寿山、长堤、岛屿和桥梁组织成完整景观。',
            'detail': '昆明湖是颐和园的主体水面，也是整个园林最重要的视觉核心。无论你从长廊、佛香阁、石舫还是十七孔桥观看，最后都会被湖面带来的开阔感吸引。它不仅适合观景和乘船，也把万寿山、长堤、岛屿和桥梁组织成完整的山水格局。\n\n来到湖边时，可以放慢脚步，先看远处的万寿山和佛香阁，再看湖面、堤岸和桥的关系。颐和园最核心的结构就是“一山一水”：万寿山提供高度和背景，昆明湖提供开阔和倒影。前半段看过入口、宫廷区和山体建筑后，再来到昆明湖边，会明显感到空间突然打开。'
        },
        {
            'title': '南湖岛',
            'image': SUMMER_PALACE_IMAGES['nanhu_island'],
            'images': [SUMMER_PALACE_IMAGES['nanhu_island']],
            'audio': '',
            'latitude': 39.9914,
            'longitude': 116.2731,
            'map_x': 64,
            'map_y': 70,
            'time': '建议停留 15-25 分钟',
            'text': '南湖岛位于昆明湖东南部，通过十七孔桥与东堤相连，是观看湖面、远山和桥梁关系的重要节点。',
            'detail': '南湖岛位于昆明湖东南部，通过十七孔桥与东堤相连。走到这里，会从岸边进入湖中岛屿，观看万寿山和湖面的角度也随之改变。这个“从岸到岛”的移动过程，是颐和园湖区体验中很有意思的一段。\n\n在南湖岛上，可以回看十七孔桥，也可以远望万寿山和佛香阁。和在长廊看湖不同，这里是从湖中回望北岸，视线更开阔，也更容易理解颐和园的多点互看关系。建议在岛上停留一会儿，不只拍桥，也看远处山体、湖面和岸线如何连成一幅完整景观。'
        },
        {
            'title': '十七孔桥',
            'image': SUMMER_PALACE_IMAGES['seventeen_arch_bridge'],
            'images': [SUMMER_PALACE_IMAGES['seventeen_arch_bridge']],
            'audio': '',
            'latitude': 39.9915,
            'longitude': 116.2754,
            'map_x': 72,
            'map_y': 66,
            'time': '建议停留 20-30 分钟',
            'text': '十七孔桥连接昆明湖东堤与南湖岛，是颐和园湖区最重要的景观桥。这里适合安排在路线后段，用开阔湖景作为收束。',
            'detail': '十七孔桥位于昆明湖东南部，是连接东堤与南湖岛的重要桥梁。远看桥身像一道舒展的弧线，把湖面、岛屿和远处万寿山景观连接起来。这里是颐和园湖区最适合拍远景和夕照的位置之一。\n\n走上桥时，可以留意桥洞的节奏、栏杆上的石狮，以及桥两侧不断变化的湖面视线。下午光线好的时候，桥身、湖面和远山会形成很清楚的层次。把十七孔桥放在路线后段很合适：从东宫门、长廊、佛香阁或石舫一路走来，最后在这里看到最开阔的湖区景观，会有一种从宫廷建筑走向山水园林的完整收束感。'
        },
        {
            'title': '铜牛',
            'image': SUMMER_PALACE_IMAGES['bronze_ox'],
            'images': [SUMMER_PALACE_IMAGES['bronze_ox']],
            'audio': '',
            'latitude': 39.9926,
            'longitude': 116.2768,
            'map_x': 78,
            'map_y': 59,
            'time': '建议停留 10-15 分钟',
            'text': '铜牛位于昆明湖东堤附近，是湖区很有故事性的陈设点，适合讲镇水寓意和皇家园林中的象征物。',
            'detail': '铜牛位于昆明湖东堤附近，是湖区一处很有故事感的小景点。它体量不算大，但放在开阔湖面旁很醒目，也让湖区景观多了一层吉祥和镇水的象征意味。经过十七孔桥或东堤时，值得在这里短暂停留。\n\n看铜牛时，不要只把它当作一件孤立的雕塑。把它和身后的昆明湖、旁边的堤岸、远处的桥一起看，会发现颐和园的湖区并不只是自然风景，也有许多被精心安放的文化符号。宏大的湖山景观之外，这类小节点能让游览多一些细节和记忆点。'
        },
        {
            'title': '文昌院',
            'image': SUMMER_PALACE_IMAGES['wenchang_pavilion'],
            'images': [SUMMER_PALACE_IMAGES['wenchang_pavilion']],
            'audio': '',
            'latitude': 39.9962,
            'longitude': 116.2784,
            'map_x': 80,
            'map_y': 43,
            'time': '建议停留 20-30 分钟',
            'text': '文昌院位于东部区域，适合对文物、陈设和历史展览感兴趣的游客补充参观。',
            'detail': '文昌院位于颐和园东部区域，适合在湖山游览之外补充观看文物和展陈。相比长廊、佛香阁、昆明湖这些以空间景观取胜的地点，文昌院更适合细看展品，了解颐和园相关历史和宫廷文化。\n\n如果你喜欢文物、器物和展览，可以把文昌院安排在返程前。完成十七孔桥、铜牛等湖区节点后，如果还有时间，回到东部区域参观文昌院，会让整条路线从入口宫廷区、山水景观、湖区桥岛，最后回到文物展示，形成一个更完整的参观闭环。'
        },
    ]

    route_map = {
        'title': '颐和园路线选择',
        'subtitle': '拖动地图查看区域，点击景点名称进入详情，可放大缩小',
        'map_image': SUMMER_PALACE_IMAGES['overview_map'],
        'default_route': 'lake_hill',
        'routes': [
            {
                'id': 'classic',
                'title': '经典半日线',
                'duration': '3.0h',
                'distance': '2.8km',
                'description': '东宫门进入，经仁寿殿、德和园、长廊、排云殿到佛香阁，再从昆明湖边收束。',
                'stops': [0, 1, 2, 3, 4, 5, 9],
            },
            {
                'id': 'lake_hill',
                'title': '湖山完整线',
                'duration': '5.5h',
                'distance': '5.2km',
                'description': '覆盖东部宫廷区、万寿山前山、苏州街、石舫、昆明湖、南湖岛和十七孔桥。',
                'stops': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            },
            {
                'id': 'photo',
                'title': '轻松拍照线',
                'duration': '2.5h',
                'distance': '2.4km',
                'description': '少爬山，重点走长廊、石舫、昆明湖、十七孔桥和铜牛，适合亲子、长辈和拍照行程。',
                'stops': [0, 3, 8, 9, 11, 12, 13],
            },
        ],
    }

    content = (
        '这是一条北京颐和园互动路线导览示范帖。颐和园以万寿山和昆明湖为骨架，兼具皇家宫苑、山水园林、'
        '湖岸游赏和历史建筑等多重体验。建议先根据体力和时间选择路线：半日游客可走经典线，想完整体验湖山格局可走完整线，'
        '以拍照和轻松游览为主则选择轻松拍照线。正文下方的俯视路线图可以切换三种路线，点击地图上的景点图标即可进入详细介绍，'
        '并继续使用播放语音和导航过去功能。'
    )

    return (
        '颐和园：沿湖山路线走进皇家园林',
        content,
        json.dumps([SUMMER_PALACE_IMAGES['cover'], SUMMER_PALACE_IMAGES['tower_buddhist_incense']], ensure_ascii=False),
        '北京市海淀区新建宫门路19号',
        39.9999,
        116.2755,
        4,
        2600,
        'palace_guide',
        '2026-06-05T10:00:00Z',
        756,
        28,
        6200,
        '北京',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def temple_of_heaven_post():
    guide_items = [
        guide_item(
            '祈年殿',
            TEMPLE_OF_HEAVEN_IMAGES['hall_of_prayer'],
            39.8822,
            116.4066,
            50,
            17,
            '建议停留 25-35 分钟',
            '祈年殿是天坛最具代表性的建筑，适合作为整条路线的视觉高潮。站在殿前，可以同时观察圆形殿身、三重蓝色琉璃瓦和层层抬升的台基。',
            detail_copy(
                '祈年殿是天坛最容易被游客记住的建筑，也是理解明清祭天文化的核心地点之一。它的圆形殿身、蓝色琉璃瓦和高起的圆形台基，都在强调“天”的意象。走到殿前时，建议先退到广场边缘看整体，再慢慢靠近看屋顶层次、殿身比例和台基栏板。',
                '参观时不要只拍正面照片，可以绕着外圈走一小段，从不同方向观察它与周围柏树、院墙和开阔地面的关系。祈年殿最适合安排在路线前段，因为它会先建立天坛“圆形建筑、开阔坛域、庄重轴线”的整体印象，之后再看皇穹宇、圜丘坛时会更容易理解。'
            ),
            [TEMPLE_OF_HEAVEN_IMAGES['hall_of_prayer'], TEMPLE_OF_HEAVEN_IMAGES['cover']],
        ),
        guide_item(
            '皇乾殿',
            TEMPLE_OF_HEAVEN_IMAGES['imperial_hall_of_heaven'],
            39.8835,
            116.4066,
            50,
            10,
            '建议停留 10-15 分钟',
            '皇乾殿位于祈年殿北侧，是祭祀相关牌位供奉空间。这里适合在看完祈年殿后补充理解建筑群的完整功能。',
            detail_copy(
                '皇乾殿位于祈年殿院落北侧，很多游客会因为祈年殿太醒目而忽略它。实际上，它与祈年殿共同组成祈谷坛区域的一部分，帮助游客理解这里不是单一“打卡建筑”，而是一组围绕祭祀活动安排的建筑群。',
                '走到皇乾殿时，可以回头看祈年殿，再观察两者之间的轴线关系。这里停留时间不必太久，但很适合用来整理方向：南侧是刚刚看过的祈年殿，继续向南会沿丹陛桥前往皇穹宇和圜丘坛，路线会从祈谷区域逐渐进入更开阔的祭天空间。'
            ),
        ),
        guide_item(
            '丹陛桥',
            TEMPLE_OF_HEAVEN_IMAGES['danbi_bridge'],
            39.8793,
            116.4066,
            50,
            31,
            '建议停留 15-20 分钟',
            '丹陛桥连接祈谷坛和圜丘坛区域，是天坛路线中最重要的步行轴线。沿桥南行，可以感受到祭祀空间被拉长后的仪式感。',
            detail_copy(
                '丹陛桥并不是普通意义上的桥，而是一条连接祈年殿区域与圜丘坛区域的高起甬道。走在这里，周围空间会变得非常开阔，游客能清楚感到自己正沿着一条被强调出来的南北轴线移动。',
                '建议慢慢走完这一段，不要急着直接去下一个景点。你可以边走边回望祈年殿，再向南看皇穹宇和圜丘坛方向。天坛的游览体验很大一部分来自这种“在路上”的仪式感：建筑之间不是简单相邻，而是通过长距离轴线把人的行走节奏组织起来。'
            ),
        ),
        guide_item(
            '皇穹宇',
            TEMPLE_OF_HEAVEN_IMAGES['imperial_vault'],
            39.8747,
            116.4066,
            50,
            47,
            '建议停留 20-30 分钟',
            '皇穹宇是圜丘坛北侧的重要建筑，圆形院墙和殿宇组合很适合观察天坛建筑对“圆”的强调。',
            detail_copy(
                '皇穹宇位于圜丘坛北侧，建筑尺度比祈年殿小，但空间非常精致。走进院落后，可以明显看到圆形院墙把建筑包裹起来，形成一种收束而安静的氛围。这里适合从“空间声音”和“建筑形态”两个角度观看。',
                '参观时建议先站在院落中部看皇穹宇，再沿着院墙慢慢走。这里会连接到回音壁、三音石等很受游客欢迎的小景点，但不要只把它们当作趣味体验。圆墙、中心建筑和脚下石面共同构成了一个围绕祭天礼仪展开的空间。'
            ),
        ),
        guide_item(
            '回音壁',
            TEMPLE_OF_HEAVEN_IMAGES['echo_wall'],
            39.8746,
            116.4063,
            42,
            47,
            '建议停留 10-20 分钟',
            '回音壁围绕皇穹宇院落展开，是天坛最有互动感的地点之一。游客可以在不影响他人的前提下体验声音反射。',
            detail_copy(
                '回音壁是皇穹宇院落中最容易吸引游客尝试互动的地方。它利用圆形墙体形成声音反射效果，站在合适位置轻声说话，另一侧有机会听到声音传来。实际体验会受人流、噪声和站位影响，不一定每次都非常明显。',
                '来到这里时，建议先观察墙体弧度，再选择人少的位置体验。即使没有听到特别清楚的回声，也可以把它当作理解天坛空间设计的入口：声音、圆形墙面和中心建筑在这里形成了很特别的参观记忆点。'
            ),
        ),
        guide_item(
            '三音石',
            TEMPLE_OF_HEAVEN_IMAGES['three_echo_stones'],
            39.8738,
            116.4066,
            50,
            52,
            '建议停留 10-15 分钟',
            '三音石位于皇穹宇前方，是游客体验声音反射的经典点位。这里适合短暂停留，感受天坛空间中的声学趣味。',
            detail_copy(
                '三音石位于皇穹宇前方，是天坛中另一个与声音有关的参观点。站在特定石面上发声，回响效果会让游客直观感受到空间和声音之间的关系。这里面积不大，但很适合亲子和第一次参观的游客停留。',
                '参观时注意不要长时间占住点位，也不要大声喧哗影响其他人。三音石的有趣之处不只在“听到几声回音”，更在于它让人意识到：天坛的空间并不是只供观看，人的行走、停留和声音都会参与到体验里。'
            ),
        ),
        guide_item(
            '圜丘坛',
            TEMPLE_OF_HEAVEN_IMAGES['circular_mound_altar'],
            39.8712,
            116.4066,
            50,
            69,
            '建议停留 25-35 分钟',
            '圜丘坛是祭天仪式的重要坛台，开阔、简洁、层层上升。登坛远望时，可以感受到天坛空间最纯粹的礼制气质。',
            detail_copy(
                '圜丘坛是天坛南部最重要的祭天坛台。和祈年殿的高大建筑不同，圜丘坛更强调开阔、简洁和层层上升的空间。登上坛台时，四周视野打开，游客会更直接地感受到古代祭天场所追求的庄重与秩序。',
                '建议从台阶下方先看整体，再登上不同层级观察栏板、石面和中心位置。这里没有复杂装饰，却非常适合作为天坛路线的收束点。走完祈年殿、丹陛桥、皇穹宇之后来到圜丘坛，会发现整条路线从建筑之美逐渐过渡到礼制空间本身。'
            ),
        ),
        guide_item(
            '斋宫',
            TEMPLE_OF_HEAVEN_IMAGES['palace_of_abstinence'],
            39.8767,
            116.3994,
            24,
            44,
            '建议停留 20-30 分钟',
            '斋宫位于主轴线西侧，是皇帝祭祀前斋戒停留的区域。这里适合想看天坛更完整功能的游客绕行。',
            detail_copy(
                '斋宫位于天坛主轴线西侧，是皇帝祭祀前斋戒居住和准备的地方。它不像祈年殿那样醒目，却能帮助游客理解祭天并不是某一刻的仪式，而是一整套准备、行进和祭祀流程。',
                '如果时间充裕，建议从主轴线绕到斋宫看一看。这里的院落氛围比中轴线安静，建筑也更接近日常停留空间。参观后再回到主线，会更清楚地意识到天坛既有公开庄严的坛庙空间，也有为仪式服务的配套区域。'
            ),
        ),
        guide_item(
            '神乐署',
            TEMPLE_OF_HEAVEN_IMAGES['divine_music_administration'],
            39.8735,
            116.3990,
            24,
            56,
            '建议停留 20-30 分钟',
            '神乐署与祭祀音乐相关，适合对礼乐制度和古代仪式音乐感兴趣的游客补充参观。',
            detail_copy(
                '神乐署与祭祀音乐和礼乐活动相关，是天坛中很适合补充文化背景的地点。来到这里，游客可以把注意力从建筑形态转向仪式中的声音、队列和礼乐安排，理解祭天活动为什么需要如此复杂的配套系统。',
                '参观时可以把神乐署和皇穹宇、回音壁、三音石联系起来看：一个展示礼乐制度，一个让游客直接感受声音在空间中的变化。对于喜欢历史文化的游客，这里能让天坛不只是一组漂亮建筑，而是一套完整礼制生活的遗存。'
            ),
        ),
        guide_item(
            '七星石',
            TEMPLE_OF_HEAVEN_IMAGES['seven_star_stones'],
            39.8866,
            116.4108,
            72,
            10,
            '建议停留 10-15 分钟',
            '七星石位于祈年殿以东偏北区域，是天坛园林游线中的小节点，适合顺路短暂停留。',
            detail_copy(
                '七星石位于天坛园林区域，相比祈年殿、圜丘坛等核心建筑，它更像一处安静的小景观。这里适合在主线游览之外顺路停留，感受天坛作为大型公园的一面。',
                '如果你从祈年殿区域向东或向北散步，可以把七星石作为短暂停靠点。它不会占用太多时间，却能让路线从庄重的坛庙建筑转入更轻松的园林步行。适合时间充裕、喜欢慢走的游客。'
            ),
        ),
        guide_item(
            '古柏林',
            TEMPLE_OF_HEAVEN_IMAGES['ancient_cypress_grove'],
            39.8808,
            116.4117,
            76,
            33,
            '建议停留 15-25 分钟',
            '古柏林环绕天坛多处区域，是营造庄重氛围的重要景观。慢走其间，可以感受坛庙空间的安静和年代感。',
            detail_copy(
                '天坛里大量古柏让整个园区具有非常稳定、安静的气质。走在古柏林中，游客会明显感到这里不同于普通城市公园：树木、坛墙、甬道和建筑共同营造出庄重而克制的氛围。',
                '古柏林适合作为路线中的缓冲段。看完祈年殿或圜丘坛后，可以在树荫下慢慢走一段，让参观节奏放松下来。对于拍照来说，这里也能提供非常好的纵深和光影，但更重要的是感受天坛长期保存下来的历史时间感。'
            ),
        ),
    ]

    route_map = {
        'title': '天坛路线选择',
        'subtitle': '拖动地图查看区域，点击景点名称进入详情，可在任意位置放大缩小',
        'map_image': TEMPLE_OF_HEAVEN_IMAGES['overview_map'],
        'default_route': 'central',
        'routes': [
            {
                'id': 'central',
                'title': '祭天中轴线',
                'duration': '2.5h',
                'distance': '2.6km',
                'description': '从祈年殿沿丹陛桥南行，经皇穹宇、回音壁、三音石到圜丘坛，适合第一次来天坛的游客。',
                'stops': [0, 1, 2, 3, 4, 5, 6],
            },
            {
                'id': 'complete',
                'title': '坛庙完整线',
                'duration': '4.0h',
                'distance': '4.2km',
                'description': '覆盖中轴核心、斋宫、神乐署、七星石和古柏林，适合想完整理解天坛功能的游客。',
                'stops': list(range(11)),
            },
            {
                'id': 'easy',
                'title': '轻松慢游线',
                'duration': '2.0h',
                'distance': '2.0km',
                'description': '少绕行，重点看祈年殿、皇穹宇、圜丘坛和古柏林，适合亲子、长辈和拍照行程。',
                'stops': [0, 2, 3, 4, 6, 10],
            },
        ],
    }

    content = (
        '这是一条面向游客的北京天坛公园互动导览。天坛不只是祈年殿一座建筑，而是一套围绕祭天、祈谷、斋戒和礼乐展开的空间系统。'
        '第一次参观建议优先走祭天中轴线：从祈年殿建立整体印象，再沿丹陛桥前往皇穹宇和圜丘坛。时间充裕时，可以把斋宫、神乐署、七星石和古柏林加入路线，'
        '这样既能看到最经典的建筑，也能理解仪式准备、声音体验和园林环境如何共同构成天坛。正文下方地图可拖动、缩放，并可点击景点进入详情。'
    )

    return (
        '天坛公园：沿祭天中轴走进明清礼制空间',
        content,
        json.dumps([TEMPLE_OF_HEAVEN_IMAGES['cover'], TEMPLE_OF_HEAVEN_IMAGES['hall_of_prayer']], ensure_ascii=False),
        '北京市东城区天坛东里甲1号',
        39.8822,
        116.4066,
        3,
        2200,
        'beijing_fan',
        '2026-06-05T11:00:00Z',
        642,
        31,
        5480,
        '北京',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def badaling_great_wall_post():
    guide_items = [
        guide_item('关城', BADALING_IMAGES['pass_city'], 40.3594, 116.0202, 14, 76, '建议停留 15-25 分钟', '关城是八达岭长城游览的起点，适合先建立南北两线方向感，再决定登北线还是南线。', detail_copy('关城是进入八达岭长城时最重要的起点之一。站在这里，可以先观察城门、城墙走势和两侧山势，再决定接下来走北线还是南线。北线通常景观更经典、人流也更多；南线相对舒缓，适合想避开拥挤的游客。', '建议在关城先停留一会儿，不要急着冲上城墙。可以看清出口、返程点和卫生间等服务设施，再根据体力选择路线。长城游览最重要的是量力而行，先把方向和返程方式确认好，后面的登城体验会轻松很多。'), [BADALING_IMAGES['pass_city'], BADALING_IMAGES['wall_02']]),
        guide_item('望京石', BADALING_IMAGES['wangjing_stone'], 40.3600, 116.0190, 20, 70, '建议停留 10-15 分钟', '望京石是关城附近的观景节点，适合登城前后短暂停留，感受八达岭一带的山势。', detail_copy('望京石位于八达岭关城附近，是一个适合短暂停留的地点。它不像敌楼那样需要攀登很久，却能帮助游客先感受到八达岭所在山口的地形特点。', '如果当天人流较多，可以把这里作为整理节奏的缓冲点。先看山势和长城走向，再继续往好汉坡或北线敌楼前进，会更容易理解八达岭为什么被称为重要关隘。')),
        guide_item('好汉碑', BADALING_IMAGES['hero_tablet'], 40.3607, 116.0184, 27, 64, '建议停留 10-20 分钟', '好汉碑是八达岭最受欢迎的拍照点之一，适合作为登城纪念，但建议避开拥挤时段。', detail_copy('好汉碑是八达岭长城最具纪念感的拍照点之一。很多游客来到这里都会合影，但它的意义不只是“打卡”，也承载了人们登临长城、完成一段攀登后的成就感。', '拍照时注意排队和让行，不建议在狭窄路段长时间停留。如果人多，可以先继续向上走，返程时再看是否补拍。八达岭的真正体验还在城墙行走、敌楼眺望和山脊视野中。')),
        guide_item('好汉坡', BADALING_IMAGES['hero_slope'], 40.3619, 116.0175, 35, 57, '建议停留 15-25 分钟', '好汉坡坡度较明显，是体验长城攀登感的重要路段。这里适合放慢速度，边走边看山脊线。', detail_copy('好汉坡是八达岭北线中很能体现攀登感的路段。随着坡度上升，游客会明显感到脚下城墙顺着山脊起伏，视野也逐渐打开。这里很适合感受长城如何依山就势，而不是只看单个敌楼。', '建议穿防滑鞋，扶好栏杆，遇到拥挤时不要逆行抢道。可以每走一段就回头看看关城方向，山势、城墙和人流会形成非常直观的层次。体力一般的游客可以把这里作为主要体验点，不一定强求继续登到更高处。')),
        guide_item('北一楼', BADALING_IMAGES['north_tower_1'], 40.3627, 116.0167, 43, 50, '建议停留 10-15 分钟', '北一楼是北线较早抵达的敌楼节点，适合第一次休息和回望关城。', detail_copy('北一楼是从关城出发沿北线前进时较早遇到的敌楼节点。走到这里后，游客可以短暂休息，并回望刚刚走过的城墙和关城区域。', '敌楼适合观察长城的防御功能：它既是瞭望点，也是城墙节奏中的停顿。参观时不要只在门口拍照，可以走到视野较开阔的位置，看城墙如何继续向山脊延伸。')),
        guide_item('北二楼', BADALING_IMAGES['north_tower_2'], 40.3636, 116.0158, 51, 43, '建议停留 10-20 分钟', '北二楼继续抬高视线，适合观察北线城墙连续起伏的节奏。', detail_copy('北二楼比北一楼视野更开阔一些，适合观察北线长城连续起伏的走势。走到这里时，城墙、敌楼和山体之间的关系会更加明显。', '如果时间或体力有限，可以在这里评估是否继续往北四楼、北八楼前进。长城路线没有必要勉强走到最远，找到适合自己的折返点，往往比赶路更舒服。')),
        guide_item('北四楼', BADALING_IMAGES['north_tower_4'], 40.3650, 116.0142, 62, 34, '建议停留 15-25 分钟', '北四楼是北线经典观景节点，适合拍摄长城沿山脊展开的远景。', detail_copy('北四楼是八达岭北线中很适合观景的节点。走到这里，山势更开阔，长城在远处起伏延伸的画面也更完整。对于想拍摄长城曲线和敌楼层次的游客，这里很值得停留。', '建议选择不阻挡通行的位置拍照。除了朝前看，也可以回望来路，关城和近处城墙会被山体衬托出来。这里适合作为经典线的重要停留点。')),
        guide_item('北八楼', BADALING_IMAGES['north_tower_8'], 40.3674, 116.0124, 78, 22, '建议停留 20-30 分钟', '北八楼是八达岭北线人气很高的高处节点，视野开阔，但对体力和人流耐受度要求更高。', detail_copy('北八楼是八达岭北线最受游客关注的高处节点之一。到达这里需要一定体力，但视野也更开阔，能看到长城沿山脊向远处延伸的壮观景象。', '如果当天人很多，前往北八楼要预留更多时间，也要注意下行安全。到达后不建议停留过久阻塞通道，可以快速完成观景和拍照，再根据指示返程或继续前行。体力一般的游客可以把北四楼作为替代终点。')),
        guide_item('南一楼', BADALING_IMAGES['south_tower_1'], 40.3587, 116.0210, 18, 82, '建议停留 10-20 分钟', '南一楼位于南线起步段，游客相对分散，适合想轻松体验长城的人。', detail_copy('南一楼位于八达岭南线起步段，相比北线热门路段，南线通常更适合慢走和避开密集人流。这里坡度和节奏相对舒缓，适合亲子、长辈或不想走太远的游客。', '如果你不追求登到最高点，可以从关城向南走到南一楼、南四楼一带，再返回。南线能看到不同方向的山势，也能保留完整的长城行走体验。')),
        guide_item('南四楼', BADALING_IMAGES['south_tower_4'], 40.3568, 116.0235, 31, 88, '建议停留 15-25 分钟', '南四楼是南线较完整的观景节点，适合作为轻松路线的折返点。', detail_copy('南四楼适合作为八达岭南线的主要停留点或折返点。走到这里，游客既能体验一定距离的城墙行走，又不必承受北线高峰路段的拥挤。', '建议在这里回望关城方向，观察南北两线的走势差异。返程时注意下坡速度，不要边走边看手机。对于轻松路线来说，南四楼已经能提供较完整的长城体验。')),
        guide_item('长城博物馆', BADALING_IMAGES['great_wall_museum'], 40.3577, 116.0176, 16, 61, '建议停留 30-45 分钟', '长城博物馆适合在登城前后补充历史背景，帮助游客理解长城的修筑、防御和交通意义。', detail_copy('长城博物馆适合安排在登城前后参观。登城前看，可以先了解长城修筑、防御体系和沿线历史；登城后看，则能把刚刚看到的城墙、敌楼和关隘与历史背景联系起来。', '如果同行有孩子或对历史感兴趣，博物馆很值得预留时间。它能让八达岭不只是一段登山拍照路线，而是一处与军事防御、边塞交通和历史记忆相关的文化遗产。')),
        guide_item('詹天佑纪念馆', BADALING_IMAGES['zhan_tianyou_memorial'], 40.3570, 116.0166, 10, 57, '建议停留 25-40 分钟', '詹天佑纪念馆位于八达岭周边，适合把长城游览与京张铁路历史联系起来。', detail_copy('詹天佑纪念馆适合对近代交通史感兴趣的游客补充参观。八达岭不仅有长城，也与京张铁路和近代工程史密切相关，把这里加入路线，会让当天行程从古代关隘延伸到近代交通建设。', '如果时间充裕，可以在登城后安排纪念馆作为收束。长城展示的是山地防御与关隘格局，纪念馆则让游客看到现代工程如何穿越同样复杂的山地环境，两者放在一起很有对照感。')),
    ]

    route_map = {
        'title': '八达岭长城路线选择',
        'subtitle': '拖动地图查看区域，点击景点名称进入详情，可在任意位置放大缩小',
        'map_image': BADALING_IMAGES['overview_map'],
        'default_route': 'classic',
        'routes': [
            {'id': 'classic', 'title': '北线经典线', 'duration': '3.0h', 'distance': '3.2km', 'description': '从关城出发，经好汉碑、好汉坡、北一楼、北二楼、北四楼到北八楼，适合第一次登八达岭。', 'stops': [0, 2, 3, 4, 5, 6, 7]},
            {'id': 'complete', 'title': '雄关完整线', 'duration': '5.0h', 'distance': '5.0km', 'description': '串联关城、北线、南线、博物馆和詹天佑纪念馆，适合时间充裕的游客。', 'stops': list(range(12))},
            {'id': 'south', 'title': '轻松南线', 'duration': '2.5h', 'distance': '2.3km', 'description': '从关城走南一楼、南四楼，再补充长城博物馆和詹天佑纪念馆，坡度相对友好。', 'stops': [0, 8, 9, 10, 11]},
        ],
    }

    content = (
        '这是一条北京八达岭长城互动导览。八达岭的重点不只是登高拍照，而是沿山脊观察关城、敌楼、城墙走势和山口地形。'
        '第一次来可选择北线经典线，想完整体验可加入南线和博物馆；同行有长辈或孩子时，南线会更轻松。正文下方地图可拖动、缩放，并可点击每个点位进入详情。'
    )

    return (
        '八达岭长城：沿关城敌楼登临北国雄关',
        content,
        json.dumps([BADALING_IMAGES['cover'], BADALING_IMAGES['wall_02'], BADALING_IMAGES['wall_06']], ensure_ascii=False),
        '北京市延庆区G6京藏高速58号出口',
        40.3594,
        116.0202,
        4,
        3200,
        'explorer',
        '2026-06-05T12:00:00Z',
        824,
        37,
        7390,
        '北京',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def old_summer_palace_post():
    guide_items = [
        guide_item('正大光明遗址', OLD_SUMMER_PALACE_IMAGES['zhengda_guangming'], 40.0087, 116.2980, 19, 34, '建议停留 15-25 分钟', '正大光明遗址适合作为圆明园路线起点，帮助游客先建立遗址公园的历史尺度。', detail_copy('正大光明遗址是圆明园中很适合建立历史感的起点。来到这里时，可以先把圆明园理解为曾经规模宏大的皇家园林，而不是只看西洋楼遗址几处残柱。', '参观时建议先阅读现场说明，再观察遗址位置和周围开阔空间。圆明园的特别之处在于“遗址感”：很多地方留下的是位置、基址和记忆，需要游客边走边想象曾经的园林格局。'), [OLD_SUMMER_PALACE_IMAGES['zhengda_guangming']]),
        guide_item('九州清晏遗址', OLD_SUMMER_PALACE_IMAGES['jiuzhou_qingyan'], 40.0103, 116.2945, 28, 28, '建议停留 15-25 分钟', '九州清晏遗址属于圆明园核心区域之一，适合理解园中园和宫苑生活空间。', detail_copy('九州清晏遗址曾是圆明园中重要的居住和游赏区域。今天参观时，虽然很难看到完整建筑，但仍可以通过遗址范围、道路和周边水系想象当年的宫苑空间。', '建议把这里和福海、蓬岛瑶台一起看。圆明园不是单一轴线园林，而是由许多景区组合而成，九州清晏能帮助游客理解这种“多景区串联”的特点。')),
        guide_item('福海', OLD_SUMMER_PALACE_IMAGES['fuhai'], 40.0110, 116.2996, 43, 45, '建议停留 20-35 分钟', '福海是圆明园重要水面，适合放慢脚步，看湖面如何组织周边景区。', detail_copy('福海是圆明园中非常重要的水面，也是理解园林格局的关键。站在湖边，游客可以感受到圆明园曾经并不是密集建筑堆叠，而是以水面、岛屿、堤岸和建筑共同组织景观。', '参观福海时建议沿湖边慢走一段，观察不同方向的视野变化。圆明园遗址公园的魅力不只在残存石构件，也在这些仍然保留下来的地形、水面和空间关系。')),
        guide_item('蓬岛瑶台', OLD_SUMMER_PALACE_IMAGES['pengdao_yaotai'], 40.0112, 116.3022, 51, 41, '建议停留 15-25 分钟', '蓬岛瑶台位于水景相关区域，适合理解圆明园对仙境意象和湖岛景观的营造。', detail_copy('蓬岛瑶台这一名称本身就带有仙境意象。参观这里时，可以把注意力放在水面、岛屿和视线组织上，想象皇家园林如何借助神话和山水意象营造游赏体验。', '建议与福海连在一起看。湖面提供开阔背景，岛屿和景点则提供停留与想象的中心。这里适合慢走，不适合匆匆路过。')),
        guide_item('万方安和', OLD_SUMMER_PALACE_IMAGES['wanfang_anhe'], 40.0095, 116.2917, 21, 48, '建议停留 15-25 分钟', '万方安和是圆明园中名称很有象征意味的遗址点，适合观察园林空间的平面布局想象。', detail_copy('万方安和是圆明园中很有代表性的遗址名称之一。今天来到这里，更多看到的是遗址位置和空间轮廓，但这正是圆明园参观的特点：游客需要在遗址和说明之间重建曾经的园林想象。', '建议把这里作为西部遗址线的一处停留点。看完后再前往澹泊宁静或福海，会更容易理解圆明园不同景区之间不是孤立存在，而是通过道路、水面和景名意象联系在一起。')),
        guide_item('澹泊宁静', OLD_SUMMER_PALACE_IMAGES['danbo_ningjing'], 40.0083, 116.2903, 18, 56, '建议停留 15-25 分钟', '澹泊宁静适合在西部遗址线中短暂停留，感受圆明园景名背后的文人审美。', detail_copy('澹泊宁静这一景名带有明显的文人审美色彩。参观时，可以把它和圆明园作为皇家园林的身份联系起来看：这里既有皇家的规模，也借用了许多诗意化、书斋化的命名和空间想象。', '游客可以在这里放慢节奏，不必急着寻找“完整建筑”。圆明园很多景点的价值，恰恰在于让人通过遗址、名称和环境去想象已经消失的景观。')),
        guide_item('长春园', OLD_SUMMER_PALACE_IMAGES['changchun_garden'], 40.0124, 116.3080, 69, 29, '建议停留 15-25 分钟', '长春园是圆明园三园之一，前往西洋楼遗址前适合先理解区域关系。', detail_copy('长春园是圆明园三园之一，也是前往西洋楼遗址区域时需要理解的空间背景。很多游客会直接奔向大水法，但先知道自己进入的是长春园范围，会更容易理解西洋楼遗址并非孤立景点。', '参观时可以把长春园作为从湖园遗址转向西洋楼遗址的过渡。前一段看的是中式园林和湖面格局，后一段则会看到西式建筑遗存与历史创伤记忆。')),
        guide_item('西洋楼遗址', OLD_SUMMER_PALACE_IMAGES['western_mansions'], 40.0133, 116.3132, 78, 36, '建议停留 30-45 分钟', '西洋楼遗址是圆明园最具辨识度的区域，适合重点观看石构件、喷泉遗址和中西合璧的园林记忆。', detail_copy('西洋楼遗址是圆明园最受关注的区域之一。这里保留下来的石构件、柱础和喷泉遗迹，让游客能直观看到圆明园中曾经存在的西式建筑和水法景观。', '建议预留较长时间，不要只在大水法前拍照。沿着遗址区域慢慢走，观察石材、构件和空间轴线，会发现这里既展示了中西合璧的园林想象，也承载着近代历史记忆。')),
        guide_item('大水法', OLD_SUMMER_PALACE_IMAGES['great_fountain'], 40.0131, 116.3148, 84, 42, '建议停留 20-30 分钟', '大水法是圆明园最知名的遗址之一，残存石构件具有很强的历史辨识度。', detail_copy('大水法是圆明园遗址中最知名的画面之一。残存的石构件让许多游客第一次真正感受到圆明园从辉煌园林到遗址公园的历史转变。这里很适合作为西洋楼区域的重点停留点。', '参观时建议先看整体轮廓，再走近看石材细节。拍照之外，也可以留意现场说明，理解它原本与喷泉、水法和周边建筑的关系。这里的震撼不只是视觉上的残缺，更来自历史记忆本身。')),
        guide_item('海晏堂遗址', OLD_SUMMER_PALACE_IMAGES['haiyantang_ruins'], 40.0138, 116.3124, 76, 48, '建议停留 20-30 分钟', '海晏堂遗址与著名水法和十二生肖兽首故事相关，适合补充圆明园文物记忆。', detail_copy('海晏堂遗址与圆明园水法景观和十二生肖兽首故事密切相关，是西洋楼区域中很值得停留的地点。即使今天无法看到完整建筑，也能通过遗址和说明理解其曾经的复杂设计。', '建议把海晏堂和大水法连在一起参观。前者帮助游客理解水法系统和文物记忆，后者提供最具辨识度的遗址画面。两处合看，会比单独打卡更完整。')),
        guide_item('远瀛观遗址', OLD_SUMMER_PALACE_IMAGES['yuanyingguan'], 40.0143, 116.3158, 88, 34, '建议停留 15-25 分钟', '远瀛观遗址位于西洋楼区域，适合继续观察欧式建筑遗存和遗址空间。', detail_copy('远瀛观遗址同属西洋楼区域，适合在大水法和海晏堂之后继续观看。这里能让游客看到西洋楼并不是单点景观，而是一组建筑、喷泉和庭园空间的组合。', '参观时可以沿着遗址路径慢慢移动，观察不同遗址之间的距离和方向。这样会更容易想象当年的游赏路线，而不是只把圆明园理解为几个残存石柱。')),
        guide_item('方外观遗址', OLD_SUMMER_PALACE_IMAGES['fangwaiguan'], 40.0149, 116.3170, 92, 27, '建议停留 15-25 分钟', '方外观遗址适合与远瀛观、大水法一起观看，补足西洋楼区域的空间层次。', detail_copy('方外观遗址是西洋楼区域游览中可以继续补充的一站。这里的价值在于帮助游客扩大对西洋楼的理解：它不是只有一处著名遗址，而是由多个建筑和庭园节点构成。', '建议按照地图点位顺路参观，不必来回折返。走到这里时，可以回想刚刚经过的大水法、海晏堂和远瀛观，把它们串成一段完整的遗址路线。')),
        guide_item('黄花阵', OLD_SUMMER_PALACE_IMAGES['huanghuazhen'], 40.0158, 116.3140, 84, 23, '建议停留 20-35 分钟', '黄花阵是西洋楼区域中很有游园趣味的迷宫遗址，适合亲子和慢游游客。', detail_copy('黄花阵是西洋楼区域中很有游园趣味的地点，常被理解为迷宫式景观。相比大水法的历史震撼，黄花阵更能让游客感受到圆明园曾经作为游赏园林的娱乐性和空间趣味。', '如果同行有孩子，这里很适合停留。参观时可以把它放在西洋楼遗址线的后段，让路线从庄重的历史遗址转向稍微轻松的游园体验。')),
        guide_item('圆明园展览馆', OLD_SUMMER_PALACE_IMAGES['exhibition_hall'], 40.0072, 116.3006, 45, 64, '建议停留 30-45 分钟', '圆明园展览馆适合作为行程收束，补充园林历史、复原图和文物信息。', detail_copy('圆明园展览馆适合作为行程收束。看完遗址后再进入展览馆，游客会更容易把现场看到的残存空间、照片、复原图和历史叙述联系起来。', '建议至少预留半小时。圆明园的参观很需要背景信息支撑，展览馆能帮助游客理解三园格局、重要景区、历史变迁和保护意义。对于第一次来圆明园的人，这里能让整趟游览更完整。')),
    ]

    route_map = {
        'title': '圆明园路线选择',
        'subtitle': '拖动地图查看区域，点击景点名称进入详情，可在任意位置放大缩小',
        'map_image': OLD_SUMMER_PALACE_IMAGES['overview_map'],
        'default_route': 'ruins',
        'routes': [
            {'id': 'west', 'title': '湖园遗址线', 'duration': '3.0h', 'distance': '3.0km', 'description': '从正大光明遗址进入，串联九州清晏、福海、蓬岛瑶台、万方安和和澹泊宁静。', 'stops': [0, 1, 2, 3, 4, 5]},
            {'id': 'ruins', 'title': '西洋楼遗址线', 'duration': '3.5h', 'distance': '3.4km', 'description': '重点看长春园、西洋楼遗址、大水法、海晏堂、远瀛观、方外观和黄花阵。', 'stops': [6, 7, 8, 9, 10, 11, 12]},
            {'id': 'complete', 'title': '三园完整线', 'duration': '5.5h', 'distance': '5.5km', 'description': '覆盖湖园遗址、西洋楼遗址和圆明园展览馆，适合时间充裕的深度游。', 'stops': list(range(14))},
        ],
    }

    content = (
        '这是一条北京圆明园遗址公园互动导览。圆明园的参观重点不是寻找完整宫殿，而是在遗址、水面、园路和展览之间重建“万园之园”的历史想象。'
        '第一次来建议先看湖园遗址，再前往西洋楼区域；时间充裕时，把圆明园展览馆放在最后，会更容易理解遗址保护和历史变迁。正文下方地图可拖动、缩放，并可点击景点进入详情。'
    )

    return (
        '圆明园遗址公园：沿湖园遗址回望万园之园',
        content,
        json.dumps([OLD_SUMMER_PALACE_IMAGES['cover'], OLD_SUMMER_PALACE_IMAGES['dashuifa'], OLD_SUMMER_PALACE_IMAGES['haiyantang']], ensure_ascii=False),
        '北京市海淀区清华西路28号',
        40.0110,
        116.3039,
        4,
        2400,
        'culture_seeker',
        '2026-06-05T13:00:00Z',
        689,
        26,
        5120,
        '北京',
        '',
        json.dumps(guide_items, ensure_ascii=False),
        json.dumps(route_map, ensure_ascii=False),
    )


def canton_tower_post():
    guide_items = [
        guide_item('塔下广场', GUANGZHOU_TOWER_IMAGES['base_square'], 23.1058, 113.3236, 47, 62, '建议停留 15-25 分钟', '塔下广场适合作为广州塔路线起点，先观察塔身比例、周边人流和珠江方向。', detail_copy('塔下广场是广州塔最直接的观看位置。来到这里时，可以先抬头观察塔身的扭转曲线，再环顾周边的海珠有轨电车、珠江岸线和对岸城市天际线。广州塔不是孤立地标，它和珠江新城、海心沙、花城广场共同构成广州新中轴的视觉中心。', '建议先在广场建立方向感，再决定是否登塔。白天适合看结构和城市尺度，傍晚以后适合等灯光亮起。这里也是拍摄全身塔影的基础点，后续去江边或海心桥时，会更容易理解广州塔在城市景观中的位置。'), [GUANGZHOU_TOWER_IMAGES['base_square'], GUANGZHOU_TOWER_IMAGES['base_square_detail']]),
        guide_item('观景平台', GUANGZHOU_TOWER_IMAGES['view_platform'], 23.1061, 113.3238, 50, 42, '建议停留 30-50 分钟', '登上观景平台后，可以俯瞰珠江两岸、珠江新城和老城方向，适合作为整条导览的核心。', detail_copy('观景平台是广州塔最能体现“登高看城”的地点。站在高处，珠江像一条清晰的城市轴线，把海珠、天河、越秀和荔湾等区域联系起来。第一次来广州的游客，可以在这里快速建立城市空间印象：哪里是珠江新城，哪里是老城区，城市如何沿江展开。', '如果时间允许，建议在平台停留久一点，沿不同方向慢慢看，而不是只拍几张照片就离开。晴天能看到更远的山水轮廓，夜晚则能看到灯光、桥梁和楼群形成的城市夜景。这里适合作为广州塔导览的重点停留点。'), [GUANGZHOU_TOWER_IMAGES['view_platform'], GUANGZHOU_TOWER_IMAGES['view_platform_detail']]),
        guide_item('海心桥视角', GUANGZHOU_TOWER_IMAGES['haixin_bridge_view'], 23.1130, 113.3249, 62, 56, '建议停留 20-30 分钟', '海心桥方向适合回望广州塔，把塔、珠江和珠江新城一起纳入画面。', detail_copy('海心桥或珠江两岸步道，是回看广州塔的好位置。离开塔身之后，游客会发现广州塔从“身边的建筑”变成“城市画面里的中心”。这里适合拍摄塔身、江面、桥梁和对岸楼群同框的照片。', '建议傍晚或夜间前往，灯光亮起后城市层次更丰富。走到桥上时注意通行秩序，不要长时间停在狭窄位置。这里适合作为广州塔路线的收束点。')),
        guide_item('珠江夜景', GUANGZHOU_TOWER_IMAGES['pearl_river_night'], 23.1108, 113.3219, 69, 70, '建议停留 25-45 分钟', '珠江夜景适合在登塔后安排，沿江慢走或选择游船，感受广州夜间城市界面。', detail_copy('珠江夜景是广州塔游览之后最自然的延伸。登塔时从高处看城市，来到江边则从水岸看塔和楼群。两种视角互相补充，会让游客更完整地理解广州塔为什么成为广州的城市名片。', '如果体力充足，可以沿江慢走；如果想轻松一些，可以考虑珠江夜游。建议预留弹性时间，因为夜景体验受天气、灯光和人流影响较大。')),
    ]
    route_map = build_route_map('广州塔路线选择', '城市中轴导览', GUANGZHOU_TOWER_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '经典登塔线', 'duration': '2.5h', 'distance': '1.8km', 'description': '塔下广场进入，登观景平台，再到海心桥回望广州塔，适合第一次来广州塔的游客。', 'stops': [0, 1, 2]},
        {'id': 'night', 'title': '珠江夜景线', 'duration': '3.0h', 'distance': '2.6km', 'description': '傍晚登塔，再到海心桥和江边看夜景，适合拍照。', 'stops': [0, 1, 2, 3]},
        {'id': 'family', 'title': '轻松体验线', 'duration': '1.5h', 'distance': '1.2km', 'description': '少排队、少折返，重点看塔下广场和江边视角。', 'stops': [0, 2, 3]},
    ])
    return guangzhou_post('广州塔：沿城市中轴俯瞰珠江夜色', '这是一条广州塔正式旅游导览。广州塔最适合从“城市中轴”理解：它不只是高塔，也是一处把珠江、海心沙、珠江新城和海珠滨水空间联系起来的观景节点。第一次来建议先在塔下广场看塔身，再根据天气和排队情况选择登塔，最后到江边或海心桥回望夜景。正文下方地图可拖动、缩放，并可点击景点进入详情。', GUANGZHOU_TOWER_IMAGES, '广州市海珠区阅江西路222号', 23.1061, 113.3240, 1, 2600, 'canton_guide', 934, 36, 7200, guide_items, route_map)


def baiyun_mountain_post():
    guide_items = [
        guide_item('云台花园', BAIYUN_MOUNTAIN_IMAGES['yuntai_garden'], 23.1641, 113.2939, 18, 70, '建议停留 30-45 分钟', '云台花园位于白云山南麓，适合作为轻松路线起点，先进入山麓花园氛围。', detail_copy('云台花园适合作为白云山游览的温和开场。这里比直接登山更轻松，花木、步道和开阔空间能帮助游客从城市道路过渡到山林环境。对于亲子、长辈或不想一开始就爬坡的人，这里是很好的起点。', '建议在这里确认当天体力和路线。如果只想轻松游览，可以把云台花园和山麓步道作为主线；如果想登高看城，再继续前往能仁寺、山顶广场和摩星岭。')),
        guide_item('能仁寺', BAIYUN_MOUNTAIN_IMAGES['nengren_temple'], 23.1706, 113.2950, 31, 58, '建议停留 20-35 分钟', '能仁寺是白云山中人文气息较强的节点，适合在登山过程中放慢节奏。', detail_copy('能仁寺让白云山不只是一条登山路线，也带有岭南山林寺院的文化层次。走到这里时，可以短暂停下，看看建筑、院落和山林环境如何结合。它不像山顶那样强调视野，而是提供一种更安静的中途停留体验。', '建议把能仁寺作为登山节奏中的缓冲点。白云山路线不必一味赶向最高处，中途的寺院、树荫和山路变化，同样是游览体验的一部分。')),
        guide_item('鸣春谷', BAIYUN_MOUNTAIN_IMAGES['mingchun_valley'], 23.1751, 113.2967, 42, 49, '建议停留 25-40 分钟', '鸣春谷适合感受白云山的自然生态和林间声音，是从城市切换到山林的明显节点。', detail_copy('鸣春谷是白云山中更偏自然生态体验的地点。来到这里，游客会明显感到城市噪声变弱，林木、鸟声和山风成为主要感受。对于第一次来白云山的人，这里能帮助理解“城市绿肺”的含义。', '建议慢走，不要只把它当作去山顶的通道。可以在林荫处休息一会儿，再继续向上。天气炎热时，这里也适合调整体力。'), [BAIYUN_MOUNTAIN_IMAGES['mingchun_valley'], BAIYUN_MOUNTAIN_IMAGES['mingchun_valley_detail']]),
        guide_item('山顶广场', BAIYUN_MOUNTAIN_IMAGES['summit_square'], 23.1814, 113.2992, 55, 38, '建议停留 20-35 分钟', '山顶广场是登高前后的集散节点，适合休息、补给和观察广州城市方向。', detail_copy('山顶广场是白云山路线中很实用的停留点。这里适合休息、补给，也适合判断是否继续前往摩星岭。站在较开阔的位置，可以开始看到广州城区的方向和山体起伏。', '建议在这里根据体力选择：时间紧或体力一般，可以把山顶广场作为折返点；想完成登高线的游客，再继续向摩星岭前进。')),
        guide_item('摩星岭', BAIYUN_MOUNTAIN_IMAGES['moxing_gate'], 23.1855, 113.2957, 70, 27, '建议停留 35-60 分钟', '摩星岭是白云山最高峰区域，适合作为登山路线的核心终点。', detail_copy('摩星岭是白云山最重要的登高节点之一。走到这里时，游客会真正感受到白云山作为广州北部屏障和城市观景高地的意义。天气好的时候，可以远望城区、珠江新城和更远的城市轮廓。', '建议不要把摩星岭安排在行程太晚的时候，返程也要预留体力。这里适合停留久一点，拍照之外也可以看山体与城市之间的关系。'), [BAIYUN_MOUNTAIN_IMAGES['moxing_gate'], BAIYUN_MOUNTAIN_IMAGES['moxing_gate_detail']]),
        guide_item('明珠楼', BAIYUN_MOUNTAIN_IMAGES['mingzhu_tower'], 23.1900, 113.2912, 82, 35, '建议停留 20-35 分钟', '明珠楼方向适合深度路线延伸，能补充白云山西北侧的山林和观景体验。', detail_copy('明珠楼适合时间充裕、想走完整白云山路线的游客。相比常规登顶线路，这里更像是把游览从热门节点延伸到山林深处，适合慢走和补充观景。', '如果只安排半日游，可以不强求明珠楼；如果你想把白云山当作一次完整登山休闲体验，这里值得加入路线。')),
    ]
    route_map = build_route_map('白云山路线选择', '云山登高导览', BAIYUN_MOUNTAIN_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '经典登高线', 'duration': '3.0h', 'distance': '3.2km', 'description': '云台花园进入，经能仁寺、鸣春谷到摩星岭，适合第一次登白云山。', 'stops': [0, 1, 2, 3, 4]},
        {'id': 'deep', 'title': '山林完整线', 'duration': '4.5h', 'distance': '5.0km', 'description': '在经典线基础上延伸明珠楼，适合体力较好的游客。', 'stops': [0, 1, 2, 3, 4, 5]},
        {'id': 'easy', 'title': '轻松花园线', 'duration': '1.8h', 'distance': '1.6km', 'description': '以云台花园和山麓步道为主，适合亲子和长辈。', 'stops': [0, 1, 2]},
    ])
    return guangzhou_post('白云山：沿云山步道登临羊城第一秀', '这是一条广州白云山正式旅游导览。白云山适合把“城市绿肺”和“登高看城”结合起来游览：山麓有花园和林荫步道，中段有寺院和自然谷地，高处则能俯瞰广州城市轮廓。建议根据体力选择路线，半日可走经典登高线，时间充裕再延伸明珠楼。正文下方地图可拖动、缩放，并可点击景点进入详情。', BAIYUN_MOUNTAIN_IMAGES, '广州市白云区广园中路白云山景区', 23.1855, 113.2957, 1, 2200, 'mountain_guide', 812, 31, 6500, guide_items, route_map)


def chen_clan_academy_post():
    guide_items = [
        guide_item('头门', CHEN_CLAN_ACADEMY_IMAGES['head_gate'], 23.1289, 113.2402, 50, 80, '建议停留 10-20 分钟', '头门是进入陈家祠的第一道空间，适合先观察门面、屋脊装饰和岭南祠堂气质。', detail_copy('头门是陈家祠游览的开场。站在门前，游客可以先看建筑正面的比例、灰塑陶塑和屋脊装饰，再进入院落。陈家祠的精彩不只在单个展品，而在建筑本身就是一件大型工艺作品。', '建议不要急着穿过入口。先看屋顶、门额和两侧细部，再进入中轴院落，这样后面看木雕、砖雕、石雕时会更有整体感。')),
        guide_item('聚贤堂', CHEN_CLAN_ACADEMY_IMAGES['juxian_hall'], 23.1290, 113.2402, 50, 58, '建议停留 20-30 分钟', '聚贤堂是陈家祠中轴核心空间，适合理解祠堂建筑的礼仪格局。', detail_copy('聚贤堂位于陈家祠中轴线上，是理解整组建筑格局的重要地点。来到这里，可以观察院落、厅堂和廊道如何形成层层推进的空间秩序。这里原本与宗族祭祀、议事和教育活动相关，今天则帮助游客理解岭南宗祠的公共性。', '参观时建议站在院落中间回看前后建筑，感受轴线和围合关系。陈家祠的装饰很丰富，但不要只盯着细节，先看清空间，再看工艺，会更容易理解。')),
        guide_item('中进院落', CHEN_CLAN_ACADEMY_IMAGES['middle_courtyard'], 23.1291, 113.2401, 50, 43, '建议停留 15-25 分钟', '中进院落适合观察廊、院、厅之间的关系，也是拍摄建筑层次的好位置。', detail_copy('中进院落是陈家祠空间层次最清楚的地方之一。游客站在这里，可以同时看到屋顶、廊道、庭院和厅堂之间的关系。阳光从院落落下，建筑装饰的阴影会让砖木石细节更加突出。', '建议在这里慢走一圈，从不同角度看屋脊、梁架和廊柱。陈家祠的美不只是“装饰多”，而是装饰和建筑结构结合得非常紧密。')),
        guide_item('木雕', CHEN_CLAN_ACADEMY_IMAGES['wood_carving'], 23.1292, 113.2401, 32, 35, '建议停留 15-25 分钟', '木雕适合近距离观看人物故事、花鸟纹样和层层镂刻的工艺细节。', detail_copy('陈家祠的木雕常出现在梁架、屏门和室内构件上。近距离看时，会发现人物、花鸟、瑞兽和故事场景层次很丰富，工匠通过镂空、浮雕和线条变化制造出很强的空间感。', '建议不要只拍远景，可以找一处木雕细节认真看几分钟。先看整体图案，再看人物表情、衣纹和背景，游客会更容易感受到岭南民间工艺的细腻。')),
        guide_item('砖雕', CHEN_CLAN_ACADEMY_IMAGES['brick_carving'], 23.1292, 113.2403, 68, 35, '建议停留 15-25 分钟', '砖雕常位于墙面和檐下位置，适合观察灰砖上细密的线条和故事画面。', detail_copy('砖雕是陈家祠非常有代表性的装饰类型。它往往在墙面、门楼和檐下展开，用看似朴素的灰砖表现人物、山水、花草和故事。相比色彩鲜明的陶塑，砖雕更含蓄，但细节非常耐看。', '参观时可以把砖雕和木雕对照着看：木雕更强调层次和穿透感，砖雕更强调线条和浅浮雕效果。两者合在一起，构成陈家祠“建筑即展览”的体验。')),
        guide_item('陶塑灰塑', CHEN_CLAN_ACADEMY_IMAGES['pottery_plaster'], 23.1293, 113.2402, 50, 22, '建议停留 20-30 分钟', '陶塑和灰塑集中在屋脊、檐口等高处，是陈家祠最容易让游客抬头惊叹的部分。', detail_copy('陈家祠屋脊上的陶塑、灰塑是非常醒目的装饰。它们常常呈现人物故事、瑞兽、花鸟和戏曲场景，色彩与屋顶线条一起构成岭南建筑鲜明的视觉特征。', '建议在院落中找一个开阔位置抬头观看，不要只看平视范围。很多精彩细节都在高处，肉眼看不清时可以用手机放大观察。')),
        guide_item('后进展厅', CHEN_CLAN_ACADEMY_IMAGES['rear_gallery'], 23.1294, 113.2402, 50, 12, '建议停留 25-40 分钟', '后进展厅适合把建筑工艺与广东民间工艺展览联系起来，作为路线收束。', detail_copy('后进展厅适合作为陈家祠游览的收束。看完建筑空间和装饰细节后，再进入展厅观看民间工艺，会更容易理解这些工艺并不是孤立展品，而是与广东地方生活、信仰和审美相连。', '建议最后预留一段安静时间看展，不要把全部时间都用在门口拍照。陈家祠最值得带走的，是对岭南建筑和民间工艺整体气质的理解。')),
    ]
    route_map = build_route_map('陈家祠路线选择', '岭南建筑工艺导览', CHEN_CLAN_ACADEMY_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '建筑中轴线', 'duration': '1.5h', 'distance': '0.8km', 'description': '从头门到聚贤堂和后进展厅，适合第一次参观。', 'stops': [0, 1, 2, 6]},
        {'id': 'craft', 'title': '工艺细节线', 'duration': '2.0h', 'distance': '1.0km', 'description': '重点看木雕、砖雕、陶塑灰塑，适合文化爱好者。', 'stops': [0, 3, 4, 5, 6]},
        {'id': 'photo', 'title': '轻松拍照线', 'duration': '1.0h', 'distance': '0.6km', 'description': '少走回头路，重点看门面、院落和屋脊。', 'stops': [0, 2, 5]},
    ])
    return guangzhou_post('陈家祠：走进岭南建筑艺术博物馆', '这是一条广州陈家祠正式旅游导览。陈家祠最适合把“建筑”和“工艺”放在一起看：门面、院落、厅堂、屋脊和雕塑装饰共同构成岭南建筑艺术的完整现场。建议先走中轴线建立空间感，再近看木雕、砖雕、陶塑和灰塑细节。正文下方地图可拖动、缩放，并可点击景点进入详情。', CHEN_CLAN_ACADEMY_IMAGES, '广州市荔湾区中山七路恩龙里34号', 23.1290, 113.2402, 1, 1800, 'lingnan_curator', 778, 29, 5900, guide_items, route_map)


def yuexiu_park_post():
    guide_items = [
        guide_item('五羊石像', YUEXIU_PARK_IMAGES['five_rams'], 23.1407, 113.2577, 35, 55, '建议停留 20-30 分钟', '五羊石像是广州城市象征，适合作为越秀公园导览的核心打卡点。', detail_copy('五羊石像是越秀公园最具辨识度的景点，也是广州“羊城”称号最直观的城市符号。来到这里时，可以先听一听五羊传说，再观察石像位置和周边山体环境。它不是普通雕塑，而是广州城市记忆的一部分。', '建议在这里停留，不只拍照，也可以理解广州为什么会把五羊作为城市象征。之后再去镇海楼和古城墙，会发现越秀公园把传说、城市史和山地公园连接在一起。')),
        guide_item('镇海楼', YUEXIU_PARK_IMAGES['zhenhai_tower'], 23.1407, 113.2600, 58, 38, '建议停留 25-40 分钟', '镇海楼是广州博物馆所在的重要建筑，适合理解广州城史。', detail_copy('镇海楼又常被称为“五层楼”，是越秀山上非常重要的历史建筑。它今天与广州博物馆联系在一起，适合游客从这里了解广州城市发展、城防和地域文化。', '建议把镇海楼作为越秀公园的重点停留点。先看建筑外观和位置，再进入展览理解广州城史。看完五羊石像后再来到这里，会从城市传说进入更具体的历史叙事。')),
        guide_item('广州博物馆', YUEXIU_PARK_IMAGES['guangzhou_museum'], 23.1408, 113.2600, 60, 31, '建议停留 40-60 分钟', '广州博物馆适合系统了解广州历史，是越秀公园中最值得慢看的室内节点。', detail_copy('广州博物馆能让越秀公园游览从户外景观转入城市历史。展览通常会把广州的地理、商贸、民俗和城市发展串联起来，帮助游客理解这座城市为什么长期是岭南重要中心。', '建议至少预留半小时以上。看完展览再回到公园山路，会更容易把镇海楼、古城墙、五羊石像和广州城市记忆联系起来。')),
        guide_item('明代古城墙', YUEXIU_PARK_IMAGES['ming_city_wall'], 23.1415, 113.2606, 70, 46, '建议停留 15-25 分钟', '明代古城墙适合观察广州旧城防遗存，补充越秀山与城市中轴关系。', detail_copy('明代古城墙是越秀公园中容易被匆匆路过却很有历史感的地点。它提醒游客，越秀山并不只是休闲公园，也曾与广州城防、城市边界和历史空间有关。', '参观时可以沿墙体慢走一段，观察石材、走向和地势。把它和镇海楼一起看，会更容易理解越秀山在广州城史中的位置。')),
        guide_item('中山纪念碑', YUEXIU_PARK_IMAGES['sun_yat_sen_monument'], 23.1398, 113.2591, 47, 26, '建议停留 15-25 分钟', '中山纪念碑是越秀山上的近现代纪念节点，适合补充城市公共记忆。', detail_copy('中山纪念碑让越秀公园的历史层次从古代城防延伸到近现代公共纪念。这里的空间更庄重，适合短暂停留，理解广州城市历史并不只属于古代，也与近现代政治和公共记忆相连。', '建议把它安排在镇海楼或古城墙之后参观，路线会从城市传说、古代城防，逐步过渡到近现代纪念。')),
        guide_item('越秀山湖区', YUEXIU_PARK_IMAGES['lake_area'], 23.1378, 113.2579, 30, 76, '建议停留 20-35 分钟', '湖区适合作为路线放松段，感受越秀公园作为城市中心绿地的一面。', detail_copy('越秀山湖区更适合放松和休息。看过五羊石像、镇海楼和古城墙之后，来到湖边会感到节奏变慢，也能理解越秀公园为什么同时承担城市历史空间和市民休闲空间。', '建议把湖区放在路线后半段。这里适合补水、休息，也适合根据体力决定是否继续深度游。')),
    ]
    route_map = build_route_map('越秀公园路线选择', '城史与城市绿地导览', YUEXIU_PARK_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '城史经典线', 'duration': '2.5h', 'distance': '2.0km', 'description': '五羊石像、镇海楼、博物馆和古城墙串联，适合第一次参观。', 'stops': [0, 1, 2, 3]},
        {'id': 'deep', 'title': '完整慢游线', 'duration': '3.5h', 'distance': '3.0km', 'description': '加入中山纪念碑和湖区，完整体验越秀山。', 'stops': [0, 1, 2, 3, 4, 5]},
        {'id': 'easy', 'title': '轻松公园线', 'duration': '1.5h', 'distance': '1.4km', 'description': '看五羊石像和湖区，适合亲子、长辈和短暂停留。', 'stops': [0, 5, 1]},
    ])
    return guangzhou_post('越秀公园：从五羊石像走进广州城史', '这是一条广州越秀公园正式旅游导览。越秀公园不是单纯的城市公园，它把五羊传说、镇海楼、广州博物馆、古城墙和山水绿地放在同一个空间里。第一次来建议从五羊石像开始，再到镇海楼和博物馆理解广州城史，最后用湖区作为放松收束。正文下方地图可拖动、缩放，并可点击景点进入详情。', YUEXIU_PARK_IMAGES, '广州市越秀区解放北路988号', 23.1407, 113.2590, 1, 2100, 'city_history_guide', 745, 24, 6100, guide_items, route_map)


def shamian_island_post():
    guide_items = [
        guide_item('沙面大街', SHAMIAN_ISLAND_IMAGES['main_street'], 23.1060, 113.2490, 28, 53, '建议停留 25-40 分钟', '沙面大街适合作为路线主轴，沿街观察欧陆建筑、古树和安静街巷。', detail_copy('沙面大街是沙面岛最适合慢走的主线。这里的建筑尺度、人行空间和古树环境都和广州其他繁华街区不同，游客会明显感到节奏放慢。欧陆建筑、骑楼式细节和珠江边气息共同构成沙面的独特氛围。', '建议从街道一端慢慢走，不要只找单个建筑打卡。沙面的魅力在连续街景中，适合边走边看门窗、阳台、树影和街道转角。')),
        guide_item('露德圣母堂', SHAMIAN_ISLAND_IMAGES['lourdes_chapel'], 23.1068, 113.2487, 38, 38, '建议停留 15-25 分钟', '露德圣母堂是沙面岛上重要的宗教建筑，适合观察小尺度教堂与街区关系。', detail_copy('露德圣母堂是沙面岛上很有辨识度的宗教建筑。它的体量不算庞大，却和周边街巷、绿树和老建筑形成安静的空间氛围。来到这里时，可以把它看作沙面历史街区多元文化的一部分。', '参观时保持安静，尊重宗教场所秩序。即使不进入内部，也可以从外部看立面、窗洞和建筑与街道之间的距离。')),
        guide_item('沙面基督堂', SHAMIAN_ISLAND_IMAGES['christ_church'], 23.1072, 113.2476, 50, 32, '建议停留 15-25 分钟', '沙面基督堂适合与露德圣母堂对照观看，理解沙面多元建筑风貌。', detail_copy('沙面基督堂与露德圣母堂一起，构成沙面宗教建筑的重要节点。两处建筑风格、尺度和街区位置各有特点，适合游客对照观看，而不是孤立打卡。', '建议把它放在沙面大街慢行路线中顺路参观。看完后继续向旧领事馆建筑群移动，街区历史层次会更清楚。')),
        guide_item('旧领事馆建筑群', SHAMIAN_ISLAND_IMAGES['former_consulates'], 23.1065, 113.2472, 63, 44, '建议停留 25-45 分钟', '旧领事馆建筑群是沙面最能体现近代历史街区气质的部分，适合慢看建筑立面。', detail_copy('旧领事馆建筑群是沙面岛历史风貌的重点。这里的建筑不只是“好看”，也记录了广州近代对外交往、租界历史和城市空间变化。游客可以从立面、柱廊、窗型和庭院边界观察不同建筑的风格差异。', '建议慢看，不要把所有建筑都当作背景墙。可以选择几座保存较好的建筑，仔细看门廊、阳台和墙面比例。这样会更容易理解沙面为什么和广州其他老街区气质不同。')),
        guide_item('白鹅潭江边', SHAMIAN_ISLAND_IMAGES['riverfront'], 23.1053, 113.2480, 68, 64, '建议停留 20-35 分钟', '白鹅潭江边适合作为路线收束，观看珠江水面、对岸城市和沙面岛边界。', detail_copy('白鹅潭江边让沙面岛从街区空间转向珠江水岸。走到这里时，可以看到岛屿与水面的关系，也能感受到广州作为珠江城市的一面。江风、树影和对岸建筑会让路线节奏自然放慢。', '建议把江边放在行程后段，作为休息和拍照位置。傍晚光线柔和时，沙面建筑和珠江水面会更有层次。')),
        guide_item('古树街巷', SHAMIAN_ISLAND_IMAGES['tree_lanes'], 23.1064, 113.2496, 40, 70, '建议停留 20-30 分钟', '古树街巷适合轻松拍照和慢走，感受沙面作为历史街区的日常气息。', detail_copy('沙面的古树街巷是最适合慢走的部分。相比明确的景点名称，这些树荫、路口和老建筑之间的日常空间，反而更能体现沙面气质。游客在这里可以放慢脚步，看光影落在墙面和路面上的变化。', '建议不要只追求热门拍照点。沿着树荫走一段，偶尔停下看门牌、窗户和阳台，沙面的细节会慢慢显出来。')),
    ]
    route_map = build_route_map('沙面岛路线选择', '历史街区慢行导览', SHAMIAN_ISLAND_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '经典慢行线', 'duration': '2.0h', 'distance': '1.6km', 'description': '沙面大街、教堂、旧领事馆和江边串联，适合第一次来。', 'stops': [0, 1, 2, 3, 4]},
        {'id': 'photo', 'title': '轻松拍照线', 'duration': '1.2h', 'distance': '1.0km', 'description': '重点走街巷、古树和江边，适合拍照和散步。', 'stops': [0, 5, 4]},
        {'id': 'history', 'title': '建筑历史线', 'duration': '2.5h', 'distance': '1.8km', 'description': '重点看宗教建筑和旧领事馆建筑群，适合建筑爱好者。', 'stops': [1, 2, 3, 0, 4]},
    ])
    return guangzhou_post('沙面岛：沿珠江漫步欧陆建筑街区', '这是一条广州沙面岛正式旅游导览。沙面最适合慢走：它不是靠单个宏大景点取胜，而是通过欧陆建筑、古树街巷、教堂、旧领事馆和珠江水岸共同形成历史街区气质。建议从沙面大街开始，顺路看教堂和旧建筑，最后到白鹅潭江边收束。正文下方地图可拖动、缩放，并可点击景点进入详情。', SHAMIAN_ISLAND_IMAGES, '广州市荔湾区沙面大街', 23.1060, 113.2488, 1, 1600, 'shamian_walker', 702, 22, 5400, guide_items, route_map)


def shanghai_bund_post():
    guide_items = [
        guide_item('外滩源', SHANGHAI_BUND_IMAGES['bund_origin'], 31.2443, 121.4903, 30, 24, '建议停留 25-40 分钟', '外滩源适合作为外滩路线起点，先看苏州河口、历史建筑和城市空间转折。', detail_copy('外滩源位于苏州河与黄浦江交汇附近，是理解外滩历史街区的好起点。来到这里时，游客可以先观察桥梁、河口和近代建筑之间的关系，上海的港口、金融和城市开放历史会在这个位置变得更具体。', '建议从这里慢慢向南走，不要一开始就直奔最拥挤的观景平台。外滩的魅力在连续街景中，先看清街区尺度，再看江对岸陆家嘴天际线，会更有层次。')),
        guide_item('万国建筑群', SHANGHAI_BUND_IMAGES['international_buildings'], 31.2397, 121.4894, 38, 36, '建议停留 35-55 分钟', '万国建筑群是外滩最重要的历史界面，适合边走边看立面、门廊和屋顶线。', detail_copy('万国建筑群是外滩最具辨识度的部分。游客沿中山东一路行走时，可以看到不同年代、不同风格的近代建筑连续展开。它们不是单独的漂亮楼房，而是上海近代金融、航运和城市发展的实体见证。', '参观时建议放慢速度，从北向南看建筑立面、门廊、柱式和屋顶轮廓。白天适合观察细节，傍晚灯光亮起后适合整体感受。不要只把镜头对着陆家嘴，对身后的建筑群也留出时间。')),
        guide_item('黄浦江观景带', SHANGHAI_BUND_IMAGES['huangpu_river_view'], 31.2384, 121.4915, 52, 45, '建议停留 30-50 分钟', '黄浦江观景带适合看陆家嘴天际线、江面船只和外滩整体城市画面。', detail_copy('黄浦江观景带是第一次来上海最直观的城市观景位置。站在江边，陆家嘴的高楼、黄浦江的船只、外滩历史建筑和人流共同构成上海最经典的城市画面。这里适合建立“浦西历史、浦东现代”的空间对照。', '建议选择清晨、傍晚或夜间停留，人流和光线都会更友好。拍照时可以先拍宽画面，再找桥、栏杆、船只作为前景。这里也是判断是否继续夜游黄浦江或前往南京东路的好节点。')),
        guide_item('陈毅广场', SHANGHAI_BUND_IMAGES['chenyi_square'], 31.2369, 121.4910, 58, 55, '建议停留 15-25 分钟', '陈毅广场位于外滩中段，适合短暂停留，整理方向并继续南北两侧路线。', detail_copy('陈毅广场是外滩中段的重要公共空间。这里比普通步道更开阔，适合游客短暂停下，回看万国建筑群，也看向黄浦江对岸。它能把外滩从单纯观景带变成一处有城市纪念和公共活动意味的空间。', '建议把这里作为中途休息点，不必停留太久。看完后可以继续向南走十六铺方向，或者转向南京东路步行街。')),
        guide_item('南京东路外滩口', SHANGHAI_BUND_IMAGES['nanjing_road_entry'], 31.2406, 121.4891, 43, 63, '建议停留 20-35 分钟', '南京东路外滩口连接外滩和商业步行街，适合作为路线收束或转场。', detail_copy('南京东路外滩口是外滩与上海传统商业街区连接最紧密的位置。游客从江边转入街道，会明显感到城市节奏从观景转向购物、餐饮和夜间人流。这里很适合把外滩游览延伸到人民广场方向。', '如果只安排外滩，可以在这里收束；如果还有体力，可以沿南京东路继续步行。夜间霓虹、人流和历史建筑会让上海的城市气质从江岸转入街区内部。')),
    ]
    route_map = build_route_map('外滩路线选择', '黄浦江历史街区导览', SHANGHAI_BUND_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '外滩经典线', 'duration': '2.5h', 'distance': '2.0km', 'description': '外滩源、万国建筑群、黄浦江观景带和南京东路串联，适合第一次来。', 'stops': [0, 1, 2, 4]},
        {'id': 'night', 'title': '夜景慢行线', 'duration': '3.0h', 'distance': '2.4km', 'description': '傍晚看建筑灯光、江面和陆家嘴夜景，适合拍照。', 'stops': [1, 2, 3, 4]},
        {'id': 'history', 'title': '建筑历史线', 'duration': '2.8h', 'distance': '1.8km', 'description': '重点观察外滩源和万国建筑群，适合城市历史爱好者。', 'stops': [0, 1, 3]},
    ])
    return city_guide_post('上海市', '上海外滩：沿黄浦江读懂近代城市天际线', '这是一条上海外滩正式旅游导览。外滩最适合从“浦西历史建筑与浦东现代天际线的对望”来理解：一侧是万国建筑群和近代城市记忆，一侧是陆家嘴高楼与当代上海。建议从外滩源开始，沿江慢走万国建筑群，再到黄浦江观景带和南京东路外滩口收束。正文下方地图可拖动、缩放，并可点击景点进入详情。', SHANGHAI_BUND_IMAGES, '上海市黄浦区中山东一路', 31.2400, 121.4900, 2, 3600, 'shanghai_guide', 980, 42, 8200, guide_items, route_map)


def yu_garden_post():
    guide_items = [
        guide_item('九曲桥', YU_GARDEN_IMAGES['nine_turning_bridge'], 31.2272, 121.4920, 47, 54, '建议停留 20-35 分钟', '九曲桥是豫园外部最经典的进入画面，适合先看水面、桥线和人流节奏。', detail_copy('九曲桥是豫园区域最容易被游客记住的空间。桥面转折、水面倒影、湖心亭和周边传统建筑共同形成非常上海老城厢的画面。这里人流通常较多，但也最能体现豫园区域的热闹气息。', '建议在桥边先停留，不要急着穿过。可以从不同角度看桥线和湖心亭的关系，再进入园内。早上或傍晚人少时更适合拍照。')),
        guide_item('湖心亭', YU_GARDEN_IMAGES['huxinting_teahouse'], 31.2274, 121.4922, 55, 47, '建议停留 15-25 分钟', '湖心亭适合与九曲桥一起观看，是豫园区域最有辨识度的茶楼景观。', detail_copy('湖心亭位于水面之中，与九曲桥共同构成豫园外部最经典的视觉中心。游客可以把它看作从城市街巷进入园林氛围前的过渡：外面是热闹商市，里面则逐渐进入曲折、收放有致的园林空间。', '如果时间宽裕，可以在附近短暂停留喝茶或休息。即使不进入茶楼，也建议观察屋顶、窗格和水面倒影，这些细节会让豫园不只是“老街拍照点”。')),
        guide_item('三穗堂', YU_GARDEN_IMAGES['sansui_hall'], 31.2278, 121.4926, 42, 32, '建议停留 20-30 分钟', '三穗堂是进入豫园后理解厅堂院落关系的重要节点，适合慢看建筑尺度。', detail_copy('三穗堂是豫园中较重要的厅堂空间。来到这里时，游客可以从门窗、匾额、院落和屋檐关系入手，看江南园林如何用不大的空间组织出层次。它不像开阔广场那样一眼看完，而是需要边走边看。', '建议在这里先看整体院落，再看建筑细节。豫园的参观不要只追求“拍到一个全景”，更适合从一个门洞、一段廊道、一处窗景慢慢进入。')),
        guide_item('大假山', YU_GARDEN_IMAGES['great_rockery'], 31.2281, 121.4924, 32, 42, '建议停留 20-35 分钟', '大假山是豫园山石景观的重点，适合理解江南园林“咫尺山林”的营造。', detail_copy('大假山体现了江南园林把山水浓缩进城市空间的能力。游客在这里可以看到叠石、洞壑、路径和植物如何共同制造山林感。它的精彩不在规模庞大，而在近距离内形成起伏、遮挡和转折。', '参观时建议绕行观看，不要只在正面停留。随着行走角度变化，假山会不断呈现新的层次，这正是园林游览的乐趣所在。')),
        guide_item('点春堂', YU_GARDEN_IMAGES['dianchun_hall'], 31.2284, 121.4920, 61, 34, '建议停留 15-25 分钟', '点春堂适合补充豫园历史与厅堂空间，帮助游客从景观转入人文叙事。', detail_copy('点春堂是豫园中很适合补充历史背景的厅堂节点。游客在这里可以把园林从“好看的庭院”进一步理解为一处有主人、活动和城市历史的空间。厅堂、庭院和展陈共同让豫园的文化层次更清楚。', '建议把它安排在大假山之后参观，路线会从山石景观转向厅堂人文。停留时间不必过长，但可以认真阅读现场说明。')),
        guide_item('豫园商城', YU_GARDEN_IMAGES['yuyuan_bazaar'], 31.2270, 121.4934, 70, 66, '建议停留 30-60 分钟', '豫园商城适合作为路线收束，体验老城厢商业、点心和夜间灯光。', detail_copy('豫园商城位于园林外部，是上海老城厢商业氛围最浓的区域之一。这里的建筑、灯光、餐饮和人流非常热闹，与园内相对精致的园林空间形成对照。游客可以在这里补充小吃、伴手礼和夜景体验。', '建议把商城放在后段，不要一开始就被商业街耗掉全部体力。看完园内空间后再出来逛，会更容易区分“园林豫园”和“豫园商圈”的不同体验。')),
    ]
    route_map = build_route_map('豫园路线选择', '老城厢江南园林导览', YU_GARDEN_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '经典园林线', 'duration': '2.5h', 'distance': '1.2km', 'description': '九曲桥、湖心亭、三穗堂、大假山和点春堂串联。', 'stops': [0, 1, 2, 3, 4]},
        {'id': 'family', 'title': '轻松亲子线', 'duration': '1.6h', 'distance': '0.9km', 'description': '重点看桥、湖心亭和商城，节奏轻松。', 'stops': [0, 1, 5]},
        {'id': 'night', 'title': '夜景烟火线', 'duration': '2.0h', 'distance': '1.0km', 'description': '傍晚看九曲桥、湖心亭和豫园商城灯光。', 'stops': [5, 0, 1]},
    ])
    return city_guide_post('上海市', '上海豫园：走进老城厢里的江南园林', '这是一条上海豫园正式旅游导览。豫园适合把“园林空间”和“老城厢烟火气”一起看：园内有厅堂、假山、廊道和水面，园外有九曲桥、湖心亭和热闹商城。建议先从九曲桥建立整体印象，再进入园内慢看山石和厅堂，最后到豫园商城收束。正文下方地图可拖动、缩放，并可点击景点进入详情。', YU_GARDEN_IMAGES, '上海市黄浦区福佑路168号', 31.2278, 121.4925, 2, 2800, 'garden_story', 850, 33, 6900, guide_items, route_map)


def shanghai_museum_post():
    guide_items = [
        guide_item('博物馆大厅', SHANGHAI_MUSEUM_IMAGES['museum_hall'], 31.2302, 121.4708, 50, 76, '建议停留 10-20 分钟', '大厅适合作为参观起点，先建立楼层方向和展厅顺序。', detail_copy('上海博物馆适合有节奏地参观。进入大厅后，游客可以先查看楼层、临展和重点展厅位置，再决定从青铜器、陶瓷、书画或玉器开始。不要一进门就随意乱走，否则容易在展厅之间消耗体力。', '建议先选两到三个重点展厅，再根据时间补充其他内容。博物馆参观不是看得越多越好，而是要让每个展厅都留出认真观看的时间。')),
        guide_item('青铜器馆', SHANGHAI_MUSEUM_IMAGES['bronze_gallery'], 31.2303, 121.4708, 35, 58, '建议停留 35-50 分钟', '青铜器馆适合作为核心展厅，理解礼器、铭文和古代制度。', detail_copy('青铜器馆是上海博物馆最值得重点观看的展厅之一。游客可以从器形、纹饰、铭文和用途入手，理解青铜器不仅是艺术品，也和礼制、权力、祭祀、宴饮等古代生活密切相关。', '建议不要只看最大、最华丽的器物。可以挑几件说明较完整的展品慢慢读，观察器物名称、年代和用途。这样会比快速扫过整个展厅更有收获。')),
        guide_item('陶瓷馆', SHANGHAI_MUSEUM_IMAGES['ceramics_gallery'], 31.2304, 121.4707, 63, 58, '建议停留 35-50 分钟', '陶瓷馆适合按照时代线索观看，从早期陶器到成熟瓷器建立审美脉络。', detail_copy('陶瓷馆能帮助游客直观看到中国陶瓷从实用器物到审美高峰的发展过程。器形、釉色、胎质和装饰会随着时代变化而不断丰富。即使不熟悉专业术语，也可以从颜色、光泽和器物比例开始观察。', '建议按展厅顺序慢慢走，不要只寻找名品。把不同年代的器物放在一起比较，会更容易看出技术和审美的变化。')),
        guide_item('书法馆', SHANGHAI_MUSEUM_IMAGES['calligraphy_gallery'], 31.2305, 121.4708, 35, 38, '建议停留 25-40 分钟', '书法馆适合安静观看线条、章法和笔墨节奏，建议放慢速度。', detail_copy('书法馆需要游客把节奏慢下来。书法的精彩不只在“写了什么字”，更在笔画的轻重、行气、章法和纸面空间。即使看不懂全部内容，也可以从线条节奏和整体气息感受作品。', '建议选择几件作品认真看，而不是逐件拍照。站近看笔画，退后看整体布局，会比只看展签更容易进入状态。')),
        guide_item('绘画馆', SHANGHAI_MUSEUM_IMAGES['painting_gallery'], 31.2305, 121.4709, 63, 38, '建议停留 25-45 分钟', '绘画馆适合看山水、人物、花鸟的构图和笔墨，适合与书法馆连看。', detail_copy('绘画馆适合与书法馆连在一起参观。中国绘画常常不追求单点透视，而是通过笔墨、留白和移动视线组织画面。游客可以把山水画当作一次纸面上的游览，顺着画面慢慢移动视线。', '建议不要离展柜太近一直看局部。先看整体构图，再看树石、人物或题跋细节，会更容易理解作品。')),
        guide_item('玉器馆', SHANGHAI_MUSEUM_IMAGES['jade_gallery'], 31.2306, 121.4708, 50, 24, '建议停留 25-40 分钟', '玉器馆适合观察材质、工艺和礼仪用途，是博物馆路线的精致收束。', detail_copy('玉器馆展示的是材质、工艺和礼仪意义的结合。玉器往往不以巨大尺寸取胜，而是依靠细腻的打磨、纹饰和象征意义体现价值。游客可以观察光泽、颜色和雕工细节。', '建议把玉器馆放在后段，作为相对安静的收束。看完青铜和陶瓷后，再看玉器，会更容易感受到不同材质带来的审美差异。')),
    ]
    route_map = build_route_map('上海博物馆路线选择', '古代艺术展厅导览', SHANGHAI_MUSEUM_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '镇馆经典线', 'duration': '3.0h', 'distance': '1.4km', 'description': '大厅、青铜器、陶瓷、书画和玉器串联，适合第一次参观。', 'stops': [0, 1, 2, 3, 4, 5]},
        {'id': 'short', 'title': '两小时精选线', 'duration': '2.0h', 'distance': '0.9km', 'description': '重点看青铜器、陶瓷和玉器，适合时间有限。', 'stops': [0, 1, 2, 5]},
        {'id': 'art', 'title': '书画审美线', 'duration': '2.5h', 'distance': '1.0km', 'description': '重点观看书法、绘画和玉器，适合安静慢看。', 'stops': [0, 3, 4, 5]},
    ])
    return city_guide_post('上海市', '上海博物馆：沿展厅看懂中国古代艺术', '这是一条上海博物馆正式旅游导览。上海博物馆适合按“材质与艺术门类”来参观：青铜、陶瓷、书法、绘画和玉器各自代表不同的观看方式。建议先在大厅确定路线，再选择重点展厅慢看，避免把博物馆变成匆忙打卡。正文下方地图可拖动、缩放，并可点击景点进入详情。', SHANGHAI_MUSEUM_IMAGES, '上海市黄浦区人民大道201号', 31.2304, 121.4707, 3, 2200, 'museum_curator', 790, 28, 6100, guide_items, route_map)


def shenzhen_bay_park_post():
    guide_items = [
        guide_item('滨海步道', SHENZHEN_BAY_IMAGES['coastal_promenade'], 22.5232, 113.9445, 22, 48, '建议停留 35-60 分钟', '滨海步道是深圳湾公园的主线，适合沿海岸慢走，看海湾、桥梁和城市界面。', detail_copy('滨海步道是深圳湾公园最适合展开游览的部分。游客沿海边行走时，可以同时看到开阔水面、红树林方向、深圳湾大桥和城市天际线。这里的重点不是单个建筑，而是海湾城市的连续景观。', '建议选择清晨、傍晚或天气通透时前往。步道较长，不必一次走完，可根据体力选择折返点。')),
        guide_item('人才公园视角', SHENZHEN_BAY_IMAGES['talent_park_view'], 22.5165, 113.9367, 38, 34, '建议停留 25-45 分钟', '人才公园方向适合看深圳湾与后海城市天际线，适合拍照和休息。', detail_copy('人才公园方向能把深圳湾水面和后海高楼放在同一个画面中。这里适合游客感受深圳作为海滨现代城市的一面：开阔、年轻、节奏轻快。', '建议在这里短暂停留，找一处不影响通行的位置看水面和建筑。傍晚光线会让城市轮廓更柔和。')),
        guide_item('深圳湾大桥远眺', SHENZHEN_BAY_IMAGES['shenzhen_bay_bridge'], 22.5080, 113.9340, 55, 58, '建议停留 20-35 分钟', '深圳湾大桥远眺点适合看海湾尺度，也是理解深圳与湾区联系的视觉节点。', detail_copy('深圳湾大桥远眺点让游客把视线从公园内部延伸到更大的湾区空间。桥梁、水面和远处城市共同构成深圳湾的开放感。这里适合拍摄宽画面，也适合在路线中放慢节奏。', '建议不要为了追桥走得太远，量力而行即可。天气晴朗时视野更好，阴天也可以把这里作为安静休息点。')),
        guide_item('日出剧场', SHENZHEN_BAY_IMAGES['sunrise_theater'], 22.5028, 113.9270, 70, 42, '建议停留 25-40 分钟', '日出剧场适合看开阔水面和天空变化，是清晨或傍晚的重点停留点。', detail_copy('日出剧场名字本身就提示了它最适合的观看时间。这里面向水面，空间开阔，清晨、黄昏和天气变化时都很有画面感。游客可以坐下休息，感受海风和城市远景。', '建议把这里作为轻松路线的核心停留点。拍照之外，也可以留出十几分钟不赶路，深圳湾的魅力就在这种开阔的海岸节奏里。')),
        guide_item('红树林方向', SHENZHEN_BAY_IMAGES['mangrove_direction'], 22.5360, 113.9670, 84, 30, '建议停留 30-50 分钟', '红树林方向适合补充生态观察，理解深圳湾不只是城市景观，也有湿地生态。', detail_copy('红树林方向让深圳湾公园从城市海岸转向生态观察。游客可以留意潮汐、水鸟、树木和湿地边界，理解这里不只是跑步和拍照的地方，也承担城市生态空间功能。', '建议安静观看，不要惊扰鸟类或进入非开放区域。带孩子同行时，这里很适合讲解城市与自然如何共存。')),
    ]
    route_map = build_route_map('深圳湾公园路线选择', '滨海慢行导览', SHENZHEN_BAY_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '滨海经典线', 'duration': '2.5h', 'distance': '3.0km', 'description': '沿滨海步道串联人才公园视角、大桥远眺和日出剧场。', 'stops': [0, 1, 2, 3]},
        {'id': 'easy', 'title': '轻松看海线', 'duration': '1.5h', 'distance': '1.6km', 'description': '少走路，重点看滨海步道和日出剧场。', 'stops': [0, 3]},
        {'id': 'eco', 'title': '湿地生态线', 'duration': '3.0h', 'distance': '3.5km', 'description': '从步道延伸到红树林方向，适合自然观察。', 'stops': [0, 1, 4]},
    ])
    return city_guide_post('深圳市', '深圳湾公园：沿滨海步道看海湾城市', '这是一条深圳湾公园正式旅游导览。深圳湾最适合从“海湾、城市天际线和湿地生态”三个角度来游览：一边是现代城区，一边是开阔水面，远处还有桥梁和红树林方向。建议根据体力选择步道长度，清晨和傍晚体验最好。正文下方地图可拖动、缩放，并可点击景点进入详情。', SHENZHEN_BAY_IMAGES, '深圳市南山区深圳湾公园', 22.5190, 113.9450, 2, 2600, 'bay_walker', 760, 26, 6000, guide_items, route_map)


def lianhuashan_park_post():
    guide_items = [
        guide_item('风筝广场', LIANHUASHAN_IMAGES['kite_square'], 22.5556, 114.0570, 28, 72, '建议停留 20-35 分钟', '风筝广场是莲花山公园轻松开场，适合先感受市民公园氛围。', detail_copy('风筝广场是莲花山公园很有生活气息的地方。这里常能看到散步、放风筝和休闲的人群，游客可以先从这里感受深圳市民公园的日常节奏。', '建议把这里作为上山前的缓冲点。整理路线、补水后再沿步道前往山顶广场，体验会更从容。')),
        guide_item('山顶步道', LIANHUASHAN_IMAGES['summit_trail'], 22.5586, 114.0588, 45, 55, '建议停留 25-45 分钟', '山顶步道坡度适中，适合边走边看绿地与城市之间的变化。', detail_copy('山顶步道是莲花山公园从市民绿地过渡到城市观景的关键路段。随着海拔抬升，树木、坡道和城市建筑会逐渐发生变化，游客能感受到深圳中心区被公园绿地包裹的一面。', '建议放慢速度，不必赶路。莲花山不以艰难登山取胜，而是以轻松、开放和城市视野见长。')),
        guide_item('山顶广场', LIANHUASHAN_IMAGES['summit_square'], 22.5602, 114.0597, 56, 40, '建议停留 25-40 分钟', '山顶广场是莲花山公园核心节点，适合俯瞰福田中心区。', detail_copy('山顶广场是莲花山公园最重要的停留点。来到这里，游客可以俯瞰福田中心区、市民中心和周边高楼，深圳的城市轴线和现代化形象会非常直观。', '建议选择能见度好的时间上山。站在广场边缘看城市，再回头看公园绿地，会更容易理解莲花山为什么是深圳中心区的重要公共空间。')),
        guide_item('城市观景台', LIANHUASHAN_IMAGES['city_view'], 22.5606, 114.0600, 66, 34, '建议停留 20-35 分钟', '城市观景台适合拍摄市民中心和福田天际线，是路线的视觉高潮。', detail_copy('城市观景台是拍摄深圳中心区的好位置。这里能把市民中心、深南大道方向和周边高楼纳入视野，适合游客理解深圳作为年轻城市的空间尺度。', '建议不要只拍一张全景。可以观察道路、广场、建筑和公园之间的关系，深圳的城市规划感会更清楚。')),
        guide_item('湖区与草坪', LIANHUASHAN_IMAGES['lake_lawn'], 22.5542, 114.0610, 72, 67, '建议停留 30-50 分钟', '湖区与草坪适合作为下山后的放松段，适合亲子和轻松散步。', detail_copy('湖区与草坪让莲花山公园从城市观景回到休闲空间。这里适合下山后放松，也适合同行有孩子或长辈时调整节奏。', '建议把它放在路线后半段。看完山顶城市景观后，在草坪和湖边慢走，会让整趟游览更完整。')),
    ]
    route_map = build_route_map('莲花山公园路线选择', '中心区登高导览', LIANHUASHAN_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '登高观城线', 'duration': '2.0h', 'distance': '2.0km', 'description': '风筝广场、山顶步道、山顶广场和城市观景台串联。', 'stops': [0, 1, 2, 3]},
        {'id': 'family', 'title': '轻松亲子线', 'duration': '1.5h', 'distance': '1.5km', 'description': '以风筝广场、湖区和草坪为主，节奏轻松。', 'stops': [0, 4]},
        {'id': 'complete', 'title': '公园完整线', 'duration': '2.8h', 'distance': '2.8km', 'description': '登山观景后回到湖区草坪，完整体验公园。', 'stops': [0, 1, 2, 3, 4]},
    ])
    return city_guide_post('深圳市', '深圳莲花山公园：登上中心区绿丘俯瞰城市', '这是一条深圳莲花山公园正式旅游导览。莲花山的重点不是高难度爬山，而是在城市中心用一段轻松步道登高看深圳：山下是市民公园，山上能俯瞰福田中心区和城市轴线。建议从风筝广场出发，沿步道到山顶广场，再根据体力回到湖区和草坪。正文下方地图可拖动、缩放，并可点击景点进入详情。', LIANHUASHAN_IMAGES, '深圳市福田区红荔路6030号', 22.5580, 114.0590, 2, 2300, 'lotus_hill_guide', 735, 24, 5700, guide_items, route_map)


def dapeng_fortress_post():
    guide_items = [
        guide_item('南门城楼', DAPENG_FORTRESS_IMAGES['south_gate'], 22.5988, 114.5097, 50, 82, '建议停留 20-35 分钟', '南门城楼是大鹏所城的经典入口，适合先建立古城防御和街巷方向感。', detail_copy('南门城楼是进入大鹏所城时最有仪式感的位置。游客可以先观察城门、城墙和城内街巷的关系，理解这里曾经作为海防所城的功能，而不只是普通古村落。', '建议在城门前停留一会儿，先看城楼和门洞，再进入街巷。这样后面看将军第、古井和民居时，会更容易把它们放回所城格局中。')),
        guide_item('赖恩爵将军第', DAPENG_FORTRESS_IMAGES['general_house'], 22.5980, 114.5085, 36, 50, '建议停留 25-45 分钟', '将军第适合理解大鹏所城的海防人物和家族空间，是文化重点。', detail_copy('赖恩爵将军第是大鹏所城中很值得停留的人文节点。它让游客从城门和街巷进入具体人物与家族空间，理解这座所城与海防、家族和地方历史之间的联系。', '建议认真看建筑格局和说明，不要只把它当成老房子拍照。将军第能让大鹏所城的历史叙事更加具体。')),
        guide_item('古城街巷', DAPENG_FORTRESS_IMAGES['old_lanes'], 22.5985, 114.5089, 56, 55, '建议停留 35-60 分钟', '古城街巷适合慢走，观察岭南民居、巷道尺度和生活痕迹。', detail_copy('古城街巷是大鹏所城最适合慢走的部分。相比单个景点，街巷连续的尺度、墙面、门楼和转角更能体现古城气质。游客可以从巷道宽窄、院落入口和建筑材料中感受历史街区。', '建议不要只沿最热闹的商业路走。可以选择一两条较安静的巷子慢慢看，注意不打扰居民和店铺正常生活。')),
        guide_item('大鹏粮仓', DAPENG_FORTRESS_IMAGES['granary'], 22.5979, 114.5094, 68, 40, '建议停留 15-25 分钟', '大鹏粮仓适合补充所城生活和军事后勤背景，让古城功能更完整。', detail_copy('粮仓类空间能帮助游客理解所城不只是城墙和官署，也需要粮食、后勤和日常管理支撑。来到这里时，可以把它和城门、街巷、将军第联系起来看。', '建议作为中途补充节点，不必停留太久。它的价值在于让游客看到古城运行的实际层面。')),
        guide_item('较场尾方向', DAPENG_FORTRESS_IMAGES['jiaochangwei_direction'], 22.5966, 114.5075, 78, 68, '建议停留 30-60 分钟', '较场尾方向适合作为路线延伸，把古城游览转向海边休闲。', detail_copy('较场尾方向适合在看完大鹏所城后延伸。古城提供历史和街巷体验，海边则让行程变得轻松，适合休息、吃饭或看海。', '建议根据时间决定是否加入。只看古城约两小时即可，如果想完整体验大鹏半日游，可以把较场尾放在后段。')),
    ]
    route_map = build_route_map('大鹏所城路线选择', '海防古城街巷导览', DAPENG_FORTRESS_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '古城经典线', 'duration': '2.0h', 'distance': '1.4km', 'description': '南门城楼、将军第、古城街巷和粮仓串联。', 'stops': [0, 1, 2, 3]},
        {'id': 'deep', 'title': '海防历史线', 'duration': '2.8h', 'distance': '1.8km', 'description': '重点看城门、将军第和古城功能空间，适合历史爱好者。', 'stops': [0, 1, 3, 2]},
        {'id': 'coast', 'title': '古城海边线', 'duration': '3.5h', 'distance': '2.8km', 'description': '古城游览后延伸较场尾方向，适合半日慢游。', 'stops': [0, 1, 2, 4]},
    ])
    return city_guide_post('深圳市', '深圳大鹏所城：沿海防古城走进岭南街巷', '这是一条深圳大鹏所城正式旅游导览。大鹏所城适合从“海防古城”理解：城门、街巷、将军第、粮仓和周边海岸共同构成它的历史气质。建议先从南门城楼进入，慢走古城街巷，再根据时间延伸到较场尾方向。正文下方地图可拖动、缩放，并可点击景点进入详情。', DAPENG_FORTRESS_IMAGES, '深圳市龙岗区大鹏所城', 22.5985, 114.5090, 2, 1900, 'dapeng_guard', 690, 22, 5200, guide_items, route_map)


def beihai_park_post():
    guide_items = [
        guide_item('南门入口', BEIHAI_PARK_IMAGES['south_gate'], 39.9245, 116.3965, 54, 84, '建议停留 10-20 分钟', '南门入口适合作为北海公园路线起点，先建立湖面、琼华岛和白塔方向。', detail_copy('北海公园从南门进入后，游客很快能感受到湖面、岛屿和皇家园林之间的关系。这里适合先整理方向：湖心是琼华岛和白塔，北岸还有九龙壁等人文节点。', '建议不要一进园就急着上岛。先在入口附近看一眼湖面和白塔位置，再决定是先登岛还是沿湖慢走。')),
        guide_item('琼华岛', BEIHAI_PARK_IMAGES['qionghua_island'], 39.9258, 116.3907, 48, 56, '建议停留 30-50 分钟', '琼华岛是北海公园核心，适合边登高边看湖面和园林空间。', detail_copy('琼华岛是北海公园的空间中心。游客登岛过程中会不断看到湖面、树木、坡道和殿宇之间的变化，皇家园林的层次感会逐渐展开。', '建议放慢脚步上行，不要只把白塔当作终点。沿途的视线变化、台阶和建筑位置同样值得看。')),
        guide_item('白塔', BEIHAI_PARK_IMAGES['white_pagoda'], 39.9264, 116.3900, 50, 42, '建议停留 25-40 分钟', '白塔是北海最具辨识度的景观，也是俯看湖面和北京老城的重点。', detail_copy('白塔是北海公园最具标志性的景观。站在塔附近，可以把湖面、岛屿、城墙方向和北京老城的尺度联系起来。它不只是拍照背景，也是整座园林的视觉中心。', '建议在这里停留一段时间，选择不同方向看湖面和周边。天气好时视野更开阔，傍晚光线也很适合拍照。'), [BEIHAI_PARK_IMAGES['white_pagoda'], BEIHAI_PARK_IMAGES['white_pagoda_detail']]),
        guide_item('九龙壁', BEIHAI_PARK_IMAGES['nine_dragon_wall'], 39.9309, 116.3929, 72, 26, '建议停留 20-35 分钟', '九龙壁是北岸重要文化节点，适合观察琉璃工艺和龙纹细节。', detail_copy('九龙壁是北海公园北岸很值得专门观看的景点。琉璃色彩、龙纹姿态和壁面尺度都很有视觉冲击力，适合游客近距离观察细节。', '建议不要只拍远景，可以从左到右慢慢看龙身、云纹和色彩变化。把它和白塔、湖面放在同一条路线中，会让北海既有园林景观，也有工艺细节。')),
        guide_item('五龙亭', BEIHAI_PARK_IMAGES['five_dragon_pavilions'], 39.9313, 116.3907, 66, 38, '建议停留 20-35 分钟', '五龙亭临湖而建，适合休息、看湖面和回望白塔。', detail_copy('五龙亭是北海湖边很适合休息的节点。亭子、水面和远处白塔形成经典园林视线，游客可以在这里把登岛和沿湖两种体验连接起来。', '建议把五龙亭放在路线后半段。走累后在这里看湖面，会比匆匆经过更舒服。'), [BEIHAI_PARK_IMAGES['five_dragon_pavilions'], BEIHAI_PARK_IMAGES['five_dragon_pavilions_detail']]),
        guide_item('北海湖面', BEIHAI_PARK_IMAGES['lake_view'], 39.9275, 116.3935, 39, 68, '建议停留 30-60 分钟', '北海湖面适合作为路线放松段，可沿湖慢走或视情况选择游船。', detail_copy('北海湖面是整座公园最能放慢节奏的部分。无论是沿湖步行还是选择游船，游客都能从不同角度看白塔、琼华岛和岸边建筑。', '建议把湖面放在最后收束。看过白塔和九龙壁后，再沿湖慢走，会更容易感受到北海作为皇家园林和城市公园的双重气质。')),
    ]
    route_map = build_route_map('北海公园路线选择', '皇家湖岛园林导览', BEIHAI_PARK_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '湖岛经典线', 'duration': '2.5h', 'distance': '2.2km', 'description': '南门、琼华岛、白塔、五龙亭和湖面串联。', 'stops': [0, 1, 2, 4, 5]},
        {'id': 'culture', 'title': '皇家文化线', 'duration': '3.2h', 'distance': '2.8km', 'description': '登白塔后到九龙壁和五龙亭，兼顾景观与工艺。', 'stops': [0, 1, 2, 3, 4]},
        {'id': 'easy', 'title': '轻松湖畔线', 'duration': '1.8h', 'distance': '1.6km', 'description': '少登高，以湖面、五龙亭和白塔远景为主。', 'stops': [0, 5, 4]},
    ])
    return city_guide_post('北京', '北海公园：沿湖岛白塔走进皇家园林', '这是一条北京北海公园正式旅游导览。北海适合从“湖面、琼华岛、白塔和北岸文化节点”来理解：它既是皇家园林，也是今天北京市中心很适合慢走的湖畔公园。建议从南门进入，先看湖面和琼华岛，再登白塔，最后沿湖去九龙壁和五龙亭。正文下方地图可拖动、缩放，并可点击景点进入详情。', BEIHAI_PARK_IMAGES, '北京市西城区文津街1号', 39.9280, 116.3907, 3, 2400, 'beihai_guide', 720, 25, 5600, guide_items, route_map)


def yonghe_temple_post():
    guide_items = [
        guide_item('昭泰门', YONGHE_TEMPLE_IMAGES['zhaotai_gate'], 39.9470, 116.4096, 50, 82, '建议停留 10-20 分钟', '昭泰门适合作为雍和宫参观开场，先建立中轴线和礼佛空间秩序。', detail_copy('昭泰门是进入雍和宫后很适合整理方向的位置。游客可以先感受中轴线、院落和殿宇之间层层递进的关系，理解这里不是单点建筑，而是一组庄重的寺院空间。', '建议从入口开始保持安静，不要只顾拍照。先看清路线和礼佛动线，再继续向北参观，会更符合现场氛围。')),
        guide_item('雍和门', YONGHE_TEMPLE_IMAGES['yonghe_gate'], 39.9474, 116.4096, 50, 64, '建议停留 15-25 分钟', '雍和门是中轴线上的重要节点，适合观察殿门、院落和香火空间。', detail_copy('雍和门位于雍和宫中轴线上，游客走到这里时会明显感到空间由入口逐渐转入更核心的礼佛区域。殿门、院落和香火共同营造出庄重氛围。', '参观时注意现场秩序，尊重礼佛游客。可以站在院落边缘观察建筑尺度和人流动线，不建议长时间挡在正中。')),
        guide_item('雍和宫大殿', YONGHE_TEMPLE_IMAGES['main_hall'], 39.9478, 116.4096, 50, 48, '建议停留 20-35 分钟', '雍和宫大殿是核心殿宇之一，适合理解清代皇家寺院的空间气质。', detail_copy('雍和宫大殿是参观中的重点殿宇。游客可以从殿宇尺度、屋顶、匾额和院落位置感受清代皇家寺院的庄重气质。这里的观看重点不是热闹，而是秩序、礼仪和空间层次。', '建议在殿外安静观看，进入殿内时遵守现场规定。不要强行拍摄不允许拍照的空间，把注意力放在建筑、气味、声音和人的礼佛行为上。')),
        guide_item('永佑殿', YONGHE_TEMPLE_IMAGES['yongyou_hall'], 39.9481, 116.4096, 50, 34, '建议停留 15-25 分钟', '永佑殿适合补充雍和宫从王府到寺院的历史层次。', detail_copy('永佑殿让游客继续沿中轴线深入。雍和宫原本有王府背景，后来成为藏传佛教寺院，这种身份转变让它在北京寺庙中很特别。', '建议把这里作为中段停留点，联系前后殿宇一起看。单独看一座殿可能印象有限，沿中轴连续观看会更完整。')),
        guide_item('法轮殿', YONGHE_TEMPLE_IMAGES['falun_hall'], 39.9485, 116.4096, 50, 22, '建议停留 20-35 分钟', '法轮殿是理解藏传佛教艺术和寺院仪式感的重要节点。', detail_copy('法轮殿是雍和宫中很有藏传佛教特色的空间之一。游客可以观察建筑装饰、供奉内容和殿宇氛围，理解雍和宫与普通汉传寺院在视觉和仪式感上的差异。', '建议安静观看，尽量不打扰礼佛和参观秩序。这里适合慢看，不适合匆匆拍照就离开。')),
        guide_item('万福阁', YONGHE_TEMPLE_IMAGES['wanfu_pavilion'], 39.9489, 116.4096, 50, 10, '建议停留 25-40 分钟', '万福阁是雍和宫路线的高潮，适合作为中轴线收束。', detail_copy('万福阁是雍和宫参观中非常重要的高潮节点。走到这里时，游客已经从入口、殿门和多重殿宇一路向北推进，空间层层递进的感受会非常清楚。', '建议把万福阁作为参观终点来慢看。到达后可以回想刚刚经过的每一重院落，雍和宫的游览体验正是在这种递进中形成的。')),
    ]
    route_map = build_route_map('雍和宫路线选择', '皇家寺院中轴导览', YONGHE_TEMPLE_IMAGES['overview_map'], [
        {'id': 'classic', 'title': '中轴礼佛线', 'duration': '2.0h', 'distance': '1.0km', 'description': '昭泰门、雍和门、大殿、法轮殿和万福阁串联。', 'stops': [0, 1, 2, 4, 5]},
        {'id': 'history', 'title': '皇家寺院线', 'duration': '2.5h', 'distance': '1.2km', 'description': '重点理解王府、皇家寺院和藏传佛教空间。', 'stops': [0, 2, 3, 4, 5]},
        {'id': 'easy', 'title': '安静慢游线', 'duration': '1.5h', 'distance': '0.8km', 'description': '少走回头路，按中轴线安静参观主要殿宇。', 'stops': [0, 1, 2, 5]},
    ])
    return city_guide_post('北京', '雍和宫：沿中轴殿宇感受皇家寺院', '这是一条北京雍和宫正式旅游导览。雍和宫适合沿中轴线慢慢参观：从昭泰门到雍和门、雍和宫大殿、法轮殿和万福阁，空间逐层递进，既有清代皇家建筑气质，也有藏传佛教寺院氛围。建议保持安静、尊重礼佛秩序，把重点放在院落、殿宇和整体氛围上。正文下方地图可拖动、缩放，并可点击景点进入详情。', YONGHE_TEMPLE_IMAGES, '北京市东城区雍和宫大街12号', 39.9480, 116.4096, 2, 2100, 'lama_temple_guide', 710, 23, 5500, guide_items, route_map)



def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    ensure_schema(c)

    users = [
        ('palace_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🏯'}, ensure_ascii=False)),
        ('travel_boy', '123456', json.dumps({'type': 'preset', 'emoji': '🧳'}, ensure_ascii=False)),
        ('beijing_fan', '123456', json.dumps({'type': 'preset', 'emoji': '🏮'}, ensure_ascii=False)),
        ('explorer', '123456', json.dumps({'type': 'preset', 'emoji': '🔎'}, ensure_ascii=False)),
        ('nature_lover', '123456', json.dumps({'type': 'preset', 'emoji': '🌿'}, ensure_ascii=False)),
        ('culture_seeker', '123456', json.dumps({'type': 'preset', 'emoji': '🎨'}, ensure_ascii=False)),
        ('canton_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🌉'}, ensure_ascii=False)),
        ('mountain_guide', '123456', json.dumps({'type': 'preset', 'emoji': '⛰️'}, ensure_ascii=False)),
        ('lingnan_curator', '123456', json.dumps({'type': 'preset', 'emoji': '🪭'}, ensure_ascii=False)),
        ('city_history_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🏛️'}, ensure_ascii=False)),
        ('shamian_walker', '123456', json.dumps({'type': 'preset', 'emoji': '🚶'}, ensure_ascii=False)),
        ('shanghai_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🌃'}, ensure_ascii=False)),
        ('garden_story', '123456', json.dumps({'type': 'preset', 'emoji': '🌸'}, ensure_ascii=False)),
        ('museum_curator', '123456', json.dumps({'type': 'preset', 'emoji': '🏺'}, ensure_ascii=False)),
        ('bay_walker', '123456', json.dumps({'type': 'preset', 'emoji': '🌊'}, ensure_ascii=False)),
        ('lotus_hill_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🪷'}, ensure_ascii=False)),
        ('dapeng_guard', '123456', json.dumps({'type': 'preset', 'emoji': '🏰'}, ensure_ascii=False)),
        ('beihai_guide', '123456', json.dumps({'type': 'preset', 'emoji': '⛲'}, ensure_ascii=False)),
        ('lama_temple_guide', '123456', json.dumps({'type': 'preset', 'emoji': '🛕'}, ensure_ascii=False)),
    ]

    c.executemany(
        '''
        INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
            password = excluded.password,
            avatar = excluded.avatar
        WHERE users.password = '123456'
        ''',
        users
    )

    posts = [
        forbidden_city_post(),
        summer_palace_post(),
        temple_of_heaven_post(),
        badaling_great_wall_post(),
        old_summer_palace_post(),
        canton_tower_post(),
        baiyun_mountain_post(),
        chen_clan_academy_post(),
        yuexiu_park_post(),
        shamian_island_post(),
        shanghai_bund_post(),
        yu_garden_post(),
        shanghai_museum_post(),
        shenzhen_bay_park_post(),
        lianhuashan_park_post(),
        dapeng_fortress_post(),
        beihai_park_post(),
        yonghe_temple_post(),
    ]

    for title_pattern in ('故宫博物院%', '颐和园%', '天坛公园%', '八达岭长城%', '圆明园遗址公园%', '广州塔%', '白云山%', '陈家祠%', '越秀公园%', '沙面岛%', '上海外滩%', '上海豫园%', '上海博物馆%', '深圳湾公园%', '深圳莲花山公园%', '深圳大鹏所城%', '北海公园%', '雍和宫%'):
        c.execute('DELETE FROM posts WHERE title LIKE ?', (title_pattern,))

    for post, audio_slug in zip(posts, GUIDE_AUDIO_SLUGS):
        post = normalize_post_tuple(post)
        post, audio_url_en = attach_audio_paths(post, audio_slug)
        c.execute('DELETE FROM posts WHERE title = ?', (post[0],))
        c.execute('''
            INSERT INTO posts
            (title, content, photos, location, latitude, longitude, duration, people, author, publish_time, likes, comments, views, city, audio_url, audio_url_en, guide_items, route_map)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', post[:15] + (audio_url_en,) + post[15:])

    conn.commit()
    conn.close()

    print('北京 7 个、广州 5 个、上海 3 个、深圳 3 个导览演示帖插入成功')
    print('图片来源：')
    for source in IMAGE_SOURCES:
        print(f"- {source['file']}: {source['source']} ({source['author']}, {source['license']})")


if __name__ == '__main__':
    main()
