# 导航贴图片配置：
# 每一项都是一张单独可替换的图片。
# 'cover' 会写入数据库 posts.photos[0]，也就是首页卡片和详情页顶部的帖子封面。
# 'overview_map' 会写入数据库 posts.route_map.map_image，也就是正文下方路线选择区域的地图底图。
# 完整替换速查见：导航贴图片替换说明.md
# 增加或替换图片的方法：
# 1. 把图片文件放到对应景点目录，例如 my-app/assets/guides/beijing/temple-of-heaven/。
# 2. 在下面对应的图片字典里找到景点名注释，例如“祈年殿景点照片”，只替换这一行路径。
# 3. 如果要换帖子封面，修改对应字典里的 'cover'。
# 4. 每个小景点都已经预留独立图片键；即使现在共用同一张图，后续也可以单独替换。
# 5. 改完后运行：cd my-app && python3 insert_posts.py，让数据库重新写入最新图片配置。
FORBIDDEN_CITY_IMAGES = {
    # 故宫帖子主封面图：用于首页/推荐卡片和详情页顶部；替换故宫封面照片时只改这一行。
    'cover': '/assets/guides/app-style-covers/posts/故宫博物院.jpg',

    # 故宫正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名；替换地图底图时只改这一行。
    'overview_map': '/assets/guides/beijing/forbidden-city/route-map.svg',

    # 午门景点主照片：用于“午门”导览卡片和详情页第一张；替换午门正门或城台照片时只改这一行。
    'meridian_gate': '/assets/guides/beijing/forbidden-city/meridian-gate.jpg',

    # 午门补充照片一：用于“午门”详情页补充图；替换午门旧角度、历史版本或备选照片时只改这一行。
    'meridian_gate_2010': '/assets/guides/beijing/forbidden-city/meridian-gate-2010.jpg',

    # 午门补充照片二：用于“午门”详情页补充图；替换午门另一角度或备选照片时只改这一行。
    'meridian_gate_2015': '/assets/guides/beijing/forbidden-city/meridian-gate-2015.jpg',

    # 太和殿景点主照片：用于“太和殿”导览卡片和详情页第一张；替换外朝核心建筑或太和殿广场照片时只改这一行。
    'hall_of_supreme_harmony': '/assets/guides/beijing/forbidden-city/hall-of-supreme-harmony.jpg',

    # 太和殿补充照片：用于“太和殿”详情页第二张；替换太和殿远景、侧面或备选照片时只改这一行。
    'hall_of_supreme_harmony_2010': '/assets/guides/beijing/forbidden-city/hall-of-supreme-harmony-2010.jpg',

    # 乾清宫景点主照片：用于“乾清宫”导览卡片和详情页第一张；替换内廷前部建筑或室内视角照片时只改这一行。
    'palace_of_heavenly_purity': '/assets/guides/beijing/forbidden-city/palace-of-heavenly-purity.jpg',

    # 乾清宫补充照片：用于“乾清宫”详情页第二张；替换乾清宫外观或院落角度照片时只改这一行。
    'palace_of_heavenly_purity_exterior': '/assets/guides/beijing/forbidden-city/palace-of-heavenly-purity-exterior.jpg',

    # 珍宝馆景点主照片：用于“珍宝馆”导览卡片和详情页第一张；替换珍宝馆空间或展厅照片时只改这一行。
    'treasure_gallery': '/assets/guides/beijing/forbidden-city/treasure-gallery.jpg',

    # 珍宝馆展品补充照片：用于“珍宝馆”详情页第二张；替换玉器、器物或重点展品照片时只改这一行。
    'treasure_qing_jade': '/assets/guides/beijing/forbidden-city/treasure-qing-jade.jpg',

    # 角楼景点主照片：用于“角楼”导览卡片和详情页第一张；替换角楼与护城河照片时只改这一行。
    'corner_tower': '/assets/guides/beijing/forbidden-city/corner-tower.jpg',

    # 角楼蓝天补充照片：用于“角楼”详情页补充图，也可作为备用封面；替换蓝天白天角楼照片时只改这一行。
    'corner_tower_blue_sky': '/assets/guides/beijing/forbidden-city/corner-tower-blue-sky.jpg',

    # 角楼夜景补充照片：用于“角楼”详情页补充图；替换角楼夜景或灯光照片时只改这一行。
    'corner_tower_night': '/assets/guides/beijing/forbidden-city/corner-tower-night.jpg',
}

SUMMER_PALACE_IMAGES = {
    # 颐和园帖子主封面图：用于首页/推荐卡片和详情页顶部；替换颐和园封面全景照片时只改这一行。
    'cover': '/assets/guides/app-style-covers/posts/颐和园.jpg',

    # 颐和园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名；替换地图底图时只改这一行。
    'overview_map': '/assets/guides/beijing/summer-palace/clean-guide-map.svg',

    # 东宫门景点照片：用于“东宫门”导览卡片和详情页；替换入口门楼或东宫门外观照片时只改这一行。
    'east_palace_gate': '/assets/guides/beijing/summer-palace/east-palace-gate.jpg',

    # 仁寿殿景点照片：用于“仁寿殿”导览卡片和详情页；替换殿前院落、殿宇外观或办公空间照片时只改这一行。
    'renshou_hall': '/assets/guides/web-replacements/summer-palace-renshou-hall-cover-web.jpg',

    # 德和园景点照片：用于“德和园”导览卡片和详情页；替换大戏楼、院落或戏曲空间照片时只改这一行。
    'dehe_garden': '/assets/guides/user-provided/summer-palace/dehe-garden-1.png',
    'dehe_garden_detail': '/assets/guides/user-provided/summer-palace/dehe-garden-2.png',

    # 昆明湖补充照片：用于“昆明湖”详情页第二张；替换湖面、远山或水岸补充照片时只改这一行。
    'kunming_lake': '/assets/guides/beijing/summer-palace/kunming-lake.jpg',

    # 昆明湖主照片：用于“昆明湖”导览卡片和详情页第一张；替换开阔湖面主图时只改这一行。
    'kunming_lake_wide': '/assets/guides/user-provided/summer-palace/kunming-lake-1.png',

    # 长廊补充照片：用于“长廊”详情页第二张；替换廊内彩画、柱廊或细节照片时只改这一行。
    'long_corridor': '/assets/guides/beijing/summer-palace/long-corridor.jpg',

    # 长廊主照片：用于“长廊”导览卡片和详情页第一张；替换长廊外观或主视角照片时只改这一行。
    'long_gallery': '/assets/guides/beijing/summer-palace/long-gallery.jpg',

    # 排云殿景点照片：用于“排云殿”导览卡片和详情页；替换万寿山前殿宇或轴线空间照片时只改这一行。
    'paiyun_dian': '/assets/guides/user-provided/summer-palace/paiyun-dian-1.png',

    # 佛香阁景点照片：用于“佛香阁”导览卡片和详情页；替换佛香阁近景、登高视角或万寿山标志照片时只改这一行。
    'tower_buddhist_incense': '/assets/guides/beijing/summer-palace/tower-buddhist-incense.jpg',

    # 智慧海景点照片：用于“智慧海”导览卡片和详情页；替换无梁殿、琉璃装饰或山顶建筑照片时只改这一行。
    'sea_of_wisdom': '/assets/guides/user-provided/summer-palace/sea-of-wisdom-1.png',
    'sea_of_wisdom_detail': '/assets/guides/user-provided/summer-palace/sea-of-wisdom-2.png',

    # 苏州街景点照片：用于“苏州街”导览卡片和详情页；替换水街、店铺或后湖区域照片时只改这一行。
    'suzhou_street': '/assets/guides/user-provided/summer-palace/suzhou-street-1.png',
    'suzhou_street_detail': '/assets/guides/user-provided/summer-palace/suzhou-street-2.png',

    # 石舫景点照片：用于“石舫”导览卡片和详情页；替换石舫船体、湖边视角或清晏舫照片时只改这一行。
    'marble_boat': '/assets/guides/user-provided/summer-palace/marble-boat-1.png',
    'marble_boat_detail': '/assets/guides/user-provided/summer-palace/marble-boat-2.png',

    # 南湖岛景点照片：用于“南湖岛”导览卡片和详情页；替换岛上建筑、湖心视角或桥岛关系照片时只改这一行。
    'nanhu_island': '/assets/guides/beijing/summer-palace/nanhu-island.jpg',

    # 十七孔桥景点照片：用于“十七孔桥”导览卡片和详情页；替换桥身、夕阳或湖岸远景照片时只改这一行。
    'seventeen_arch_bridge': '/assets/guides/beijing/summer-palace/seventeen-arch-bridge-6.jpg',

    # 铜牛景点照片：用于“铜牛”导览卡片和详情页；替换铜牛雕塑、湖边位置或近景照片时只改这一行。
    'bronze_ox': '/assets/guides/beijing/summer-palace/bronze-ox.jpg',

    # 文昌院景点照片：用于“文昌院”导览卡片和详情页；替换文昌阁、院藏展陈或东堤文化节点照片时只改这一行。
    'wenchang_pavilion': '/assets/guides/beijing/summer-palace/wenchang-pavilion.jpg',
}

