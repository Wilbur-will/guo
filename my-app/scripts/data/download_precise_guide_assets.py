import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


BOOTSTRAP_ROOT = Path(__file__).resolve().parents[2]
if str(BOOTSTRAP_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOTSTRAP_ROOT))

from app.paths import APP_ROOT

GUIDE_IMAGES = APP_ROOT / "app" / "catalog" / "guide_images.py"
ASSET_ROOT = APP_ROOT / "assets" / "guides"
USER_AGENT = "guo-chuang-local-guide-assets/1.0"


ASSETS = [
    ("TEMPLE_OF_HEAVEN_IMAGES", "imperial_hall_of_heaven", "beijing/temple-of-heaven/imperial-hall-of-heaven.jpg", ["Temple of Heaven Imperial Hall of Heaven Beijing", "皇乾殿 天坛"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "danbi_bridge", "beijing/temple-of-heaven/danbi-bridge.jpg", ["Temple of Heaven Danbi Bridge", "天坛 丹陛桥"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "imperial_vault", "beijing/temple-of-heaven/imperial-vault.jpg", ["Imperial Vault of Heaven Temple of Heaven", "皇穹宇 天坛"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "echo_wall", "beijing/temple-of-heaven/echo-wall.jpg", ["Echo Wall Temple of Heaven", "天坛 回音壁"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "three_echo_stones", "beijing/temple-of-heaven/three-echo-stones.jpg", ["Three Echo Stones Temple of Heaven", "天坛 三音石"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "circular_mound_altar", "beijing/temple-of-heaven/circular-mound-altar.jpg", ["Circular Mound Altar Temple of Heaven", "天坛 圜丘坛"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "palace_of_abstinence", "beijing/temple-of-heaven/palace-of-abstinence.jpg", ["Palace of Abstinence Temple of Heaven", "天坛 斋宫"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "divine_music_administration", "beijing/temple-of-heaven/divine-music-administration.jpg", ["Divine Music Administration Temple of Heaven", "天坛 神乐署"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "seven_star_stones", "beijing/temple-of-heaven/seven-star-stones.jpg", ["Seven Star Stones Temple of Heaven", "天坛 七星石"]),
    ("TEMPLE_OF_HEAVEN_IMAGES", "ancient_cypress_grove", "beijing/temple-of-heaven/ancient-cypress-grove.jpg", ["Temple of Heaven ancient cypress grove", "天坛 古柏林"]),

    ("BADALING_IMAGES", "pass_city", "beijing/badaling-great-wall/pass-city.jpg", ["Badaling Great Wall pass city", "八达岭 关城"]),
    ("BADALING_IMAGES", "wangjing_stone", "beijing/badaling-great-wall/wangjing-stone.jpg", ["Badaling Wangjing Stone", "八达岭 望京石"]),
    ("BADALING_IMAGES", "hero_tablet", "beijing/badaling-great-wall/hero-tablet.jpg", ["Badaling Great Wall hero tablet", "八达岭 好汉碑"]),
    ("BADALING_IMAGES", "hero_slope", "beijing/badaling-great-wall/hero-slope.jpg", ["Badaling Great Wall hero slope", "八达岭 好汉坡"]),
    ("BADALING_IMAGES", "north_tower_1", "beijing/badaling-great-wall/north-tower-1.jpg", ["Badaling Great Wall North first tower", "八达岭 北一楼"]),
    ("BADALING_IMAGES", "north_tower_2", "beijing/badaling-great-wall/north-tower-2.jpg", ["Badaling Great Wall North second tower", "八达岭 北二楼"]),
    ("BADALING_IMAGES", "north_tower_4", "beijing/badaling-great-wall/north-tower-4.jpg", ["Badaling Great Wall North fourth tower", "八达岭 北四楼"]),
    ("BADALING_IMAGES", "north_tower_8", "beijing/badaling-great-wall/north-tower-8.jpg", ["Badaling Great Wall North eighth tower", "八达岭 北八楼"]),
    ("BADALING_IMAGES", "south_tower_1", "beijing/badaling-great-wall/south-tower-1.jpg", ["Badaling Great Wall South first tower", "八达岭 南一楼"]),
    ("BADALING_IMAGES", "south_tower_4", "beijing/badaling-great-wall/south-tower-4.jpg", ["Badaling Great Wall South fourth tower", "八达岭 南四楼"]),
    ("BADALING_IMAGES", "great_wall_museum", "beijing/badaling-great-wall/great-wall-museum.jpg", ["Great Wall Museum Badaling", "八达岭 长城博物馆"]),
    ("BADALING_IMAGES", "zhan_tianyou_memorial", "beijing/badaling-great-wall/zhan-tianyou-memorial.jpg", ["Zhan Tianyou Memorial Hall Badaling", "八达岭 詹天佑纪念馆"]),

    ("OLD_SUMMER_PALACE_IMAGES", "zhengda_guangming", "beijing/old-summer-palace/zhengda-guangming.jpg", ["Old Summer Palace Zhengda Guangming ruins", "圆明园 正大光明遗址"]),
    ("OLD_SUMMER_PALACE_IMAGES", "jiuzhou_qingyan", "beijing/old-summer-palace/jiuzhou-qingyan.jpg", ["Old Summer Palace Jiuzhou Qingyan", "圆明园 九州清晏遗址"]),
    ("OLD_SUMMER_PALACE_IMAGES", "fuhai", "beijing/old-summer-palace/fuhai.jpg", ["Old Summer Palace Fuhai lake", "圆明园 福海"]),
    ("OLD_SUMMER_PALACE_IMAGES", "pengdao_yaotai", "beijing/old-summer-palace/pengdao-yaotai.jpg", ["Old Summer Palace Pengdao Yaotai", "圆明园 蓬岛瑶台"]),
    ("OLD_SUMMER_PALACE_IMAGES", "wanfang_anhe", "beijing/old-summer-palace/wanfang-anhe.jpg", ["Old Summer Palace Wanfang Anhe", "圆明园 万方安和"]),
    ("OLD_SUMMER_PALACE_IMAGES", "danbo_ningjing", "beijing/old-summer-palace/danbo-ningjing.jpg", ["Old Summer Palace Danbo Ningjing", "圆明园 澹泊宁静"]),
    ("OLD_SUMMER_PALACE_IMAGES", "changchun_garden", "beijing/old-summer-palace/changchun-garden.jpg", ["Old Summer Palace Changchun Garden", "圆明园 长春园"]),
    ("OLD_SUMMER_PALACE_IMAGES", "western_mansions", "beijing/old-summer-palace/western-mansions.jpg", ["Old Summer Palace Western Mansions ruins", "圆明园 西洋楼遗址"]),
    ("OLD_SUMMER_PALACE_IMAGES", "yuanyingguan", "beijing/old-summer-palace/yuanyingguan.jpg", ["Old Summer Palace Yuanyingguan ruins", "圆明园 远瀛观遗址"]),
    ("OLD_SUMMER_PALACE_IMAGES", "fangwaiguan", "beijing/old-summer-palace/fangwaiguan.jpg", ["Old Summer Palace Fangwaiguan ruins", "圆明园 方外观遗址"]),
    ("OLD_SUMMER_PALACE_IMAGES", "huanghuazhen", "beijing/old-summer-palace/huanghuazhen.jpg", ["Old Summer Palace Huanghuazhen maze", "圆明园 黄花阵"]),
    ("OLD_SUMMER_PALACE_IMAGES", "exhibition_hall", "beijing/old-summer-palace/exhibition-hall.jpg", ["Old Summer Palace exhibition hall", "圆明园 展览馆"]),

    ("GUANGZHOU_TOWER_IMAGES", "ferris_wheel", "guangzhou/canton-tower/ferris-wheel.jpg", ["Canton Tower bubble tram ferris wheel", "广州塔 摩天轮"]),
    ("GUANGZHOU_TOWER_IMAGES", "sky_drop", "guangzhou/canton-tower/sky-drop.jpg", ["Canton Tower sky drop", "广州塔 极速云霄"]),
    ("GUANGZHOU_TOWER_IMAGES", "pearl_river_night", "guangzhou/canton-tower/pearl-river-night.jpg", ["Pearl River night Canton Tower", "珠江夜景 广州塔"]),

    ("BAIYUN_MOUNTAIN_IMAGES", "yuntai_garden", "guangzhou/baiyun-mountain/yuntai-garden.jpg", ["Yuntai Garden Baiyun Mountain Guangzhou", "白云山 云台花园"]),
    ("BAIYUN_MOUNTAIN_IMAGES", "nengren_temple", "guangzhou/baiyun-mountain/nengren-temple.jpg", ["Nengren Temple Baiyun Mountain Guangzhou", "白云山 能仁寺"]),
    ("BAIYUN_MOUNTAIN_IMAGES", "mingchun_valley", "guangzhou/baiyun-mountain/mingchun-valley.jpg", ["Mingchun Valley Baiyun Mountain Guangzhou", "白云山 鸣春谷"]),
    ("BAIYUN_MOUNTAIN_IMAGES", "summit_square", "guangzhou/baiyun-mountain/summit-square.jpg", ["Baiyun Mountain summit square Guangzhou", "白云山 山顶广场"]),
    ("BAIYUN_MOUNTAIN_IMAGES", "mingzhu_tower", "guangzhou/baiyun-mountain/mingzhu-tower.jpg", ["Mingzhu Tower Baiyun Mountain Guangzhou", "白云山 明珠楼"]),

    ("CHEN_CLAN_ACADEMY_IMAGES", "head_gate", "guangzhou/chen-clan-academy/head-gate.jpg", ["Chen Clan Ancestral Hall entrance gate Guangzhou", "陈家祠 头门"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "juxian_hall", "guangzhou/chen-clan-academy/juxian-hall.jpg", ["Chen Clan Ancestral Hall Juxian Hall", "陈家祠 聚贤堂"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "middle_courtyard", "guangzhou/chen-clan-academy/middle-courtyard.jpg", ["Chen Clan Ancestral Hall courtyard Guangzhou", "陈家祠 院落"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "wood_carving", "guangzhou/chen-clan-academy/wood-carving.jpg", ["Chen Clan Ancestral Hall wood carving", "陈家祠 木雕"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "brick_carving", "guangzhou/chen-clan-academy/brick-carving.jpg", ["Chen Clan Ancestral Hall brick carving", "陈家祠 砖雕"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "pottery_plaster", "guangzhou/chen-clan-academy/pottery-plaster.jpg", ["Chen Clan Ancestral Hall pottery ridge plaster sculpture", "陈家祠 陶塑 灰塑"]),
    ("CHEN_CLAN_ACADEMY_IMAGES", "rear_gallery", "guangzhou/chen-clan-academy/rear-gallery.jpg", ["Chen Clan Ancestral Hall exhibition hall", "陈家祠 展厅"]),

    ("YUEXIU_PARK_IMAGES", "ming_city_wall", "guangzhou/yuexiu-park/ming-city-wall.jpg", ["Yuexiu Park Ming city wall Guangzhou", "越秀公园 明代古城墙"]),
    ("YUEXIU_PARK_IMAGES", "sun_yat_sen_monument", "guangzhou/yuexiu-park/sun-yat-sen-monument.jpg", ["Sun Yat-sen Monument Yuexiu Park Guangzhou", "越秀公园 中山纪念碑"]),
    ("YUEXIU_PARK_IMAGES", "lake_area", "guangzhou/yuexiu-park/lake-area.jpg", ["Yuexiu Park lake Guangzhou", "越秀公园 湖"]),

    ("SHAMIAN_ISLAND_IMAGES", "main_street", "guangzhou/shamian-island/main-street.jpg", ["Shamian Island main street Guangzhou", "沙面大街"]),
    ("SHAMIAN_ISLAND_IMAGES", "lourdes_chapel", "guangzhou/shamian-island/lourdes-chapel.jpg", ["Our Lady of Lourdes Chapel Shamian Guangzhou", "沙面 露德圣母堂"]),
    ("SHAMIAN_ISLAND_IMAGES", "christ_church", "guangzhou/shamian-island/christ-church.jpg", ["Shamian Christ Church Guangzhou", "沙面 基督堂"]),
    ("SHAMIAN_ISLAND_IMAGES", "former_consulates", "guangzhou/shamian-island/former-consulates.jpg", ["Shamian former consulate buildings Guangzhou", "沙面 旧领事馆"]),
    ("SHAMIAN_ISLAND_IMAGES", "riverfront", "guangzhou/shamian-island/riverfront.jpg", ["Shamian Island riverfront Pearl River Guangzhou", "沙面 白鹅潭 江边"]),
    ("SHAMIAN_ISLAND_IMAGES", "tree_lanes", "guangzhou/shamian-island/tree-lanes.jpg", ["Shamian Island tree lined street Guangzhou", "沙面 古树 街巷"]),

    ("SHANGHAI_BUND_IMAGES", "bund_origin", "shanghai/bund/bund-origin.jpg", ["Waitanyuan Bund origin Shanghai", "外滩源 上海"]),
    ("SHANGHAI_BUND_IMAGES", "international_buildings", "shanghai/bund/international-buildings.jpg", ["The Bund international architecture Shanghai", "外滩 万国建筑群"]),
    ("SHANGHAI_BUND_IMAGES", "huangpu_river_view", "shanghai/bund/huangpu-river-view.jpg", ["Huangpu River promenade Bund Shanghai", "外滩 黄浦江 观景带"]),
    ("SHANGHAI_BUND_IMAGES", "chenyi_square", "shanghai/bund/chenyi-square.jpg", ["Chen Yi Square Bund Shanghai", "外滩 陈毅广场"]),
    ("SHANGHAI_BUND_IMAGES", "nanjing_road_entry", "shanghai/bund/nanjing-road-entry.jpg", ["Nanjing Road entrance Bund Shanghai", "南京东路 外滩口"]),

    ("YU_GARDEN_IMAGES", "nine_turning_bridge", "shanghai/yu-garden/nine-turning-bridge.jpg", ["Nine-turning Bridge Yu Garden Shanghai", "豫园 九曲桥"]),
    ("YU_GARDEN_IMAGES", "huxinting_teahouse", "shanghai/yu-garden/huxinting-teahouse.jpg", ["Huxinting Teahouse Yu Garden Shanghai", "豫园 湖心亭"]),
    ("YU_GARDEN_IMAGES", "sansui_hall", "shanghai/yu-garden/sansui-hall.jpg", ["Sansui Hall Yu Garden Shanghai", "豫园 三穗堂"]),
    ("YU_GARDEN_IMAGES", "great_rockery", "shanghai/yu-garden/great-rockery.jpg", ["Great Rockery Yu Garden Shanghai", "豫园 大假山"]),
    ("YU_GARDEN_IMAGES", "dianchun_hall", "shanghai/yu-garden/dianchun-hall.jpg", ["Dianchun Hall Yu Garden Shanghai", "豫园 点春堂"]),

    ("SHANGHAI_MUSEUM_IMAGES", "museum_hall", "shanghai/shanghai-museum/museum-hall.jpg", ["Shanghai Museum hall interior", "上海博物馆 大厅"]),
    ("SHANGHAI_MUSEUM_IMAGES", "bronze_gallery", "shanghai/shanghai-museum/bronze-gallery.jpg", ["Shanghai Museum bronze gallery", "上海博物馆 青铜器馆"]),
    ("SHANGHAI_MUSEUM_IMAGES", "ceramics_gallery", "shanghai/shanghai-museum/ceramics-gallery.jpg", ["Shanghai Museum ceramics gallery", "上海博物馆 陶瓷馆"]),
    ("SHANGHAI_MUSEUM_IMAGES", "calligraphy_gallery", "shanghai/shanghai-museum/calligraphy-gallery.jpg", ["Shanghai Museum calligraphy gallery", "上海博物馆 书法馆"]),
    ("SHANGHAI_MUSEUM_IMAGES", "painting_gallery", "shanghai/shanghai-museum/painting-gallery.jpg", ["Shanghai Museum painting gallery", "上海博物馆 绘画馆"]),
    ("SHANGHAI_MUSEUM_IMAGES", "jade_gallery", "shanghai/shanghai-museum/jade-gallery.jpg", ["Shanghai Museum jade gallery", "上海博物馆 玉器馆"]),

    ("SHENZHEN_BAY_IMAGES", "coastal_promenade", "shenzhen/shenzhen-bay-park/coastal-promenade.jpg", ["Shenzhen Bay Park coastal promenade", "深圳湾公园 滨海步道"]),
    ("SHENZHEN_BAY_IMAGES", "talent_park_view", "shenzhen/shenzhen-bay-park/talent-park-view.jpg", ["Shenzhen Talent Park skyline bay", "深圳 人才公园 后海 天际线"]),
    ("SHENZHEN_BAY_IMAGES", "shenzhen_bay_bridge", "shenzhen/shenzhen-bay-park/shenzhen-bay-bridge.jpg", ["Shenzhen Bay Bridge view", "深圳湾大桥 远眺"]),
    ("SHENZHEN_BAY_IMAGES", "sunrise_theater", "shenzhen/shenzhen-bay-park/sunrise-theater.jpg", ["Shenzhen Bay Park Sunrise Theater", "深圳湾公园 日出剧场"]),
    ("SHENZHEN_BAY_IMAGES", "mangrove_direction", "shenzhen/shenzhen-bay-park/mangrove-direction.jpg", ["Shenzhen Bay Mangrove Nature Reserve", "深圳湾 红树林"]),

    ("LIANHUASHAN_IMAGES", "kite_square", "shenzhen/lianhuashan-park/kite-square.jpg", ["Lianhuashan Park kite square Shenzhen", "莲花山公园 风筝广场"]),
    ("LIANHUASHAN_IMAGES", "summit_trail", "shenzhen/lianhuashan-park/summit-trail.jpg", ["Lianhuashan Park summit trail Shenzhen", "莲花山公园 山顶步道"]),
    ("LIANHUASHAN_IMAGES", "summit_square", "shenzhen/lianhuashan-park/summit-square.jpg", ["Lianhuashan Park summit square Shenzhen", "莲花山公园 山顶广场"]),
    ("LIANHUASHAN_IMAGES", "city_view", "shenzhen/lianhuashan-park/city-view.jpg", ["Lianhuashan Park Shenzhen city view Civic Center", "莲花山公园 城市观景台"]),
    ("LIANHUASHAN_IMAGES", "lake_lawn", "shenzhen/lianhuashan-park/lake-lawn.jpg", ["Lianhuashan Park lake lawn Shenzhen", "莲花山公园 湖区 草坪"]),

    ("DAPENG_FORTRESS_IMAGES", "south_gate", "shenzhen/dapeng-fortress/south-gate.jpg", ["Dapeng Fortress south gate Shenzhen", "大鹏所城 南门"]),
    ("DAPENG_FORTRESS_IMAGES", "general_house", "shenzhen/dapeng-fortress/general-house.jpg", ["Dapeng Fortress Lai Enjue General House", "大鹏所城 赖恩爵 将军第"]),
    ("DAPENG_FORTRESS_IMAGES", "old_lanes", "shenzhen/dapeng-fortress/old-lanes.jpg", ["Dapeng Fortress old lanes Shenzhen", "大鹏所城 古城街巷"]),
    ("DAPENG_FORTRESS_IMAGES", "granary", "shenzhen/dapeng-fortress/granary.jpg", ["Dapeng Fortress granary Shenzhen", "大鹏所城 粮仓"]),
    ("DAPENG_FORTRESS_IMAGES", "jiaochangwei_direction", "shenzhen/dapeng-fortress/jiaochangwei-direction.jpg", ["Jiaochangwei Dapeng Shenzhen beach", "较场尾 大鹏 深圳"]),

    ("BEIHAI_PARK_IMAGES", "south_gate", "beijing/beihai-park/south-gate.jpg", ["Beihai Park south gate Beijing", "北海公园 南门"]),
    ("BEIHAI_PARK_IMAGES", "qionghua_island", "beijing/beihai-park/qionghua-island.jpg", ["Qionghua Island Beihai Park Beijing", "北海公园 琼华岛"]),
    ("BEIHAI_PARK_IMAGES", "white_pagoda", "beijing/beihai-park/white-pagoda.jpg", ["Beihai Park White Dagoba Beijing", "北海公园 白塔"]),
    ("BEIHAI_PARK_IMAGES", "nine_dragon_wall", "beijing/beihai-park/nine-dragon-wall.jpg", ["Nine Dragon Wall Beihai Park Beijing", "北海公园 九龙壁"]),
    ("BEIHAI_PARK_IMAGES", "five_dragon_pavilions", "beijing/beihai-park/five-dragon-pavilions.jpg", ["Five Dragon Pavilions Beihai Park Beijing", "北海公园 五龙亭"]),
    ("BEIHAI_PARK_IMAGES", "lake_view", "beijing/beihai-park/lake-view.jpg", ["Beihai Park lake Beijing", "北海公园 湖面"]),

    ("YONGHE_TEMPLE_IMAGES", "zhaotai_gate", "beijing/yonghe-temple/zhaotai-gate.jpg", ["Yonghe Temple Zhaotai Gate Beijing", "雍和宫 昭泰门"]),
    ("YONGHE_TEMPLE_IMAGES", "yonghe_gate", "beijing/yonghe-temple/yonghe-gate.jpg", ["Yonghe Temple Yonghe Gate Beijing", "雍和门 雍和宫"]),
    ("YONGHE_TEMPLE_IMAGES", "main_hall", "beijing/yonghe-temple/main-hall.jpg", ["Yonghe Temple main hall Beijing", "雍和宫 大殿"]),
    ("YONGHE_TEMPLE_IMAGES", "yongyou_hall", "beijing/yonghe-temple/yongyou-hall.jpg", ["Yonghe Temple Yongyou Hall Beijing", "雍和宫 永佑殿"]),
    ("YONGHE_TEMPLE_IMAGES", "falun_hall", "beijing/yonghe-temple/falun-hall.jpg", ["Yonghe Temple Falun Hall Beijing", "雍和宫 法轮殿"]),
    ("YONGHE_TEMPLE_IMAGES", "wanfu_pavilion", "beijing/yonghe-temple/wanfu-pavilion.jpg", ["Yonghe Temple Wanfu Pavilion Beijing", "雍和宫 万福阁"]),
]


def request_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def request_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as response:
        content_type = response.headers.get("Content-Type", "")
        return response.read(), content_type


def commons_candidates(query):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": "6",
        "gsrlimit": "8",
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
        "iiurlwidth": "1920",
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    data = request_json(url)
    pages = list((data.get("query") or {}).get("pages", {}).values())
    pages.sort(key=lambda page: page.get("index", 999))
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        mime = info.get("mime", "")
        if not mime.startswith("image/") or mime == "image/svg+xml":
            continue
        title = page.get("title", "")
        lower_title = title.lower()
        if any(token in lower_title for token in ("map", "logo", "icon", "flag", ".djvu", ".pdf")):
            continue
        yield {
            "title": title,
            "url": info.get("thumburl") or info.get("url"),
            "page": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
            "mime": mime,
        }


def openverse_candidates(query):
    params = {
        "q": query,
        "page_size": "8",
    }
    url = "https://api.openverse.engineering/v1/images/?" + urllib.parse.urlencode(params)
    data = request_json(url)
    for item in data.get("results", []):
        title = item.get("title") or ""
        lower_title = title.lower()
        image_url = item.get("url") or item.get("thumbnail")
        if not image_url:
            continue
        if any(token in lower_title for token in ("map", "logo", "icon", "flag", ".djvu", ".pdf")):
            continue
        yield {
            "title": title,
            "url": image_url,
            "page": item.get("foreign_landing_url") or item.get("creator_url") or image_url,
            "mime": "",
        }


def is_image(data):
    return data.startswith(b"\xff\xd8\xff") or data.startswith(b"\x89PNG\r\n\x1a\n") or data.startswith(b"RIFF")


def download_asset(target, queries):
    target_path = ASSET_ROOT / target
    target_path.parent.mkdir(parents=True, exist_ok=True)

    last_error = ""
    for query in queries:
        for provider in (commons_candidates, openverse_candidates):
            try:
                candidates = provider(query)
                provider_error = ""
                for candidate in candidates:
                    if not candidate["url"]:
                        continue
                    data, content_type = request_bytes(candidate["url"])
                    if not content_type.startswith(("image/jpeg", "image/png", "image/webp")) or not is_image(data):
                        provider_error = f"not image: {candidate['url']} {content_type}"
                        continue
                    target_path.write_bytes(data)
                    return {
                        "asset": "/assets/guides/" + target,
                        "query": query,
                        "source": candidate["page"],
                        "title": candidate["title"],
                        "mime": candidate["mime"] or content_type,
                        "bytes": len(data),
                    }
                if provider_error:
                    last_error = provider_error
            except Exception as exc:
                last_error = repr(exc)
            time.sleep(0.6)
        time.sleep(0.2)
    raise RuntimeError(last_error or "no Commons image candidate")


def current_path(source, dict_name, key):
    start = source.index(f"{dict_name} = {{")
    brace_start = source.index("{", start)
    depth = 0
    end = brace_start
    for index in range(brace_start, len(source)):
        char = source[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end = index
                break
    block = source[brace_start:end]
    match = re.search(rf"'{re.escape(key)}'\s*:\s*'([^']+)'", block)
    return match.group(1) if match else ""


def replace_path(source, dict_name, key, asset_path):
    start = source.index(f"{dict_name} = {{")
    brace_start = source.index("{", start)
    depth = 0
    end = brace_start
    for index in range(brace_start, len(source)):
        char = source[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end = index
                break
    block = source[brace_start:end]
    pattern = re.compile(rf"('{re.escape(key)}'\s*:\s*)'[^']+'")
    new_block, count = pattern.subn(rf"\1'{asset_path}'", block, count=1)
    if count != 1:
        raise RuntimeError(f"could not update {dict_name}.{key}")
    return source[:brace_start] + new_block + source[end:]


def main():
    successes = []
    failures = []
    source = GUIDE_IMAGES.read_text(encoding="utf-8")

    for dict_name, key, target, queries in ASSETS:
        asset_path = "/assets/guides/" + target
        if current_path(source, dict_name, key) == asset_path and (ASSET_ROOT / target).exists():
            print(f"SKIP {dict_name}.{key} already local -> {asset_path}", flush=True)
            continue
        try:
            result = download_asset(target, queries)
            source = replace_path(source, dict_name, key, result["asset"])
            GUIDE_IMAGES.write_text(source, encoding="utf-8")
            successes.append({"dict": dict_name, "key": key, **result})
            print(f"OK {dict_name}.{key} -> {result['asset']} | {result['title']}", flush=True)
        except Exception as exc:
            failures.append({"dict": dict_name, "key": key, "target": target, "queries": queries, "error": repr(exc)})
            print(f"FAIL {dict_name}.{key}: {exc}", flush=True)
        time.sleep(3.0)

    (ASSET_ROOT / "downloaded-guide-image-sources.json").write_text(
        json.dumps({"successes": successes, "failures": failures}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"downloaded={len(successes)} failed={len(failures)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
