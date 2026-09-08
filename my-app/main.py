from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import math
import json
import urllib.parse
import urllib.request

from app.catalog.heritage_images import HERITAGE_ROUTE_IMAGES
from app.paths import DB_PATH, SEED_DATA_PATH


app = FastAPI()

GUIDE_AUTHORS = {
    'palace_guide',
    'garden_curator',
    'ritual_guide',
    'wall_walker',
    'beijing_fan',
    'explorer',
    'culture_seeker',
    'canton_guide',
    'mountain_guide',
    'lingnan_curator',
    'city_history_guide',
    'shamian_walker',
    'shanghai_guide',
    'garden_story',
    'museum_curator',
    'bay_walker',
    'lotus_hill_guide',
    'dapeng_guard',
    'beihai_guide',
    'lama_temple_guide'
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_no_cache_headers(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def read_root():
    return FileResponse("index.html")

class User(BaseModel):
    username: str
    password: str
    avatar: str = None

class TranslationRequest(BaseModel):
    text: str
    target: str = 'en'

class RouteRecommendationRequest(BaseModel):
    username: str = ''
    preferences: list[str] = []
    available_hours: float = 4
    start_location: dict = {}
    tags: list[str] = []
    travel_date: str = ''
    route_focus: str = 'auto'

TRANSLATION_CACHE = {}

HERITAGE_SEED_ITEMS = [
    {
        'name': '景泰蓝制作技艺',
        'category': '传统技艺',
        'subcategory': '金属胎珐琅工艺',
        'inheritor': '北京珐琅厂工艺团队',
        'inheritor_intro': '以国家级工艺师和青年技师共同承担制胎、掐丝、点蓝、烧蓝、磨光等流程展示。',
        'historical_background': '景泰蓝在明清宫廷中发展成熟，因明代景泰年间蓝釉器物最具代表性而得名，是理解宫廷审美与手工技艺的重要窗口。',
        'location_name': '北京市东城区珐琅厂文化体验区',
        'city': '北京',
        'province': '北京',
        'latitude': 39.8954,
        'longitude': 116.4246,
        'activity_time': '周二至周日 09:30-16:30',
        'best_visit_time': '工作日上午，适合安排 1.5 小时体验',
        'suitable_duration': 90,
        'tags': ['传统技艺', '室内', '手工体验', '亲子', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['景泰蓝制作技艺'],
        'source_url': ''
    },
    {
        'name': '京剧',
        'category': '传统戏剧',
        'subcategory': '戏曲表演',
        'inheritor': '京剧院青年演员与票友社群',
        'inheritor_intro': '通过唱念做打、脸谱和行当讲解，让游客先建立观看京剧的入口。',
        'historical_background': '京剧形成于清代，融合徽调、汉调、昆曲等声腔，是中国戏曲舞台艺术的代表。',
        'location_name': '北京市前门传统戏楼片区',
        'city': '北京',
        'province': '北京',
        'latitude': 39.8995,
        'longitude': 116.3974,
        'activity_time': '演出多集中在 19:00-21:00，白天可预约体验课',
        'best_visit_time': '傍晚先体验妆造或行当讲解，晚上看折子戏',
        'suitable_duration': 120,
        'tags': ['传统戏剧', '夜间', '室内', '表演', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['天坛神乐署礼乐展示'],
        'source_url': ''
    },
    {
        'name': '陈家祠广府工艺导赏',
        'category': '传统技艺',
        'subcategory': '广府建筑装饰',
        'inheritor': '陈家祠岭南工艺讲解团队',
        'inheritor_intro': '围绕木雕、砖雕、石雕、陶塑和灰塑看广府工艺如何装饰祠堂空间。',
        'historical_background': '陈家祠以岭南建筑装饰工艺著称，集中呈现广府祠堂里的木石砖雕、陶塑灰塑和彩绘工艺。',
        'location_name': '广州市荔湾区陈家祠',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1290,
        'longitude': 113.2402,
        'activity_time': '周二至周日 09:00-17:30',
        'best_visit_time': '上午看中轴建筑，下午看装饰细节',
        'suitable_duration': 90,
        'tags': ['传统技艺', '岭南', '历史建筑', '室内', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['陈家祠广府工艺导赏'],
        'source_url': ''
    },
    {
        'name': '粤剧',
        'category': '传统戏剧',
        'subcategory': '岭南戏曲',
        'inheritor': '粤剧艺术博物馆驻场讲解与演员团队',
        'inheritor_intro': '通过身段、水袖、唱腔和戏服展示，将岭南声腔转化为可体验内容。',
        'historical_background': '粤剧流行于粤港澳及海外华人社区，是岭南文化传播的重要载体。',
        'location_name': '广州市荔湾区粤剧艺术博物馆',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1191,
        'longitude': 113.2498,
        'activity_time': '周二至周日 09:00-17:00，部分夜间演出需预约',
        'best_visit_time': '下午参观展陈，傍晚接续沙面或永庆坊',
        'suitable_duration': 100,
        'tags': ['传统戏剧', '岭南', '表演', '室内', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['沙面近代建筑导赏'],
        'source_url': ''
    },
    {
        'name': '上海老城厢民俗导赏',
        'category': '民俗',
        'subcategory': '老城厢生活',
        'inheritor': '上海老城厢文化讲解团队',
        'inheritor_intro': '围绕豫园、城隍庙街区和老城厢生活记忆，讲解上海传统城市空间。',
        'historical_background': '上海老城厢保留了江南园林、商业街巷和民俗活动的复合场景，是理解上海传统生活的重要入口。',
        'location_name': '上海市黄浦区老城厢文化空间',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2272,
        'longitude': 121.4920,
        'activity_time': '每日 09:00-20:00，民俗活动以节庆为主',
        'best_visit_time': '豫园游览前后安排 60-90 分钟',
        'suitable_duration': 80,
        'tags': ['民俗', '城市漫步', '园林', '轻松', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['上海老城厢民俗导赏'],
        'source_url': ''
    },
    {
        'name': '大鹏所城民俗',
        'category': '民俗',
        'subcategory': '海防古城生活',
        'inheritor': '大鹏所城社区讲解员',
        'inheritor_intro': '以城门、街巷、宗祠和海防故事串联社区记忆。',
        'historical_background': '大鹏所城见证了岭南海防、宗族聚落与滨海贸易，是深圳历史文化的重要根脉。',
        'location_name': '深圳市大鹏新区大鹏所城',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5978,
        'longitude': 114.4775,
        'activity_time': '全天开放，民俗活动多在节庆与周末',
        'best_visit_time': '上午避开暑热，安排 2 小时慢行',
        'suitable_duration': 120,
        'tags': ['民俗', '古城', '户外', '深度', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['大鹏所城民俗'],
        'source_url': ''
    },
    {
        'name': '宫廷建筑彩画',
        'category': '传统美术',
        'subcategory': '建筑装饰',
        'inheritor': '古建彩画修缮团队',
        'inheritor_intro': '通过梁枋纹样、设色规则和修缮工序讲解，让游客理解中国古建筑表面的秩序与审美。',
        'historical_background': '宫廷建筑彩画将等级制度、吉祥纹样和木构保护结合在一起，是理解皇家建筑不可缺少的细节。',
        'location_name': '北京市东城区故宫周边古建研学点',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9163,
        'longitude': 116.3972,
        'activity_time': '周二至周日 10:00-16:00，研学讲解需预约',
        'best_visit_time': '故宫或天坛参观前后安排 60-90 分钟',
        'suitable_duration': 75,
        'tags': ['传统美术', '历史建筑', '室内', '深度', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['宫廷建筑彩画'],
        'source_url': ''
    },
    {
        'name': '苏州园林造园技艺',
        'category': '传统技艺',
        'subcategory': '园林营造',
        'inheritor': '江南园林讲解与营造研究团队',
        'inheritor_intro': '从借景、叠石、理水、花窗和动线讲起，把园林从“好看”转化为可理解的空间体验。',
        'historical_background': '江南园林以有限空间组织山水、建筑和游线，体现文人审美与生活方式。',
        'location_name': '上海豫园及江南园林文化空间',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2272,
        'longitude': 121.4920,
        'activity_time': '每日 09:00-16:30',
        'best_visit_time': '上午或工作日下午，适合与老城厢体验结合',
        'suitable_duration': 90,
        'tags': ['传统技艺', '园林', '历史建筑', '户外', '轻松'],
        'cover_image': HERITAGE_ROUTE_IMAGES['苏州园林造园技艺'],
        'source_url': ''
    },
    {
        'name': '广府木雕与砖雕',
        'category': '传统技艺',
        'subcategory': '建筑雕刻',
        'inheritor': '岭南建筑工艺讲解团队',
        'inheritor_intro': '围绕祠堂构件、屋脊装饰和木石砖雕细节，讲解广府工艺如何服务宗族空间。',
        'historical_background': '广府木雕、砖雕和陶塑灰塑共同构成岭南建筑装饰体系，是祠堂与民居空间的重要文化语言。',
        'location_name': '广州市荔湾区陈家祠',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1290,
        'longitude': 113.2402,
        'activity_time': '周二至周日 09:00-17:30',
        'best_visit_time': '上午看中轴线，下午看工艺细节',
        'suitable_duration': 100,
        'tags': ['传统技艺', '岭南', '历史建筑', '室内', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['广府木雕与砖雕'],
        'source_url': ''
    },
    {
        'name': '长城营造与防御体系',
        'category': '传统技艺',
        'subcategory': '军事建筑营造',
        'inheritor': '长城保护讲解团队',
        'inheritor_intro': '从敌楼、关城、城墙走势和山势关系入手，解释长城为什么这样修、怎样守。',
        'historical_background': '长城不仅是城墙，也是关隘、敌楼、烽燧和交通体系组成的军事防御网络。',
        'location_name': '北京市延庆区八达岭长城',
        'city': '北京',
        'province': '北京',
        'latitude': 40.3594,
        'longitude': 116.0202,
        'activity_time': '旺季 06:30-16:30，淡季以景区公告为准',
        'best_visit_time': '清晨或下午，避开正午人流',
        'suitable_duration': 150,
        'tags': ['传统技艺', '历史建筑', '户外', '深度', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['长城营造与防御体系'],
        'source_url': ''
    },
    {
        'name': '海派博物馆文物导赏',
        'category': '博物馆',
        'subcategory': '文物导赏',
        'inheritor': '上海博物馆公共教育讲解团队',
        'inheritor_intro': '通过青铜器、陶瓷、书画和工艺品建立中国古代艺术的观看方法。',
        'historical_background': '博物馆导赏把文物从孤立展品转化为可比较、可理解的文化线索，适合外籍游客建立中国艺术入口。',
        'location_name': '上海市黄浦区上海博物馆',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2304,
        'longitude': 121.4700,
        'activity_time': '周二至周日 09:00-17:00',
        'best_visit_time': '雨天、炎热天气或半日室内路线',
        'suitable_duration': 120,
        'tags': ['博物馆', '室内', '国际友好', '深度', '少走路'],
        'cover_image': HERITAGE_ROUTE_IMAGES['海派博物馆文物导赏'],
        'source_url': ''
    },
    {
        'name': '滨海渔俗与海湾生活',
        'category': '民俗',
        'subcategory': '滨海生活',
        'inheritor': '深圳湾滨海文化讲解团队',
        'inheritor_intro': '结合海湾生态、渔业记忆和城市滨海空间，讲解深圳从海边聚落到湾区城市的变化。',
        'historical_background': '滨海民俗记录了渔业、口岸、迁徙和城市化之间的关系，是理解深圳城市文化的一条温和入口。',
        'location_name': '深圳市南山区深圳湾公园',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5147,
        'longitude': 113.9440,
        'activity_time': '全天开放，傍晚体验较佳',
        'best_visit_time': '傍晚慢行，适合轻松路线',
        'suitable_duration': 90,
        'tags': ['民俗', '户外', '轻松', '适合拍照', '城市漫步'],
        'cover_image': HERITAGE_ROUTE_IMAGES['滨海渔俗与海湾生活'],
        'source_url': ''
    }
]

HERITAGE_SEED_ITEMS[1].update({
    'name': '天坛神乐署礼乐展示',
    'category': '传统音乐',
    'subcategory': '礼乐文化',
    'inheritor': '天坛礼乐文化讲解团队',
    'inheritor_intro': '以神乐署建筑、祭祀音乐和明清礼制为线索，帮助游客理解礼乐如何服务国家祭典。',
    'historical_background': '神乐署是明清祭祀乐舞训练和管理的重要空间，适合与天坛中轴导览一起理解祭天礼仪。',
    'location_name': '北京市东城区天坛神乐署',
    'city': '北京',
    'province': '北京',
    'latitude': 39.8822,
    'longitude': 116.4128,
    'activity_time': '周二至周日 09:00-16:30，礼乐讲解按场次开放',
    'best_visit_time': '天坛中轴参观后安排 45-60 分钟',
    'suitable_duration': 60,
    'tags': ['传统音乐', '礼制', '室内', '国际友好', '深度'],
    'cover_image': HERITAGE_ROUTE_IMAGES['天坛神乐署礼乐展示']
})

HERITAGE_SEED_ITEMS[3].update({
    'name': '沙面近代建筑导赏',
    'category': '城市文化',
    'subcategory': '历史建筑',
    'inheritor': '沙面街区文化讲解团队',
    'inheritor_intro': '围绕欧陆建筑立面、街区尺度和珠江口岸记忆，讲解广州近代城市文化。',
    'historical_background': '沙面保留了广州近代商贸、外侨社区和建筑风格交汇的街区肌理，是理解岭南开放城市气质的入口。',
    'location_name': '广州市荔湾区沙面岛',
    'city': '广州市',
    'province': '广东省',
    'latitude': 23.1099,
    'longitude': 113.2399,
    'activity_time': '全天开放，建筑导赏建议 09:30-17:30',
    'best_visit_time': '上午或傍晚，适合慢走和拍照',
    'suitable_duration': 90,
    'tags': ['历史建筑', '城市漫步', '岭南', '户外', '适合拍照'],
    'cover_image': HERITAGE_ROUTE_IMAGES['沙面近代建筑导赏']
})

HERITAGE_SEED_ITEMS.extend([
    {
        'name': '故宫宫廷器物导赏',
        'category': '博物馆',
        'subcategory': '宫廷工艺',
        'inheritor': '故宫珍宝馆公共教育团队',
        'inheritor_intro': '用玉器、金银器和宫廷陈设讲解清代审美、工艺和礼制生活。',
        'historical_background': '故宫珍宝馆集中呈现宫廷器物工艺，是理解皇家生活与手工体系的直接场景。',
        'location_name': '北京市东城区故宫博物院珍宝馆',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9182,
        'longitude': 116.3999,
        'activity_time': '周二至周日 08:30-16:30',
        'best_visit_time': '故宫中轴游览后接续珍宝馆',
        'suitable_duration': 75,
        'tags': ['博物馆', '传统技艺', '室内', '深度', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['故宫宫廷器物导赏'],
        'source_url': ''
    },
    {
        'name': '颐和园长廊彩画',
        'category': '传统美术',
        'subcategory': '园林彩画',
        'inheritor': '颐和园古建彩画讲解团队',
        'inheritor_intro': '从长廊画面、题材和修缮方法入手，读懂皇家园林里的图像叙事。',
        'historical_background': '颐和园长廊以连续彩画连接湖山游线，是园林空间、历史故事和装饰技艺结合的典型案例。',
        'location_name': '北京市海淀区颐和园长廊',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9996,
        'longitude': 116.2725,
        'activity_time': '每日 08:30-17:00',
        'best_visit_time': '上午沿昆明湖慢行时穿插观看',
        'suitable_duration': 60,
        'tags': ['传统美术', '园林', '历史建筑', '户外', '轻松'],
        'cover_image': HERITAGE_ROUTE_IMAGES['颐和园长廊彩画'],
        'source_url': ''
    },
    {
        'name': '颐和园皇家园林营造',
        'category': '传统技艺',
        'subcategory': '园林营造',
        'inheritor': '颐和园园林讲解团队',
        'inheritor_intro': '把万寿山、昆明湖、长廊和十七孔桥串成一条可理解的造园逻辑。',
        'historical_background': '颐和园以山水格局组织皇家园林空间，体现借景、理水、轴线和游线的综合设计。',
        'location_name': '北京市海淀区颐和园',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9999,
        'longitude': 116.2755,
        'activity_time': '每日 08:30-17:00',
        'best_visit_time': '上午或傍晚，适合 2 小时湖山路线',
        'suitable_duration': 120,
        'tags': ['园林', '历史建筑', '户外', '适合拍照', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['颐和园皇家园林营造'],
        'source_url': ''
    },
    {
        'name': '圆明园遗址记忆导赏',
        'category': '城市文化',
        'subcategory': '遗址保护',
        'inheritor': '圆明园遗址公园讲解团队',
        'inheritor_intro': '围绕西洋楼遗址、福海和园林遗存，讲解遗址保护与历史记忆。',
        'historical_background': '圆明园遗址承载清代园林营造、近代创伤记忆和当代遗址保护教育。',
        'location_name': '北京市海淀区圆明园遗址公园',
        'city': '北京',
        'province': '北京',
        'latitude': 40.0084,
        'longitude': 116.3028,
        'activity_time': '每日 07:00-19:00',
        'best_visit_time': '下午光线较好，适合遗址慢行',
        'suitable_duration': 120,
        'tags': ['历史建筑', '园林', '户外', '深度', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['圆明园遗址记忆导赏'],
        'source_url': ''
    },
    {
        'name': '北海白塔与皇家园林导赏',
        'category': '城市文化',
        'subcategory': '皇家园林',
        'inheritor': '北海公园文化讲解团队',
        'inheritor_intro': '用琼华岛、白塔和湖面视线讲解皇家园林的空间组织。',
        'historical_background': '北海是北京皇家园林体系的重要组成，湖岛白塔构成极具识别度的城市文化景观。',
        'location_name': '北京市西城区北海公园',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9250,
        'longitude': 116.3899,
        'activity_time': '每日 06:30-20:00',
        'best_visit_time': '下午沿湖慢行',
        'suitable_duration': 90,
        'tags': ['园林', '历史建筑', '户外', '轻松', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['北海白塔与皇家园林导赏'],
        'source_url': ''
    },
    {
        'name': '雍和宫藏传佛教建筑导赏',
        'category': '城市文化',
        'subcategory': '宗教建筑',
        'inheritor': '雍和宫中轴建筑讲解团队',
        'inheritor_intro': '沿牌楼、天王殿、雍和宫殿宇讲解皇家寺院的空间秩序。',
        'historical_background': '雍和宫由王府转为皇家寺院，保留清代宫廷与藏传佛教文化交汇的建筑形态。',
        'location_name': '北京市东城区雍和宫',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9470,
        'longitude': 116.4174,
        'activity_time': '每日 09:00-16:30',
        'best_visit_time': '工作日上午，适合安静参观',
        'suitable_duration': 75,
        'tags': ['历史建筑', '室内', '深度', '国际友好', '少走路'],
        'cover_image': HERITAGE_ROUTE_IMAGES['雍和宫藏传佛教建筑导赏'],
        'source_url': ''
    },
    {
        'name': '越秀五羊传说与城史',
        'category': '民俗',
        'subcategory': '城市传说',
        'inheritor': '越秀公园城史讲解团队',
        'inheritor_intro': '从五羊石像、镇海楼和古城遗存讲起，把广州城市记忆转化成步行路线。',
        'historical_background': '五羊传说是广州城市身份的重要象征，越秀山同时保存城防、楼阁和近现代公园记忆。',
        'location_name': '广州市越秀区越秀公园',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1393,
        'longitude': 113.2644,
        'activity_time': '每日 06:00-22:00',
        'best_visit_time': '上午登楼看城史，下午避暑慢行',
        'suitable_duration': 90,
        'tags': ['民俗', '城市漫步', '户外', '岭南', '轻松'],
        'cover_image': HERITAGE_ROUTE_IMAGES['越秀五羊传说与城史'],
        'source_url': ''
    },
    {
        'name': '广州塔中轴城市导赏',
        'category': '城市文化',
        'subcategory': '城市地标',
        'inheritor': '广州城市中轴讲解团队',
        'inheritor_intro': '从珠江、新中轴和城市天际线讲解广州当代城市形象。',
        'historical_background': '广州塔是广州新中轴和珠江景观的代表节点，适合把传统岭南城市与当代都市连接起来。',
        'location_name': '广州市海珠区广州塔',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1067,
        'longitude': 113.3245,
        'activity_time': '每日 09:30-22:30',
        'best_visit_time': '傍晚至夜间，适合珠江夜景',
        'suitable_duration': 90,
        'tags': ['城市漫步', '夜间', '户外', '适合拍照', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['广州塔中轴城市导赏'],
        'source_url': ''
    },
    {
        'name': '白云山山水民俗路线',
        'category': '民俗',
        'subcategory': '山水游憩',
        'inheritor': '白云山文化讲解团队',
        'inheritor_intro': '结合摩星岭、山道和羊城山水审美，讲解广州人的登高游憩传统。',
        'historical_background': '白云山长期是广州城郊山水游憩地，承载登高、观城和市民休闲记忆。',
        'location_name': '广州市白云区白云山',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1821,
        'longitude': 113.2977,
        'activity_time': '每日 06:00-21:00',
        'best_visit_time': '清晨或傍晚，避开正午',
        'suitable_duration': 120,
        'tags': ['民俗', '户外', '轻松', '适合拍照', '城市漫步'],
        'cover_image': HERITAGE_ROUTE_IMAGES['白云山山水民俗路线'],
        'source_url': ''
    },
    {
        'name': '外滩近代建筑导赏',
        'category': '城市文化',
        'subcategory': '近代建筑',
        'inheritor': '外滩建筑讲解团队',
        'inheritor_intro': '沿中山东一路识别不同建筑风格，理解上海近代金融与口岸城市记忆。',
        'historical_background': '外滩建筑群记录了上海近代城市发展、金融机构和黄浦江天际线的形成。',
        'location_name': '上海市黄浦区外滩',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2402,
        'longitude': 121.4908,
        'activity_time': '全天开放，建筑导赏建议 09:00-21:00',
        'best_visit_time': '傍晚看立面与江景',
        'suitable_duration': 90,
        'tags': ['历史建筑', '城市漫步', '户外', '适合拍照', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['外滩近代建筑导赏'],
        'source_url': ''
    },
    {
        'name': '豫园江南园林导赏',
        'category': '传统技艺',
        'subcategory': '园林营造',
        'inheritor': '豫园园林文化讲解团队',
        'inheritor_intro': '从亭台、假山、池水和游线讲解江南园林的空间方法。',
        'historical_background': '豫园以老城厢空间承载江南园林审美，是上海城市中理解传统园林的代表场景。',
        'location_name': '上海市黄浦区豫园',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2272,
        'longitude': 121.4920,
        'activity_time': '每日 09:00-16:30',
        'best_visit_time': '上午避开人流',
        'suitable_duration': 90,
        'tags': ['传统技艺', '园林', '历史建筑', '户外', '轻松'],
        'cover_image': HERITAGE_ROUTE_IMAGES['豫园江南园林导赏'],
        'source_url': ''
    },
    {
        'name': '大鹏海防古城导赏',
        'category': '城市文化',
        'subcategory': '海防建筑',
        'inheritor': '大鹏所城文化讲解团队',
        'inheritor_intro': '沿城门、街巷和宗祠讲解深圳海防与聚落生活。',
        'historical_background': '大鹏所城是深圳重要历史根脉，连接岭南海防、宗族聚落和滨海贸易记忆。',
        'location_name': '深圳市龙岗区大鹏所城',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5978,
        'longitude': 114.4775,
        'activity_time': '全天开放，讲解多在 09:00-17:30',
        'best_visit_time': '上午慢行古城',
        'suitable_duration': 120,
        'tags': ['历史建筑', '民俗', '户外', '深度', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['大鹏海防古城导赏'],
        'source_url': ''
    },
    {
        'name': '莲花山城市记忆路线',
        'category': '城市文化',
        'subcategory': '城市公园',
        'inheritor': '莲花山公园城市导赏团队',
        'inheritor_intro': '从山顶广场、城市轴线和中心区视野讲解深圳现代城市发展。',
        'historical_background': '莲花山公园是观察深圳中心区空间变化的重要节点，适合把城市建设史转化为现场体验。',
        'location_name': '深圳市福田区莲花山公园',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5552,
        'longitude': 114.0596,
        'activity_time': '每日 06:00-23:00',
        'best_visit_time': '傍晚登顶看城市天际线',
        'suitable_duration': 75,
        'tags': ['城市漫步', '户外', '轻松', '适合拍照', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['莲花山城市记忆路线'],
        'source_url': ''
    },
    {
        'name': '前门大栅栏老字号街区',
        'category': '街区文化',
        'subcategory': '老字号商业街',
        'inheritor': '前门大栅栏街区讲解团队',
        'inheritor_intro': '以老字号店铺、胡同肌理、牌楼界面和传统商业礼仪为线索，带用户理解北京老城商业生活。',
        'historical_background': '前门大栅栏长期连接宫城、会馆、戏楼和市井商业，是北京老城里最容易把非遗技艺、老字号饮食、传统戏曲和街巷生活放在同一条步行线上理解的街区。',
        'location_name': '北京市西城区前门大栅栏',
        'city': '北京',
        'province': '北京',
        'latitude': 39.8958,
        'longitude': 116.3919,
        'activity_time': '每日 10:00-21:00，老字号和展陈空间以现场营业为准',
        'best_visit_time': '下午到傍晚，适合接续前门、戏楼或夜间小吃',
        'suitable_duration': 90,
        'tags': ['街区文化', '老字号', '城市漫步', '民俗', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['前门大栅栏老字号街区'],
        'source_url': ''
    },
    {
        'name': '北京胡同四合院生活导赏',
        'category': '街区文化',
        'subcategory': '胡同居住文化',
        'inheritor': '北京老城街区讲解团队',
        'inheritor_intro': '从胡同尺度、门墩门楼、院落秩序和邻里生活讲起，把游客从“拍胡同”带到“看懂胡同”。',
        'historical_background': '胡同与四合院构成北京老城最基本的生活单元。它们不仅是建筑形态，也保存着家庭伦理、街坊交往、节令活动和城市治理的细节。',
        'location_name': '北京市东城区胡同街区',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9395,
        'longitude': 116.4036,
        'activity_time': '全天开放，居民区建议 09:00-18:00 轻声慢行',
        'best_visit_time': '上午光线柔和，适合安静步行',
        'suitable_duration': 75,
        'tags': ['街区文化', '历史建筑', '城市漫步', '轻松', '少走路'],
        'cover_image': HERITAGE_ROUTE_IMAGES['北京胡同四合院生活导赏'],
        'source_url': ''
    },
    {
        'name': '永庆坊西关生活街区',
        'category': '街区文化',
        'subcategory': '西关生活',
        'inheritor': '永庆坊与西关文化讲解团队',
        'inheritor_intro': '围绕骑楼、趟栊门、粤剧博物馆和荔湾水系，讲解广州西关生活方式。',
        'historical_background': '永庆坊所在的西关片区汇聚粤剧、骑楼、老字号与水边街巷，是理解广州传统生活和当代街区更新的温和入口。',
        'location_name': '广州市荔湾区永庆坊',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1196,
        'longitude': 113.2485,
        'activity_time': '街区全天开放，展馆多为 09:00-17:00',
        'best_visit_time': '下午接续粤剧艺术博物馆，傍晚沿荔枝湾慢走',
        'suitable_duration': 100,
        'tags': ['街区文化', '岭南', '城市漫步', '民俗', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['永庆坊西关生活街区'],
        'source_url': ''
    },
    {
        'name': '广州北京路古道街区',
        'category': '街区文化',
        'subcategory': '古道与商业中轴',
        'inheritor': '广州古城中轴讲解团队',
        'inheritor_intro': '从古道遗址、骑楼商业和城市中轴讲起，让用户在繁华街面下看到广州城史层次。',
        'historical_background': '北京路一带叠压着古代道路遗存、传统商业和现代步行街，是广州城市中轴连续发展的可视化现场。',
        'location_name': '广州市越秀区北京路步行街',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1252,
        'longitude': 113.2698,
        'activity_time': '每日 10:00-22:00，古道遗址展示以现场开放为准',
        'best_visit_time': '下午到夜间，适合接续越秀公园或珠江沿线',
        'suitable_duration': 80,
        'tags': ['街区文化', '历史建筑', '城市漫步', '岭南', '夜间'],
        'cover_image': HERITAGE_ROUTE_IMAGES['广州北京路古道街区'],
        'source_url': ''
    },
    {
        'name': '人民公园海派生活导赏',
        'category': '街区文化',
        'subcategory': '公共生活与海派城市',
        'inheritor': '人民广场片区公共文化讲解团队',
        'inheritor_intro': '把人民公园、上海博物馆、南京路和城市公共空间联系起来，观察海派生活的日常面。',
        'historical_background': '人民广场和人民公园周边集中呈现上海现代公共文化、博物馆资源和商业街区，适合与外滩或上海博物馆形成半日线路。',
        'location_name': '上海市黄浦区人民公园',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2316,
        'longitude': 121.4708,
        'activity_time': '公园每日开放，博物馆多为 09:00-17:00',
        'best_visit_time': '雨天可优先博物馆，晴天接续南京路步行',
        'suitable_duration': 75,
        'tags': ['街区文化', '博物馆', '城市漫步', '轻松', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['人民公园海派生活导赏'],
        'source_url': ''
    },
    {
        'name': '上海石库门里弄生活导赏',
        'category': '街区文化',
        'subcategory': '里弄居住文化',
        'inheritor': '海派里弄文化讲解团队',
        'inheritor_intro': '从石库门门头、弄堂尺度、公共厨房和邻里生活讲解上海近代居住文化。',
        'historical_background': '石库门和里弄连接江南民居、近代城市化和海派生活方式，是上海城市记忆中最具生活质感的部分。',
        'location_name': '上海市黄浦区石库门里弄街区',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2195,
        'longitude': 121.4752,
        'activity_time': '街区全天开放，展馆以 10:00-18:00 为主',
        'best_visit_time': '上午或傍晚，适合低强度街区慢行',
        'suitable_duration': 90,
        'tags': ['街区文化', '历史建筑', '城市漫步', '民俗', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['上海石库门里弄生活导赏'],
        'source_url': ''
    },
    {
        'name': '南头古城广府移民记忆',
        'category': '街区文化',
        'subcategory': '古城与移民记忆',
        'inheritor': '南头古城街区讲解团队',
        'inheritor_intro': '围绕古城门、祠堂、街巷和更新后的公共空间，讲解深圳更早的城市根脉。',
        'historical_background': '南头古城保留岭南城址和移民生活记忆，也呈现深圳城市更新后的公共文化空间，是理解深圳不只有现代天际线的重要补充。',
        'location_name': '深圳市南山区南头古城',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5393,
        'longitude': 113.9295,
        'activity_time': '街区全天开放，展陈空间多为 10:00-18:00',
        'best_visit_time': '下午慢行，傍晚可接续南山周边餐饮',
        'suitable_duration': 90,
        'tags': ['街区文化', '历史建筑', '民俗', '城市漫步', '轻松'],
        'cover_image': HERITAGE_ROUTE_IMAGES['南头古城广府移民记忆'],
        'source_url': ''
    },
    {
        'name': '深圳华侨城创意街区导赏',
        'category': '街区文化',
        'subcategory': '城市更新与创意社区',
        'inheritor': '华侨城创意文化讲解团队',
        'inheritor_intro': '从工业空间改造、设计店铺、公共艺术和社区活动讲解深圳当代文化街区。',
        'historical_background': '华侨城创意文化园体现深圳从产业空间到文化消费和创意社区的转化，适合与传统古城路线形成新旧城市对照。',
        'location_name': '深圳市南山区华侨城创意文化园',
        'city': '深圳市',
        'province': '广东省',
        'latitude': 22.5398,
        'longitude': 113.9815,
        'activity_time': '街区全天开放，店铺多为 11:00-21:00',
        'best_visit_time': '下午到傍晚，适合轻松看展和街区停留',
        'suitable_duration': 80,
        'tags': ['街区文化', '城市漫步', '轻松', '适合拍照', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['深圳华侨城创意街区导赏'],
        'source_url': ''
    },
    {
        'name': '京剧',
        'category': '传统戏剧',
        'subcategory': '戏曲表演',
        'inheritor': '北京京剧院与戏曲公共教育团队',
        'inheritor_intro': '从生旦净丑、唱念做打、脸谱行当和服装水袖入手，让用户先看懂舞台规则，再进入演出欣赏。',
        'historical_background': '京剧形成于清代，融合徽调、汉调、昆曲等声腔，是中国戏曲舞台艺术的代表性非遗项目。它的价值不只在剧情，更在程式化身段、唱腔板式、脸谱色彩和舞台调度。',
        'location_name': '北京市前门传统戏楼片区',
        'city': '北京',
        'province': '北京',
        'latitude': 39.8995,
        'longitude': 116.3974,
        'activity_time': '演出多集中在 19:00-21:00，白天可预约妆造或行当体验',
        'best_visit_time': '傍晚先体验行当讲解，晚上看折子戏或经典选段',
        'suitable_duration': 120,
        'tags': ['传统戏剧', '表演', '室内', '夜间', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['京剧'],
        'source_url': ''
    },
    {
        'name': '北京皮影戏',
        'category': '传统戏剧',
        'subcategory': '影偶表演',
        'inheritor': '北京皮影戏传承与展演团队',
        'inheritor_intro': '通过影偶雕刻、操纵杆、灯影幕布和唱白配合，让用户看到“幕后手艺”和“台前影像”如何合成。',
        'historical_background': '皮影戏以兽皮或纸板雕刻人物，经灯光投影形成表演，是集雕刻、美术、音乐、说唱和戏剧于一体的传统戏剧形态。',
        'location_name': '北京市东城区非遗展演空间',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9148,
        'longitude': 116.4039,
        'activity_time': '周末及节假日常有亲子展演，具体以场馆排期为准',
        'best_visit_time': '下午安排 60-90 分钟，适合亲子和初次了解非遗',
        'suitable_duration': 75,
        'tags': ['传统戏剧', '民间美术', '亲子', '室内', '手工体验'],
        'cover_image': HERITAGE_ROUTE_IMAGES['北京皮影戏'],
        'source_url': ''
    },
    {
        'name': '北京剪纸',
        'category': '传统美术',
        'subcategory': '民间剪纸',
        'inheritor': '北京剪纸非遗体验团队',
        'inheritor_intro': '从折纸、起稿、阴刻阳刻和吉祥纹样讲起，让用户理解一张红纸里的节令礼俗。',
        'historical_background': '剪纸广泛用于年节窗花、婚俗装饰和民间祝福，是中国民间美术最直观、最容易被用户理解和参与的非遗形式之一。',
        'location_name': '北京市西城区非遗体验空间',
        'city': '北京',
        'province': '北京',
        'latitude': 39.9026,
        'longitude': 116.3775,
        'activity_time': '体验课多为 10:00-17:00，节庆期间活动更集中',
        'best_visit_time': '上午或下午，适合 1 小时轻体验',
        'suitable_duration': 60,
        'tags': ['传统美术', '手工体验', '亲子', '室内', '民俗'],
        'cover_image': HERITAGE_ROUTE_IMAGES['北京剪纸'],
        'source_url': ''
    },
    {
        'name': '粤剧表演艺术',
        'category': '传统戏剧',
        'subcategory': '岭南戏曲',
        'inheritor': '粤剧艺术博物馆驻场讲解与演员团队',
        'inheritor_intro': '通过身段、水袖、唱腔、锣鼓点和戏服展示，把岭南声腔转化为可观看、可体验的内容。',
        'historical_background': '粤剧流行于粤港澳及海外华人社区，是岭南文化传播的重要载体。它融合唱做念打、南派武功、广府方言和精致戏服，是广州非遗路线里最应该被优先看到的内容。',
        'location_name': '广州市荔湾区粤剧艺术博物馆',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1191,
        'longitude': 113.2498,
        'activity_time': '周二至周日 09:00-17:00，部分演出需预约',
        'best_visit_time': '下午参观展陈，傍晚接续永庆坊或荔枝湾',
        'suitable_duration': 100,
        'tags': ['传统戏剧', '岭南', '表演', '室内', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['粤剧表演艺术'],
        'source_url': ''
    },
    {
        'name': '广东醒狮',
        'category': '传统舞蹈',
        'subcategory': '岭南节庆表演',
        'inheritor': '广东醒狮传承与训练团队',
        'inheritor_intro': '从狮头扎作、鼓点、采青、步法和高桩动作讲起，让用户理解醒狮不是“热闹表演”，而是完整的身体技艺。',
        'historical_background': '醒狮是岭南节庆和民俗活动中极具识别度的非遗项目，连接武术训练、音乐节奏、扎作工艺和社区仪式。',
        'location_name': '广州市荔湾区非遗展演空间',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1226,
        'longitude': 113.2448,
        'activity_time': '节庆、周末和展演日较多，具体以现场排期为准',
        'best_visit_time': '周末下午或节庆期间，适合安排 60-90 分钟',
        'suitable_duration': 75,
        'tags': ['传统舞蹈', '岭南', '表演', '民俗', '适合拍照'],
        'cover_image': HERITAGE_ROUTE_IMAGES['广东醒狮'],
        'source_url': ''
    },
    {
        'name': '广绣',
        'category': '传统美术',
        'subcategory': '岭南刺绣',
        'inheritor': '广绣工艺展示与体验团队',
        'inheritor_intro': '通过针法、色线、图案层次和绣面光泽讲解广绣的精细工艺，适合做近距离观察。',
        'historical_background': '广绣是粤绣的重要代表，以构图饱满、色彩明丽和针法丰富著称，常见于服饰、屏风、挂幅和礼仪用品。',
        'location_name': '广州市越秀区非遗展示空间',
        'city': '广州市',
        'province': '广东省',
        'latitude': 23.1292,
        'longitude': 113.2643,
        'activity_time': '展陈空间多为 10:00-17:00，手作体验需预约',
        'best_visit_time': '上午或雨天室内体验',
        'suitable_duration': 70,
        'tags': ['传统美术', '岭南', '手工体验', '室内', '深度'],
        'cover_image': HERITAGE_ROUTE_IMAGES['广绣'],
        'source_url': ''
    },
    {
        'name': '昆曲',
        'category': '传统戏剧',
        'subcategory': '雅部戏曲',
        'inheritor': '昆曲公共教育与演出团队',
        'inheritor_intro': '从水磨腔、身段、折子戏和文人审美讲起，让用户感受昆曲的慢节奏与细腻表达。',
        'historical_background': '昆曲被称为“百戏之祖”，其声腔、身段和文学性深刻影响了中国戏曲发展，适合作为传统戏剧深度路线的代表项目。',
        'location_name': '上海市中心戏曲展演空间',
        'city': '上海市',
        'province': '上海',
        'latitude': 31.2316,
        'longitude': 121.4708,
        'activity_time': '演出和导赏以剧场排期为准，常见于周末下午或夜间',
        'best_visit_time': '周末下午导赏后接晚场演出',
        'suitable_duration': 120,
        'tags': ['传统戏剧', '表演', '室内', '深度', '国际友好'],
        'cover_image': HERITAGE_ROUTE_IMAGES['昆曲'],
        'source_url': ''
    }
])

HERITAGE_VISIT_ACTIONS = {
    '景泰蓝制作技艺': '看掐丝、点蓝等宫廷珐琅工艺流程，适合做一段手作体验。',
    '天坛神乐署礼乐展示': '听礼乐讲解，理解祭天仪式中的音乐、空间和礼制。',
    '陈家祠广府工艺导赏': '看木雕、砖雕、陶塑和灰塑细节，读懂广府祠堂装饰工艺。',
    '沙面近代建筑导赏': '沿街慢走，看欧陆建筑立面和广州近代口岸记忆。',
    '上海老城厢民俗导赏': '逛豫园和老城厢街区，看上海传统生活与民俗空间。',
    '大鹏所城民俗': '走城门、街巷和宗祠，了解深圳海防古城生活。',
    '宫廷建筑彩画': '看梁枋彩画和修缮讲解，理解古建筑表面的纹样秩序。',
    '苏州园林造园技艺': '看叠石、理水、借景和游线，理解江南园林怎么被设计出来。',
    '广府木雕与砖雕': '看祠堂构件和雕刻细节，理解岭南建筑装饰语言。',
    '长城营造与防御体系': '沿关城和敌楼行走，了解长城如何依山势组织防御。',
    '海派博物馆文物导赏': '看青铜、陶瓷和书画展品，建立中国古代艺术观看方法。',
    '滨海渔俗与海湾生活': '沿海湾慢行，了解深圳滨海生活、渔业记忆和城市变化。',
    '故宫宫廷器物导赏': '看玉器、金银器和宫廷陈设，理解皇家生活与工艺审美。',
    '颐和园长廊彩画': '沿长廊看连续彩画，读懂园林中的历史故事和装饰技艺。',
    '颐和园皇家园林营造': '沿湖山游线看万寿山、昆明湖和长廊，理解皇家园林布局。',
    '圆明园遗址记忆导赏': '看西洋楼遗址和园林遗存，理解遗址保护与历史记忆。',
    '北海白塔与皇家园林导赏': '沿湖岛看白塔和皇家园林视线，适合轻松慢游。',
    '雍和宫藏传佛教建筑导赏': '沿中轴殿宇参观，理解皇家寺院空间秩序。',
    '越秀五羊传说与城史': '看五羊石像和镇海楼，把广州城史串成步行路线。',
    '广州塔中轴城市导赏': '登高或沿珠江看城市中轴，感受广州当代天际线。',
    '白云山山水民俗路线': '登山看城景，体验广州人的登高游憩传统。',
    '外滩近代建筑导赏': '沿黄浦江识别建筑风格，理解上海近代金融与口岸城市。',
    '豫园江南园林导赏': '看亭台、假山和水院，理解上海老城厢里的江南园林。',
    '大鹏海防古城导赏': '沿古城街巷看海防建筑和社区记忆。',
    '莲花山城市记忆路线': '登上城市绿丘，看深圳中心区发展和城市轴线。',
    '前门大栅栏老字号街区': '沿前门到大栅栏慢走，看老字号、戏楼和北京老城商业生活。',
    '北京胡同四合院生活导赏': '放慢脚步看门楼、院落和胡同尺度，理解北京老城居住文化。',
    '永庆坊西关生活街区': '走骑楼街巷、看粤剧空间和西关生活，适合与荔枝湾一起安排。',
    '广州北京路古道街区': '在步行街下方看古道遗址，把商业街和广州城史联系起来。',
    '人民公园海派生活导赏': '从公园、博物馆和南京路看上海公共生活与海派城市气质。',
    '上海石库门里弄生活导赏': '看石库门门头和弄堂尺度，理解上海近代居住生活。',
    '南头古城广府移民记忆': '走古城门和街巷，看深圳更早的岭南城址与移民记忆。',
    '深圳华侨城创意街区导赏': '看旧空间更新、设计店铺和公共艺术，理解深圳当代文化街区。',
    '京剧': '看生旦净丑、脸谱、身段和唱念做打，晚上可接一场折子戏。',
    '北京皮影戏': '看影偶、灯影幕布和幕后操纵，理解雕刻、说唱和表演如何合在一起。',
    '北京剪纸': '看红纸纹样和阴刻阳刻，适合做一段轻量手作体验。',
    '粤剧表演艺术': '看粤剧身段、水袖、戏服和锣鼓点，理解岭南戏曲的声音与舞台。',
    '广东醒狮': '看狮头、鼓点、步法和采青动作，感受岭南节庆表演。',
    '广绣': '近距离看针法、色线和绣面层次，适合安排室内深度观察。',
    '昆曲': '听水磨腔、看身段和折子戏，适合传统戏剧深度体验。'
}

HERITAGE_RICH_COPY = {
    '景泰蓝制作技艺': {
        'visit_action': '重点看掐丝、点蓝、烧蓝和磨光。细铜丝先被掐成花叶、云纹、回纹等轮廓，再把矿物色釉一点点填入纹样格子里，最后经过反复烧制和打磨，才会出现明亮、厚润、带金属边线的蓝色光泽。',
        'inheritor_intro': '北京珐琅厂工艺团队以制胎、掐丝、点蓝、烧蓝、磨光、镀金等完整流程展示景泰蓝。体验时不要只看成品，可以特别观察铜丝如何决定图案边界、釉色如何在烧制后变得沉稳通透。',
        'historical_background': '景泰蓝又称铜胎掐丝珐琅，在明清宫廷中高度成熟，尤其因明代景泰年间蓝釉器物风格鲜明而得名。它把金属工艺、绘画纹样、釉料烧成和宫廷审美结合在一起，是理解皇家器物制度、吉祥图案和手工精度的重要入口。'
    },
    '天坛神乐署礼乐展示': {
        'visit_action': '重点看祭祀音乐、乐舞训练空间和礼制说明。这里不是单纯听音乐，而是理解声音、步伐、队列和建筑轴线如何共同服务祭天仪式。',
        'inheritor_intro': '天坛礼乐文化讲解团队会从神乐署建筑、乐器陈列、祭祀乐章和明清礼制讲起。适合先走天坛中轴，再进入神乐署，把祈年殿、圜丘坛和礼乐制度连成一个完整系统。',
        'historical_background': '神乐署曾是明清祭祀乐舞训练和管理的重要机构。祭天礼仪强调秩序、方位、节奏与等级，礼乐并不是背景音乐，而是国家仪式的一部分；理解神乐署，才能看懂天坛为什么以如此严整的空间组织呈现。'
    },
    '陈家祠广府工艺导赏': {
        'visit_action': '重点看木雕、砖雕、石雕、陶塑、灰塑和彩绘如何同时出现在一座祠堂里。屋脊、梁架、门罩、檐口和屏风处都有密集细节，适合慢慢找人物故事、花鸟纹样和吉祥寓意。',
        'inheritor_intro': '陈家祠岭南工艺讲解团队会把建筑构件当作工艺展柜来看。游客可以沿中轴走，也可以停在屋檐和门楼下观察材料差异：木雕讲层次，砖雕讲刀法，陶塑灰塑讲色彩和屋脊叙事。',
        'historical_background': '陈家祠是广府祠堂建筑与岭南装饰工艺的集中代表。它原本承担宗族教育、祭祀和会馆功能，如今则像一部立体的广府工艺百科，展示地方社会如何用建筑装饰表达家族、礼仪和审美。'
    },
    '沙面近代建筑导赏': {
        'visit_action': '沿沙面大街、教堂和旧领事馆建筑群慢走，重点看柱廊、拱窗、阳台、山花和街道尺度。这里的价值不在单栋建筑打卡，而在整片街区保留了近代口岸城市的空间气质。',
        'inheritor_intro': '沙面街区文化讲解团队会从建筑立面、街区尺度和珠江口岸记忆讲起。适合上午或傍晚慢行，边看欧陆建筑边理解广州近代商贸、外侨社区和城市开放史。',
        'historical_background': '沙面曾是广州近代对外贸易和外侨活动的重要区域，留下了多种西式建筑风格与岭南城市生活交汇的痕迹。它让游客看到广州不是只有传统祠堂和现代高楼，也有一段面向海洋和世界的近代城市记忆。'
    },
    '上海老城厢民俗导赏': {
        'visit_action': '围绕豫园、城隍庙和老城厢街巷看市井生活、节庆消费、香火记忆和江南园林。适合边走边看店铺招牌、院落入口和人流动线。',
        'inheritor_intro': '上海老城厢文化讲解团队会把园林、庙市、商业街和居民生活放在一起讲。游客可以从豫园的精致空间进入，再走到城隍庙周边感受传统民俗如何变成城市公共生活。',
        'historical_background': '老城厢是上海传统城市空间的重要遗存，在开埠以前就承载着庙会、商贸、居住和园林生活。它与外滩、南京路代表的近代上海不同，更能看到上海作为江南城市的民俗底色。'
    },
    '大鹏所城民俗': {
        'visit_action': '走城门、街巷、宗祠和古井，重点看海防古城里的日常生活痕迹。这里适合慢行，不适合只拍城门就离开。',
        'inheritor_intro': '大鹏所城社区讲解员会把海防故事、宗族聚落和滨海生活串起来。游客可以从南门进入，沿老街看祠堂、将军第和居民院落，理解深圳更早的历史根脉。',
        'historical_background': '大鹏所城始建于明代，是岭南海防体系的重要节点。它记录了军事防御、滨海贸易、宗族聚居和地方民俗的交叠，是深圳从海防边地到现代城市之前的重要历史层。'
    },
    '宫廷建筑彩画': {
        'visit_action': '重点看梁枋上的和玺彩画、旋子彩画、苏式彩画以及龙凤、云纹、卷草等纹样。彩画既是装饰，也是木构建筑的保护层和等级语言。',
        'inheritor_intro': '古建彩画修缮团队会从纹样等级、设色规则、矿物颜料和修缮工序讲起。游客可以对照宫殿屋檐下的梁枋细节，理解为什么皇家建筑的颜色和图案不能随意使用。',
        'historical_background': '宫廷建筑彩画在明清皇家建筑中形成严格规范。它把礼制等级、吉祥象征、木构保护和视觉秩序结合起来，是理解紫禁城、坛庙和皇家园林不可缺少的细节。'
    },
    '苏州园林造园技艺': {
        'visit_action': '重点看叠石、理水、借景、花窗和游线。园林不是把景物摆在一起，而是通过转折、遮挡、框景和步移景异，让小空间产生丰富层次。',
        'inheritor_intro': '江南园林讲解与营造研究团队会用“怎么走、在哪里停、从哪个窗看”来解释造园。适合放慢脚步看路径和视线，而不是只拍亭子和假山。',
        'historical_background': '江南园林以有限空间组织山水、建筑和文人生活，体现了中国传统空间审美。造园技艺连接建筑、绘画、诗文和日常起居，是传统生活方式的综合表达。'
    },
    '广府木雕与砖雕': {
        'visit_action': '重点看祠堂梁架、门罩、墀头和墙面上的雕刻。木雕常表现人物故事和花鸟瑞兽，砖雕则更讲究刀法、层次和灰色材质里的细腻光影。',
        'inheritor_intro': '岭南建筑工艺讲解团队会从构件位置和题材寓意讲起。游客可以把雕刻当作“写在建筑上的故事书”，看宗族空间如何用图像表达祝福、教化和身份。',
        'historical_background': '广府木雕、砖雕与陶塑灰塑共同构成岭南建筑装饰体系。它们不仅美化建筑，也反映地方财富、宗族礼仪、民间信仰和工匠组织，是广府文化极具辨识度的视觉语言。'
    },
    '长城营造与防御体系': {
        'visit_action': '沿关城、城墙、敌楼和山脊走势观察，重点看长城如何顺应地形。每一段坡度、转折和敌楼间距，都和防御、瞭望、交通有关。',
        'inheritor_intro': '长城保护讲解团队会从夯筑、包砖、排水、敌楼和关隘体系讲起。游客不只是“爬长城”，而是在现场理解山势、军事组织和建筑技术如何结合。',
        'historical_background': '长城不是单一城墙，而是关隘、敌台、烽燧、墙体和道路组成的庞大防御系统。八达岭一带因地势险要、保存较好，能直观看到明代北方防御工程的组织方式。'
    },
    '海派博物馆文物导赏': {
        'visit_action': '重点看青铜器、陶瓷、书画和玉器如何呈现中国古代艺术脉络。适合雨天或炎热天气做半日室内文化路线。',
        'inheritor_intro': '上海博物馆公共教育讲解团队会帮助游客建立观看方法：先看器形、纹样、材质和用途，再看时代风格和审美变化。',
        'historical_background': '博物馆导赏把孤立展品转化为可比较的文化线索。上海作为现代都市，借博物馆把中国古代艺术、海派公共文化和国际游客的理解入口连接起来。'
    },
    '滨海渔俗与海湾生活': {
        'visit_action': '沿海湾步道看红树林、海面、桥梁和滨海公共空间，重点理解渔业记忆、口岸变化和现代城市生活的关系。',
        'inheritor_intro': '深圳湾滨海文化讲解团队会把海湾生态、渔村记忆和城市化放在一起讲。适合傍晚慢行，边看海风和天际线边理解深圳从海边聚落到湾区城市的变化。',
        'historical_background': '滨海民俗记录了渔业、迁徙、口岸和城市建设之间的关系。深圳的现代形象很强，但海湾生活提醒游客：城市的根脉也来自海岸、潮汐和社区劳动。'
    },
    '故宫宫廷器物导赏': {
        'visit_action': '重点看玉器、金银器、珐琅器和宫廷陈设。不要只看“贵重”，要看材料、工艺、纹样和礼制用途如何共同塑造皇家审美。',
        'inheritor_intro': '故宫珍宝馆公共教育团队会从器物功能、制作工艺和宫廷生活讲起。游客可以把每件器物当作宫廷制度的缩影，理解什么场合使用、谁能使用、为什么这样装饰。',
        'historical_background': '故宫珍宝馆集中呈现清代宫廷器物工艺。它让游客从宏大的宫殿转向细密的生活物件，看到皇家权力、礼仪秩序和手工体系如何落在一只杯、一件玉器或一件珐琅器上。'
    },
    '颐和园长廊彩画': {
        'visit_action': '沿长廊慢走，重点看梁枋上的山水、人物、花鸟和故事图像。长廊不只是遮阳避雨的通道，也是一条连续展开的图像叙事带。',
        'inheritor_intro': '颐和园古建彩画讲解团队会从画面题材、构图位置和修缮方式讲起。游客可以边走边找熟悉的历史故事和文学题材，感受皇家园林里的视觉阅读。',
        'historical_background': '颐和园长廊以连续彩画连接万寿山和昆明湖游线，是园林空间、历史故事和装饰技艺结合的典型案例。它体现了皇家园林把行走、休憩和观看组织成完整体验的能力。'
    },
    '颐和园皇家园林营造': {
        'visit_action': '重点看万寿山、昆明湖、长廊、佛香阁和十七孔桥之间的空间关系。皇家园林的精彩在于山水格局、轴线和视线的组织。',
        'inheritor_intro': '颐和园园林讲解团队会把湖、山、建筑和步行动线串成一套造园逻辑。游客适合先建立方向感，再沿湖慢行，看建筑如何借山水增强气势。',
        'historical_background': '颐和园继承并发展了中国皇家园林传统，以昆明湖和万寿山为骨架，融合政治礼仪、休闲游赏和江南园林意象。它展示了皇家权力如何通过山水空间被视觉化。'
    },
    '圆明园遗址记忆导赏': {
        'visit_action': '重点看西洋楼遗址、大水法、海晏堂、福海和遗址保护说明。这里的体验不是怀旧拍照，而是理解废墟如何承载历史记忆。',
        'inheritor_intro': '圆明园遗址公园讲解团队会从清代园林营造、近代劫难和当代保护教育三条线讲起。游客适合放慢节奏，在遗址细节和空旷感中理解历史重量。',
        'historical_background': '圆明园曾是清代大型皇家园林群，融合中式山水与西洋楼建筑。它的遗址状态本身就是历史的一部分，提醒游客园林技艺、国家记忆和文物保护之间的复杂关系。'
    },
    '北海白塔与皇家园林导赏': {
        'visit_action': '沿湖看琼华岛、白塔、五龙亭和湖面视线。重点观察白塔如何成为北京老城天际线和皇家园林视觉中心。',
        'inheritor_intro': '北海公园文化讲解团队会从湖岛格局、藏传佛教符号和皇家游赏空间讲起。适合下午沿湖慢行，路线轻松但文化信息丰富。',
        'historical_background': '北海是北京皇家园林体系的重要组成，历史层累深厚。湖岛白塔的组合把宗教象征、皇家审美和城市景观结合起来，是理解北京古都空间的重要节点。'
    },
    '雍和宫藏传佛教建筑导赏': {
        'visit_action': '沿中轴看牌楼、天王殿、雍和宫大殿、法轮殿和万福阁。重点看皇家建筑形制如何与藏传佛教图像、法器和空间礼仪结合。',
        'inheritor_intro': '雍和宫中轴建筑讲解团队会从王府、行宫到皇家寺院的转变讲起。游客可以看殿宇尺度、屋顶等级和宗教陈设，理解多元文化如何进入北京城市空间。',
        'historical_background': '雍和宫由清代王府转为皇家寺院，是宫廷政治、藏传佛教和多民族文化交流的重要场所。它的建筑空间保留了清代皇家秩序，也呈现宗教仪式的庄严感。'
    },
    '越秀五羊传说与城史': {
        'visit_action': '看五羊石像、镇海楼、明代城墙和越秀山地形，重点理解传说、城防和城市记忆如何叠在同一座公园里。',
        'inheritor_intro': '越秀公园城史讲解团队会从五羊传说讲到广州城墙和镇海楼。游客可以把这里当作广州城市身份的入门点：既有民间传说，也有真实城防遗存。',
        'historical_background': '五羊传说是广州“羊城”身份的重要来源，越秀山则保存着古城防和近现代公园记忆。它把神话、地形、城市建设和公共休闲结合起来，是理解广州城史的温和入口。'
    },
    '广州塔中轴城市导赏': {
        'visit_action': '从广州塔、海心桥、珠江和新中轴看城市天际线。重点理解传统岭南城市如何延展为当代都市景观。',
        'inheritor_intro': '广州城市中轴讲解团队会把珠江、新中轴、花城广场和广州塔联系起来讲。适合傍晚到夜间，视觉体验强，也方便衔接珠江夜景。',
        'historical_background': '广州塔是广州新中轴和珠江景观的代表节点。它不是传统非遗本体，但能帮助游客理解当代广州如何在历史城市基础上塑造新的公共形象。'
    },
    '白云山山水民俗路线': {
        'visit_action': '登山看城景、山道、摩星岭和市民休闲场景。重点感受广州人登高、观城和亲近山水的日常传统。',
        'inheritor_intro': '白云山文化讲解团队会从羊城山水审美、登高习俗和市民游憩讲起。适合清晨或傍晚，避开正午，把自然体验和城市文化结合起来。',
        'historical_background': '白云山长期是广州城郊山水游憩地，既承载文人题咏，也承载普通市民的登高休闲。它让游客看到民俗不只发生在节庆，也存在于城市人与山水的日常关系里。'
    },
    '外滩近代建筑导赏': {
        'visit_action': '沿中山东一路看银行、海关、饭店和外滩源建筑群。重点识别古典主义、装饰艺术等建筑风格和黄浦江视线。',
        'inheritor_intro': '外滩建筑讲解团队会从建筑立面、金融机构和口岸城市记忆讲起。游客适合傍晚慢走，看立面细节和浦江两岸的时代对照。',
        'historical_background': '外滩建筑群记录了上海近代金融、贸易和城市现代化进程。它不是传统非遗，但能作为海派文化和近代城市史的重要场景，辅助理解上海的文化路线。'
    },
    '豫园江南园林导赏': {
        'visit_action': '看九曲桥、湖心亭、假山、水院、厅堂和游线。重点理解江南园林如何在老城厢里组织精致、曲折和可停留的空间。',
        'inheritor_intro': '豫园园林文化讲解团队会从亭台、叠石、理水和借景讲起。游客适合上午避开人流，慢慢看一步一景和空间转折。',
        'historical_background': '豫园承载江南园林审美和上海老城厢生活记忆。它把私家园林、商业街区和民俗活动连接在一起，是理解传统上海和江南造园方法的重要现场。'
    },
    '大鹏海防古城导赏': {
        'visit_action': '沿古城门、街巷、将军第和粮仓走，重点看海防体系如何进入社区生活。这里适合慢行，不适合只做古城门打卡。',
        'inheritor_intro': '大鹏所城文化讲解团队会把军事防御、宗族聚落和滨海贸易联系起来。游客可以从城门进入，再在街巷中看深圳更早的历史层。',
        'historical_background': '大鹏所城是深圳重要历史根脉，见证明清海防、岭南宗族和滨海交通。它帮助游客把深圳从现代都市的单一印象中拉回更长的地方历史。'
    },
    '莲花山城市记忆路线': {
        'visit_action': '登上山顶广场，看中心区轴线、城市天际线和公园公共生活。重点理解深圳如何通过城市空间表达改革开放后的发展记忆。',
        'inheritor_intro': '莲花山公园城市导赏团队会从山顶视野、中心区规划和市民公共生活讲起。适合傍晚登顶，视线开阔，也容易让游客建立深圳城市方向感。',
        'historical_background': '莲花山公园是观察深圳中心区变化的重要节点。它不是传统非遗本体，但作为城市记忆场景，可以辅助理解深圳从边陲小城到现代都市的空间叙事。'
    },
    '前门大栅栏老字号街区': {
        'visit_action': '沿前门到大栅栏慢走，看老字号招牌、戏楼、胡同和传统商业街面。适合与京剧、剪纸、皮影等非遗体验互相补充。',
        'inheritor_intro': '前门大栅栏街区讲解团队会从老字号、会馆、戏楼和市井商业讲起。游客可以把这里当作北京非遗体验的步行底盘，白天看街区，晚上接演出。',
        'historical_background': '前门大栅栏长期连接宫城、会馆、戏楼和商业生活，是北京老城最具代表性的传统商业街区之一。它让非遗不再悬浮在展柜里，而回到真实的消费、表演和街巷场景中。'
    },
    '北京胡同四合院生活导赏': {
        'visit_action': '看胡同尺度、门楼门墩、院落格局和街坊生活。重点理解北京老城不是一组单独景点，而是一套居住秩序和日常关系。',
        'inheritor_intro': '北京老城街区讲解团队会从院落空间、邻里关系和城市肌理讲起。游客适合轻声慢行，尊重居民生活，在细节里理解胡同文化。',
        'historical_background': '胡同与四合院构成北京老城最基本的生活单元。它们承载家庭结构、街坊交往、节令习俗和城市治理，是许多非遗活动发生的日常空间背景。'
    },
    '永庆坊西关生活街区': {
        'visit_action': '走骑楼街巷、粤剧艺术博物馆和荔枝湾周边，重点看西关生活、粤剧文化和城市更新如何相遇。',
        'inheritor_intro': '永庆坊与西关文化讲解团队会从趟栊门、骑楼、粤剧和水边街巷讲起。适合下午到傍晚，既能看非遗，也能感受广州街区气质。',
        'historical_background': '永庆坊所在的西关片区汇聚粤剧、老字号、骑楼和水系生活，是广州传统生活与当代街区更新交汇的典型区域。它让粤剧等非遗拥有更真实的城市背景。'
    },
    '广州北京路古道街区': {
        'visit_action': '看古道遗址、骑楼商业、步行街人流和城市中轴线索。重点理解热闹商业街下面叠压着广州城史。',
        'inheritor_intro': '广州古城中轴讲解团队会从古代道路遗存、商业传统和越秀城史讲起。适合下午到夜间，与广绣、醒狮、粤剧等体验形成轻松路线。',
        'historical_background': '北京路一带叠压着古代道路、传统商业和现代步行街，是广州城市中轴延续发展的可视化现场。它适合作为非遗体验后的街区补充，让游客看到文化如何进入日常消费空间。'
    },
    '人民公园海派生活导赏': {
        'visit_action': '从人民公园、人民广场、上海博物馆和南京路看公共文化生活。重点理解海派城市不是单一建筑风格，而是公共空间、商业和文化设施的组合。',
        'inheritor_intro': '人民广场片区公共文化讲解团队会把博物馆、公园和商业街联系起来讲。适合雨天或半日轻路线，也能衔接昆曲、博物馆和外滩。',
        'historical_background': '人民广场和人民公园周边集中呈现上海现代公共文化。它连接博物馆资源、商业街区和市民日常，是理解海派生活方式的便利入口。'
    },
    '上海石库门里弄生活导赏': {
        'visit_action': '看石库门门头、弄堂尺度、公共空间和近代居住痕迹。重点感受上海人的邻里生活和海派城市肌理。',
        'inheritor_intro': '海派里弄文化讲解团队会从门头样式、弄堂秩序和居住生活讲起。适合上午或傍晚慢行，避免只把石库门当作拍照背景。',
        'historical_background': '石库门和里弄连接江南民居传统、近代城市化和海派生活方式。它是上海城市记忆中最有生活质感的部分，也能为昆曲、博物馆和老城厢路线提供城市背景。'
    },
    '南头古城广府移民记忆': {
        'visit_action': '走古城门、祠堂、街巷和更新后的公共空间，重点看深圳更早的城址和移民生活。',
        'inheritor_intro': '南头古城街区讲解团队会从岭南城址、移民记忆和城市更新讲起。适合下午慢行，把古城空间和深圳当代文化对照起来。',
        'historical_background': '南头古城保留岭南古城和移民生活记忆，是深圳不只有现代天际线的重要证据。它把历史城址、社区生活和当代更新放在同一现场。'
    },
    '深圳华侨城创意街区导赏': {
        'visit_action': '看旧工业空间改造、设计店铺、公共艺术和社区活动。重点理解深圳当代文化街区如何形成。',
        'inheritor_intro': '华侨城创意文化讲解团队会从空间更新、设计消费和公共艺术讲起。适合下午到傍晚轻松看展，也能和传统古城路线形成新旧对照。',
        'historical_background': '华侨城创意文化园体现深圳从产业空间到文化消费和创意社区的转化。它不是传统非遗本体，但能辅助理解当代城市文化如何继续生产新的生活方式。'
    },
    '京剧': {
        'visit_action': '重点看生旦净丑、脸谱、髯口、靠旗、水袖和唱念做打。京剧的魅力不只在剧情，而在演员如何用程式化动作表现骑马、开门、行路、作战和情绪。',
        'inheritor_intro': '北京京剧院与戏曲公共教育团队会从行当、唱腔、身段和舞台规则讲起。第一次看京剧时，建议先听一段导赏，再看折子戏，这样更容易理解“一桌二椅”如何变成千军万马。',
        'historical_background': '京剧形成于清代，融合徽调、汉调、昆曲等声腔，并在北京宫廷和城市戏园中成熟。它被视为中国戏曲代表性剧种，脸谱色彩、锣鼓节奏和程式身段共同构成高度凝练的舞台语言。'
    },
    '北京皮影戏': {
        'visit_action': '重点看影偶雕刻、关节连接、操纵杆、灯影幕布和唱白配合。观众看到的是影窗上的人物，真正的技艺却藏在幕后双手、灯光和唱腔之间。',
        'inheritor_intro': '北京皮影戏传承与展演团队会把雕刻、美术、音乐和表演拆开讲给游客看。适合亲子体验，也适合对民间戏剧感兴趣的用户近距离观察影偶结构。',
        'historical_background': '皮影戏以皮革或纸板雕刻人物，通过灯光投影形成表演，兼具造型艺术、说唱文学和戏剧叙事。它曾广泛存在于民间节庆和乡村娱乐中，是中国传统戏剧非常古老、也非常直观的一支。'
    },
    '北京剪纸': {
        'visit_action': '重点看红纸纹样、折叠方式、阴刻阳刻和吉祥题材。窗花、生肖、福字、团花看似简单，其实把节令祝福和民间审美压缩在一张纸里。',
        'inheritor_intro': '北京剪纸非遗体验团队会从起稿、折纸、下刀和纹样寓意讲起。游客可以亲手剪一个小作品，理解为什么剪纸既是装饰，也是年节礼俗和家庭祝愿。',
        'historical_background': '剪纸是中国民间美术中传播最广、参与门槛最低的形式之一。它常用于春节、婚俗、庙会和居家装饰，图案里有祈福、纳祥、丰收和团圆的寓意，是日常生活里的非遗。'
    },
    '粤剧表演艺术': {
        'visit_action': '重点看粤语唱腔、水袖身段、南派武功、锣鼓点和华丽戏服。粤剧的地方性很强，声音、语言、节奏和服饰都带有鲜明岭南气质。',
        'inheritor_intro': '粤剧艺术博物馆驻场讲解与演员团队会通过身段示范、戏服展示和唱腔片段帮助游客入门。适合把粤剧博物馆、永庆坊和西关街巷连成一条半日路线。',
        'historical_background': '粤剧流行于粤港澳和海外华人社区，是岭南文化传播的重要载体。它融合地方方言、民间音乐、武术动作和戏曲程式，既是舞台艺术，也是广府社群记忆。'
    },
    '广东醒狮': {
        'visit_action': '重点看狮头扎作、鼓点节奏、步法、采青和高桩动作。醒狮不是单纯热闹表演，它需要武术底子、团队默契和对节庆仪式的理解。',
        'inheritor_intro': '广东醒狮传承与训练团队会从狮头结构、鼓乐口令和动作寓意讲起。游客可以观察狮头眼神、身体起伏和鼓点变化，感受岭南节庆现场的力量。',
        'historical_background': '醒狮是岭南民俗活动中极具识别度的非遗项目，常见于春节、开市、庆典和社区仪式。它连接武术训练、扎作工艺、音乐节奏和祈福观念，是地方社区凝聚力的象征。'
    },
    '广绣': {
        'visit_action': '重点看针法、色线、绣面光泽和图案层次。广绣常用明丽色彩表现花鸟、人物和瑞兽，近看能看到线的走向和层层叠色。',
        'inheritor_intro': '广绣工艺展示与体验团队会从构图、配色、针法和绣线质感讲起。适合在室内展陈中慢看，尤其适合对服饰、手工和传统美术感兴趣的游客。',
        'historical_background': '广绣是粤绣的重要代表，历史上与外销贸易、礼仪用品和地方审美密切相关。它以构图饱满、色彩华丽、针法丰富著称，是岭南传统美术中最精细的一类。'
    },
    '昆曲': {
        'visit_action': '重点听水磨腔，看身段、眼神、台步和折子戏里的细腻情绪。昆曲节奏较慢，适合静下来看演员如何用很小的动作表达复杂心境。',
        'inheritor_intro': '昆曲公共教育与演出团队会从曲牌、身段、文学文本和舞台审美讲起。第一次体验可以选择导赏或折子戏，比直接看长剧更容易进入。',
        'historical_background': '昆曲被称为“百戏之祖”，兴盛于明清，对许多中国戏曲剧种产生深远影响。它以典雅唱腔、细腻身段和文学性著称，是传统戏剧中最能体现文人审美的一支。'
    }
}

for seed_item in HERITAGE_SEED_ITEMS:
    rich_copy = HERITAGE_RICH_COPY.get(seed_item['name'])
    if rich_copy:
        seed_item.update(rich_copy)

HERITAGE_EXPERIENCE_PLACES = {
    '京剧': [
        {'name': '正乙祠戏楼', 'location_name': '北京市西城区前门西河沿街正乙祠戏楼', 'latitude': 39.8996, 'longitude': 116.3918, 'duration': 120, 'best_time': '晚场演出或周末导赏', 'experience': '在老戏楼里看京剧选段，空间本身就有传统戏楼的声场和仪式感。', 'tags': ['传统戏剧', '表演', '夜间', '室内']},
        {'name': '湖广会馆大戏楼', 'location_name': '北京市西城区虎坊路湖广会馆', 'latitude': 39.8916, 'longitude': 116.3852, 'duration': 100, 'best_time': '下午导赏或夜间演出', 'experience': '适合把会馆建筑、戏楼空间和京剧表演放在一起体验。', 'tags': ['传统戏剧', '历史建筑', '室内']},
        {'name': '老舍茶馆', 'location_name': '北京市西城区前门西大街老舍茶馆', 'latitude': 39.8992, 'longitude': 116.3927, 'duration': 90, 'best_time': '晚间综合演出', 'experience': '适合初次体验京剧和曲艺，边喝茶边看折子戏、曲艺和民俗节目。', 'tags': ['传统戏剧', '表演', '夜间', '国际友好']},
        {'name': '梅兰芳大剧院', 'location_name': '北京市西城区平安里西大街梅兰芳大剧院', 'latitude': 39.9322, 'longitude': 116.3638, 'duration': 120, 'best_time': '正式演出日', 'experience': '更适合想认真看一场完整剧目的用户，舞台条件和演出信息相对清晰。', 'tags': ['传统戏剧', '表演', '深度']},
        {'name': '长安大戏院', 'location_name': '北京市东城区建国门内大街长安大戏院', 'latitude': 39.9081, 'longitude': 116.4352, 'duration': 120, 'best_time': '晚场演出', 'experience': '适合把王府井、建国门一带行程和京剧晚场衔接起来。', 'tags': ['传统戏剧', '表演', '夜间']}
    ],
    '北京皮影戏': [
        {'name': '中国木偶艺术剧院', 'location_name': '北京市朝阳区安华西里中国木偶艺术剧院', 'latitude': 39.9640, 'longitude': 116.3949, 'duration': 75, 'best_time': '周末亲子场', 'experience': '适合亲子用户看木偶、皮影等传统偶戏展演，理解幕后操纵。', 'tags': ['传统戏剧', '亲子', '室内']},
        {'name': '北京民俗博物馆', 'location_name': '北京市朝阳区东岳庙北京民俗博物馆', 'latitude': 39.9277, 'longitude': 116.4430, 'duration': 70, 'best_time': '节庆活动或周末', 'experience': '在民俗展陈环境里理解皮影和节令、庙会、民间表演的关系。', 'tags': ['民俗', '传统戏剧', '室内']},
        {'name': '中国工艺美术馆 中国非物质文化遗产馆', 'location_name': '北京市朝阳区湖景东路中国工艺美术馆', 'latitude': 40.0086, 'longitude': 116.3970, 'duration': 90, 'best_time': '白天展陈时段', 'experience': '适合把皮影和其他非遗门类一起看，信息密度高，适合深度用户。', 'tags': ['博物馆', '非遗', '室内', '深度']},
        {'name': '前门非遗体验空间', 'location_name': '北京市西城区前门大栅栏片区', 'latitude': 39.8958, 'longitude': 116.3919, 'duration': 60, 'best_time': '下午到傍晚', 'experience': '适合把皮影轻体验和前门老城街区一起安排，步行友好。', 'tags': ['亲子', '手工体验', '城市漫步']}
    ],
    '北京剪纸': [
        {'name': '中国工艺美术馆 中国非物质文化遗产馆', 'location_name': '北京市朝阳区湖景东路中国工艺美术馆', 'latitude': 40.0086, 'longitude': 116.3970, 'duration': 75, 'best_time': '白天展陈时段', 'experience': '可以从作品、纹样和工艺说明里理解剪纸的民俗寓意。', 'tags': ['传统美术', '室内', '亲子']},
        {'name': '北京百工坊', 'location_name': '北京市东城区光明路北京百工坊', 'latitude': 39.8860, 'longitude': 116.4332, 'duration': 70, 'best_time': '上午或下午体验课', 'experience': '适合做一段剪纸手作，把阴刻阳刻和吉祥纹样真正做一遍。', 'tags': ['传统美术', '手工体验', '亲子']},
        {'name': '北京民俗博物馆', 'location_name': '北京市朝阳区东岳庙北京民俗博物馆', 'latitude': 39.9277, 'longitude': 116.4430, 'duration': 60, 'best_time': '节庆和民俗活动日', 'experience': '适合结合年节、窗花、庙会等场景理解剪纸。', 'tags': ['传统美术', '民俗', '室内']},
        {'name': '西城非遗体验中心', 'location_name': '北京市西城区什刹海周边非遗体验空间', 'latitude': 39.9398, 'longitude': 116.3850, 'duration': 60, 'best_time': '下午轻体验', 'experience': '适合少走路路线，把胡同街区和剪纸手作接在一起。', 'tags': ['手工体验', '少走路', '城市漫步']}
    ],
    '景泰蓝制作技艺': [
        {'name': '北京珐琅厂文化体验区', 'location_name': '北京市东城区安乐林路北京珐琅厂', 'latitude': 39.8954, 'longitude': 116.4246, 'duration': 90, 'best_time': '工作日上午', 'experience': '看制胎、掐丝、点蓝、烧蓝等流程，是最直接的景泰蓝工艺入口。', 'tags': ['传统技艺', '手工体验', '室内']},
        {'name': '北京百工坊', 'location_name': '北京市东城区光明路北京百工坊', 'latitude': 39.8860, 'longitude': 116.4332, 'duration': 75, 'best_time': '上午或下午体验课', 'experience': '适合把景泰蓝和其他北京手工艺一起做轻量体验。', 'tags': ['传统技艺', '手工体验', '亲子']},
        {'name': '中国工艺美术馆 中国非物质文化遗产馆', 'location_name': '北京市朝阳区湖景东路中国工艺美术馆', 'latitude': 40.0086, 'longitude': 116.3970, 'duration': 90, 'best_time': '白天展陈时段', 'experience': '适合看景泰蓝成品和工艺体系，偏展陈和审美理解。', 'tags': ['博物馆', '传统技艺', '深度']},
        {'name': '故宫珍宝馆', 'location_name': '北京市东城区故宫博物院珍宝馆', 'latitude': 39.9182, 'longitude': 116.3999, 'duration': 75, 'best_time': '故宫中轴游览后', 'experience': '适合从宫廷器物角度理解珐琅、玉器、金银器的审美系统。', 'tags': ['博物馆', '传统技艺', '历史建筑']}
    ],
    '天坛神乐署礼乐展示': [
        {'name': '天坛神乐署', 'location_name': '北京市东城区天坛公园神乐署', 'latitude': 39.8822, 'longitude': 116.4128, 'duration': 60, 'best_time': '天坛中轴参观后', 'experience': '看祭祀音乐、乐舞空间和礼制说明，适合理解天坛不是单纯拍建筑。', 'tags': ['传统音乐', '礼制', '室内']},
        {'name': '天坛公园中轴线', 'location_name': '北京市东城区天坛公园', 'latitude': 39.8820, 'longitude': 116.4066, 'duration': 90, 'best_time': '上午或下午', 'experience': '沿祈年殿、丹陛桥、圜丘坛建立祭天礼仪的空间顺序。', 'tags': ['礼制', '历史建筑', '户外']},
        {'name': '北京古代建筑博物馆', 'location_name': '北京市西城区先农坛北京古代建筑博物馆', 'latitude': 39.8835, 'longitude': 116.3872, 'duration': 75, 'best_time': '白天室内参观', 'experience': '适合补充礼制建筑、坛庙空间和古建知识。', 'tags': ['博物馆', '历史建筑', '室内']}
    ],
    '粤剧表演艺术': [
        {'name': '粤剧艺术博物馆', 'location_name': '广州市荔湾区恩宁路粤剧艺术博物馆', 'latitude': 23.1191, 'longitude': 113.2498, 'duration': 100, 'best_time': '下午展陈与导赏', 'experience': '看粤剧服饰、唱腔、舞台和园林式博物馆空间，是广州粤剧体验首选。', 'tags': ['传统戏剧', '岭南', '室内']},
        {'name': '广东粤剧院', 'location_name': '广州市越秀区广东粤剧院', 'latitude': 23.1327, 'longitude': 113.2714, 'duration': 120, 'best_time': '正式演出日', 'experience': '适合认真看一场粤剧演出，理解唱腔和舞台程式。', 'tags': ['传统戏剧', '表演', '深度']},
        {'name': '八和会馆', 'location_name': '广州市荔湾区八和会馆片区', 'latitude': 23.1187, 'longitude': 113.2506, 'duration': 70, 'best_time': '下午街区慢行', 'experience': '适合了解粤剧行会记忆和西关街区里的戏曲生态。', 'tags': ['传统戏剧', '街区文化', '岭南']},
        {'name': '永庆坊粤剧街区', 'location_name': '广州市荔湾区永庆坊', 'latitude': 23.1196, 'longitude': 113.2485, 'duration': 90, 'best_time': '下午到傍晚', 'experience': '把粤剧博物馆、骑楼街巷和西关生活串起来，适合第一次来广州的用户。', 'tags': ['传统戏剧', '城市漫步', '适合拍照']}
    ],
    '广东醒狮': [
        {'name': '广州文化馆新馆', 'location_name': '广州市海珠区广州文化馆新馆', 'latitude': 23.0818, 'longitude': 113.3228, 'duration': 75, 'best_time': '周末或展演活动日', 'experience': '适合看岭南非遗展演和醒狮活动，场馆空间开阔。', 'tags': ['传统舞蹈', '岭南', '表演']},
        {'name': '永庆坊节庆展演点', 'location_name': '广州市荔湾区永庆坊', 'latitude': 23.1196, 'longitude': 113.2485, 'duration': 60, 'best_time': '节庆和周末活动', 'experience': '适合把醒狮、粤剧和西关街区放在同一条慢行路线里。', 'tags': ['传统舞蹈', '民俗', '城市漫步']},
        {'name': '荔湾湖公园民俗活动点', 'location_name': '广州市荔湾区荔湾湖公园', 'latitude': 23.1239, 'longitude': 113.2406, 'duration': 60, 'best_time': '节庆活动日', 'experience': '节庆时适合看醒狮、庙会和岭南社区民俗氛围。', 'tags': ['传统舞蹈', '民俗', '户外']},
        {'name': '佛山祖庙醒狮展演区', 'location_name': '佛山市禅城区祖庙博物馆', 'latitude': 23.0307, 'longitude': 113.1123, 'duration': 100, 'best_time': '上午或下午固定展演', 'experience': '如果愿意跨城，佛山祖庙更适合看南狮、武术和岭南祠庙文化。', 'tags': ['传统舞蹈', '岭南', '表演', '深度']}
    ],
    '广绣': [
        {'name': '广东民间工艺博物馆 陈家祠', 'location_name': '广州市荔湾区陈家祠', 'latitude': 23.1290, 'longitude': 113.2402, 'duration': 80, 'best_time': '上午或下午展陈', 'experience': '适合把广绣和广府木雕、砖雕、陶塑一起看，理解岭南工艺系统。', 'tags': ['传统美术', '岭南', '室内']},
        {'name': '广州文化馆新馆', 'location_name': '广州市海珠区广州文化馆新馆', 'latitude': 23.0818, 'longitude': 113.3228, 'duration': 75, 'best_time': '非遗展陈或体验活动日', 'experience': '适合看广绣、广彩等岭南非遗展示，活动日可能有手作体验。', 'tags': ['传统美术', '手工体验', '室内']},
        {'name': '北京路非遗体验片区', 'location_name': '广州市越秀区北京路步行街', 'latitude': 23.1252, 'longitude': 113.2698, 'duration': 60, 'best_time': '下午到夜间', 'experience': '适合把广绣轻体验和广州古道商业街区一起安排。', 'tags': ['传统美术', '城市漫步', '岭南']}
    ],
    '昆曲': [
        {'name': '上海昆剧团', 'location_name': '上海市徐汇区上海昆剧团', 'latitude': 31.1926, 'longitude': 121.4444, 'duration': 120, 'best_time': '演出或导赏排期日', 'experience': '适合深度用户听水磨腔、看身段和折子戏，体验更完整。', 'tags': ['传统戏剧', '表演', '深度']},
        {'name': '宛平剧院', 'location_name': '上海市徐汇区宛平剧院', 'latitude': 31.1918, 'longitude': 121.4449, 'duration': 120, 'best_time': '晚场或周末演出', 'experience': '适合把昆曲、越剧等传统戏曲演出纳入上海半日文化路线。', 'tags': ['传统戏剧', '表演', '室内']},
        {'name': '上海大剧院', 'location_name': '上海市黄浦区上海大剧院', 'latitude': 31.2307, 'longitude': 121.4729, 'duration': 120, 'best_time': '正式演出日', 'experience': '适合想看高规格舞台呈现的用户，可与人民广场、博物馆串联。', 'tags': ['传统戏剧', '表演', '国际友好']},
        {'name': '天蟾逸夫舞台', 'location_name': '上海市黄浦区天蟾逸夫舞台', 'latitude': 31.2366, 'longitude': 121.4787, 'duration': 120, 'best_time': '晚场演出', 'experience': '适合把南京路、人民广场和传统戏曲晚场连接起来。', 'tags': ['传统戏剧', '夜间', '城市漫步']}
    ]
}

for seed_item in HERITAGE_SEED_ITEMS:
    seed_item['experience_places'] = HERITAGE_EXPERIENCE_PLACES.get(seed_item['name'], [])

for seed_item in HERITAGE_SEED_ITEMS:
    seed_item['source_url'] = 'local-navigation-demo'
    if not seed_item.get('visit_action'):
        seed_item['visit_action'] = HERITAGE_VISIT_ACTIONS.get(
            seed_item['name'],
            seed_item.get('inheritor_intro') or seed_item.get('best_visit_time', '')
        )

HERITAGE_CATEGORY_PRIORITY = {
    '传统戏剧': 0,
    '传统技艺': 1,
    '传统音乐': 2,
    '传统舞蹈': 3,
    '传统美术': 4,
    '曲艺': 5,
    '民俗': 6,
    '博物馆': 7,
    '街区文化': 8,
    '城市文化': 9
}

CORE_HERITAGE_CATEGORIES = {
    '传统戏剧',
    '传统技艺',
    '传统音乐',
    '传统舞蹈',
    '传统美术',
    '曲艺',
    '民俗'
}

CORE_HERITAGE_ITEM_NAMES = {
    '京剧',
    '北京皮影戏',
    '北京剪纸',
    '景泰蓝制作技艺',
    '天坛神乐署礼乐展示',
    '粤剧表演艺术',
    '广东醒狮',
    '广绣',
    '昆曲'
}

def heritage_sort_key(item):
    name = item.get('name') or ''
    category = item.get('category') or ''
    body_priority = 0 if name in CORE_HERITAGE_ITEM_NAMES else 1
    return (
        body_priority,
        HERITAGE_CATEGORY_PRIORITY.get(item.get('category') or '', 99),
        normalize_search_text(item.get('city') or ''),
        normalize_search_text(item.get('name') or '')
    )

def is_core_heritage_item(item):
    return (item.get('name') or '') in CORE_HERITAGE_ITEM_NAMES

def is_scene_support_item(item):
    category = item.get('category') or ''
    return category in {'城市文化', '街区文化', '博物馆'} or not is_core_heritage_item(item)

def infer_route_focus(preferences, requested_tags, requested_focus='auto'):
    focus = normalize_search_text(requested_focus)
    if focus in {'heritage', '非遗为主', '非遗主线'}:
        return 'heritage'
    if focus in {'attraction', '景点为主', '景点主线', 'place'}:
        return 'attraction'

    preference_text = normalize_search_text(' '.join(preferences + requested_tags))
    attraction_keywords = {'景点', '景区', '街区', '城市漫步', '历史建筑', '园林', '博物馆', '适合拍照'}
    heritage_keywords = {'非遗', '传统戏剧', '传统技艺', '传统美术', '传统音乐', '传统舞蹈', '民俗', '手工体验', '表演'}
    attraction_hits = sum(1 for keyword in attraction_keywords if normalize_search_text(keyword) in preference_text)
    heritage_hits = sum(1 for keyword in heritage_keywords if normalize_search_text(keyword) in preference_text)
    return 'attraction' if attraction_hits > heritage_hits else 'heritage'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        avatar TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS follows (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        follower TEXT NOT NULL,
        following TEXT NOT NULL,
        FOREIGN KEY (follower) REFERENCES users(username) ON DELETE CASCADE,
        FOREIGN KEY (following) REFERENCES users(username) ON DELETE CASCADE,
        UNIQUE(follower, following)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS posts (
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
    c.execute('PRAGMA table_info(posts)')
    post_columns = [column[1] for column in c.fetchall()]
    if 'content' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN content TEXT DEFAULT ''")
    if 'city' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN city TEXT DEFAULT ''")
    if 'audio_url' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN audio_url TEXT DEFAULT ''")
    if 'audio_url_en' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN audio_url_en TEXT DEFAULT ''")
    if 'guide_items' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN guide_items TEXT DEFAULT '[]'")
    if 'route_map' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN route_map TEXT DEFAULT '{}'")
    if 'tags' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN tags TEXT DEFAULT '[]'")
    if 'heritage_id' not in post_columns:
        c.execute("ALTER TABLE posts ADD COLUMN heritage_id INTEGER")
    c.execute('''CREATE TABLE IF NOT EXISTS heritage_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        category TEXT NOT NULL,
        subcategory TEXT DEFAULT '',
        inheritor TEXT DEFAULT '',
        inheritor_intro TEXT DEFAULT '',
        historical_background TEXT DEFAULT '',
        location_name TEXT DEFAULT '',
        city TEXT DEFAULT '',
        province TEXT DEFAULT '',
        latitude REAL,
        longitude REAL,
        activity_time TEXT DEFAULT '',
        best_visit_time TEXT DEFAULT '',
        suitable_duration INTEGER DEFAULT 60,
        visit_action TEXT DEFAULT '',
        experience_places TEXT DEFAULT '[]',
        tags TEXT DEFAULT '[]',
        cover_image TEXT DEFAULT '',
        source_url TEXT DEFAULT '',
        created_at TEXT NOT NULL
    )''')
    c.execute('PRAGMA table_info(heritage_items)')
    heritage_columns = [column[1] for column in c.fetchall()]
    if 'visit_action' not in heritage_columns:
        c.execute("ALTER TABLE heritage_items ADD COLUMN visit_action TEXT DEFAULT ''")
    if 'experience_places' not in heritage_columns:
        c.execute("ALTER TABLE heritage_items ADD COLUMN experience_places TEXT DEFAULT '[]'")
    c.execute('''CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        author TEXT NOT NULL,
        content TEXT NOT NULL,
        publish_time TEXT NOT NULL,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
        UNIQUE(username, post_id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS post_likes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE,
        FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
        UNIQUE(username, post_id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        content TEXT NOT NULL,
        send_time TEXT NOT NULL,
        is_read INTEGER DEFAULT 0,
        FOREIGN KEY (sender) REFERENCES users(username) ON DELETE CASCADE,
        FOREIGN KEY (receiver) REFERENCES users(username) ON DELETE CASCADE
    )''')
    ensure_guide_author_users(c)
    ensure_heritage_items(c)
    ensure_seed_data(c)
    conn.commit()
    conn.close()

def build_preset_avatar(emoji):
    return json.dumps({'type': 'preset', 'emoji': emoji}, ensure_ascii=False)

GUIDE_AUTHOR_AVATARS = {
    'palace_guide': '🏯',
    'garden_curator': '🌿',
    'ritual_guide': '⛩️',
    'wall_walker': '🧭',
    'beijing_fan': '🏮',
    'explorer': '🔎',
    'culture_seeker': '🎨',
    'canton_guide': '🌉',
    'mountain_guide': '⛰️',
    'lingnan_curator': '🪭',
    'city_history_guide': '🏛️',
    'shamian_walker': '🚶',
    'shanghai_guide': '🌃',
    'garden_story': '🌸',
    'museum_curator': '🏺',
    'bay_walker': '🌊',
    'lotus_hill_guide': '🪷',
    'dapeng_guard': '🏰',
    'beihai_guide': '⛲',
    'lama_temple_guide': '🛕'
}

def ensure_guide_author_users(cursor):
    for username in GUIDE_AUTHORS:
        avatar = build_preset_avatar(GUIDE_AUTHOR_AVATARS.get(username, '🧭'))
        cursor.execute(
            '''
            INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET avatar = excluded.avatar
            WHERE users.password = '123456'
            ''',
            (username, '123456', avatar)
        )

def ensure_message_user(cursor, username):
    if not username:
        return
    if username in GUIDE_AUTHORS:
        avatar = build_preset_avatar(GUIDE_AUTHOR_AVATARS.get(username, '🧭'))
        cursor.execute(
            '''
            INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET avatar = excluded.avatar
            WHERE users.password = '123456'
            ''',
            (username, '123456', avatar)
        )

def ensure_heritage_items(cursor):
    now = datetime.now().isoformat()
    seed_names = [item['name'] for item in HERITAGE_SEED_ITEMS]
    placeholders = ','.join(['?'] * len(seed_names))
    cursor.execute(
        f"DELETE FROM heritage_items WHERE (source_url IS NULL OR source_url IN ('', 'local-navigation-demo')) AND name NOT IN ({placeholders})",
        seed_names
    )
    for item in HERITAGE_SEED_ITEMS:
        cursor.execute('''
            INSERT INTO heritage_items
            (name, category, subcategory, inheritor, inheritor_intro, historical_background,
             location_name, city, province, latitude, longitude, activity_time, best_visit_time,
             suitable_duration, visit_action, experience_places, tags, cover_image, source_url, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                category = excluded.category,
                subcategory = excluded.subcategory,
                inheritor = excluded.inheritor,
                inheritor_intro = excluded.inheritor_intro,
                historical_background = excluded.historical_background,
                location_name = excluded.location_name,
                city = excluded.city,
                province = excluded.province,
                latitude = excluded.latitude,
                longitude = excluded.longitude,
                activity_time = excluded.activity_time,
                best_visit_time = excluded.best_visit_time,
                suitable_duration = excluded.suitable_duration,
                visit_action = excluded.visit_action,
                experience_places = excluded.experience_places,
                tags = excluded.tags,
                cover_image = excluded.cover_image,
                source_url = excluded.source_url
        ''', (
            item['name'],
            item['category'],
            item.get('subcategory', ''),
            item.get('inheritor', ''),
            item.get('inheritor_intro', ''),
            item.get('historical_background', ''),
            item.get('location_name', ''),
            item.get('city', ''),
            item.get('province', ''),
            item.get('latitude'),
            item.get('longitude'),
            item.get('activity_time', ''),
            item.get('best_visit_time', ''),
            item.get('suitable_duration', 60),
            item.get('visit_action', ''),
            json.dumps(item.get('experience_places', []), ensure_ascii=False),
            json.dumps(item.get('tags', []), ensure_ascii=False),
            item.get('cover_image', ''),
            item.get('source_url', ''),
            now
        ))

def ensure_seed_data(cursor):
    if not SEED_DATA_PATH.exists():
        return

    with SEED_DATA_PATH.open('r', encoding='utf-8') as seed_file:
        seed_data = json.load(seed_file)

    demo_password = seed_data.get('demo_password', '123456')

    for user in seed_data.get('users', []):
        username = user.get('username')
        if not username:
            continue
        cursor.execute(
            '''
            INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET avatar = excluded.avatar
            ''',
            (username, demo_password, user.get('avatar'))
        )

    for post in seed_data.get('posts', []):
        cursor.execute(
            '''
            INSERT OR IGNORE INTO posts
            (id, title, content, photos, location, latitude, longitude, duration, people,
             author, publish_time, likes, comments, views, city, audio_url, audio_url_en,
             guide_items, route_map, tags, heritage_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                post.get('id'),
                post.get('title'),
                post.get('content', ''),
                post.get('photos'),
                post.get('location'),
                post.get('latitude'),
                post.get('longitude'),
                post.get('duration'),
                post.get('people'),
                post.get('author'),
                post.get('publish_time'),
                post.get('likes', 0),
                post.get('comments', 0),
                post.get('views', 0),
                post.get('city', ''),
                post.get('audio_url', ''),
                post.get('audio_url_en', ''),
                post.get('guide_items', '[]'),
                post.get('route_map', '{}'),
                post.get('tags', '[]'),
                post.get('heritage_id'),
            )
        )

    for follow in seed_data.get('follows', []):
        cursor.execute(
            'INSERT OR IGNORE INTO follows (follower, following) VALUES (?, ?)',
            (follow.get('follower'), follow.get('following'))
        )

    for comment in seed_data.get('comments', []):
        cursor.execute(
            '''
            INSERT OR IGNORE INTO comments (id, post_id, author, content, publish_time)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                comment.get('id'),
                comment.get('post_id'),
                comment.get('author'),
                comment.get('content'),
                comment.get('publish_time'),
            )
        )

    for favorite in seed_data.get('favorites', []):
        cursor.execute(
            'INSERT OR IGNORE INTO favorites (username, post_id) VALUES (?, ?)',
            (favorite.get('username'), favorite.get('post_id'))
        )

    for like in seed_data.get('post_likes', []):
        cursor.execute(
            'INSERT OR IGNORE INTO post_likes (username, post_id) VALUES (?, ?)',
            (like.get('username'), like.get('post_id'))
        )

init_db()

def parse_json_field(value, fallback):
    if not value:
        return fallback
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return fallback

def serialize_post(post, avatar_key='author_avatar'):
    photos = parse_json_field(post['photos'], [])
    guide_items = parse_json_field(post['guide_items'] if 'guide_items' in post.keys() else None, [])
    route_map = parse_json_field(post['route_map'] if 'route_map' in post.keys() else None, {})
    tags = parse_json_field(post['tags'] if 'tags' in post.keys() else None, [])

    result = {
        'id': post['id'],
        'title': post['title'],
        'content': post['content'] or '',
        'photos': photos,
        'location': post['location'],
        'latitude': post['latitude'],
        'longitude': post['longitude'],
        'duration': post['duration'],
        'people': post['people'],
        'author': post['author'],
        'publish_time': post['publish_time'],
        'likes': int(post['likes']) if post['likes'] else 0,
        'comments': int(post['comments']) if post['comments'] else 0,
        'views': int(post['views']) if post['views'] else 0,
        'city': post['city'] if 'city' in post.keys() else '',
        'audio_url': post['audio_url'] if 'audio_url' in post.keys() else '',
        'audio_url_en': post['audio_url_en'] if 'audio_url_en' in post.keys() else '',
        'guide_items': guide_items,
        'route_map': route_map,
        'tags': tags,
        'heritage_id': post['heritage_id'] if 'heritage_id' in post.keys() else None,
        'post_type': 'guide' if guide_items and post['author'] in GUIDE_AUTHORS else 'user'
    }

    if avatar_key in post.keys():
        result['author_avatar'] = post[avatar_key]

    return result


def is_guide_post_data(post_data):
    return bool(post_data.get('guide_items')) and post_data.get('author') in GUIDE_AUTHORS


def normalize_search_text(value):
    return ''.join(str(value or '').lower().split())

def compact_preview(value, max_length=96):
    text = ' '.join(str(value or '').split())
    if len(text) <= max_length:
        return text
    return f"{text[:max_length]}..."


def filter_posts_by_type(posts, post_type):
    if post_type == 'guide':
        return [post for post in posts if is_guide_post_data(post)]
    if post_type == 'user':
        return [post for post in posts if not is_guide_post_data(post)]
    return posts


def filter_posts_by_tag(posts, tag):
    if not tag:
        return posts
    return [post for post in posts if tag in (post.get('tags') or [])]

def haversine_km(lat1, lon1, lat2, lon2):
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return None
    radius = 6371
    phi1 = math.radians(float(lat1))
    phi2 = math.radians(float(lat2))
    d_phi = math.radians(float(lat2) - float(lat1))
    d_lambda = math.radians(float(lon2) - float(lon1))
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    return radius * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def route_distance_label(distance_km):
    if distance_km is None:
        return '距离需以实际定位为准'
    if distance_km < 1:
        return f"约 {int(distance_km * 1000)} 米"
    return f"约 {distance_km:.1f} 公里"

def route_transfer_advice(distance_km, is_first_stop=False):
    if distance_km is None:
        return '建议打开地图导航确认实时交通，再按推荐站点顺序游览。'
    if distance_km <= 1.2:
        minutes = max(8, int(distance_km / 4.2 * 60))
        return f"步行约 {minutes} 分钟可达，沿途适合直接进入街区慢行。"
    if distance_km <= 5:
        ride_minutes = max(10, int(distance_km / 16 * 60) + 6)
        return f"建议地铁、公交或骑行接驳，约 {ride_minutes} 分钟；到站后再步行进入核心区域。"
    if is_first_stop:
        minutes = max(25, int(distance_km / 28 * 60) + 10)
        return f"距离起点较远，建议优先使用地铁或网约车，约 {minutes} 分钟抵达首站。"
    minutes = max(25, int(distance_km / 24 * 60) + 12)
    return f"两站间跨度较大，建议地铁或网约车接驳，约 {minutes} 分钟；时间紧可跳过本段。"

def build_navigation_url(item):
    lat = item.get('latitude')
    lon = item.get('longitude')
    title = item.get('location_name') or item.get('name') or item.get('title') or ''
    if lat is not None and lon is not None:
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(title)}"

def route_feasibility_label(total_minutes, available_minutes, selected_count):
    if not selected_count:
        return '暂未找到可用路线'
    if total_minutes <= available_minutes:
        return '时间匹配，可以按顺序完整游览'
    if total_minutes <= available_minutes + 45:
        return '略紧凑，建议减少拍照停留或优先走前几站'
    return '时间偏紧，建议改短线或减少站点'

def order_route_by_reachability(items, start_lat, start_lon):
    remaining = list(items)
    ordered = []
    current_lat = start_lat
    current_lon = start_lon
    while remaining:
        if current_lat is None or current_lon is None:
            remaining.sort(key=lambda candidate: candidate.get('score', 0), reverse=True)
            ordered.extend(remaining)
            break
        best_index = min(
            range(len(remaining)),
            key=lambda index: haversine_km(
                current_lat,
                current_lon,
                remaining[index].get('latitude'),
                remaining[index].get('longitude')
            ) if haversine_km(current_lat, current_lon, remaining[index].get('latitude'), remaining[index].get('longitude')) is not None else 99999
        )
        next_item = remaining.pop(best_index)
        ordered.append(next_item)
        current_lat = next_item.get('latitude')
        current_lon = next_item.get('longitude')
    return ordered

def order_route_by_line_role(items, start_lat, start_lon):
    main_items = [item for item in items if item.get('route_line_role') == 'main']
    support_items = [item for item in items if item.get('route_line_role') != 'main']
    if not main_items:
        return order_route_by_reachability(items, start_lat, start_lon)
    ordered_main = order_route_by_reachability(main_items, start_lat, start_lon)
    last = ordered_main[-1]
    ordered_support = order_route_by_reachability(support_items, last.get('latitude'), last.get('longitude'))
    return ordered_main + ordered_support

def enrich_route_navigation(selected, start):
    start_name = start.get('name') or start.get('city') or '当前位置'
    current_label = start_name
    current_lat = start.get('latitude')
    current_lon = start.get('longitude')
    total_transfer_minutes = 0

    for index, item in enumerate(selected):
        distance = haversine_km(current_lat, current_lon, item.get('latitude'), item.get('longitude'))
        transfer_minutes = 0 if distance is None else max(8, int(distance / 18 * 60) + (6 if distance > 1.2 else 0))
        total_transfer_minutes += transfer_minutes
        item.update({
            'route_order': index + 1,
            'from_name': current_label,
            'distance_from_previous_km': round(distance, 2) if distance is not None else None,
            'distance_from_previous_label': route_distance_label(distance),
            'arrival_guidance': route_transfer_advice(distance, is_first_stop=(index == 0)),
            'navigation_url': build_navigation_url(item)
        })
        current_label = item.get('location_name') or item.get('name') or item.get('title') or f"第 {index + 1} 站"
        current_lat = item.get('latitude')
        current_lon = item.get('longitude')

    for index, item in enumerate(selected):
        next_item = selected[index + 1] if index + 1 < len(selected) else None
        if next_item:
            next_distance = haversine_km(item.get('latitude'), item.get('longitude'), next_item.get('latitude'), next_item.get('longitude'))
            item['next_stop_hint'] = f"下一站：{next_item.get('name') or next_item.get('title')}，{route_transfer_advice(next_distance)}"
        else:
            item['next_stop_hint'] = '这是最后一站，完成后可就近返程或继续查看附近内容。'

    return total_transfer_minutes

def serialize_heritage_item(row):
    tags = parse_json_field(row['tags'] if 'tags' in row.keys() else None, [])
    experience_places = parse_json_field(row['experience_places'] if 'experience_places' in row.keys() else None, [])
    return {
        'id': row['id'],
        'name': row['name'],
        'category': row['category'],
        'subcategory': row['subcategory'] or '',
        'inheritor': row['inheritor'] or '',
        'inheritor_intro': row['inheritor_intro'] or '',
        'historical_background': row['historical_background'] or '',
        'location_name': row['location_name'] or '',
        'city': row['city'] or '',
        'province': row['province'] or '',
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'activity_time': row['activity_time'] or '',
        'best_visit_time': row['best_visit_time'] or '',
        'suitable_duration': int(row['suitable_duration'] or 60),
        'visit_action': row['visit_action'] if 'visit_action' in row.keys() else '',
        'experience_places': experience_places,
        'tags': tags,
        'cover_image': row['cover_image'] or '',
        'source_url': row['source_url'] or ''
    }

def split_translation_text(text, max_length=900):
    parts = []
    current = ''
    for paragraph in str(text or '').split('\n'):
        candidate = f"{current}\n{paragraph}" if current else paragraph
        if len(candidate) <= max_length:
            current = candidate
            continue
        if current:
            parts.append(current)
        if len(paragraph) <= max_length:
            current = paragraph
        else:
            for start in range(0, len(paragraph), max_length):
                parts.append(paragraph[start:start + max_length])
            current = ''
    if current:
        parts.append(current)
    return parts or ['']

def translate_text_chunk(text, target='en'):
    if not text:
        return ''

    cache_key = (target, text)
    if cache_key in TRANSLATION_CACHE:
        return TRANSLATION_CACHE[cache_key]

    query = urllib.parse.urlencode({
        'client': 'gtx',
        'sl': 'zh-CN',
        'tl': target,
        'dt': 't',
        'q': text
    })
    request = urllib.request.Request(
        f'https://translate.googleapis.com/translate_a/single?{query}',
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    try:
        with urllib.request.urlopen(request, timeout=6) as response:
            data = json.loads(response.read().decode('utf-8'))
        translated = ''.join(part[0] or '' for part in data[0]).strip()
        TRANSLATION_CACHE[cache_key] = translated or text
        return TRANSLATION_CACHE[cache_key]
    except Exception:
        return text

@app.post("/translate")
def translate_text(data: TranslationRequest):
    text = data.text or ''
    target = 'en' if data.target != 'zh' else 'zh-CN'
    if not text.strip():
        return {'translated': text}

    translated_parts = [
        translate_text_chunk(part, target)
        for part in split_translation_text(text)
    ]
    return {'translated': '\n'.join(translated_parts)}

@app.post("/login")
def login(user: User):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT password, avatar FROM users WHERE username = ?', (user.username,))
    result = c.fetchone()
    conn.close()
    
    if result and result[0] == user.password:
        return {"message": "登录成功！欢迎回来！", "username": user.username, "avatar": result[1]}
    
    raise HTTPException(status_code=400, detail="账号或密码错误！")

@app.post("/register")
def register(user: User):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)', 
                (user.username, user.password, user.avatar))
        conn.commit()
        return {"message": "注册成功！", "username": user.username, "avatar": user.avatar}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="账号已存在，请直接登录！")
    finally:
        conn.close()

@app.post("/update-avatar")
def update_avatar(data: dict):
    username = data.get('username')
    avatar = data.get('avatar')
    
    if not username or not avatar:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE users SET avatar = ? WHERE username = ?', (avatar, username))
    conn.commit()
    conn.close()
    return {"message": "头像更新成功！"}

@app.get("/users/{username}")
def get_user(username: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT username, avatar FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return {"username": result[0], "avatar": result[1]}
    
    raise HTTPException(status_code=404, detail="用户不存在！")

@app.post("/publish")
def publish_post(data: dict):
    init_db()
    
    title = data.get('title')
    content = data.get('content', '')
    photos = data.get('photos', [])
    location = data.get('location')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    duration = data.get('duration', 1)
    people = data.get('people', 1)
    author = data.get('author')
    publish_time = data.get('publish_time') or data.get('publishTime')
    city = data.get('city', '')
    # 普通用户发帖不保存语音导览数据；语音和路线只保留给内置导览帖子。
    audio_url = ''
    guide_items = []
    route_map = {}
    tags = data.get('tags') or []
    
    if not title or not author or not publish_time:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    photos_json = json.dumps(photos)
    guide_items_json = json.dumps(guide_items)
    route_map_json = json.dumps(route_map)
    tags_json = json.dumps(tags)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO posts
            (title, content, photos, location, latitude, longitude, duration, people, author, publish_time, city, audio_url, guide_items, route_map, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, content, photos_json, location, latitude, longitude, duration, people, author, publish_time, city, audio_url, guide_items_json, route_map_json, tags_json))
        conn.commit()
        return {"message": "发布成功！"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

@app.get("/get_user_likes")
def get_user_likes(username: str):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('SELECT SUM(likes) as total_likes FROM posts WHERE author = ?', (username,))
    result = c.fetchone()
    total_likes = result['total_likes'] if result['total_likes'] else 0
    
    conn.close()
    return {'likes': total_likes}

@app.get("/posts/{author}")
def get_user_posts(author: str):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('''
        SELECT p.*, u.avatar AS author_avatar
        FROM posts p
        LEFT JOIN users u ON p.author = u.username
        WHERE p.author = ?
        ORDER BY p.publish_time DESC
    ''', (author,))
    posts = c.fetchall()
    
    result = []
    for post in posts:
        result.append(serialize_post(post))
    
    conn.close()
    return result

@app.get("/all-posts")
def get_all_posts(exclude_author: str = None, post_type: str = 'all', tag: str = None):
    """获取帖子列表。post_type=guide 用于首页内置导览，post_type=user 用于用户普通帖。"""
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 联合查询帖子和作者信息
    if exclude_author:
        c.execute('''
            SELECT p.*, u.avatar 
            FROM posts p 
            LEFT JOIN users u ON p.author = u.username 
            WHERE p.author != ?
            ORDER BY p.publish_time DESC
        ''', (exclude_author,))
    else:
        c.execute('''
            SELECT p.*, u.avatar 
            FROM posts p 
            LEFT JOIN users u ON p.author = u.username 
            ORDER BY p.publish_time DESC
        ''')
    posts = c.fetchall()
    
    result = []
    for post in posts:
        result.append(serialize_post(post, avatar_key='avatar'))

    result = filter_posts_by_type(result, post_type)
    result = filter_posts_by_tag(result, tag)
    
    conn.close()
    return result

@app.get("/post/{post_id}")
def get_post_detail(post_id: int):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 先检查帖子是否存在，同时获取作者头像
    c.execute('''
        SELECT p.*, u.avatar AS author_avatar
        FROM posts p
        LEFT JOIN users u ON p.author = u.username
        WHERE p.id = ?
    ''', (post_id,))
    post = c.fetchone()
    
    if not post:
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    # 增加浏览量（使用 COALESCE 处理可能不存在的 views 字段）
    c.execute('UPDATE posts SET views = COALESCE(views, 0) + 1 WHERE id = ?', (post_id,))
    conn.commit()
    
    # 重新查询获取更新后的帖子数据
    c.execute('''
        SELECT p.*, u.avatar AS author_avatar
        FROM posts p
        LEFT JOIN users u ON p.author = u.username
        WHERE p.id = ?
    ''', (post_id,))
    post = c.fetchone()
    
    result = serialize_post(post)
    
    conn.close()
    return result

@app.get("/search")
def search_posts(q: str = ''):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute('''
        SELECT p.*, u.avatar AS author_avatar
        FROM posts p
        LEFT JOIN users u ON p.author = u.username
        ORDER BY p.publish_time DESC
    ''')
    posts = c.fetchall()

    query = normalize_search_text(q)
    result = []
    for post in posts:
        item = serialize_post(post)
        if query:
            haystack = normalize_search_text(
                f"{item.get('title', '')} {item.get('content', '')} {item.get('location', '')} {item.get('city', '')} {item.get('author', '')}"
            )
            if query not in haystack:
                continue
        result.append(item)
    
    conn.close()
    return result

@app.put("/post/{post_id}")
def update_post(post_id: int, data: dict):
    init_db()
    
    title = data.get('title')
    content = data.get('content', '')
    photos = data.get('photos')
    location = data.get('location')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    duration = data.get('duration')
    people = data.get('people')
    city = data.get('city', '')
    audio_url = data.get('audio_url') or data.get('audioUrl') or ''
    guide_items = data.get('guide_items') or data.get('guideItems') or []
    route_map = data.get('route_map') or data.get('routeMap') or {}
    tags = data.get('tags') or []
    
    if not title:
        raise HTTPException(status_code=400, detail="缺少必要参数")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    photos_json = json.dumps(photos) if photos is not None else None
    guide_items_json = json.dumps(guide_items)
    route_map_json = json.dumps(route_map)
    tags_json = json.dumps(tags)
    
    if photos_json is None:
        c.execute('''UPDATE posts
                     SET title = ?, content = ?, location = ?, latitude = ?, longitude = ?, duration = ?, people = ?, city = ?, audio_url = ?, guide_items = ?, route_map = ?, tags = ?
                     WHERE id = ?''', (title, content, location, latitude, longitude, duration, people, city, audio_url, guide_items_json, route_map_json, tags_json, post_id))
    else:
        c.execute('''UPDATE posts
                     SET title = ?, content = ?, photos = ?, location = ?, latitude = ?, longitude = ?, duration = ?, people = ?, city = ?, audio_url = ?, guide_items = ?, route_map = ?, tags = ?
                     WHERE id = ?''', (title, content, photos_json, location, latitude, longitude, duration, people, city, audio_url, guide_items_json, route_map_json, tags_json, post_id))
    
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    conn.commit()
    conn.close()
    
    return {"message": "更新成功"}

@app.delete("/post/{post_id}")
def delete_post(post_id: int):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    conn.commit()
    conn.close()
    
    return {"message": "删除成功"}

@app.post("/post/{post_id}/like")
def like_post(post_id: int, data: dict = None):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    username = (data or {}).get('username')
    
    c.execute('SELECT likes FROM posts WHERE id = ?', (post_id,))
    post = c.fetchone()
    if not post:
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")

    if username:
        c.execute('INSERT OR IGNORE INTO post_likes (username, post_id) VALUES (?, ?)', (username, post_id))
        if c.rowcount > 0:
            c.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (post_id,))
    else:
        c.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (post_id,))
    
    conn.commit()
    
    c.execute('SELECT likes FROM posts WHERE id = ?', (post_id,))
    result = c.fetchone()
    
    conn.close()
    return {"likes": result[0], "is_liked": True}

@app.delete("/post/{post_id}/like")
def unlike_post(post_id: int, data: dict = None):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    username = (data or {}).get('username')

    c.execute('SELECT likes FROM posts WHERE id = ?', (post_id,))
    post = c.fetchone()
    if not post:
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")

    if username:
        c.execute('DELETE FROM post_likes WHERE username = ? AND post_id = ?', (username, post_id))
        if c.rowcount > 0:
            c.execute('UPDATE posts SET likes = CASE WHEN likes > 0 THEN likes - 1 ELSE 0 END WHERE id = ?', (post_id,))
    else:
        c.execute('UPDATE posts SET likes = CASE WHEN likes > 0 THEN likes - 1 ELSE 0 END WHERE id = ?', (post_id,))

    conn.commit()
    c.execute('SELECT likes FROM posts WHERE id = ?', (post_id,))
    result = c.fetchone()

    conn.close()
    return {"likes": result[0], "is_liked": False}

@app.get("/post/{post_id}/check-like")
def check_like(post_id: int, username: str):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT 1 FROM post_likes WHERE username = ? AND post_id = ?', (username, post_id))
    result = c.fetchone()
    conn.close()

    return {"is_liked": result is not None}

@app.post("/post/{post_id}/comment")
def add_comment(post_id: int, data: dict):
    init_db()
    
    author = data.get('author')
    content = data.get('content')
    
    if not author or not content:
        raise HTTPException(status_code=400, detail="缺少必要参数")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT id FROM posts WHERE id = ?', (post_id,))
    if not c.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    c.execute('INSERT INTO comments (post_id, author, content, publish_time) VALUES (?, ?, ?, ?)', 
            (post_id, author, content, datetime.now().isoformat()))
    
    c.execute('UPDATE posts SET comments = comments + 1 WHERE id = ?', (post_id,))
    
    conn.commit()
    conn.close()
    return {"message": "评论成功"}

@app.get("/post/{post_id}/comments")
def get_comments(post_id: int):
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY publish_time DESC', (post_id,))
    comments = c.fetchall()
    
    result = []
    for comment in comments:
        result.append({
            'id': comment['id'],
            'post_id': comment['post_id'],
            'author': comment['author'],
            'content': comment['content'],
            'publish_time': comment['publish_time']
        })
    
    conn.close()
    return result

@app.post("/change-password")
def change_password(data: dict):
    username = data.get('username')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    
    if not username or not old_password or not new_password:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    
    if not result or result[0] != old_password:
        conn.close()
        raise HTTPException(status_code=400, detail="旧密码错误！")
    
    c.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
    conn.commit()
    conn.close()
    
    return {"message": "密码修改成功！"}

@app.post("/follow")
def follow_user(data: dict):
    follower = data.get('follower')
    following = data.get('following')
    
    if not follower or not following:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    if follower == following:
        raise HTTPException(status_code=400, detail="不能关注自己！")
    
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    
    try:
        c.execute('INSERT INTO follows (follower, following) VALUES (?, ?)', (follower, following))
        conn.commit()
        conn.close()
        return {"message": "关注成功！"}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="已经关注过该用户！")

@app.post("/unfollow")
def unfollow_user(data: dict):
    follower = data.get('follower')
    following = data.get('following')
    
    if not follower or not following:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('DELETE FROM follows WHERE follower = ? AND following = ?', (follower, following))
    
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="未关注该用户！")
    
    conn.commit()
    conn.close()
    return {"message": "取消关注成功！"}

# ==================== 收藏相关接口 ====================
@app.post("/favorite")
def add_favorite(data: dict):
    username = data.get('username')
    post_id = data.get('post_id')
    
    if not username or post_id is None:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    try:
        c.execute('INSERT INTO favorites (username, post_id) VALUES (?, ?)', (username, post_id))
        conn.commit()
        conn.close()
        return {"message": "收藏成功！"}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="已经收藏过该帖子！")

@app.delete("/favorite")
def remove_favorite(data: dict):
    username = data.get('username')
    post_id = data.get('post_id')
    
    if not username or post_id is None:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('DELETE FROM favorites WHERE username = ? AND post_id = ?', (username, post_id))
    
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="未收藏该帖子！")
    
    conn.commit()
    conn.close()
    return {"message": "取消收藏成功！"}

@app.get("/favorites/{username}")
def get_user_favorites(username: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('''
        SELECT p.*, u.avatar 
        FROM posts p 
        LEFT JOIN users u ON p.author = u.username
        WHERE p.id IN (SELECT post_id FROM favorites WHERE username = ?)
        ORDER BY p.publish_time DESC
    ''', (username,))
    posts = c.fetchall()
    
    import json
    result = []
    for post in posts:
        photos = json.loads(post['photos']) if post['photos'] else []
        result.append({
            'id': post['id'],
            'title': post['title'],
            'content': post['content'] or '',
            'photos': photos,
            'location': post['location'],
            'latitude': post['latitude'],
            'longitude': post['longitude'],
            'duration': post['duration'],
            'people': post['people'],
            'author': post['author'],
            'author_avatar': post['avatar'],
            'publish_time': post['publish_time'],
            'likes': int(post['likes']) if post['likes'] else 0,
            'comments': int(post['comments']) if post['comments'] else 0,
            'views': int(post['views']) if post['views'] else 0
        })
    
    conn.close()
    return result

@app.get("/check-favorite")
def check_favorite(username: str, post_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT * FROM favorites WHERE username = ? AND post_id = ?', (username, post_id))
    result = c.fetchone()
    
    conn.close()
    return {"is_favorited": result is not None}

# ==================== 关注相关接口 ====================
@app.get("/followers/{username}")
def get_following(username: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute('SELECT following FROM follows WHERE follower = ?', (username,))
    result = c.fetchall()
    
    following_list = [row['following'] for row in result]
    
    conn.close()
    return {"following": following_list}

@app.get("/check-follow")
def check_follow(follower: str, following: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT * FROM follows WHERE follower = ? AND following = ?', (follower, following))
    result = c.fetchone()
    
    conn.close()
    return {"is_following": result is not None}

@app.get("/nearby-posts")
def get_nearby_posts(latitude: float = 39.9042, longitude: float = 116.4074, radius: float = 1000.0, post_type: str = 'user', tag: str = None):
    """
    获取附近的帖子
    :param latitude: 当前纬度，默认北京
    :param longitude: 当前经度，默认北京
    :param radius: 搜索半径（公里），默认1000公里
    """
    init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 使用 Haversine 公式计算距离，SQLite 三角函数在少量浮点误差下可能越界，做夹取保护。
    c.execute('''
        SELECT p.*, u.avatar AS author_avatar,
               (6371 * acos(min(1, max(-1, cos(radians(?)) * cos(radians(p.latitude)) * cos(radians(p.longitude) - radians(?)) + sin(radians(?)) * sin(radians(p.latitude)))))) AS distance
        FROM posts
        p
        LEFT JOIN users u ON p.author = u.username
        WHERE p.latitude IS NOT NULL AND p.longitude IS NOT NULL
    ''', (latitude, longitude, latitude))
    
    posts = c.fetchall()
    
    # 在Python中过滤距离
    filtered_posts = []
    for post in posts:
        distance = post['distance']
        if distance <= radius:
            filtered_posts.append(post)
    
    def recommendation_score(post):
        distance = float(post['distance'] or 0)
        likes = int(post['likes'] or 0)
        views = int(post['views'] or 0)
        comments = int(post['comments'] or 0)
        like_rate = likes / max(views, 1)
        engagement = math.log1p(likes * 2 + comments * 3)
        distance_score = 1 / (1 + distance / 10)
        return like_rate * 0.45 + distance_score * 0.35 + engagement * 0.20

    def build_result(candidate_posts):
        ordered_posts = list(candidate_posts)
        ordered_posts.sort(key=recommendation_score, reverse=True)

        result = []
        for post in ordered_posts:
            post_data = serialize_post(post)
            post_data.update({
                'distance': round(post['distance'], 2),
                'like_rate': round((int(post['likes'] or 0) / max(int(post['views'] or 0), 1)), 3),
                'recommendation_score': round(recommendation_score(post), 3)
            })
            result.append(post_data)

        result = filter_posts_by_type(result, post_type)
        return filter_posts_by_tag(result, tag)

    result = build_result(filtered_posts)

    # 如果附近没有匹配当前类型/标签的帖子，用所有有位置信息的同类帖子兜底。
    if len(result) == 0 and len(filtered_posts) != len(posts):
        result = build_result(posts)
    
    conn.close()
    return result

@app.get("/heritage-items")
def get_heritage_items(city: str = '', category: str = '', tag: str = ''):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM heritage_items ORDER BY city, category, name')
    rows = c.fetchall()
    conn.close()

    items = [serialize_heritage_item(row) for row in rows]
    if city:
        normalized_city = normalize_search_text(city)
        items = [
            item for item in items
            if normalized_city in normalize_search_text(item.get('city')) or normalized_city in normalize_search_text(item.get('province'))
        ]
    if category:
        items = [item for item in items if item.get('category') == category]
    if tag:
        items = [item for item in items if tag in (item.get('tags') or [])]
    items.sort(key=heritage_sort_key)
    return items

@app.get("/heritage-items/{item_id}")
def get_heritage_item(item_id: int):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM heritage_items WHERE id = ?', (item_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="非遗项目不存在")
    return serialize_heritage_item(row)

@app.post("/recommend-route")
def recommend_route(data: RouteRecommendationRequest):
    init_db()

    available_minutes = max(45, int(float(data.available_hours or 4) * 60))
    start = data.start_location or {}
    start_lat = start.get('latitude')
    start_lon = start.get('longitude')
    start_city = start.get('city') or start.get('name') or ''
    preferences = [str(item) for item in (data.preferences or []) if item]
    requested_tags = [str(item) for item in (data.tags or []) if item]

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM heritage_items')
    heritage_rows = c.fetchall()
    c.execute('''
        SELECT p.*, u.avatar AS author_avatar
        FROM posts p
        LEFT JOIN users u ON p.author = u.username
        WHERE p.guide_items IS NOT NULL AND p.guide_items != '[]'
    ''')
    guide_rows = c.fetchall()
    conn.close()

    candidates = []

    def city_matches(candidate_city):
        if not start_city:
            return False
        return normalize_search_text(candidate_city) in normalize_search_text(start_city) or normalize_search_text(start_city) in normalize_search_text(candidate_city)

    def score_common(candidate):
        item_tags = candidate.get('tags') or []
        category = candidate.get('category') or ''
        title = candidate.get('heritage_name') or candidate.get('name') or candidate.get('title') or ''
        display_title = candidate.get('name') or candidate.get('title') or title
        duration = int(candidate.get('estimated_minutes') or 60)
        distance = candidate.get('distance_km')
        matched_preferences = [
            pref for pref in preferences
            if pref == category or pref in item_tags or normalize_search_text(pref) in normalize_search_text(display_title)
        ]
        matched_tags = [tag for tag in requested_tags if tag in item_tags or normalize_search_text(tag) in normalize_search_text(display_title)]
        interest_score = min(1, len(matched_preferences) / max(1, len(preferences))) if preferences else 0.45
        tag_score = min(1, len(matched_tags) / max(1, len(requested_tags))) if requested_tags else 0.45
        time_score = 1 if duration <= available_minutes else max(0, 1 - (duration - available_minutes) / max(available_minutes, 1))
        city_score = 1 if city_matches(candidate.get('city', '')) else 0.35
        if distance is None:
            distance_score = city_score
        else:
            distance_score = 1 / (1 + distance / 8)
        heat_score = min(1, math.log1p(candidate.get('heat', 0)) / 9)
        core_heritage_score = 1 if title in CORE_HERITAGE_ITEM_NAMES else (0.65 if category in CORE_HERITAGE_CATEGORIES else 0.2)
        score = (
            interest_score * 0.32
            + distance_score * 0.20
            + time_score * 0.13
            + tag_score * 0.13
            + core_heritage_score * 0.17
            + heat_score * 0.05
        )
        reasons = []
        if matched_preferences:
            reasons.append(f"匹配兴趣：{'、'.join(matched_preferences[:2])}")
        if matched_tags:
            reasons.append(f"命中标签：{'、'.join(matched_tags[:2])}")
        if distance is not None:
            reasons.append(f"距离起点约 {round(distance, 1)}km")
        elif city_matches(candidate.get('city', '')):
            reasons.append(f"位于你选择的城市：{candidate.get('city')}")
        if duration <= available_minutes:
            reasons.append(f"适合 {round(available_minutes / 60, 1)} 小时行程")
        return round(score, 3), reasons or ['综合文化深度、距离和时间适配推荐']

    for row in heritage_rows:
        item = serialize_heritage_item(row)
        if start_city and not city_matches(item.get('city', '')):
            continue
        experience_places = item.get('experience_places') or []
        place_options = experience_places if is_core_heritage_item(item) and experience_places else [None]
        for place in place_options:
            place = place or {}
            place_lat = place.get('latitude', item.get('latitude'))
            place_lon = place.get('longitude', item.get('longitude'))
            place_name = place.get('name') or item.get('location_name') or item.get('name')
            distance = haversine_km(start_lat, start_lon, place_lat, place_lon)
            heritage_name = item.get('name')
            title = f"{heritage_name} · {place_name}" if place else heritage_name
            place_experience = place.get('experience') or ''
            description_parts = [
                place_experience,
                item.get('inheritor_intro') or '',
                item.get('historical_background') or ''
            ]
            candidate = {
                **item,
                'type': 'heritage',
                'name': title,
                'heritage_name': heritage_name,
                'experience_place': place,
                'other_experience_places': experience_places,
                'location_name': place.get('location_name') or item.get('location_name') or '',
                'latitude': place_lat,
                'longitude': place_lon,
                'estimated_minutes': place.get('duration') or item.get('suitable_duration') or 60,
                'distance_km': distance,
                'heat': 220 if is_core_heritage_item(item) else 180,
                'visit_action': place_experience or item.get('visit_action') or item.get('inheritor_intro') or '',
                'description': ' '.join(part for part in description_parts if part),
                'tags': list(dict.fromkeys((item.get('tags') or []) + (place.get('tags') or [])))
            }
            score, reasons = score_common(candidate)
            candidate_role = 'core_heritage' if is_core_heritage_item(item) else 'scene_support'
            candidate.update({'score': score, 'reason': '；'.join(reasons), 'route_role': candidate_role})
            candidates.append(candidate)

    for row in guide_rows:
        post = serialize_post(row)
        if start_city and not city_matches(post.get('city') or ''):
            continue
        guide_tags = post.get('tags') or []
        if not guide_tags:
            title_text = normalize_search_text(f"{post.get('title')} {post.get('content')}")
            if '园林' in title_text or '公园' in title_text:
                guide_tags.append('园林')
            if '建筑' in title_text or '宫' in title_text or '塔' in title_text:
                guide_tags.append('历史建筑')
            if '岭南' in title_text or '广州' in title_text:
                guide_tags.append('岭南')
            if '博物馆' in title_text:
                guide_tags.append('博物馆')
        distance = haversine_km(start_lat, start_lon, post.get('latitude'), post.get('longitude'))
        candidate = {
            'type': 'guide_post',
            'id': post['id'],
            'title': post['title'],
            'name': post['title'],
            'category': '城市导览',
            'subcategory': '景点路线',
            'city': post.get('city') or '',
            'location_name': post.get('location') or '',
            'latitude': post.get('latitude'),
            'longitude': post.get('longitude'),
            'estimated_minutes': max(60, int(post.get('duration') or 1) * 60),
            'tags': guide_tags,
            'cover_image': (post.get('photos') or [''])[0],
            'distance_km': distance,
            'heat': int(post.get('likes') or 0) * 2 + int(post.get('comments') or 0) * 3 + int(post.get('views') or 0),
            'visit_action': compact_preview(post.get('content') or post.get('title')),
            'description': compact_preview(post.get('content') or post.get('title')),
            'post': post
        }
        score, reasons = score_common(candidate)
        candidate.update({'score': score, 'reason': '；'.join(reasons), 'route_role': 'scene_support'})
        candidates.append(candidate)

    route_focus = infer_route_focus(preferences, requested_tags, data.route_focus)
    main_role = 'core_heritage' if route_focus == 'heritage' else 'scene_support'
    support_role = 'scene_support' if main_role == 'core_heritage' else 'core_heritage'

    def role_rank(candidate):
        return 0 if candidate.get('route_role') == main_role else 1

    candidates.sort(key=lambda item: (role_rank(item), -item['score']))
    main_candidates = [item for item in candidates if item.get('route_role') == main_role]
    support_candidates = [item for item in candidates if item.get('route_role') == support_role]

    selected = []
    used_minutes = 0
    used_names = set()

    main_target = 2 if available_minutes >= 300 else 1
    support_target = 2 if available_minutes >= 240 else 1

    def add_candidate(candidate, role_label):
        nonlocal used_minutes
        candidate_key = candidate.get('heritage_name') if candidate.get('route_role') == 'core_heritage' else candidate.get('name')
        if not candidate or candidate_key in used_names:
            return False
        next_minutes = candidate.get('estimated_minutes') or 60
        if selected and used_minutes + next_minutes > available_minutes + 45:
            return False
        candidate['route_line_role'] = role_label
        selected.append(candidate)
        used_names.add(candidate_key)
        used_minutes += next_minutes
        return True

    for candidate in main_candidates:
        if len([item for item in selected if item.get('route_line_role') == 'main']) >= main_target:
            break
        add_candidate(candidate, 'main')

    def distance_to_selected(candidate):
        distances = [
            haversine_km(candidate.get('latitude'), candidate.get('longitude'), item.get('latitude'), item.get('longitude'))
            for item in selected
        ]
        distances = [distance for distance in distances if distance is not None]
        return min(distances) if distances else candidate.get('distance_km') or 99999

    support_candidates.sort(key=lambda item: (distance_to_selected(item), -item.get('score', 0)))
    for candidate in support_candidates:
        if len([item for item in selected if item.get('route_line_role') == 'support']) >= support_target:
            break
        add_candidate(candidate, 'support')

    if len(selected) < 2:
        for candidate in candidates:
            if len(selected) >= 4:
                break
            add_candidate(candidate, 'main' if candidate.get('route_role') == main_role else 'support')

    if not selected and candidates:
        selected = candidates[:1]
        selected[0]['route_line_role'] = 'main'
        used_minutes = selected[0].get('estimated_minutes') or 60

    selected = order_route_by_line_role(selected, start_lat, start_lon)
    transfer_minutes = enrich_route_navigation(selected, start)
    total_route_minutes = used_minutes + transfer_minutes
    while len(selected) > 1 and total_route_minutes > available_minutes + 30:
        removed = selected.pop()
        used_minutes -= removed.get('estimated_minutes') or 60
        transfer_minutes = enrich_route_navigation(selected, start)
        total_route_minutes = used_minutes + transfer_minutes

    if selected and not any(item.get('route_line_role') == 'main' for item in selected) and main_candidates:
        selected = []
        used_minutes = 0
        used_names = set()
        for candidate in main_candidates:
            if add_candidate(candidate, 'main'):
                break
        support_candidates.sort(key=lambda item: (distance_to_selected(item), -item.get('score', 0)))
        for candidate in support_candidates:
            if add_candidate(candidate, 'support'):
                break
        selected = order_route_by_line_role(selected, start_lat, start_lon)
        transfer_minutes = enrich_route_navigation(selected, start)
        total_route_minutes = used_minutes + transfer_minutes
        while len(selected) > 1 and total_route_minutes > available_minutes + 30:
            removed = next((item for item in reversed(selected) if item.get('route_line_role') == 'support'), selected[-1])
            selected.remove(removed)
            used_minutes -= removed.get('estimated_minutes') or 60
            transfer_minutes = enrich_route_navigation(selected, start)
            total_route_minutes = used_minutes + transfer_minutes

    city_label = start_city or (selected[0].get('city') if selected else '中国')
    preference_label = '、'.join(preferences[:2]) if preferences else '文化深度'
    feasibility = route_feasibility_label(total_route_minutes, available_minutes, len(selected))
    transport_summary = '已按当前位置和点位距离重新排序，优先减少绕路；具体路况以地图实时导航为准。'
    if selected:
        first_stop = selected[0].get('name') or selected[0].get('title')
        transport_summary = f"先从{start.get('name') or start_city or '当前位置'}前往{first_stop}，再按卡片顺序游览。{transport_summary}"
    focus_label = '非遗为主，周边景点辅助' if route_focus == 'heritage' else '景点为主，周边非遗辅助'

    return {
        'route_title': f"{city_label}{preference_label}智能文化路线",
        'summary': f'当前采用“{focus_label}”生成：根据用户偏好、可用时间、地点距离、标签命中、内容热度和站点顺路程度生成。',
        'route_plan': {
            'focus': route_focus,
            'focus_label': focus_label,
            'feasibility': feasibility,
            'transport_summary': transport_summary,
            'arrival_hint': selected[0].get('arrival_guidance') if selected else '',
            'stop_count': len(selected),
            'visit_minutes': used_minutes,
            'transfer_minutes': transfer_minutes,
            'total_minutes': total_route_minutes
        },
        'total_duration_minutes': total_route_minutes,
        'visit_duration_minutes': used_minutes,
        'transfer_duration_minutes': transfer_minutes,
        'available_minutes': available_minutes,
        'items': selected,
        'debug_weights': {
            'preference': 0.32,
            'distance': 0.20,
            'time': 0.13,
            'tags': 0.13,
            'core_heritage': 0.17,
            'heat': 0.05
        }
    }

# ==================== 消息相关接口 ====================
@app.post("/send-message")
def send_message(data: dict):
    sender = data.get('sender')
    receiver = data.get('receiver')
    content = data.get('content')
    
    if not sender or not receiver or not content:
        raise HTTPException(status_code=400, detail="缺少必要参数！")
    
    init_db()

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    c = conn.cursor()
    ensure_message_user(c, sender)
    ensure_message_user(c, receiver)
    
    send_time = datetime.now().isoformat()
    
    c.execute('INSERT INTO messages (sender, receiver, content, send_time) VALUES (?, ?, ?, ?)', 
              (sender, receiver, content, send_time))
    
    conn.commit()
    conn.close()
    return {"message": "消息发送成功！"}

@app.get("/messages/{username}")
def get_user_messages(username: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 获取用户收到的消息
    c.execute('''
        SELECT sender, COUNT(*) as unread_count
        FROM messages 
        WHERE receiver = ? AND is_read = 0
        GROUP BY sender
    ''', (username,))
    unread_result = c.fetchall()
    
    # 获取用户发送或收到消息的所有用户，同时获取头像
    c.execute('''
        SELECT t.user, u.avatar
        FROM (
            SELECT DISTINCT sender AS user FROM messages WHERE receiver = ?
            UNION
            SELECT DISTINCT receiver AS user FROM messages WHERE sender = ?
        ) t
        LEFT JOIN users u ON t.user = u.username
    ''', (username, username))
    users_result = c.fetchall()
    
    conn.close()
    
    # 构建未读消息字典
    unread_dict = {row['sender']: row['unread_count'] for row in unread_result}
    
    # 返回消息用户列表及未读数量
    result = []
    for row in users_result:
        user = row['user']
        result.append({
            'username': user,
            'avatar': row['avatar'],
            'unread': unread_dict.get(user, 0)
        })
    
    return {"messages": result}

@app.get("/chat-history/{user1}/{user2}")
def get_chat_history(user1: str, user2: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # 获取两个用户之间的聊天记录
    c.execute('''
        SELECT sender, receiver, content, send_time, is_read
        FROM messages
        WHERE (sender = ? AND receiver = ?) OR (sender = ? AND receiver = ?)
        ORDER BY send_time ASC
    ''', (user1, user2, user2, user1))
    
    messages = c.fetchall()
    
    # 标记用户收到的消息为已读
    c.execute('''
        UPDATE messages 
        SET is_read = 1 
        WHERE receiver = ? AND sender = ? AND is_read = 0
    ''', (user1, user2))
    
    conn.commit()
    conn.close()
    
    result = []
    for msg in messages:
        result.append({
            'sender': msg['sender'],
            'content': msg['content'],
            'time': msg['send_time'],
            'is_read': msg['is_read']
        })
    
    return {"history": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