TEMPLE_OF_HEAVEN_IMAGES = {
    # 天坛帖子主封面图：用于首页/推荐卡片和详情页顶部；替换天坛封面照片时只改这一行。
    'cover': '/assets/guides/app-style-covers/posts/天坛公园.jpg',

    # 天坛正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名；替换地图底图时只改这一行。
    'overview_map': '/assets/guides/beijing/temple-of-heaven/route-map.svg',

    # 祈年殿景点照片：用于“祈年殿”导览卡片和详情页；替换祈年殿主建筑照片时只改这一行。
    'hall_of_prayer': '/assets/guides/beijing/temple-of-heaven/hall-of-prayer.jpg',

    # 皇乾殿景点照片：用于“皇乾殿”导览点卡片和详情页图片，替换时只改这一行。
    'imperial_hall_of_heaven': '/assets/guides/beijing/temple-of-heaven/imperial-hall-of-heaven.jpg',

    # 丹陛桥景点照片：用于“丹陛桥”导览点卡片和详情页图片，替换时只改这一行。
    'danbi_bridge': '/assets/guides/beijing/temple-of-heaven/danbi-bridge.jpg',

    # 皇穹宇景点照片：用于“皇穹宇”导览点卡片和详情页图片，替换时只改这一行。
    'imperial_vault': '/assets/guides/beijing/temple-of-heaven/imperial-vault.jpg',

    # 回音壁景点照片：用于“回音壁”导览点卡片和详情页图片，替换时只改这一行。
    'echo_wall': '/assets/guides/beijing/temple-of-heaven/echo-wall.jpg',

    # 三音石景点照片：用于“三音石”导览点卡片和详情页图片，替换时只改这一行。
    'three_echo_stones': '/assets/guides/beijing/temple-of-heaven/three-echo-stones.jpg',

    # 圜丘坛景点照片：用于“圜丘坛”导览点卡片和详情页图片，替换时只改这一行。
    'circular_mound_altar': '/assets/guides/beijing/temple-of-heaven/circular-mound-altar.jpg',

    # 斋宫景点照片：用于“斋宫”导览点卡片和详情页图片，替换时只改这一行。
    'palace_of_abstinence': '/assets/guides/beijing/temple-of-heaven/palace-of-abstinence.jpg',

    # 神乐署景点照片：用于“神乐署”导览点卡片和详情页图片，替换时只改这一行。
    'divine_music_administration': '/assets/guides/beijing/temple-of-heaven/divine-music-administration.jpg',

    # 七星石景点照片：用于“七星石”导览点卡片和详情页图片，替换时只改这一行。
    'seven_star_stones': '/assets/guides/beijing/temple-of-heaven/seven-star-stones.jpg',

    # 古柏林景点照片：用于“古柏林”导览点卡片和详情页图片，替换时只改这一行。
    'ancient_cypress_grove': '/assets/guides/beijing/temple-of-heaven/ancient-cypress-grove.jpg',
}

BADALING_IMAGES = {
    # 八达岭长城帖子主封面图：用于首页/推荐卡片和详情页顶部；替换长城山脊封面照片时只改这一行。
    'cover': '/assets/guides/app-style-covers/posts/八达岭长城.jpg',

    # 八达岭正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名；替换地图底图时只改这一行。
    'overview_map': '/assets/guides/beijing/badaling-great-wall/route-map.svg',

    # 八达岭城墙补充照片一：用于部分长城主体点位详情页补充图；替换城墙近景或备选照片时只改这一行。
    'wall_02': '/assets/guides/beijing/badaling-great-wall/wall-02.jpg',

    # 八达岭城墙补充照片二：用于北线、南线和眺望类点位详情页补充图；替换山脊远景或备选照片时只改这一行。
    'wall_06': '/assets/guides/beijing/badaling-great-wall/wall-06.jpg',

    # 关城景点照片：用于“关城”导览点卡片和详情页图片，替换时只改这一行。
    'pass_city': '/assets/guides/beijing/badaling-great-wall/pass-city.jpg',

    # 望京石景点照片：用于“望京石”导览点卡片和详情页图片，替换时只改这一行。
    'wangjing_stone': '/assets/guides/beijing/badaling-great-wall/wangjing-stone.jpg',

    # 好汉碑景点照片：用于“好汉碑”导览点卡片和详情页图片，替换时只改这一行。
    'hero_tablet': '/assets/guides/beijing/badaling-great-wall/hero-tablet.jpg',

    # 好汉坡景点照片：用于“好汉坡”导览点卡片和详情页图片，替换时只改这一行。
    'hero_slope': '/assets/guides/beijing/badaling-great-wall/hero-slope.jpg',

    # 北一楼景点照片：用于“北一楼”导览点卡片和详情页图片，替换时只改这一行。
    'north_tower_1': '/assets/guides/beijing/badaling-great-wall/north-tower-1.jpg',

    # 北二楼景点照片：用于“北二楼”导览点卡片和详情页图片，替换时只改这一行。
    'north_tower_2': '/assets/guides/beijing/badaling-great-wall/north-tower-2.jpg',

    # 北四楼景点照片：用于“北四楼”导览点卡片和详情页图片，替换时只改这一行。
    'north_tower_4': '/assets/guides/beijing/badaling-great-wall/north-tower-4.jpg',

    # 北八楼景点照片：用于“北八楼”导览点卡片和详情页图片，替换时只改这一行。
    'north_tower_8': '/assets/guides/beijing/badaling-great-wall/north-tower-8.jpg',

    # 南一楼景点照片：用于“南一楼”导览点卡片和详情页图片，替换时只改这一行。
    'south_tower_1': '/assets/guides/beijing/badaling-great-wall/south-tower-1.jpg',

    # 南四楼景点照片：用于“南四楼”导览点卡片和详情页图片，替换时只改这一行。
    'south_tower_4': '/assets/guides/beijing/badaling-great-wall/south-tower-4.jpg',

    # 长城博物馆景点照片：用于“长城博物馆”导览点卡片和详情页图片，替换时只改这一行。
    'great_wall_museum': '/assets/guides/beijing/badaling-great-wall/great-wall-museum.jpg',

    # 詹天佑纪念馆景点照片：用于“詹天佑纪念馆”导览点卡片和详情页图片，替换时只改这一行。
    'zhan_tianyou_memorial': '/assets/guides/beijing/badaling-great-wall/zhan-tianyou-memorial.jpg',
}

OLD_SUMMER_PALACE_IMAGES = {
    # 圆明园帖子主封面图：用于首页/推荐卡片和详情页顶部；替换圆明园遗址封面照片时只改这一行。
    'cover': '/assets/guides/app-style-covers/posts/圆明园遗址公园.jpg',

    # 圆明园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名；替换地图底图时只改这一行。
    'overview_map': '/assets/guides/beijing/old-summer-palace/route-map.svg',

    # 大水法遗址补充照片：用于“大水法”“西洋楼遗址”等遗址点详情页补充图；替换石构件或西洋楼代表照片时只改这一行。
    'dashuifa': '/assets/guides/beijing/old-summer-palace/dashuifa.jpg',

    # 海晏堂遗址补充照片：用于“海晏堂遗址”“远瀛观遗址”等西洋楼区域详情页补充图；替换海晏堂或相关遗址照片时只改这一行。
    'haiyantang': '/assets/guides/beijing/old-summer-palace/haiyantang.jpg',

    # 正大光明遗址景点照片：用于“正大光明遗址”导览点卡片和详情页图片，替换时只改这一行。
    'zhengda_guangming': '/assets/guides/beijing/old-summer-palace/zhengda-guangming.jpg',

    # 九州清晏遗址景点照片：用于“九州清晏遗址”导览点卡片和详情页图片，替换时只改这一行。
    'jiuzhou_qingyan': '/assets/guides/beijing/old-summer-palace/jiuzhou-qingyan.jpg',

    # 福海景点照片：用于“福海”导览点卡片和详情页图片，替换时只改这一行。
    'fuhai': '/assets/guides/beijing/old-summer-palace/fuhai.jpg',

    # 蓬岛瑶台景点照片：用于“蓬岛瑶台”导览点卡片和详情页图片，替换时只改这一行。
    'pengdao_yaotai': '/assets/guides/beijing/old-summer-palace/pengdao-yaotai.jpg',

    # 万方安和景点照片：用于“万方安和”导览点卡片和详情页图片，替换时只改这一行。
    'wanfang_anhe': '/assets/guides/web-replacements/yuanmingyuan-wanfang-ruins-web.jpg',

    # 澹泊宁静景点照片：用于“澹泊宁静”导览点卡片和详情页图片，替换时只改这一行。
    'danbo_ningjing': '/assets/guides/beijing/old-summer-palace/danbo-ningjing.jpg',

    # 长春园景点照片：用于“长春园”导览点卡片和详情页图片，替换时只改这一行。
    'changchun_garden': '/assets/guides/beijing/old-summer-palace/changchun-garden.jpg',

    # 西洋楼遗址景点照片：用于“西洋楼遗址”导览点卡片和详情页图片，替换时只改这一行。
    'western_mansions': '/assets/guides/beijing/old-summer-palace/western-mansions.jpg',

    # 大水法景点照片：用于“大水法”导览点卡片和详情页图片，替换时只改这一行。
    'great_fountain': '/assets/guides/beijing/old-summer-palace/dashuifa.jpg',

    # 海晏堂遗址景点照片：用于“海晏堂遗址”导览点卡片和详情页图片，替换时只改这一行。
    'haiyantang_ruins': '/assets/guides/beijing/old-summer-palace/haiyantang.jpg',

    # 远瀛观遗址景点照片：用于“远瀛观遗址”导览点卡片和详情页图片，替换时只改这一行。
    'yuanyingguan': '/assets/guides/beijing/old-summer-palace/yuanyingguan.jpg',

    # 方外观遗址景点照片：用于“方外观遗址”导览点卡片和详情页图片，替换时只改这一行。
    'fangwaiguan': '/assets/guides/beijing/old-summer-palace/fangwaiguan.jpg',

    # 黄花阵景点照片：用于“黄花阵”导览点卡片和详情页图片，替换时只改这一行。
    'huanghuazhen': '/assets/guides/web-replacements/yuanmingyuan-huanghuazhen-web.jpg',

    # 圆明园展览馆景点照片：用于“圆明园展览馆”导览点卡片和详情页图片，替换时只改这一行。
    'exhibition_hall': '/assets/guides/web-replacements/yuanmingyuan-exhibition-cover.jpg',
}

GUANGZHOU_TOWER_IMAGES = {
    # 广州塔帖子主封面图：用于首页/推荐卡片和详情页顶部，展示广州塔竖向地标形象。
    'cover': '/assets/guides/app-style-covers/posts/广州塔.jpg',

    # 广州塔正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/guangzhou/canton-tower/route-map.svg',

    # 塔下广场景点照片：用于“塔下广场”导览卡片、详情页第一张和路线点位详情；替换塔下近景时只改这一行。
    'base_square': '/assets/guides/user-provided/canton-tower/base-square-1.png',
    'base_square_detail': '/assets/guides/user-provided/canton-tower/base-square-2.png',

    # 观景平台景点照片：用于“观景平台”导览卡片和详情页；替换登塔俯瞰、室内观景层照片时只改这一行。
    'view_platform': '/assets/guides/user-provided/canton-tower/view-platform-1.png',
    'view_platform_detail': '/assets/guides/user-provided/canton-tower/view-platform-2.png',

    # 摩天轮景点照片：用于“摩天轮”导览卡片和详情页；替换高空摩天轮或塔顶设施照片时只改这一行。
    'ferris_wheel': '/assets/guides/guangzhou/canton-tower/ferris-wheel.jpg',

    # 极速云霄景点照片：用于“极速云霄”导览卡片和详情页；替换高空刺激项目照片时只改这一行。
    'sky_drop': '/assets/guides/guangzhou/canton-tower/sky-drop.jpg',

    # 海心桥视角景点照片：用于“海心桥视角”导览卡片和详情页；替换海心桥回望广州塔照片时只改这一行。
    'haixin_bridge_view': '/assets/guides/web-replacements/guangzhou-haixin-bridge-cover-web.jpg',

    # 珠江夜景景点照片：用于“珠江夜景”导览卡片和详情页；替换珠江夜游、沿江灯光或夜景照片时只改这一行。
    'pearl_river_night': '/assets/guides/guangzhou/canton-tower/pearl-river-night.jpg',
}

BAIYUN_MOUNTAIN_IMAGES = {
    # 白云山帖子主封面图：用于首页/推荐卡片和详情页顶部，展示山体与登高氛围。
    'cover': '/assets/guides/app-style-covers/posts/白云山.jpg',

    # 白云山正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/guangzhou/baiyun-mountain/route-map.svg',

    # 云台花园景点照片：用于“云台花园”导览卡片和详情页；替换山麓花园、入口花境照片时只改这一行。
    'yuntai_garden': '/assets/guides/web-replacements/baiyun-yuntai-garden-cover-web.jpg',

    # 能仁寺景点照片：用于“能仁寺”导览卡片和详情页；替换寺院建筑、院落或香道照片时只改这一行。
    'nengren_temple': '/assets/guides/guangzhou/baiyun-mountain/nengren-temple.jpg',

    # 鸣春谷景点照片：用于“鸣春谷”导览卡片和详情页；替换林谷、自然步道或生态景观照片时只改这一行。
    'mingchun_valley': '/assets/guides/user-provided/baiyun-mountain/mingchun-valley-1.png',
    'mingchun_valley_detail': '/assets/guides/user-provided/baiyun-mountain/mingchun-valley-2.png',

    # 山顶广场景点照片：用于“山顶广场”导览卡片和详情页；替换山顶集散区或观城平台照片时只改这一行。
    'summit_square': '/assets/guides/guangzhou/baiyun-mountain/cover-scenic.jpg',

    # 摩星岭景点照片：用于“摩星岭”导览卡片和详情页；替换最高峰门楼或登顶视角照片时只改这一行。
    'moxing_gate': '/assets/guides/user-provided/baiyun-mountain/moxing-ridge-1.png',
    'moxing_gate_detail': '/assets/guides/user-provided/baiyun-mountain/moxing-ridge-2.png',

    # 明珠楼景点照片：用于“明珠楼”导览卡片和详情页；替换白云山西北侧楼阁或深度路线照片时只改这一行。
    'mingzhu_tower': '/assets/guides/generated-replacements/baiyun-mingzhu-tower.png',
}

CHEN_CLAN_ACADEMY_IMAGES = {
    # 陈家祠帖子主封面图：用于首页/推荐卡片和详情页顶部，展示岭南祠堂外观。
    'cover': '/assets/guides/app-style-covers/posts/陈家祠.jpg',

    # 陈家祠正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/guangzhou/chen-clan-academy/route-map.svg',

    # 头门景点照片：用于“头门”导览卡片和详情页；替换陈家祠正门、门楼或入口立面照片时只改这一行。
    'head_gate': '/assets/guides/web-replacements/chen-clan-head-gate-cover.jpg',

    # 聚贤堂景点照片：用于“聚贤堂”导览卡片和详情页；替换中轴厅堂、正厅或堂内空间照片时只改这一行。
    'juxian_hall': '/assets/guides/guangzhou/chen-clan-academy/juxian-hall.jpg',

    # 中进院落景点照片：用于“中进院落”导览卡片和详情页；替换院落、廊道和厅堂层次照片时只改这一行。
    'middle_courtyard': '/assets/guides/guangzhou/chen-clan-academy/middle-courtyard.jpg',

    # 木雕景点照片：用于“木雕”导览卡片和详情页；替换梁架、屏门或木雕细节照片时只改这一行。
    'wood_carving': '/assets/guides/guangzhou/chen-clan-academy/wood-carving.jpg',

    # 砖雕景点照片：用于“砖雕”导览卡片和详情页；替换墙面、檐下或门楼砖雕细节照片时只改这一行。
    'brick_carving': '/assets/guides/guangzhou/chen-clan-academy/brick-carving.jpg',

    # 陶塑灰塑景点照片：用于“陶塑灰塑”导览卡片和详情页；替换屋脊陶塑、灰塑或高处装饰照片时只改这一行。
    'pottery_plaster': '/assets/guides/guangzhou/chen-clan-academy/pottery-plaster.jpg',

    # 后进展厅景点照片：用于“后进展厅”导览卡片和详情页；替换展厅、民间工艺展陈或后进空间照片时只改这一行。
    'rear_gallery': '/assets/guides/guangzhou/chen-clan-academy/rear-gallery.jpg',
}

YUEXIU_PARK_IMAGES = {
    # 越秀公园帖子主封面图：用于首页/推荐卡片和详情页顶部，展示五羊石像。
    'cover': '/assets/guides/app-style-covers/posts/越秀公园.jpg',

    # 越秀公园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/guangzhou/yuexiu-park/route-map.svg',

    # 五羊石像景点照片：用于“五羊石像”导览卡片和详情页；替换城市象征雕塑照片时只改这一行。
    'five_rams': '/assets/guides/guangzhou/yuexiu-park/five-rams.jpg',

    # 镇海楼景点照片：用于“镇海楼”导览卡片和详情页；替换五层楼外观或越秀山建筑照片时只改这一行。
    'zhenhai_tower': '/assets/guides/guangzhou/yuexiu-park/zhenhai-tower.jpg',

    # 广州博物馆景点照片：用于“广州博物馆”导览卡片和详情页；替换馆内展陈或镇海楼展览照片时只改这一行。
    'guangzhou_museum': '/assets/guides/guangzhou/yuexiu-park/zhenhai-tower.jpg',

    # 明代古城墙景点照片：用于“明代古城墙”导览卡片和详情页；替换古城墙遗存照片时只改这一行。
    'ming_city_wall': '/assets/guides/guangzhou/yuexiu-park/ming-city-wall.jpg',

    # 中山纪念碑景点照片：用于“中山纪念碑”导览卡片和详情页；替换纪念碑或越秀山纪念空间照片时只改这一行。
    'sun_yat_sen_monument': '/assets/guides/guangzhou/yuexiu-park/sun-yat-sen-monument.jpg',

    # 越秀山湖区景点照片：用于“越秀山湖区”导览卡片和详情页；替换湖面、绿地或休闲步道照片时只改这一行。
    'lake_area': '/assets/guides/web-replacements/yuexiu-lake-area-detail-web.jpg',
}

SHAMIAN_ISLAND_IMAGES = {
    # 沙面岛帖子主封面图：用于首页/推荐卡片和详情页顶部，展示沙面欧陆建筑街景。
    'cover': '/assets/guides/app-style-covers/posts/沙面岛.jpg',

    # 沙面岛正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/guangzhou/shamian-island/route-map.svg',

    # 沙面大街景点照片：用于“沙面大街”导览卡片和详情页；替换主街、古树街景或欧陆建筑街景照片时只改这一行。
    'main_street': '/assets/guides/guangzhou/shamian-island/main-street.jpg',

    # 露德圣母堂景点照片：用于“露德圣母堂”导览卡片和详情页；替换教堂外立面、窗洞或宗教建筑照片时只改这一行。
    'lourdes_chapel': '/assets/guides/guangzhou/shamian-island/lourdes-chapel.jpg',

    # 沙面基督堂景点照片：用于“沙面基督堂”导览卡片和详情页；替换基督堂外观或街角教堂照片时只改这一行。
    'christ_church': '/assets/guides/guangzhou/shamian-island/christ-church.jpg',

    # 旧领事馆建筑群景点照片：用于“旧领事馆建筑群”导览卡片和详情页；替换旧领事馆、柱廊或欧陆建筑立面照片时只改这一行。
    'former_consulates': '/assets/guides/guangzhou/shamian-island/former-consulates.jpg',

    # 白鹅潭江边景点照片：用于“白鹅潭江边”导览卡片和详情页；替换江边、黄昏水岸或珠江视角照片时只改这一行。
    'riverfront': '/assets/guides/guangzhou/shamian-island/riverfront.jpg',

    # 古树街巷景点照片：用于“古树街巷”导览卡片和详情页；替换树荫小路、街巷光影或慢行空间照片时只改这一行。
    'tree_lanes': '/assets/guides/guangzhou/shamian-island/tree-lanes.jpg',
}

SHANGHAI_BUND_IMAGES = {
    # 外滩帖子主封面图：用于首页/推荐卡片和详情页顶部，展示外滩与陆家嘴天际线。
    'cover': '/assets/guides/app-style-covers/posts/上海外滩.jpg',

    # 外滩正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shanghai/bund/route-map.svg',

    # 外滩源景点照片：用于“外滩源”导览卡片和详情页；替换苏州河口、外滩源历史建筑或起点空间照片时只改这一行。
    'bund_origin': '/assets/guides/shanghai/bund/bund-origin.jpg',

    # 万国建筑群景点照片：用于“万国建筑群”导览卡片和详情页；替换中山东一路历史建筑立面、柱廊或屋顶线照片时只改这一行。
    'international_buildings': '/assets/guides/shanghai/bund/international-buildings.jpg',

    # 黄浦江观景带景点照片：用于“黄浦江观景带”导览卡片和详情页；替换江面、游船、陆家嘴远景照片时只改这一行。
    'huangpu_river_view': '/assets/guides/shanghai/bund/huangpu-river-view.jpg',

    # 陈毅广场景点照片：用于“陈毅广场”导览卡片和详情页；替换广场、纪念空间或外滩人流节点照片时只改这一行。
    'chenyi_square': '/assets/guides/shanghai/bund/chenyi-square.jpg',

    # 南京东路外滩口景点照片：用于“南京东路外滩口”导览卡片和详情页；替换步行街入口、外滩转场或夜景人流照片时只改这一行。
    'nanjing_road_entry': '/assets/guides/shanghai/bund/nanjing-road-entry.jpg',
}

YU_GARDEN_IMAGES = {
    # 豫园帖子主封面图：用于首页/推荐卡片和详情页顶部，展示江南园林和九曲桥空间。
    'cover': '/assets/guides/app-style-covers/posts/上海豫园.jpg',

    # 豫园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shanghai/yu-garden/route-map.svg',

    # 九曲桥景点照片：用于“九曲桥”导览卡片和详情页；替换桥面、水面、游人动线照片时只改这一行。
    'nine_turning_bridge': '/assets/guides/web-replacements/yu-garden-nine-turning-cover-web.jpg',

    # 湖心亭景点照片：用于“湖心亭”导览卡片和详情页；替换茶楼外观、池边建筑或九曲桥尽头视角照片时只改这一行。
    'huxinting_teahouse': '/assets/guides/web-replacements/yu-garden-huxinting-cover-web.jpg',

    # 三穗堂景点照片：用于“三穗堂”导览卡片和详情页；替换厅堂外观、园林入口建筑或堂前空间照片时只改这一行。
    'sansui_hall': '/assets/guides/shanghai/yu-garden/sansui-hall.jpg',

    # 大假山景点照片：用于“大假山”导览卡片和详情页；替换太湖石、假山路径或江南园林叠石照片时只改这一行。
    'great_rockery': '/assets/guides/shanghai/yu-garden/great-rockery.jpg',

    # 点春堂景点照片：用于“点春堂”导览卡片和详情页；替换厅堂、院落或园内历史建筑照片时只改这一行。
    'dianchun_hall': '/assets/guides/shanghai/yu-garden/dianchun-hall.jpg',

    # 豫园商城景点照片：用于“豫园商城”导览卡片和详情页；替换城隍庙商圈、街市灯光或外部收束区域照片时只改这一行。
    'yuyuan_bazaar': '/assets/guides/web-replacements/yu-garden-bazaar-cover-web.jpg',
}

SHANGHAI_MUSEUM_IMAGES = {
    # 上海博物馆帖子主封面图：用于首页/推荐卡片和详情页顶部，展示人民广场馆舍外观。
    'cover': '/assets/guides/app-style-covers/posts/上海博物馆.jpg',

    # 上海博物馆正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shanghai/shanghai-museum/route-map.svg',

    # 博物馆大厅景点照片：用于“博物馆大厅”导览卡片和详情页；替换入口大厅、服务台或路线起点照片时只改这一行。
    'museum_hall': '/assets/guides/shanghai/shanghai-museum/museum-hall.jpg',

    # 青铜器馆景点照片：用于“青铜器馆”导览卡片和详情页；替换青铜器展厅、鼎器或陈列空间照片时只改这一行。
    'bronze_gallery': '/assets/guides/shanghai/shanghai-museum/bronze-gallery.jpg',

    # 陶瓷馆景点照片：用于“陶瓷馆”导览卡片和详情页；替换陶瓷展柜、瓷器细节或馆内动线照片时只改这一行。
    'ceramics_gallery': '/assets/guides/shanghai/shanghai-museum/ceramics-gallery.jpg',

    # 书法馆景点照片：用于“书法馆”导览卡片和详情页；替换书法展墙、卷轴或墨迹细节照片时只改这一行。
    'calligraphy_gallery': '/assets/guides/shanghai/shanghai-museum/calligraphy-gallery.jpg',

    # 绘画馆景点照片：用于“绘画馆”导览卡片和详情页；替换国画展厅、山水画或长卷展示照片时只改这一行。
    'painting_gallery': '/assets/guides/shanghai/shanghai-museum/painting-gallery.jpg',

    # 玉器馆景点照片：用于“玉器馆”导览卡片和详情页；替换玉器展柜、玉璧玉佩或细节照片时只改这一行。
    'jade_gallery': '/assets/guides/shanghai/shanghai-museum/jade-gallery.jpg',
}

SHENZHEN_BAY_IMAGES = {
    # 深圳湾公园帖子主封面图：用于首页/推荐卡片和详情页顶部，展示滨海步道和湾区视野。
    'cover': '/assets/guides/app-style-covers/posts/深圳湾公园.jpg',

    # 深圳湾公园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shenzhen/shenzhen-bay-park/route-map.svg',

    # 滨海步道景点照片：用于“滨海步道”导览卡片和详情页；替换海边步道、开阔水面或慢行空间照片时只改这一行。
    'coastal_promenade': '/assets/guides/shenzhen/shenzhen-bay-park/coastal-promenade.jpg',

    # 人才公园视角景点照片：用于“人才公园视角”导览卡片和详情页；替换后海天际线、人才公园水岸或城市界面照片时只改这一行。
    'talent_park_view': '/assets/guides/shenzhen/shenzhen-bay-park/talent-park-view.jpg',

    # 深圳湾大桥远眺景点照片：用于“深圳湾大桥远眺”导览卡片和详情页；替换桥梁、水面或湾区远景照片时只改这一行。
    'shenzhen_bay_bridge': '/assets/guides/shenzhen/shenzhen-bay-park/shenzhen-bay-bridge.jpg',

    # 日出剧场景点照片：用于“日出剧场”导览卡片和详情页；替换剧场台阶、日出/日落水面或休息空间照片时只改这一行。
    'sunrise_theater': '/assets/guides/shenzhen/shenzhen-bay-park/sunrise-theater.jpg',

    # 红树林方向景点照片：用于“红树林方向”导览卡片和详情页；替换湿地、候鸟观察或生态步道照片时只改这一行。
    'mangrove_direction': '/assets/guides/shenzhen/shenzhen-bay-park/mangrove-direction.jpg',
}

LIANHUASHAN_IMAGES = {
    # 莲花山公园帖子主封面图：用于首页/推荐卡片和详情页顶部，展示山顶广场与福田城市天际线。
    'cover': '/assets/guides/app-style-covers/posts/深圳莲花山公园.jpg',

    # 莲花山公园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shenzhen/lianhuashan-park/route-map.svg',

    # 风筝广场景点照片：用于“风筝广场”导览卡片和详情页；替换山下广场、市民休闲或放风筝场景照片时只改这一行。
    'kite_square': '/assets/guides/shenzhen/lianhuashan-park/kite-square.jpg',

    # 山顶步道景点照片：用于“山顶步道”导览卡片和详情页；替换登山步道、林荫坡道或上山途中照片时只改这一行。
    'summit_trail': '/assets/guides/shenzhen/lianhuashan-park/summit-trail.jpg',

    # 山顶广场景点照片：用于“山顶广场”导览卡片和详情页；替换山顶平台、纪念雕像区域或观城前场照片时只改这一行。
    'summit_square': '/assets/guides/shenzhen/lianhuashan-park/summit-square.jpg',

    # 城市观景台景点照片：用于“城市观景台”导览卡片和详情页；替换福田中心区、市民中心或城市天际线照片时只改这一行。
    'city_view': '/assets/guides/shenzhen/lianhuashan-park/city-view.jpg',

    # 湖区与草坪景点照片：用于“湖区与草坪”导览卡片和详情页；替换湖边草地、亲子休息或下山收束照片时只改这一行。
    'lake_lawn': '/assets/guides/shenzhen/lianhuashan-park/lake-lawn.jpg',
}

DAPENG_FORTRESS_IMAGES = {
    # 大鹏所城帖子主封面图：用于首页/推荐卡片和详情页顶部，展示古城街巷与城门空间。
    'cover': '/assets/guides/app-style-covers/posts/深圳大鹏所城.jpg',

    # 大鹏所城正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/shenzhen/dapeng-fortress/route-map.svg',

    # 南门城楼景点照片：用于“南门城楼”导览卡片和详情页；替换古城入口、城门门洞或城楼外观照片时只改这一行。
    'south_gate': '/assets/guides/shenzhen/dapeng-fortress/south-gate.jpg',

    # 赖恩爵将军第景点照片：用于“赖恩爵将军第”导览卡片和详情页；替换将军第外观、院落或海防人物空间照片时只改这一行。
    'general_house': '/assets/guides/web-replacements/dapeng-general-house-web.jpg',

    # 古城街巷景点照片：用于“古城街巷”导览卡片和详情页；替换巷道、岭南民居或老城慢行照片时只改这一行。
    'old_lanes': '/assets/guides/web-replacements/dapeng-old-lanes-web.jpg',

    # 大鹏粮仓景点照片：用于“大鹏粮仓”导览卡片和详情页；替换粮仓建筑、后勤空间或古城功能节点照片时只改这一行。
    'granary': '/assets/guides/shenzhen/dapeng-fortress/granary.jpg',

    # 较场尾方向景点照片：用于“较场尾方向”导览卡片和详情页；替换海边延伸、民宿街区或古城到海岸转场照片时只改这一行。
    'jiaochangwei_direction': '/assets/guides/web-replacements/dapeng-jiaochangwei-direction-web.jpg',
}

BEIHAI_PARK_IMAGES = {
    # 北海公园帖子主封面图：用于首页/推荐卡片和详情页顶部，展示白塔、湖面和皇家园林气质。
    'cover': '/assets/guides/app-style-covers/posts/北海公园.jpg',

    # 北海公园正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/beijing/beihai-park/route-map.svg',

    # 南门入口景点照片：用于“南门入口”导览卡片和详情页；替换入园口、湖面初见或白塔远景照片时只改这一行。
    'south_gate': '/assets/guides/beijing/beihai-park/south-gate.jpg',

    # 琼华岛景点照片：用于“琼华岛”导览卡片和详情页；替换登岛坡道、岛上殿宇或湖心空间照片时只改这一行。
    'qionghua_island': '/assets/guides/beijing/beihai-park/qionghua-island.jpg',

    # 白塔景点照片：用于“白塔”导览卡片和详情页；替换白塔近景、登高视角或北海标志性画面照片时只改这一行。
    'white_pagoda': '/assets/guides/user-provided/beihai-park/white-pagoda-1.png',
    'white_pagoda_detail': '/assets/guides/user-provided/beihai-park/white-pagoda-2.png',

    # 九龙壁景点照片：用于“九龙壁”导览卡片和详情页；替换琉璃壁、龙纹细节或北岸文化节点照片时只改这一行。
    'nine_dragon_wall': '/assets/guides/beijing/beihai-park/nine-dragon-wall.jpg',

    # 五龙亭景点照片：用于“五龙亭”导览卡片和详情页；替换临湖亭榭、回望白塔或湖畔休息照片时只改这一行。
    'five_dragon_pavilions': '/assets/guides/user-provided/beihai-park/five-dragon-pavilions-1.png',
    'five_dragon_pavilions_detail': '/assets/guides/user-provided/beihai-park/five-dragon-pavilions-2.png',

    # 北海湖面景点照片：用于“北海湖面”导览卡片和详情页；替换湖面、游船、沿湖慢走或收束视角照片时只改这一行。
    'lake_view': '/assets/guides/beijing/beihai-park/lake-view.jpg',
}

YONGHE_TEMPLE_IMAGES = {
    # 雍和宫帖子主封面图：用于首页/推荐卡片和详情页顶部，展示雍和宫中轴殿宇。
    'cover': '/assets/guides/app-style-covers/posts/雍和宫.jpg',

    # 雍和宫正文下方互动路线地图底图：前端会叠加线路、点位和中文景点名。
    'overview_map': '/assets/guides/beijing/yonghe-temple/route-map.svg',

    # 昭泰门景点照片：用于“昭泰门”导览卡片和详情页；替换入口牌楼、第一重门或路线开场照片时只改这一行。
    'zhaotai_gate': '/assets/guides/beijing/yonghe-temple/zhaotai-gate.jpg',

    # 雍和门景点照片：用于“雍和门”导览卡片和详情页；替换殿门、香火空间或中轴院落照片时只改这一行。
    'yonghe_gate': '/assets/guides/beijing/yonghe-temple/yonghe-gate.jpg',

    # 雍和宫大殿景点照片：用于“雍和宫大殿”导览卡片和详情页；替换核心殿宇、屋顶匾额或大殿外观照片时只改这一行。
    'main_hall': '/assets/guides/beijing/yonghe-temple/main-hall.jpg',

    # 永佑殿景点照片：用于“永佑殿”导览卡片和详情页；替换中段殿宇、王府到寺院历史空间照片时只改这一行。
    'yongyou_hall': '/assets/guides/beijing/yonghe-temple/yongyou-hall.jpg',

    # 法轮殿景点照片：用于“法轮殿”导览卡片和详情页；替换藏传佛教艺术、殿宇外观或仪式空间照片时只改这一行。
    'falun_hall': '/assets/guides/beijing/yonghe-temple/falun-hall.jpg',

    # 万福阁景点照片：用于“万福阁”导览卡片和详情页；替换高大阁楼、中轴收束或终点空间照片时只改这一行。
    'wanfu_pavilion': '/assets/guides/beijing/yonghe-temple/wanfu-pavilion.jpg',
}

IMAGE_SOURCES = [
    {
        'file': 'meridian-gate.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Meridian_Gate_of_the_Forbidden_City.jpg',
        'author': 'そらみみ',
        'license': 'CC BY-SA 4.0',
    },
    {
        'file': 'hall-of-supreme-harmony.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Hall_of_Supreme_Harmony_(54449453903).jpg',
        'author': 'Wong Zihoo',
        'license': 'CC BY 2.0',
    },
    {
        'file': 'palace-of-heavenly-purity.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Dragon_Throne_Palace_of_Heavenly_Purity_Forbidden_City_Beijing.jpg',
        'author': 'Vaiz Ha',
        'license': 'CC BY 2.0',
    },
    {
        'file': 'treasure-gallery.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Forbidden_City_Palace_Museum_(9862586296).jpg',
        'author': 'Gary Todd',
        'license': 'CC0 1.0',
    },
    {
        'file': 'corner-tower.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Forbidden_City_northwest_corner_tower_and_moat.jpg',
        'author': 'Daniel Case',
        'license': 'CC BY-SA 3.0 or GFDL',
    },
    {
        'file': 'treasure-qing-jade.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Manchu_Forbidden_City_Qing_Jade_16.jpg',
        'author': 'Gary Todd',
        'license': 'CC0 1.0',
    },
    {
        'file': 'guangzhou/canton-tower/cover.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Canton_Tower_02571-Guangzhou_(32110229893).jpg',
        'author': 'xiquinhosilva',
        'license': 'CC BY 2.0',
    },
    {
        'file': 'guangzhou/canton-tower/tower.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Guangzhou_Tower.jpg',
        'author': 'Wikimedia Commons contributor',
        'license': 'Commons license',
    },
    {
        'file': 'guangzhou/baiyun-mountain/cover.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Baiyun_Mountain,Guangzhou.jpg',
        'author': 'Wikimedia Commons contributor',
        'license': 'Commons license',
    },
    {
        'file': 'guangzhou/baiyun-mountain/moxing-gate.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Moxing_Summit_gate.jpg',
        'author': 'Chintunglee',
        'license': 'CC BY-SA',
    },
    {
        'file': 'guangzhou/chen-clan-academy/cover.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Chen_Clan_Ancestral_Hall,_Guangzhou.jpg',
        'author': '钉钉',
        'license': 'CC BY-SA 4.0',
    },
    {
        'file': 'guangzhou/yuexiu-park/cover.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Five-Ram_Sculpture_of_Guangzhou.jpg',
        'author': 'xiquinhosilva',
        'license': 'CC BY 2.0',
    },
    {
        'file': 'guangzhou/yuexiu-park/zhenhai-tower.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Zhenhai_Tower_03359-Guangzhou_(32667960970).jpg',
        'author': 'xiquinhosilva',
        'license': 'CC BY 2.0',
    },
    {
        'file': 'guangzhou/shamian-island/cover.jpg',
        'source': 'https://commons.wikimedia.org/wiki/File:Shamian_Island_03165-Guangzhou_(32234640983).jpg',
        'author': 'xiquinhosilva',
        'license': 'CC BY 2.0',
    },
]

# 每个导览点最终使用的图片组。
# guide_item 里的单张主图用于默认入口；这里集中保存审图后确认的 cover/detail 图，
# insert_posts.py 会在写入数据库前把它们应用到对应导览点。
GUIDE_GALLERIES = {'故宫博物院：沿中轴线走进六百年宫城': {'午门': ['/assets/guides/curated/full-gallery/故宫博物院/01-午门-cover.jpg',
                              '/assets/guides/curated/full-gallery/故宫博物院/01-午门-detail.jpg'],
                       '太和殿': ['/assets/guides/curated/full-gallery/故宫博物院/02-太和殿-cover.jpg',
                               '/assets/guides/beijing/forbidden-city/hall-of-supreme-harmony-2010.jpg'],
                       '乾清宫': ['/assets/guides/curated/full-gallery/故宫博物院/03-乾清宫-cover.jpg',
                               '/assets/guides/beijing/forbidden-city/palace-of-heavenly-purity.jpg'],
	                       '珍宝馆': ['/assets/guides/curated/full-gallery/故宫博物院/04-珍宝馆-cover.jpg',
                               '/assets/guides/curated/full-gallery/故宫博物院/04-珍宝馆-detail.jpg'],
                       '角楼': ['/assets/guides/curated/full-gallery/故宫博物院/05-角楼-cover.jpg',
                              '/assets/guides/curated/full-gallery/故宫博物院/05-角楼-detail.jpg']},
 '颐和园：沿湖山路线走进皇家园林': {'东宫门': ['/assets/guides/curated/full-gallery/颐和园/01-东宫门-cover.jpg',
                             '/assets/guides/curated/full-gallery/颐和园/01-东宫门-detail.jpg'],
                     '仁寿殿': ['/assets/guides/web-replacements/summer-palace-renshou-hall-cover-web.jpg',
                             '/assets/guides/curated/full-gallery/颐和园/02-仁寿殿-detail.jpg'],
                     '德和园': ['/assets/guides/user-provided/summer-palace/dehe-garden-1.png',
                             '/assets/guides/user-provided/summer-palace/dehe-garden-2.png'],
                     '长廊': ['/assets/guides/curated/full-gallery/颐和园/04-长廊-cover.jpg',
                            '/assets/guides/beijing/summer-palace/long-corridor.jpg'],
                     '排云殿': ['/assets/guides/user-provided/summer-palace/paiyun-dian-1.png'],
                     '佛香阁': ['/assets/guides/curated/full-gallery/颐和园/06-佛香阁-cover.jpg',
                             '/assets/guides/curated/full-gallery/颐和园/06-佛香阁-detail.jpg'],
	                     '智慧海': ['/assets/guides/user-provided/summer-palace/sea-of-wisdom-1.png',
	                             '/assets/guides/user-provided/summer-palace/sea-of-wisdom-2.png'],
                     '苏州街': ['/assets/guides/user-provided/summer-palace/suzhou-street-1.png',
                             '/assets/guides/user-provided/summer-palace/suzhou-street-2.png'],
	                     '石舫': ['/assets/guides/user-provided/summer-palace/marble-boat-1.png',
	                            '/assets/guides/user-provided/summer-palace/marble-boat-2.png'],
                     '昆明湖': ['/assets/guides/user-provided/summer-palace/kunming-lake-1.png'],
	                     '南湖岛': ['/assets/guides/curated/full-gallery/颐和园/11-南湖岛-cover.jpg',
	                             '/assets/guides/generated-replacements/derived-details/summer-palace-nanhu-detail.jpg'],
                     '十七孔桥': ['/assets/guides/curated/full-gallery/颐和园/12-十七孔桥-cover.jpg',
                              '/assets/guides/curated/full-gallery/颐和园/12-十七孔桥-detail.jpg'],
                     '铜牛': ['/assets/guides/beijing/summer-palace/bronze-ox.jpg',
                            '/assets/guides/curated/full-gallery/颐和园/13-铜牛-detail.jpg'],
                     '文昌院': ['/assets/guides/curated/full-gallery/颐和园/14-文昌院-cover.jpg',
                             '/assets/guides/curated/full-gallery/颐和园/14-文昌院-detail.jpg']},
 '天坛公园：沿祭天中轴走进明清礼制空间': {'祈年殿': ['/assets/guides/curated/full-gallery/天坛公园/01-祈年殿-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/01-祈年殿-detail.jpg'],
                        '皇乾殿': ['/assets/guides/curated/full-gallery/天坛公园/02-皇乾殿-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/02-皇乾殿-detail.jpg'],
                        '丹陛桥': ['/assets/guides/curated/full-gallery/天坛公园/03-丹陛桥-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/03-丹陛桥-detail.jpg'],
                        '皇穹宇': ['/assets/guides/curated/full-gallery/天坛公园/04-皇穹宇-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/04-皇穹宇-detail.jpg'],
                        '回音壁': ['/assets/guides/curated/full-gallery/天坛公园/05-回音壁-cover.jpg',
                                '/assets/guides/beijing/temple-of-heaven/three-echo-stones.jpg'],
                        '三音石': ['/assets/guides/curated/full-gallery/天坛公园/06-三音石-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/06-三音石-detail.jpg'],
                        '圜丘坛': ['/assets/guides/curated/full-gallery/天坛公园/07-圜丘坛-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/07-圜丘坛-detail.jpg'],
                        '斋宫': ['/assets/guides/curated/full-gallery/天坛公园/08-斋宫-cover.jpg',
                               '/assets/guides/curated/full-gallery/天坛公园/08-斋宫-detail.jpg'],
                        '神乐署': ['/assets/guides/curated/full-gallery/天坛公园/09-神乐署-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/09-神乐署-detail.jpg'],
                        '七星石': ['/assets/guides/curated/full-gallery/天坛公园/10-七星石-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/10-七星石-detail.jpg'],
                        '古柏林': ['/assets/guides/curated/full-gallery/天坛公园/11-古柏林-cover.jpg',
                                '/assets/guides/curated/full-gallery/天坛公园/11-古柏林-detail.jpg']},
 '八达岭长城：沿关城敌楼登临北国雄关': {'关城': ['/assets/guides/curated/full-gallery/八达岭长城/01-关城-cover.jpg',
                              '/assets/guides/curated/full-gallery/八达岭长城/01-关城-detail.jpg'],
                       '望京石': ['/assets/guides/curated/full-gallery/八达岭长城/02-望京石-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/02-望京石-detail.jpg'],
                       '好汉碑': ['/assets/guides/curated/full-gallery/八达岭长城/03-好汉碑-cover.jpg',
                               '/assets/guides/beijing/badaling-great-wall/wall-06.jpg'],
                       '好汉坡': ['/assets/guides/curated/full-gallery/八达岭长城/04-好汉坡-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/04-好汉坡-detail.jpg'],
                       '北一楼': ['/assets/guides/curated/full-gallery/八达岭长城/05-北一楼-cover.jpg',
                               '/assets/guides/beijing/badaling-great-wall/wall-02.jpg'],
                       '北二楼': ['/assets/guides/curated/full-gallery/八达岭长城/06-北二楼-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/06-北二楼-detail.jpg'],
                       '北四楼': ['/assets/guides/curated/full-gallery/八达岭长城/07-北四楼-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/07-北四楼-detail.jpg'],
                       '北八楼': ['/assets/guides/curated/full-gallery/八达岭长城/08-北八楼-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/08-北八楼-detail.jpg'],
                       '南一楼': ['/assets/guides/curated/full-gallery/八达岭长城/09-南一楼-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/09-南一楼-detail.jpg'],
                       '南四楼': ['/assets/guides/curated/full-gallery/八达岭长城/10-南四楼-cover.jpg',
                               '/assets/guides/curated/full-gallery/八达岭长城/10-南四楼-detail.jpg'],
                       '长城博物馆': ['/assets/guides/curated/full-gallery/八达岭长城/11-长城博物馆-cover.jpg',
                                 '/assets/guides/curated/full-gallery/八达岭长城/11-长城博物馆-detail.jpg'],
                       '詹天佑纪念馆': ['/assets/guides/curated/full-gallery/八达岭长城/12-詹天佑纪念馆-cover.jpg',
                                  '/assets/guides/curated/full-gallery/八达岭长城/12-詹天佑纪念馆-detail.jpg']},
 '圆明园遗址公园：沿湖园遗址回望万园之园': {'正大光明遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/01-正大光明遗址-cover.jpg',
                                    '/assets/guides/curated/full-gallery/圆明园遗址公园/01-正大光明遗址-detail.jpg'],
	                         '九州清晏遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/02-九州清晏遗址-cover.jpg',
	                                    '/assets/guides/generated-replacements/derived-details/yuanmingyuan-jiuzhou-detail.jpg'],
	                         '福海': ['/assets/guides/curated/full-gallery/圆明园遗址公园/03-福海-cover.jpg',
	                                '/assets/guides/generated-replacements/derived-details/yuanmingyuan-fuhai-detail.jpg'],
                         '蓬岛瑶台': ['/assets/guides/curated/full-gallery/圆明园遗址公园/04-蓬岛瑶台-cover.jpg',
                                  '/assets/guides/beijing/old-summer-palace/fuhai.jpg'],
                         '万方安和': ['/assets/guides/web-replacements/yuanmingyuan-wanfang-ruins-web.jpg',
                                  '/assets/guides/curated/full-gallery/圆明园遗址公园/05-万方安和-detail.jpg'],
                         '澹泊宁静': ['/assets/guides/curated/full-gallery/圆明园遗址公园/06-澹泊宁静-cover.jpg',
                                  '/assets/guides/curated/full-gallery/圆明园遗址公园/06-澹泊宁静-detail.jpg'],
                         '长春园': ['/assets/guides/curated/full-gallery/圆明园遗址公园/07-长春园-cover.jpg',
                                 '/assets/guides/web-replacements/yuanmingyuan-changchunyuan-detail-web.jpg'],
	                         '西洋楼遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/08-西洋楼遗址-cover.jpg',
	                                   '/assets/guides/generated-replacements/derived-details/yuanmingyuan-western-detail.jpg'],
	                         '大水法': ['/assets/guides/curated/full-gallery/圆明园遗址公园/09-大水法-cover.jpg',
	                                 '/assets/guides/generated-replacements/derived-details/yuanmingyuan-dashuifa-detail.jpg'],
                         '海晏堂遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/10-海晏堂遗址-cover.jpg',
                                   '/assets/guides/curated/full-gallery/圆明园遗址公园/10-海晏堂遗址-detail.jpg'],
                         '远瀛观遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/11-远瀛观遗址-cover.jpg',
                                   '/assets/guides/curated/full-gallery/圆明园遗址公园/11-远瀛观遗址-detail.jpg'],
                         '方外观遗址': ['/assets/guides/curated/full-gallery/圆明园遗址公园/12-方外观遗址-cover.jpg',
                                   '/assets/guides/curated/full-gallery/圆明园遗址公园/12-方外观遗址-detail.jpg'],
                         '黄花阵': ['/assets/guides/web-replacements/yuanmingyuan-huanghuazhen-web.jpg',
                                 '/assets/guides/curated/full-gallery/圆明园遗址公园/13-黄花阵-detail.jpg'],
                         '圆明园展览馆': ['/assets/guides/web-replacements/yuanmingyuan-exhibition-cover.jpg',
                                    '/assets/guides/web-replacements/yuanmingyuan-exhibition-detail.jpg']},
 '广州塔：沿城市中轴俯瞰珠江夜色': {'塔下广场': ['/assets/guides/user-provided/canton-tower/base-square-1.png',
                              '/assets/guides/user-provided/canton-tower/base-square-2.png'],
                     '观景平台': ['/assets/guides/user-provided/canton-tower/view-platform-1.png',
                              '/assets/guides/user-provided/canton-tower/view-platform-2.png'],
                     '海心桥视角': ['/assets/guides/web-replacements/guangzhou-haixin-bridge-cover-web.jpg',
                               '/assets/guides/web-replacements/guangzhou-haixin-bridge-detail-web.jpg'],
                     '珠江夜景': ['/assets/guides/curated/full-gallery/广州塔/06-珠江夜景-cover.jpg',
                              '/assets/guides/curated/full-gallery/广州塔/06-珠江夜景-detail.jpg']},
	 '白云山：沿云山步道登临羊城第一秀': {'云台花园': ['/assets/guides/web-replacements/baiyun-yuntai-garden-cover-web.jpg',
	                               '/assets/guides/web-replacements/baiyun-yuntai-garden-detail-web.jpg'],
                      '能仁寺': ['/assets/guides/curated/full-gallery/白云山/02-能仁寺-cover.jpg',
                              '/assets/guides/guangzhou/baiyun-mountain/nengren-temple.jpg'],
	                      '鸣春谷': ['/assets/guides/user-provided/baiyun-mountain/mingchun-valley-1.png',
	                              '/assets/guides/user-provided/baiyun-mountain/mingchun-valley-2.png'],
                      '山顶广场': ['/assets/guides/guangzhou/baiyun-mountain/cover-scenic.jpg',
                               '/assets/guides/guangzhou/baiyun-mountain/cover.jpg'],
	                      '摩星岭': ['/assets/guides/user-provided/baiyun-mountain/moxing-ridge-1.png',
	                              '/assets/guides/user-provided/baiyun-mountain/moxing-ridge-2.png'],
                      '明珠楼': ['/assets/guides/generated-replacements/baiyun-mingzhu-tower.png',
                              '/assets/guides/guangzhou/baiyun-mountain/city-view.jpg']},
	 '陈家祠：走进岭南建筑艺术博物馆': {'头门': ['/assets/guides/web-replacements/chen-clan-head-gate-cover.jpg',
	                            '/assets/guides/web-replacements/chen-clan-head-gate-detail.jpg'],
	                     '聚贤堂': ['/assets/guides/guangzhou/chen-clan-academy/juxian-hall.jpg',
	                             '/assets/guides/web-replacements/chen-juxian-hall-detail-web.jpg'],
                     '中进院落': ['/assets/guides/curated/full-gallery/陈家祠/03-中进院落-cover.jpg',
                              '/assets/guides/curated/full-gallery/陈家祠/03-中进院落-detail.jpg'],
                     '木雕': ['/assets/guides/curated/full-gallery/陈家祠/04-木雕-cover.jpg',
                            '/assets/guides/curated/full-gallery/陈家祠/04-木雕-detail.jpg'],
                     '砖雕': ['/assets/guides/curated/full-gallery/陈家祠/05-砖雕-cover.jpg',
                            '/assets/guides/curated/full-gallery/陈家祠/05-砖雕-detail.jpg'],
                     '陶塑灰塑': ['/assets/guides/curated/full-gallery/陈家祠/06-陶塑灰塑-cover.jpg',
                              '/assets/guides/curated/full-gallery/陈家祠/06-陶塑灰塑-detail.jpg'],
	                     '后进展厅': ['/assets/guides/curated/full-gallery/陈家祠/07-后进展厅-cover.jpg',
	                              '/assets/guides/web-replacements/chen-rear-gallery-detail-web.jpg']},
 '越秀公园：从五羊石像走进广州城史': {'五羊石像': ['/assets/guides/curated/full-gallery/越秀公园/01-五羊石像-cover.jpg',
                               '/assets/guides/curated/full-gallery/越秀公园/01-五羊石像-detail.jpg'],
                      '镇海楼': ['/assets/guides/curated/full-gallery/越秀公园/02-镇海楼-cover.jpg',
                              '/assets/guides/curated/full-gallery/越秀公园/02-镇海楼-detail.jpg'],
                      '广州博物馆': ['/assets/guides/curated/full-gallery/越秀公园/03-广州博物馆-cover.jpg',
                                '/assets/guides/guangzhou/yuexiu-park/zhenhai-tower.jpg'],
                      '明代古城墙': ['/assets/guides/curated/full-gallery/越秀公园/04-明代古城墙-cover.jpg',
                                '/assets/guides/curated/full-gallery/越秀公园/04-明代古城墙-detail.jpg'],
                      '中山纪念碑': ['/assets/guides/curated/full-gallery/越秀公园/05-中山纪念碑-cover.jpg',
                                '/assets/guides/curated/full-gallery/越秀公园/05-中山纪念碑-detail.jpg'],
                      '越秀山湖区': ['/assets/guides/curated/full-gallery/越秀公园/06-越秀山湖区-cover.jpg',
                                '/assets/guides/web-replacements/yuexiu-lake-area-detail-web.jpg']},
 '沙面岛：沿珠江漫步欧陆建筑街区': {'沙面大街': ['/assets/guides/curated/full-gallery/沙面岛/01-沙面大街-cover.jpg',
                              '/assets/guides/curated/full-gallery/沙面岛/01-沙面大街-detail.jpg'],
                     '露德圣母堂': ['/assets/guides/curated/full-gallery/沙面岛/02-露德圣母堂-cover.jpg',
                               '/assets/guides/curated/full-gallery/沙面岛/02-露德圣母堂-detail.jpg'],
                     '沙面基督堂': ['/assets/guides/curated/full-gallery/沙面岛/03-沙面基督堂-cover.jpg',
                               '/assets/guides/curated/full-gallery/沙面岛/03-沙面基督堂-detail.jpg'],
                     '旧领事馆建筑群': ['/assets/guides/curated/full-gallery/沙面岛/04-旧领事馆建筑群-cover.jpg',
                                 '/assets/guides/curated/full-gallery/沙面岛/04-旧领事馆建筑群-detail.jpg'],
                     '白鹅潭江边': ['/assets/guides/curated/full-gallery/沙面岛/05-白鹅潭江边-cover.jpg',
                               '/assets/guides/curated/full-gallery/沙面岛/05-白鹅潭江边-detail.jpg'],
                     '古树街巷': ['/assets/guides/curated/full-gallery/沙面岛/06-古树街巷-cover.jpg',
                              '/assets/guides/curated/full-gallery/沙面岛/06-古树街巷-detail.jpg']},
 '上海外滩：沿黄浦江读懂近代城市天际线': {'外滩源': ['/assets/guides/curated/full-gallery/上海外滩/01-外滩源-cover.jpg',
                                '/assets/guides/curated/full-gallery/上海外滩/01-外滩源-detail.jpg'],
                        '万国建筑群': ['/assets/guides/curated/full-gallery/上海外滩/02-万国建筑群-cover.jpg',
                                  '/assets/guides/curated/full-gallery/上海外滩/02-万国建筑群-detail.jpg'],
                        '黄浦江观景带': ['/assets/guides/curated/full-gallery/上海外滩/03-黄浦江观景带-cover.jpg',
                                   '/assets/guides/curated/full-gallery/上海外滩/03-黄浦江观景带-detail.jpg'],
                        '陈毅广场': ['/assets/guides/curated/full-gallery/上海外滩/04-陈毅广场-cover.jpg',
                                 '/assets/guides/curated/full-gallery/上海外滩/04-陈毅广场-detail.jpg'],
                        '南京东路外滩口': ['/assets/guides/curated/full-gallery/上海外滩/05-南京东路外滩口-cover.jpg',
                                    '/assets/guides/curated/full-gallery/上海外滩/05-南京东路外滩口-detail.jpg']},
	 '上海豫园：走进老城厢里的江南园林': {'九曲桥': ['/assets/guides/web-replacements/yu-garden-nine-turning-cover-web.jpg',
	                              '/assets/guides/web-replacements/yu-garden-nine-turning-detail-web.jpg'],
                     '湖心亭': ['/assets/guides/web-replacements/yu-garden-huxinting-cover-web.jpg',
                             '/assets/guides/web-replacements/yu-garden-huxinting-detail-web.jpg'],
	                      '三穗堂': ['/assets/guides/shanghai/yu-garden/cover.jpg',
                              '/assets/guides/shanghai/yu-garden/sansui-hall.jpg'],
	                      '大假山': ['/assets/guides/curated/full-gallery/上海豫园/04-大假山-cover.jpg',
	                              '/assets/guides/web-replacements/yu-garden-rockery-detail-web.jpg'],
                      '点春堂': ['/assets/guides/curated/full-gallery/上海豫园/05-点春堂-cover.jpg',
                              '/assets/guides/curated/full-gallery/上海豫园/05-点春堂-detail.jpg'],
                     '豫园商城': ['/assets/guides/web-replacements/yu-garden-bazaar-cover-web.jpg',
                              '/assets/guides/web-replacements/yu-garden-bazaar-detail-web.jpg']},
 '上海博物馆：沿展厅看懂中国古代艺术': {'博物馆大厅': ['/assets/guides/curated/full-gallery/上海博物馆/01-博物馆大厅-cover.jpg',
                                 '/assets/guides/shanghai/shanghai-museum/museum-hall.jpg'],
                       '青铜器馆': ['/assets/guides/shanghai/shanghai-museum/bronze-gallery.jpg',
                                '/assets/guides/curated/full-gallery/上海博物馆/02-青铜器馆-detail.jpg'],
                       '陶瓷馆': ['/assets/guides/curated/full-gallery/上海博物馆/03-陶瓷馆-cover.jpg',
                               '/assets/guides/curated/full-gallery/上海博物馆/03-陶瓷馆-detail.jpg'],
                       '书法馆': ['/assets/guides/shanghai/shanghai-museum/calligraphy-gallery.jpg',
                               '/assets/guides/curated/full-gallery/上海博物馆/04-书法馆-detail.jpg'],
                       '绘画馆': ['/assets/guides/curated/full-gallery/上海博物馆/05-绘画馆-cover.jpg',
                               '/assets/guides/curated/full-gallery/上海博物馆/05-绘画馆-detail.jpg'],
                       '玉器馆': ['/assets/guides/curated/full-gallery/上海博物馆/06-玉器馆-cover.jpg',
                               '/assets/guides/curated/full-gallery/上海博物馆/06-玉器馆-detail.jpg']},
 '深圳湾公园：沿滨海步道看海湾城市': {'滨海步道': ['/assets/guides/curated/full-gallery/深圳湾公园/01-滨海步道-cover.jpg',
                               '/assets/guides/curated/full-gallery/深圳湾公园/01-滨海步道-detail.jpg'],
                      '人才公园视角': ['/assets/guides/curated/full-gallery/深圳湾公园/02-人才公园视角-cover.jpg',
                                 '/assets/guides/curated/full-gallery/深圳湾公园/02-人才公园视角-detail.jpg'],
	                      '深圳湾大桥远眺': ['/assets/guides/curated/full-gallery/深圳湾公园/03-深圳湾大桥远眺-cover.jpg',
	                                  '/assets/guides/web-replacements/shenzhen-bay-bridge-detail-web.jpg'],
                      '日出剧场': ['/assets/guides/curated/full-gallery/深圳湾公园/04-日出剧场-cover.jpg',
                               '/assets/guides/curated/full-gallery/深圳湾公园/04-日出剧场-detail.jpg'],
                      '红树林方向': ['/assets/guides/curated/full-gallery/深圳湾公园/05-红树林方向-cover.jpg',
                                '/assets/guides/curated/full-gallery/深圳湾公园/05-红树林方向-detail.jpg']},
 '深圳莲花山公园：登上中心区绿丘俯瞰城市': {'风筝广场': ['/assets/guides/curated/full-gallery/深圳莲花山公园/01-风筝广场-cover.jpg',
                                  '/assets/guides/curated/full-gallery/深圳莲花山公园/01-风筝广场-detail.jpg'],
                         '山顶步道': ['/assets/guides/curated/full-gallery/深圳莲花山公园/02-山顶步道-cover.jpg',
                                  '/assets/guides/shenzhen/lianhuashan-park/city-view.jpg'],
                         '山顶广场': ['/assets/guides/curated/full-gallery/深圳莲花山公园/03-山顶广场-cover.jpg',
                                  '/assets/guides/curated/full-gallery/深圳莲花山公园/03-山顶广场-detail.jpg'],
                         '城市观景台': ['/assets/guides/curated/full-gallery/深圳莲花山公园/04-城市观景台-cover.jpg',
                                   '/assets/guides/curated/full-gallery/深圳莲花山公园/04-城市观景台-detail.jpg'],
                         '湖区与草坪': ['/assets/guides/curated/full-gallery/深圳莲花山公园/05-湖区与草坪-cover.jpg',
                                   '/assets/guides/curated/full-gallery/深圳莲花山公园/05-湖区与草坪-detail.jpg']},
 '深圳大鹏所城：沿海防古城走进岭南街巷': {'南门城楼': ['/assets/guides/curated/full-gallery/深圳大鹏所城/01-南门城楼-cover.jpg',
                                 '/assets/guides/curated/full-gallery/深圳大鹏所城/01-南门城楼-detail.jpg'],
	                       '赖恩爵将军第': ['/assets/guides/web-replacements/dapeng-general-house-web.jpg',
                                   '/assets/guides/shenzhen/dapeng-fortress/general-house.jpg'],
	                        '古城街巷': ['/assets/guides/curated/full-gallery/深圳大鹏所城/03-古城街巷-cover.jpg',
	                                 '/assets/guides/web-replacements/dapeng-old-lanes-web.jpg'],
                        '大鹏粮仓': ['/assets/guides/curated/full-gallery/深圳大鹏所城/04-大鹏粮仓-cover.jpg',
                                 '/assets/guides/shenzhen/dapeng-fortress/granary.jpg'],
                        '较场尾方向': ['/assets/guides/curated/full-gallery/深圳大鹏所城/05-较场尾方向-cover.jpg',
                                  '/assets/guides/web-replacements/dapeng-jiaochangwei-direction-web.jpg']},
 '北海公园：沿湖岛白塔走进皇家园林': {'南门入口': ['/assets/guides/curated/full-gallery/北海公园/01-南门入口-cover.jpg',
                               '/assets/guides/curated/full-gallery/北海公园/01-南门入口-detail.jpg'],
	                      '琼华岛': ['/assets/guides/curated/full-gallery/北海公园/02-琼华岛-cover.jpg',
	                              '/assets/guides/generated-replacements/derived-details/beihai-qionghua-detail.jpg'],
                      '白塔': ['/assets/guides/user-provided/beihai-park/white-pagoda-1.png',
                             '/assets/guides/user-provided/beihai-park/white-pagoda-2.png'],
                      '九龙壁': ['/assets/guides/curated/full-gallery/北海公园/04-九龙壁-cover.jpg',
                              '/assets/guides/curated/full-gallery/北海公园/04-九龙壁-detail.jpg'],
                      '五龙亭': ['/assets/guides/user-provided/beihai-park/five-dragon-pavilions-1.png',
                              '/assets/guides/user-provided/beihai-park/five-dragon-pavilions-2.png'],
                      '北海湖面': ['/assets/guides/curated/full-gallery/北海公园/06-北海湖面-cover.jpg',
                               '/assets/guides/curated/full-gallery/北海公园/06-北海湖面-detail.jpg']},
 '雍和宫：沿中轴殿宇感受皇家寺院': {'昭泰门': ['/assets/guides/curated/full-gallery/雍和宫/01-昭泰门-cover.jpg',
                             '/assets/guides/curated/full-gallery/雍和宫/01-昭泰门-detail.jpg'],
                     '雍和门': ['/assets/guides/curated/full-gallery/雍和宫/02-雍和门-cover.jpg',
                             '/assets/guides/curated/full-gallery/雍和宫/02-雍和门-detail.jpg'],
                     '雍和宫大殿': ['/assets/guides/curated/full-gallery/雍和宫/03-雍和宫大殿-cover.jpg',
                               '/assets/guides/curated/full-gallery/雍和宫/03-雍和宫大殿-detail.jpg'],
                     '永佑殿': ['/assets/guides/curated/full-gallery/雍和宫/04-永佑殿-cover.jpg',
                             '/assets/guides/curated/full-gallery/雍和宫/04-永佑殿-detail.jpg'],
                     '法轮殿': ['/assets/guides/curated/full-gallery/雍和宫/05-法轮殿-cover.jpg',
                             '/assets/guides/curated/full-gallery/雍和宫/05-法轮殿-detail.jpg'],
                     '万福阁': ['/assets/guides/curated/full-gallery/雍和宫/06-万福阁-cover.jpg',
                             '/assets/guides/curated/full-gallery/雍和宫/06-万福阁-detail.jpg']}}
