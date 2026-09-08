const navigationPageIds = [
    'mainPage',
    'profilePage',
    'myPostsPage',
    'followingPage',
    'userPostsPage',
    'messagesPage',
    'chatPage',
    'discoverPage',
    'smartRoutePage',
    'publishPage'
];

let detailReturnState = null;
const LANGUAGE_STORAGE_KEY = 'appLanguage';
let currentLanguage = localStorage.getItem(LANGUAGE_STORAGE_KEY) || '';

const I18N = {
    zh: {
        appTitle: '文化导览',
        languageTitle: '选择显示语言',
        languageSubtitle: '请选择进入后的界面语言，之后可在页面右上角切换。',
        languageChinese: '全部中文',
        languageEnglish: 'All English',
        home: '首页',
        discover: '发现',
        smartRouteTab: '路线',
        hot: '热门',
        popularRanking: '热门推荐',
        categoryRecommendation: '分类推荐',
        categoryResultTitle: '{category} 推荐',
        categoryEmpty: '这个分类还没有用户帖子',
        loadingCategory: '正在加载分类推荐...',
        today: '今日',
        likes: '赞',
        follow: '关注',
        following: '已关注',
        followed: '关注成功',
        unfollowed: '已取消关注',
        loginRequired: '请先登录！',
        loginContinueHint: '登录后会继续刚才的操作',
        cannotFollowSelf: '不能关注自己',
        locationNearby: '附近',
        unknownLocation: '未知位置',
        anonymousUser: '匿名用户',
        authorNoContent: '作者暂未添加正文。',
        unknownTime: '未知时间',
        publishedAt: '发布于 {date}',
        duration: '体验时长',
        peopleCount: '参与人数',
        bookmark: '收藏',
        bookmarked: '已收藏',
        bookmarkSuccess: '收藏成功',
        bookmarkRemoved: '已取消收藏',
        startGuide: '开始导览',
        saveRoute: '收藏路线',
        routeSaved: '已收藏路线',
        routeAlreadySaved: '这条路线已在你的收藏里',
        routeSavedHint: '可在「我的 - 我的收藏」继续打开这条导览路线',
        shareRoute: '分享路线',
        shareReady: '路线信息已复制',
        shareReadyHint: '可以发送给同行的人一起规划行程',
        guideIntro: '景点介绍',
        routeOverview: '推荐路线',
        routeStops: '分站讲解',
        quickGuideNav: '快速查看',
        storyEntry: '读故事',
        vrEntry: '进入 VR',
        adviceEntry: '看建议',
        routeActionHint: '先看路线，再按站点听讲解和导航。',
        followRouteHint: '跟着路线游览',
        chooseRouteFirst: '先选择路线',
        chooseRouteHint: '在地图下方选择路线后，再开始导览。',
        previousStop: '上一站',
        nextStop: '下一站',
        liveRoute: '路线状态',
        locatingUser: '正在定位，稍后显示到当前站距离',
        locationDeniedHint: '开启定位后，可显示你到当前站的距离和是否偏离路线',
        currentStopLabel: '当前站',
        nextTargetLabel: '下一站',
        distanceToStop: '距当前站约 {distance}',
        onRouteHint: '你在路线附近',
        offRouteHint: '可能偏离路线，建议回到最近站点',
        remainingEstimate: '剩余约 {distance}',
        skipStop: '跳过本站',
        switchShortRoute: '改走短线',
        returnToRoute: '回到路线',
        shortRouteApplied: '已切换到短线',
        routeReturned: '已回到最近的路线站点',
        noShortRoute: '当前没有更短路线',
        routeComplete: '已经到最后一站',
        completionStamp: '完成印章',
        stampPostfix: '体验完成',
        stampDefaultText: '你不是“经过”了这个地方，而是跟着路线读完了一段城市记忆。',
        stampIt: '盖章',
        stamped: '已盖章',
        stampSaved: '印章已保存',
        stampAlreadySaved: '这个地方已经盖过章',
        viewStamps: '查看印章',
        myStamps: '我的印章',
        noStamps: '还没有完成印章',
        stampsHint: '完成一条景点导览后，印章会收藏在这里。',
        guidePoint: '导览点',
        attractionGuide: '景点导览',
        playAudio: '播放语音',
        pauseAudio: '暂停语音',
        navigateThere: '导航过去',
        cityGuide: '城市导览',
        audioGuide: '景点语音导览',
        playWholeGuide: '播放整篇',
        routeMap: '路线地图',
        routeSelection: '路线选择',
        playGuide: '播放导览',
        reset: '重置',
        recommendedRoute: '推荐路线',
        guideImage: '导览图片',
        noGuideText: '暂无导览文案。',
        viewDetailNav: '查看详情与导航',
        authWelcome: '欢迎回来',
        authCreate: '创建账号',
        usernameOrEmail: '用户名或邮箱',
        password: '密码',
        login: '登录',
        register: '注册',
        noAccount: '还没有账号？',
        haveAccount: '已有账号？',
        signUp: '注册',
        signIn: '登录',
        changeAvatar: '更换头像',
        cropAvatar: '裁剪头像',
        cancel: '取消',
        confirm: '确认',
        my: '我的',
        username: '用户名',
        fans: '粉丝',
        gainedLikes: '获赞',
        myFollowing: '我的关注',
        myPosts: '我的帖子',
        myMessages: '我的消息',
        myFavorites: '我的收藏',
        changePassword: '修改密码',
        logout: '退出登录',
        userPosts: '用户帖子',
        messages: '消息',
        chat: '聊天',
        inputMessage: '输入消息...',
        send: '发送',
        selectAvatar: '选择头像',
        presetAvatar: '预设头像',
        uploadCustomAvatar: '上传自定义头像',
        clickUpload: '点击上传',
        oldPassword: '旧密码',
        newPassword: '新密码',
        confirmNewPassword: '确认新密码',
        confirmChange: '确认修改',
        nearbyNoPosts: '附近暂无帖子',
        nearbyHint: '尝试扩大搜索范围或发布新帖子',
        locationFallbackTitle: '已使用默认城市',
        locationFallbackHint: '未获取到定位，先展示默认城市内容，可稍后重新定位或手动选择位置。',
        retry: '重试',
        selectLocation: '选择位置',
        selectLocationDesc: '点击在地图上选择位置或获取当前位置',
        hotCities: '热门城市',
        recent: '最近使用',
        noRecentLocations: '暂无最近使用的位置',
        searchPlace: '搜索城市、区域或地点...',
        locate: '定位',
        zoomIn: '放大',
        zoomOut: '缩小',
        mapHint: '点击地图或移动选择位置',
        publish: '发布',
        addPhotos: '添加照片',
        title: '标题',
        titlePlaceholder: '给这篇笔记起个标题',
        content: '正文',
        contentPlaceholder: '添加正文，分享路线、体验、避坑建议...',
        location: '定位',
        noLocationSelected: '未选择位置',
        categoryTags: '分类标签',
        daysPlaceholder: '天数',
        peoplePlaceholder: '人数',
        dayUnit: '天',
        peopleUnit: '人',
        loading: '正在加载...',
        loadingNearby: '正在加载附近笔记...',
        noPosts: '还没有发布帖子',
        publishFirstHint: '点击底部加号发布你的第一条帖子吧！',
        loadingFailed: '加载失败',
        loadingFailedHint: '网络不稳定或服务暂时不可用，请稍后重试。',
        edit: '修改',
        delete: '删除',
        editPost: '编辑帖子',
        saveChanges: '保存修改',
        postTitle: '帖子标题',
        place: '地点',
        searchPosts: '搜索帖子...',
        search: '搜索',
        noSearchResults: '没有找到相关帖子',
        comments: '评论',
        writeComment: '写下你的评论...',
        noComments: '暂无评论',
        startChat: '开始聊天',
        noMessages: '还没有消息',
        messageHint: '关注他人后可以发送私信',
        noFollowing: '还没有关注任何人',
        followingHint: '去帖子详情页关注感兴趣的作者吧！',
        noFavorites: '还没有收藏任何帖子',
        favoritesHint: '去浏览帖子并收藏喜欢的内容吧！',
        noUserPosts: '{user} 还没有发布帖子',
        myPostsTitle: '{user} 的帖子',
        requestFailed: '失败：{detail}',
        serverUnavailable: '无法连接到服务器，请检查 Python 后端是否已启动！',
        publishLoading: '发布中...',
        publishSuccess: '发布成功！',
        editSuccess: '修改成功！',
        localMock: '（本地模拟）',
        saving: '保存中...',
        draftSaved: '草稿已保存',
        draftRestored: '已恢复上次未发布的草稿',
        draftKept: '发布失败，内容已保留为草稿',
        publishNeedText: '请输入标题或正文，图片可以稍后再补',
        photoOptionalHint: '图片可选，先写一条短笔记也可以。',
        publishReadyHint: '会自动保存草稿；标题或正文填写一项即可发布。',
        addPhotoRequired: '请至少添加一张照片',
        inputTitleRequired: '请输入标题',
        inputContentRequired: '请输入正文内容',
        getLocationRequired: '请获取定位',
        inputCommentRequired: '请输入评论内容',
        deleteConfirm: '确定要删除这篇帖子吗？此操作无法撤销。',
        deleteSuccess: '删除成功！',
        deleteFailed: '删除失败',
        browserNoGeo: '您的浏览器不支持地理位置功能',
        gettingLocation: '获取位置中...',
        locationPermissionDenied: '用户拒绝了位置请求',
        locationUnavailable: '位置信息不可用',
        locationTimeout: '请求位置超时',
        locationFailed: '获取位置失败',
        yesterday: '昨天',
        monthDay: '{month}月{day}日',
        speechUnsupported: '当前音频缺失，且浏览器不支持临时朗读。',
        speechFallback: '当前音频缺失，已使用临时朗读兜底。',
        noGuideDetail: '暂无详细导览。',
        stopLabel: '第 {index} 站',
        passwordMismatch: '两次输入的新密码不一致！',
        passwordTooShort: '密码长度至少需要6位！',
        logoutConfirm: '确定要退出登录吗？',
        inputPostTitle: '请输入帖子标题',
        saveSuccess: '保存成功！',
        noMapResults: '未找到相关地点',
        defaultCity: '北京市',
        likedToast: '已点赞',
        likedHint: '会为你推荐更多类似内容',
        unlikedToast: '已取消点赞',
        savedHint: '可在「我的 - 我的收藏」继续查看',
        followHint: 'TA 的新笔记会优先出现在你的关注列表',
        commentPosted: '评论已发布',
        commentHint: '可以继续补充路线、门票或避坑问题',
        viewNow: '去看看',
        experienceFeatureKicker: '精选体验',
        experienceFeatureTitle: '像真的走进去一样认识一个景点',
        enterExperience: '进入体验',
        immersiveExperience: '沉浸体验',
        vrSectionTitle: '先试全景预览，再进入 360 视角',
        vrLiteTab: '第一档 全景预览',
        vrSphereTab: '第二档 360 视角',
        featureMetaDeepDive: '图文深游',
        travelFeeling: '旅行感受',
        travelFeelingTitle: '不是看一个点，而是读一条街',
        practicalAdvice: '实用建议',
        practicalAdviceTitle: '怎么把这里走得更有感觉',
        sceneLabel: '场景 {index}',
        timeTravel: '时间穿越',
        dossierHeading: '建筑档案',
        dossierTitle: '把眼睛训练得更敏锐',
        walkRhythm: '步行节奏',
        walkRhythmTitle: '不要赶景点，要控制速度',
        stampHeading: '完成印章',
        stampedDone: '已盖章 · 体验完成',
        timeMachineBeforeTitle: '使馆区旧日街景',
        timeMachineBeforeDesc: '从开阔街面、院墙和建筑轮廓里，看这条街曾经的城市角色。',
        smartRouteKicker: '智能路线',
        smartRouteTitle: '智能生成文化路线',
        smartRouteSubtitle: '根据兴趣、时间、地点和同行人群，推荐适合你的非遗与城市文化路线。',
        generateRoute: '生成路线',
        smartRoutePlanner: '智能文化路线',
        heritageDataModel: '推荐说明',
        heritageDataTitle: '为什么推荐这些点',
        heritageDataDesc: '这里列出路线匹配到的非遗项目、体验地点和历史背景，方便判断推荐是否靠谱。',
        viewHeritageData: '为什么推荐这些点',
        hideHeritageData: '收起推荐说明',
        routePreference: '路线生成',
        routePreferenceTitle: '快速生成文化路线',
        routePreferenceDesc: '选一个玩法和出行时间，先生成一条能直接使用的路线。',
        routeInspiration: '路线灵感',
        routeInspirationHint: '像选择旅行玩法一样，先选一个方向，再微调偏好',
        moreRouteSettings: '更多设置',
        hideRouteSettings: '收起设置',
        routeExpectation: '路线预期',
        routeExpectationHint: '系统会按这个方向生成，可先确认是否符合你的想法',
        routeOverviewCard: '路线总览',
        routeTuneTitle: '不满意？换个方向',
        routeTuneRelaxed: '更轻松',
        routeTuneDeeper: '更深度',
        routeTuneHeritage: '多一点非遗',
        routeTunePhoto: '多一点拍照点',
        routeTuneLessWalk: '减少步行',
        routeTrustHint: '优先选择距离顺、照片清晰、体验信息完整的点位',
        preferenceSettings: '偏好选择',
        preferenceHint: '需要更精确时再调整主题、体验方式和路线氛围',
        interestPreference: '兴趣偏好',
        availableTime: '可用时间',
        startCity: '出发城市',
        travelPace: '游览节奏',
        travelCompanion: '同行人群',
        routeTags: '路线标签',
        routeFocus: '路线主线',
        routeFocusAuto: '自动判断',
        routeFocusHeritage: '非遗为主，周边景点辅助',
        routeFocusAttraction: '景点为主，周边非遗辅助',
        routeFocusLabel: '主次关系',
        routeMainStop: '主线',
        routeSupportStop: '辅助',
        experiencePlaces: '可体验地点',
        moreExperiencePlaces: '更多体验地点',
        routeResult: '推荐结果',
        routeMinutes: '{minutes} 分钟',
        routeCardHint: '点击卡片查看完整信息',
        viewRouteDetail: '查看完整信息',
        closeDetail: '关闭',
        whatToDo: '到这里',
        routeFeasibility: '可用性',
        routeArrival: '如何抵达',
        routeReason: '推荐理由',
        routeNextStop: '下一站',
        routeOpenMap: '打开地图导航',
        routeTransport: '交通方案',
        routeVisitTime: '游览',
        routeTransferTime: '路上',
        heritageInheritor: '传承人',
        heritageActivity: '活动时间',
        heritageHistory: '历史背景',
        openGuide: '打开导览',
        routeGenerating: '正在生成路线...'
    },
    en: {
        appTitle: 'Culture Guide',
        languageTitle: 'Choose Display Language',
        languageSubtitle: 'Choose the interface language for this app. You can switch later from the top-right button.',
        languageChinese: '全部中文',
        languageEnglish: 'All English',
        home: 'Home',
        discover: 'Discover',
        smartRouteTab: 'Routes',
        hot: 'HOT!',
        popularRanking: 'POPULAR RANKING',
        categoryRecommendation: 'Category Picks',
        categoryResultTitle: '{category} Picks',
        categoryEmpty: 'No user posts in this category yet',
        loadingCategory: 'Loading category picks...',
        today: 'Today',
        likes: 'Likes',
        follow: 'Follow',
        following: 'Following',
        followed: 'Followed',
        unfollowed: 'Unfollowed',
        loginRequired: 'Please log in first!',
        loginContinueHint: 'We will continue your action after login',
        cannotFollowSelf: 'You cannot follow yourself',
        locationNearby: 'Nearby',
        unknownLocation: 'Unknown location',
        anonymousUser: 'Anonymous user',
        authorNoContent: 'The author has not added body text yet.',
        unknownTime: 'Unknown time',
        publishedAt: 'Published on {date}',
        duration: 'Experience Duration',
        peopleCount: 'Number of People',
        bookmark: 'Save',
        bookmarked: 'Saved',
        bookmarkSuccess: 'Saved',
        bookmarkRemoved: 'Removed from saved',
        startGuide: 'Start Guide',
        saveRoute: 'Save Route',
        routeSaved: 'Route Saved',
        routeAlreadySaved: 'This route is already saved',
        routeSavedHint: 'Find this guided route later in Me - Saved Posts',
        shareRoute: 'Share Route',
        shareReady: 'Route info copied',
        shareReadyHint: 'Send it to your travel companions for planning',
        guideIntro: 'Attraction Intro',
        routeOverview: 'Recommended Route',
        routeStops: 'Stop-by-stop Guide',
        quickGuideNav: 'Quick View',
        storyEntry: 'Read Story',
        vrEntry: 'Enter VR',
        adviceEntry: 'Tips',
        routeActionHint: 'Check the route first, then follow each stop for audio and navigation.',
        followRouteHint: 'Follow This Route',
        chooseRouteFirst: 'Choose Route First',
        chooseRouteHint: 'Select a route below the map, then start the guide.',
        previousStop: 'Previous',
        nextStop: 'Next',
        liveRoute: 'Route Status',
        locatingUser: 'Locating you to show distance to this stop',
        locationDeniedHint: 'Enable location to see distance and route drift',
        currentStopLabel: 'Current Stop',
        nextTargetLabel: 'Next Stop',
        distanceToStop: 'About {distance} to this stop',
        onRouteHint: 'You are near the route',
        offRouteHint: 'You may be off route. Return to the nearest stop.',
        remainingEstimate: 'About {distance} remaining',
        skipStop: 'Skip Stop',
        switchShortRoute: 'Short Route',
        returnToRoute: 'Return to Route',
        shortRouteApplied: 'Switched to the short route',
        routeReturned: 'Returned to the nearest route stop',
        noShortRoute: 'No shorter route available',
        routeComplete: 'You are at the final stop',
        completionStamp: 'Completion Stamp',
        stampPostfix: 'Experience Complete',
        stampDefaultText: 'You did not just pass by this place. You followed the route and read a piece of city memory.',
        stampIt: 'Stamp',
        stamped: 'Stamped',
        stampSaved: 'Stamp saved',
        stampAlreadySaved: 'This place is already stamped',
        viewStamps: 'View Stamps',
        myStamps: 'My Stamps',
        noStamps: 'No stamps yet',
        stampsHint: 'Complete a guided route to collect a stamp here.',
        guidePoint: 'Guide Point',
        attractionGuide: 'Attraction Guide',
        playAudio: 'Play Audio',
        pauseAudio: 'Pause Audio',
        navigateThere: 'Navigate',
        cityGuide: 'City Guide',
        audioGuide: 'Audio Attraction Guide',
        playWholeGuide: 'Play Full Guide',
        routeMap: 'Route Map',
        routeSelection: 'Route Options',
        playGuide: 'Play Guide',
        reset: 'Reset',
        recommendedRoute: 'Recommended Route',
        guideImage: 'Guide Image',
        noGuideText: 'No guide text yet.',
        viewDetailNav: 'Details and Navigation',
        authWelcome: 'Welcome Back',
        authCreate: 'Create Account',
        usernameOrEmail: 'Username or Email',
        password: 'Password',
        login: 'Login',
        register: 'Register',
        noAccount: "Don't have an account? ",
        haveAccount: 'Already have an account? ',
        signUp: 'Sign up',
        signIn: 'Sign in',
        changeAvatar: 'Change Avatar',
        cropAvatar: 'Crop Avatar',
        cancel: 'Cancel',
        confirm: 'Confirm',
        my: 'Me',
        username: 'Username',
        fans: 'Fans',
        gainedLikes: 'Likes',
        myFollowing: 'Following',
        myPosts: 'My Posts',
        myMessages: 'Messages',
        myFavorites: 'Saved Posts',
        changePassword: 'Change Password',
        logout: 'Log Out',
        userPosts: 'User Posts',
        messages: 'Messages',
        chat: 'Chat',
        inputMessage: 'Type a message...',
        send: 'Send',
        selectAvatar: 'Select Avatar',
        presetAvatar: 'Preset Avatars',
        uploadCustomAvatar: 'Upload Custom Avatar',
        clickUpload: 'Click to Upload',
        oldPassword: 'Old Password',
        newPassword: 'New Password',
        confirmNewPassword: 'Confirm New Password',
        confirmChange: 'Save Password',
        nearbyNoPosts: 'No nearby posts yet',
        nearbyHint: 'Try expanding the area or publishing a new post',
        locationFallbackTitle: 'Using default city',
        locationFallbackHint: 'Location was unavailable, so default city content is shown. You can retry or choose manually.',
        retry: 'Retry',
        selectLocation: 'Select Location',
        selectLocationDesc: 'Tap to choose a location on the map or use current location',
        hotCities: 'Popular Cities',
        recent: 'Recent',
        noRecentLocations: 'No recent locations',
        searchPlace: 'Search city, area, or place...',
        locate: 'Locate',
        zoomIn: 'Zoom In',
        zoomOut: 'Zoom Out',
        mapHint: 'Tap or move the map to choose a location',
        publish: 'Publish',
        addPhotos: 'Add Photos',
        title: 'Title',
        titlePlaceholder: 'Give this note a title',
        content: 'Body',
        contentPlaceholder: 'Share routes, experiences, and tips...',
        location: 'Location',
        noLocationSelected: 'No location selected',
        categoryTags: 'Category Tags',
        daysPlaceholder: 'Days',
        peoplePlaceholder: 'People',
        dayUnit: 'days',
        peopleUnit: 'people',
        loading: 'Loading...',
        loadingNearby: 'Loading nearby notes...',
        noPosts: 'No posts yet',
        publishFirstHint: 'Tap the plus button below to publish your first post.',
        loadingFailed: 'Load failed',
        loadingFailedHint: 'Network or server is unavailable. Please try again later.',
        edit: 'Edit',
        delete: 'Delete',
        editPost: 'Edit Post',
        saveChanges: 'Save Changes',
        postTitle: 'Post Title',
        place: 'Place',
        searchPosts: 'Search posts...',
        search: 'Search',
        noSearchResults: 'No matching posts found',
        comments: 'Comments',
        writeComment: 'Write a comment...',
        noComments: 'No comments yet',
        startChat: 'Start chatting',
        noMessages: 'No messages yet',
        messageHint: 'Follow someone to send direct messages',
        noFollowing: 'You are not following anyone yet',
        followingHint: 'Follow authors you like from post detail pages.',
        noFavorites: 'No saved posts yet',
        favoritesHint: 'Browse posts and save the ones you like.',
        noUserPosts: '{user} has not published any posts yet',
        myPostsTitle: "{user}'s Posts",
        requestFailed: 'Failed: {detail}',
        serverUnavailable: 'Cannot connect to the server. Please check whether the Python backend is running.',
        publishLoading: 'Publishing...',
        publishSuccess: 'Published!',
        editSuccess: 'Saved!',
        localMock: ' (local mock)',
        saving: 'Saving...',
        draftSaved: 'Draft saved',
        draftRestored: 'Restored your previous draft',
        draftKept: 'Publishing failed. Your draft was kept.',
        publishNeedText: 'Add a title or body. Photos can come later.',
        photoOptionalHint: 'Photos are optional. You can publish a quick note first.',
        publishReadyHint: 'Drafts save automatically. A title or body is enough to publish.',
        addPhotoRequired: 'Please add at least one photo',
        inputTitleRequired: 'Please enter a title',
        inputContentRequired: 'Please enter body text',
        getLocationRequired: 'Please choose a location',
        inputCommentRequired: 'Please enter a comment',
        deleteConfirm: 'Delete this post? This action cannot be undone.',
        deleteSuccess: 'Deleted!',
        deleteFailed: 'Delete failed',
        browserNoGeo: 'Your browser does not support geolocation',
        gettingLocation: 'Getting location...',
        locationPermissionDenied: 'Location permission was denied',
        locationUnavailable: 'Location information is unavailable',
        locationTimeout: 'Location request timed out',
        locationFailed: 'Failed to get location',
        yesterday: 'Yesterday',
        monthDay: '{month}/{day}',
        speechUnsupported: 'Audio is missing, and this browser does not support temporary speech reading.',
        speechFallback: 'Audio is missing, so temporary speech reading is being used.',
        noGuideDetail: 'No detailed guide text yet.',
        stopLabel: 'Stop {index}',
        passwordMismatch: 'The two new passwords do not match.',
        passwordTooShort: 'Password must be at least 6 characters.',
        logoutConfirm: 'Log out now?',
        inputPostTitle: 'Please enter a post title',
        saveSuccess: 'Saved!',
        noMapResults: 'No matching places found',
        defaultCity: 'Beijing',
        likedToast: 'Liked',
        likedHint: 'We will recommend more similar notes',
        unlikedToast: 'Like removed',
        savedHint: 'Find it later in Me - Saved Posts',
        followHint: "This author's new notes will appear in your following list",
        commentPosted: 'Comment posted',
        commentHint: 'You can keep asking about routes, tickets, or tips',
        viewNow: 'View',
        experienceFeatureKicker: 'Featured Experience',
        experienceFeatureTitle: 'Understand a place as if you walked into it',
        enterExperience: 'Start Experience',
        immersiveExperience: 'Immersive Experience',
        vrSectionTitle: 'Try the panorama preview, then enter the 360 view',
        vrLiteTab: 'Level 1 Panorama Preview',
        vrSphereTab: 'Level 2 360 View',
        featureMetaDeepDive: 'Visual Deep Dive',
        travelFeeling: 'Travel Impressions',
        travelFeelingTitle: 'Do not just see a spot; read a street',
        practicalAdvice: 'Practical Tips',
        practicalAdviceTitle: 'How to walk this place with more feeling',
        sceneLabel: 'Scene {index}',
        timeTravel: 'Time Travel',
        dossierHeading: 'Architecture Files',
        dossierTitle: 'Train your eyes to notice more',
        walkRhythm: 'Walking Rhythm',
        walkRhythmTitle: 'Do not rush the sights; control your pace',
        stampHeading: 'Completion Stamp',
        stampedDone: 'Stamped · Experience Complete',
        timeMachineBeforeTitle: 'Old Legation Quarter Streetscape',
        timeMachineBeforeDesc: "Read the street's former urban role through its broad street plane, walls, and building silhouettes.",
        smartRouteKicker: 'Smart Route',
        smartRouteTitle: 'Smart Culture Route Generator',
        smartRouteSubtitle: 'Recommend an ICH and city-culture route based on interests, time, place, and travel companions.',
        generateRoute: 'Generate Route',
        smartRoutePlanner: 'Smart Culture Route',
        heritageDataModel: 'Recommendation Notes',
        heritageDataTitle: 'Why these stops',
        heritageDataDesc: 'Shows matched heritage records, experience places, and historical context behind the route.',
        viewHeritageData: 'Why these stops',
        hideHeritageData: 'Hide explanation',
        routePreference: 'Route Generator',
        routePreferenceTitle: 'Quick culture route',
        routePreferenceDesc: 'Pick a style and time first, then generate a usable route.',
        routeInspiration: 'Route Ideas',
        routeInspirationHint: 'Pick a travel style first, then fine tune the route',
        moreRouteSettings: 'More settings',
        hideRouteSettings: 'Hide settings',
        routeExpectation: 'Route Preview',
        routeExpectationHint: 'The system will generate the route in this direction',
        routeOverviewCard: 'Route Overview',
        routeTuneTitle: 'Not ideal? Adjust it',
        routeTuneRelaxed: 'More relaxed',
        routeTuneDeeper: 'Deeper',
        routeTuneHeritage: 'More heritage',
        routeTunePhoto: 'More photo spots',
        routeTuneLessWalk: 'Less walking',
        routeTrustHint: 'Prioritizes nearby, clear-photo, experience-ready stops',
        preferenceSettings: 'Preferences',
        preferenceHint: 'Fine tune themes, experience styles, and route mood when needed',
        interestPreference: 'Interests',
        availableTime: 'Available Time',
        startCity: 'Start City',
        travelPace: 'Travel Pace',
        travelCompanion: 'Companions',
        routeTags: 'Route Tags',
        routeFocus: 'Route Focus',
        routeFocusAuto: 'Auto',
        routeFocusHeritage: 'Heritage first, nearby places assist',
        routeFocusAttraction: 'Places first, nearby heritage assists',
        routeFocusLabel: 'Focus',
        routeMainStop: 'Main',
        routeSupportStop: 'Assist',
        experiencePlaces: 'Experience Places',
        moreExperiencePlaces: 'More Places',
        routeResult: 'Recommendation',
        routeMinutes: '{minutes} min',
        routeCardHint: 'Tap a card for full details',
        viewRouteDetail: 'View Details',
        closeDetail: 'Close',
        whatToDo: 'What to do',
        routeFeasibility: 'Feasibility',
        routeArrival: 'How to get there',
        routeReason: 'Why recommended',
        routeNextStop: 'Next stop',
        routeOpenMap: 'Open map',
        routeTransport: 'Transport plan',
        routeVisitTime: 'Visit',
        routeTransferTime: 'Transfer',
        heritageInheritor: 'Inheritor',
        heritageActivity: 'Activity Time',
        heritageHistory: 'Historical Context',
        openGuide: 'Open Guide',
        routeGenerating: 'Generating route...'
    }
};

const TAG_LABELS = {
    zh: {
        food: '美食',
        place: '地点',
        shopping: '购物',
        nature: '自然',
        culture: '文化'
    },
    en: {
        food: 'Food',
        place: 'Places',
        shopping: 'Shopping',
        nature: 'Nature',
        culture: 'Culture'
    }
};

function t(key, vars = {}) {
    const dict = I18N[currentLanguage || 'zh'] || I18N.zh;
    let text = dict[key] || I18N.zh[key] || key;
    Object.entries(vars).forEach(([name, value]) => {
        text = text.replaceAll(`{${name}}`, value);
    });
    return text;
}

function showToast(message, options = {}) {
    const existing = document.getElementById('appToast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'appToast';
    toast.className = `app-toast ${options.type || 'success'}`;

    const text = document.createElement('div');
    text.className = 'app-toast-text';

    const title = document.createElement('strong');
    title.textContent = message;
    text.appendChild(title);

    if (options.detail) {
        const detail = document.createElement('span');
        detail.textContent = options.detail;
        text.appendChild(detail);
    }

    if (options.actionText && typeof options.onAction === 'function') {
        const action = document.createElement('button');
        action.type = 'button';
        action.textContent = options.actionText;
        action.onclick = () => {
            toast.remove();
            options.onAction();
        };
        toast.append(text, action);
    } else {
        toast.appendChild(text);
    }

    document.body.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('active'));

    clearTimeout(showToast.hideTimer);
    showToast.hideTimer = setTimeout(() => {
        toast.classList.remove('active');
        setTimeout(() => toast.remove(), 220);
    }, options.duration || 3200);
}

function openFavoritesFromToast() {
    document.getElementById('detailPage')?.classList.remove('active');
    showMyFavorites();
}

function openFollowingFromToast() {
    document.getElementById('detailPage')?.classList.remove('active');
    showFollowingList();
}

function renderEmptyState(title, hint = '', iconPath = '') {
    const fallbackIcon = 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 12H7v-2h10v2zm0-4H7V9h10v2z';
    return `
        <div class="empty-state">
            <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="${iconPath || fallbackIcon}"></path>
            </svg>
            <p>${escapeHtml(title)}</p>
            ${hint ? `<p class="empty-state-hint">${escapeHtml(hint)}</p>` : ''}
        </div>
    `;
}

function isUserLoggedIn() {
    return localStorage.getItem('isLoggedIn') === 'true' && Boolean(localStorage.getItem('username'));
}

function requireLogin(actionAfterAuth = null) {
    if (isUserLoggedIn()) return true;
    pendingAuthAction = typeof actionAfterAuth === 'function' ? actionAfterAuth : null;
    showToast(t('loginRequired'), {
        type: 'warning',
        detail: pendingAuthAction ? t('loginContinueHint') : ''
    });
    openAuthModal();
    return false;
}

function getTagLabel(tagId) {
    return TAG_LABELS[currentLanguage || 'zh']?.[tagId] || TAG_LABELS.zh[tagId] || tagId;
}

function shouldTranslateContent(value) {
    return currentLanguage === 'en' && typeof value === 'string' && /[\u4e00-\u9fff]/.test(value);
}

function translationCacheKey(text, target = 'en') {
    return `translation_${target}_${text}`;
}

function readTranslationCache(text, target = 'en') {
    try {
        return localStorage.getItem(translationCacheKey(text, target));
    } catch (error) {
        return null;
    }
}

function writeTranslationCache(text, translated, target = 'en') {
    try {
        localStorage.setItem(translationCacheKey(text, target), translated);
    } catch (error) {
        // Ignore quota errors; translation should still display for this render.
    }
}

async function fetchTranslation(text, target = 'en') {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 8000);

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text, target }),
            signal: controller.signal
        });
        if (!response.ok) return text;
        const data = await response.json();
        const translated = data.translated || '';
        return translated.trim() || text;
    } catch (error) {
        console.warn('自动翻译失败，显示原文:', error);
        return text;
    } finally {
        clearTimeout(timer);
    }
}

async function translateText(text, target = 'en') {
    if (!shouldTranslateContent(text)) return text;
    const cached = readTranslationCache(text, target);
    if (cached) return cached;

    const translated = await fetchTranslation(text, target);
    if (translated && translated !== text) {
        writeTranslationCache(text, translated, target);
    }
    return translated;
}

async function localizeGuideItem(item) {
    if (!item || currentLanguage !== 'en') return item;
    return {
        ...item,
        title: await translateText(item.title),
        text: await translateText(item.text),
        detail: await translateText(item.detail),
        time: await translateText(item.time)
    };
}

async function localizeRouteMap(routeMap) {
    if (!routeMap || currentLanguage !== 'en') return routeMap;
    const routes = Array.isArray(routeMap.routes)
        ? await Promise.all(routeMap.routes.map(async route => ({
            ...route,
            title: await translateText(route.title),
            description: await translateText(route.description),
            duration: await translateText(route.duration),
            distance: await translateText(route.distance),
            estimate_note: await translateText(route.estimate_note)
        })))
        : routeMap.routes;

    return {
        ...routeMap,
        title: await translateText(routeMap.title),
        subtitle: await translateText(routeMap.subtitle),
        routes
    };
}

async function localizePost(post) {
    if (!post || currentLanguage !== 'en') return post;
    const guideItems = Array.isArray(post.guide_items)
        ? await Promise.all(post.guide_items.map(localizeGuideItem))
        : post.guide_items;

    return {
        ...post,
        title: await translateText(post.title),
        content: await translateText(post.content),
        location: await translateText(post.location),
        city: await translateText(post.city),
        guide_items: guideItems,
        route_map: await localizeRouteMap(post.route_map)
    };
}

async function localizePostSummary(post, options = {}) {
    if (!post || currentLanguage !== 'en') return post;
    return {
        ...post,
        title: await translateText(post.title),
        content: options.includeContent ? await translateText(post.content) : post.content,
        location: await translateText(post.location),
        city: await translateText(post.city)
    };
}

async function translateFields(item, fields) {
    if (!item || currentLanguage !== 'en') return item;
    const translated = { ...item };
    for (const field of fields) {
        translated[field] = await translateText(item[field]);
    }
    return translated;
}

async function localizeExperienceSpot(spot, options = {}) {
    if (!spot || currentLanguage !== 'en') return spot;
    const summaryOnly = Boolean(options.summaryOnly);

    const localized = {
        ...spot,
        title: await translateText(spot.title),
        kicker: await translateText(spot.kicker),
        subtitle: await translateText(spot.subtitle)
    };

    if (summaryOnly) return localized;

    localized.meta = Array.isArray(spot.meta)
        ? await Promise.all(spot.meta.map(item => translateFields(item, ['label', 'value'])))
        : spot.meta;
    localized.intro = Array.isArray(spot.intro)
        ? await Promise.all(spot.intro.map(text => translateText(text)))
        : spot.intro;
    localized.story = Array.isArray(spot.story)
        ? await Promise.all(spot.story.map(item => translateFields(item, ['title', 'text'])))
        : spot.story;
    localized.liteHotspots = Array.isArray(spot.liteHotspots)
        ? await Promise.all(spot.liteHotspots.map(item => translateFields(item, ['title', 'text'])))
        : spot.liteHotspots;
    localized.vrCaption = await translateText(spot.vrCaption);
    localized.vrInstructions = spot.vrInstructions
        ? await translateFields(spot.vrInstructions, ['lite', 'sphere'])
        : spot.vrInstructions;
    localized.timeTravel = spot.timeTravel
        ? await translateFields(spot.timeTravel, ['beforeLabel', 'afterLabel', 'title', 'beforeText', 'afterText', 'detail'])
        : spot.timeTravel;
    localized.dossiers = Array.isArray(spot.dossiers)
        ? await Promise.all(spot.dossiers.map(item => translateFields(item, ['title', 'tag', 'text', 'focus'])))
        : spot.dossiers;
    localized.walkRhythm = Array.isArray(spot.walkRhythm)
        ? await Promise.all(spot.walkRhythm.map(item => translateFields(item, ['title', 'text', 'time'])))
        : spot.walkRhythm;
    localized.stamp = spot.stamp
        ? await translateFields(spot.stamp, ['title', 'text', 'code'])
        : spot.stamp;
    localized.practical = Array.isArray(spot.practical)
        ? await Promise.all(spot.practical.map(item => translateFields(item, ['title', 'text'])))
        : spot.practical;

    return localized;
}

function setLanguage(lang) {
    currentLanguage = lang === 'en' ? 'en' : 'zh';
    localStorage.setItem(LANGUAGE_STORAGE_KEY, currentLanguage);
    applyLanguage();
    refreshVisibleContentForLanguage();
    document.getElementById('languageGate')?.classList.remove('active');
}

function showLanguageGateIfNeeded() {
    if (!currentLanguage) {
        document.getElementById('languageGate')?.classList.add('active');
    }
}

function applyLanguage() {
    document.documentElement.lang = currentLanguage === 'en' ? 'en' : 'zh-CN';
    document.title = t('appTitle');
    document.querySelectorAll('[data-i18n]').forEach(el => {
        el.textContent = t(el.dataset.i18n);
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        el.placeholder = t(el.dataset.i18nPlaceholder);
    });
    document.querySelectorAll('[data-i18n-aria-label]').forEach(el => {
        el.setAttribute('aria-label', t(el.dataset.i18nAriaLabel));
    });

    const switchLink = document.querySelector('.auth-switch a');
    if (switchLink) {
        toggleAuthMode(true);
    }
    renderHotCategories();
    renderExperienceFeatures();
    renderPublishTags();
    loadRecentLocations();

    document.querySelectorAll('#languageToggle, #experienceLanguageToggle').forEach(button => {
        button.textContent = currentLanguage === 'en' ? '中文' : 'EN';
    });
}

async function refreshVisibleContentForLanguage() {
    const detailPage = document.getElementById('detailPage');
    if (detailPage?.classList.contains('active') && currentPostSource) {
        await showPostDetail(currentPostSource);
        return;
    }

    const experiencePage = document.getElementById('experiencePage');
    if (experiencePage?.classList.contains('active') && currentExperienceSpotSource) {
        await renderExperiencePageFromSource(currentExperienceSpotSource);
        requestAnimationFrame(() => bindLiteVr(currentExperienceSpot));
        return;
    }

    const discoverPage = document.getElementById('discoverPage');
    if (discoverPage && getComputedStyle(discoverPage).display !== 'none') {
        await loadNearbyPosts();
        return;
    }

    const smartRoutePage = document.getElementById('smartRoutePage');
    if (smartRoutePage && getComputedStyle(smartRoutePage).display !== 'none') {
        renderSmartRouteChips();
        renderHeritagePreview(smartRouteState.heritageItems);
        const result = document.getElementById('smartRouteResult');
        if (result && !result.hidden && result.innerHTML.trim()) {
            await generateSmartRoute();
        }
        return;
    }

    const myPostsPage = document.getElementById('myPostsPage');
    if (myPostsPage && getComputedStyle(myPostsPage).display !== 'none') {
        const title = document.querySelector('#myPostsPage .posts-header h1')?.textContent || '';
        if (title === t('myStamps') || title === I18N.zh.myStamps || title === I18N.en.myStamps) {
            showMyGuideStamps();
        } else if (title === t('myFavorites') || title === I18N.zh.myFavorites || title === I18N.en.myFavorites) {
            await showMyFavorites();
        } else {
            const currentUser = localStorage.getItem('username');
            if (currentUser) await loadMyPostsForProfile(currentUser);
        }
        return;
    }

    const mainPage = document.getElementById('mainPage');
    if (mainPage && getComputedStyle(mainPage).display !== 'none') {
        await loadMyPosts();
    }
}

const POST_TAGS = [
    { id: 'food', image: '/assets/categories/food.jpg' },
    { id: 'place', image: '/assets/categories/place.jpg' },
    { id: 'shopping', image: '/assets/categories/shopping.jpg' },
    { id: 'nature', image: '/assets/categories/nature.jpg' },
    { id: 'culture', image: '/assets/categories/culture.jpg' }
];

const SMART_ROUTE_PREFERENCES = ['传统技艺', '传统戏剧', '传统美术', '民俗', '历史建筑', '园林', '传统音乐', '传统舞蹈', '节庆活动', '博物馆', '城市漫步'];
const SMART_ROUTE_TAGS = ['室内', '户外', '手工体验', '表演', '亲子', '轻松', '深度', '少走路', '夜间', '岭南', '博物馆', '国际友好', '适合拍照'];
const SMART_ROUTE_PRESETS = [
    {
        id: 'halfday',
        title: '半日精华',
        desc: '少绕路，优先选代表性强、交通顺的点',
        preferences: ['传统技艺', '历史建筑'],
        tags: ['室内', '轻松', '博物馆'],
        hours: '4',
        pace: '轻松',
        companion: '国际友好',
        focus: 'auto'
    },
    {
        id: 'heritage',
        title: '非遗深度',
        desc: '把京剧、手作、展演作为主线来安排',
        preferences: ['传统戏剧', '传统技艺', '传统美术'],
        tags: ['深度', '手工体验', '表演'],
        hours: '4',
        pace: '深度',
        companion: '国际友好',
        focus: 'heritage'
    },
    {
        id: 'family',
        title: '亲子轻松',
        desc: '控制步行强度，优先室内和可互动体验',
        preferences: ['民俗', '博物馆', '传统美术'],
        tags: ['亲子', '轻松', '少走路', '室内'],
        hours: '2',
        pace: '少走路',
        companion: '亲子',
        focus: 'heritage'
    },
    {
        id: 'photo',
        title: '拍照夜游',
        desc: '兼顾城市街区、建筑氛围和夜间可逛性',
        preferences: ['城市漫步', '历史建筑', '节庆活动'],
        tags: ['适合拍照', '夜间', '户外'],
        hours: '4',
        pace: '轻松',
        companion: '适合拍照',
        focus: 'attraction'
    }
];
const SMART_CITY_LOCATIONS = {
    '北京': { name: '北京', city: '北京', latitude: 39.9042, longitude: 116.4074 },
    '广州市': { name: '广州', city: '广州市', latitude: 23.1291, longitude: 113.2644 },
    '上海市': { name: '上海', city: '上海市', latitude: 31.2304, longitude: 121.4737 },
    '深圳市': { name: '深圳', city: '深圳市', latitude: 22.5431, longitude: 114.0579 }
};
let smartRouteState = {
    preferences: ['传统技艺', '历史建筑'],
    tags: ['室内', '轻松', '博物馆'],
    activePreset: 'halfday',
    advancedOpen: false,
    heritageItems: [],
    currentRouteItems: [],
    detailReturnIndex: null
};

function renderSmartAdvancedSettings() {
    const panel = document.getElementById('smartAdvancedSettings');
    const button = document.querySelector('.smart-more-settings');
    if (panel) panel.hidden = !smartRouteState.advancedOpen;
    if (button) button.textContent = smartRouteState.advancedOpen ? t('hideRouteSettings') : t('moreRouteSettings');
}

function toggleSmartAdvancedSettings() {
    smartRouteState.advancedOpen = !smartRouteState.advancedOpen;
    renderSmartAdvancedSettings();
}

function renderSmartRoutePresets() {
    const container = document.getElementById('smartRoutePresets');
    if (!container) return;
    container.innerHTML = SMART_ROUTE_PRESETS.map(preset => `
        <button type="button" class="smart-preset-card ${smartRouteState.activePreset === preset.id ? 'active' : ''}" onclick="applySmartRoutePreset('${preset.id}')">
            <strong>${escapeHtml(preset.title)}</strong>
            <span>${escapeHtml(preset.desc)}</span>
        </button>
    `).join('');
}

function getSelectedOptionText(id) {
    const select = document.getElementById(id);
    return select?.selectedOptions?.[0]?.textContent?.trim() || '';
}

function getRouteStopEstimate(hours) {
    if (hours <= 2) return '2-3 站';
    if (hours <= 4) return '3-4 站';
    return '5-6 站';
}

function getSmartRouteExpectation() {
    const city = getSelectedOptionText('smartCity') || '北京';
    const hours = Number(document.getElementById('smartHours')?.value || 4);
    const pace = getSelectedOptionText('smartPace') || '轻松慢游';
    const companion = getSelectedOptionText('smartCompanion') || '';
    const focus = getSelectedOptionText('smartRouteFocus') || '自动判断';
    const themes = smartRouteState.preferences.slice(0, 2).join('、') || '文化体验';
    return {
        title: `${city} · ${getRouteStopEstimate(hours)} · ${themes}`,
        meta: [`${hours} 小时`, pace, companion, focus].filter(Boolean),
        hint: t('routeTrustHint')
    };
}

function renderSmartRouteExpectation() {
    const container = document.getElementById('smartRouteExpectation');
    if (!container) return;
    const expectation = getSmartRouteExpectation();
    container.innerHTML = `
        <div>
            <span>${t('routeExpectation')}</span>
            <strong>${escapeHtml(expectation.title)}</strong>
            <p>${t('routeExpectationHint')}</p>
        </div>
        <div class="smart-expectation-tags">
            ${expectation.meta.map(item => `<b>${escapeHtml(item)}</b>`).join('')}
        </div>
        <small>${escapeHtml(expectation.hint)}</small>
    `;
}

function renderSmartRouteChips() {
    renderSmartRoutePresets();
    renderSmartRouteExpectation();
    renderSmartAdvancedSettings();
    const unifiedContainer = document.getElementById('smartUnifiedChips');
    const preferenceContainer = document.getElementById('smartPreferenceChips');
    const tagContainer = document.getElementById('smartTagChips');
    if (unifiedContainer) {
        const preferenceChips = SMART_ROUTE_PREFERENCES.map(item => `
            <button type="button" class="smart-chip smart-chip-theme ${smartRouteState.preferences.includes(item) ? 'active' : ''}" onclick="toggleSmartRoutePreference('${item}')">${item}</button>
        `).join('');
        const tagChips = SMART_ROUTE_TAGS.map(item => `
            <button type="button" class="smart-chip smart-chip-experience ${smartRouteState.tags.includes(item) ? 'active' : ''}" onclick="toggleSmartRouteTag('${item}')">${item}</button>
        `).join('');
        unifiedContainer.innerHTML = preferenceChips + tagChips;
        return;
    }
    if (preferenceContainer) {
        preferenceContainer.innerHTML = SMART_ROUTE_PREFERENCES.map(item => `
            <button type="button" class="smart-chip ${smartRouteState.preferences.includes(item) ? 'active' : ''}" onclick="toggleSmartRoutePreference('${item}')">${item}</button>
        `).join('');
    }
    if (tagContainer) {
        tagContainer.innerHTML = SMART_ROUTE_TAGS.map(item => `
            <button type="button" class="smart-chip ${smartRouteState.tags.includes(item) ? 'active' : ''}" onclick="toggleSmartRouteTag('${item}')">${item}</button>
        `).join('');
    }
}

function toggleSmartRoutePreference(value) {
    smartRouteState.activePreset = '';
    if (smartRouteState.preferences.includes(value)) {
        smartRouteState.preferences = smartRouteState.preferences.filter(item => item !== value);
    } else {
        smartRouteState.preferences = [...smartRouteState.preferences, value];
    }
    renderSmartRouteChips();
}

function toggleSmartRouteTag(value) {
    smartRouteState.activePreset = '';
    if (smartRouteState.tags.includes(value)) {
        smartRouteState.tags = smartRouteState.tags.filter(item => item !== value);
    } else {
        smartRouteState.tags = [...smartRouteState.tags, value];
    }
    renderSmartRouteChips();
}

function setSmartSelectValue(id, value) {
    const select = document.getElementById(id);
    if (select && value !== undefined) select.value = value;
}

function applySmartRoutePreset(presetId) {
    const preset = SMART_ROUTE_PRESETS.find(item => item.id === presetId);
    if (!preset) return;
    smartRouteState.activePreset = preset.id;
    smartRouteState.preferences = [...preset.preferences];
    smartRouteState.tags = [...preset.tags];
    setSmartSelectValue('smartHours', preset.hours);
    setSmartSelectValue('smartPace', preset.pace);
    setSmartSelectValue('smartCompanion', preset.companion);
    setSmartSelectValue('smartRouteFocus', preset.focus);
    closeSmartRouteDetail();
    renderSmartRouteChips();
}

function markSmartRouteCustom() {
    if (smartRouteState.activePreset) {
        smartRouteState.activePreset = '';
        renderSmartRoutePresets();
    }
    renderSmartRouteExpectation();
}

async function tuneSmartRoute(direction) {
    smartRouteState.activePreset = '';
    const addTags = (...values) => {
        smartRouteState.tags = [...new Set([...smartRouteState.tags, ...values])];
    };
    const addPreferences = (...values) => {
        smartRouteState.preferences = [...new Set([...values, ...smartRouteState.preferences])];
    };
    if (direction === 'relaxed') {
        addTags('轻松', '少走路');
        setSmartSelectValue('smartPace', '轻松');
        setSmartSelectValue('smartRouteFocus', 'auto');
    } else if (direction === 'deeper') {
        addPreferences('传统技艺', '传统戏剧');
        addTags('深度', '手工体验', '表演');
        setSmartSelectValue('smartPace', '深度');
        setSmartSelectValue('smartRouteFocus', 'heritage');
    } else if (direction === 'heritage') {
        addPreferences('传统戏剧', '传统技艺', '传统美术');
        addTags('手工体验', '表演');
        setSmartSelectValue('smartRouteFocus', 'heritage');
    } else if (direction === 'photo') {
        addPreferences('城市漫步', '历史建筑', '节庆活动');
        addTags('适合拍照', '户外', '夜间');
        setSmartSelectValue('smartCompanion', '适合拍照');
        setSmartSelectValue('smartRouteFocus', 'attraction');
    } else if (direction === 'lessWalk') {
        addTags('少走路', '室内', '轻松');
        setSmartSelectValue('smartPace', '少走路');
        setSmartSelectValue('smartHours', '2');
    }
    closeSmartRouteDetail();
    renderSmartRouteChips();
    await generateSmartRoute();
}

async function loadHeritagePreview() {
    const container = document.getElementById('heritagePreviewList');
    if (!container) return;
    container.innerHTML = `<div class="smart-loading">${t('loading')}</div>`;
    try {
        const response = await fetchWithTimeout('/heritage-items', {}, 5000);
        const items = response.ok ? await response.json() : [];
        smartRouteState.heritageItems = items;
        renderHeritagePreview(items);
    } catch (error) {
        console.error('加载非遗数据失败:', error);
        container.innerHTML = `<div class="smart-loading">${t('serverUnavailable')}</div>`;
    }
}

async function toggleHeritageData() {
    const panel = document.getElementById('heritageDataPanel');
    const button = document.querySelector('.smart-secondary-link');
    if (!panel) return;
    const willOpen = panel.hidden;
    panel.hidden = !willOpen;
    if (button) button.textContent = willOpen ? t('hideHeritageData') : t('viewHeritageData');
    if (willOpen && smartRouteState.heritageItems.length === 0) {
        await loadHeritagePreview();
    } else if (willOpen) {
        renderHeritagePreview(smartRouteState.heritageItems);
    }
}

function handleSmartCityChange() {
    if (smartRouteState.heritageItems.length > 0) {
        renderHeritagePreview(smartRouteState.heritageItems);
    }
    closeSmartRouteDetail();
    markSmartRouteCustom();
}

function renderHeritagePreview(items) {
    const container = document.getElementById('heritagePreviewList');
    if (!container) return;
    const selectedCity = document.getElementById('smartCity')?.value || '';
    const cityItems = selectedCity
        ? (items || []).filter(item => item.city === selectedCity || item.city === SMART_CITY_LOCATIONS[selectedCity]?.city)
        : (items || []);
    const displayItems = (cityItems.length ? cityItems : (items || [])).slice(0, 8);
    container.innerHTML = displayItems.map(item => `
        <article class="heritage-preview-card">
            <img src="${escapeHtml(item.cover_image || '/assets/categories/culture.jpg')}" alt="${escapeHtml(item.name)}" onerror="this.onerror=null;this.src='/assets/categories/culture.jpg';">
            <div>
                <span>${escapeHtml(item.category)} · ${escapeHtml(item.city)}</span>
                <h3>${escapeHtml(item.name)}</h3>
                ${item.visit_action ? `<p><b>${t('whatToDo')}：</b>${escapeHtml(item.visit_action)}</p>` : ''}
                ${Array.isArray(item.experience_places) && item.experience_places.length ? `<p><b>${t('experiencePlaces')}：</b>${item.experience_places.length} 个可选地点</p>` : ''}
                <p><b>${t('heritageInheritor')}：</b>${escapeHtml(item.inheritor || '-')}</p>
                <p><b>${t('heritageActivity')}：</b>${escapeHtml(item.activity_time || '-')}</p>
                <p>${escapeHtml(item.historical_background || item.best_visit_time || '')}</p>
            </div>
        </article>
    `).join('');
}

async function openSmartRoutePage() {
    showSinglePage('smartRoutePage', { showBottomNav: false });
    setTopNavActive(2);
    renderSmartRouteChips();
    const result = document.getElementById('smartRouteResult');
    if (result && !result.innerHTML.trim()) {
        await generateSmartRoute();
    }
}

function closeSmartRoutePage() {
    showSinglePage('mainPage', { showBottomNav: true });
    setTopNavActive(0);
}

function getSmartRoutePayload() {
    const city = document.getElementById('smartCity')?.value || '北京';
    const pace = document.getElementById('smartPace')?.value || '';
    const companion = document.getElementById('smartCompanion')?.value || '';
    const tags = [...new Set([...smartRouteState.tags, pace, companion].filter(Boolean))];
    return {
        username: localStorage.getItem('username') || 'guest',
        preferences: smartRouteState.preferences,
        tags,
        available_hours: Number(document.getElementById('smartHours')?.value || 4),
        start_location: SMART_CITY_LOCATIONS[city] || SMART_CITY_LOCATIONS['北京'],
        route_focus: document.getElementById('smartRouteFocus')?.value || 'auto',
        travel_date: new Date().toISOString().slice(0, 10)
    };
}

async function generateSmartRoute() {
    const result = document.getElementById('smartRouteResult');
    if (!result) return;
    result.hidden = false;
    result.innerHTML = `<div class="smart-loading">${t('routeGenerating')}</div>`;
    try {
        const response = await fetchWithTimeout('/recommend-route', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(getSmartRoutePayload())
        }, 6000);
        const data = response.ok ? await response.json() : null;
        if (!data) {
            result.innerHTML = `<div class="smart-loading">${t('requestFailed', { detail: t('recommendedRoute') })}</div>`;
            return;
        }
        renderSmartRouteResult(data);
    } catch (error) {
        console.error('生成路线失败:', error);
        result.innerHTML = `<div class="smart-loading">${t('serverUnavailable')}</div>`;
    }
}

function renderSmartRouteResult(data) {
    const result = document.getElementById('smartRouteResult');
    if (!result) return;
    const items = Array.isArray(data.items) ? data.items : [];
    const routePlan = data.route_plan || {};
    smartRouteState.currentRouteItems = items;
    closeSmartRouteDetail();
    result.hidden = false;
    const city = document.getElementById('smartCity')?.selectedOptions?.[0]?.textContent || '';
    const resultSummary = city
        ? `${city} · ${t('routeMinutes', { minutes: data.total_duration_minutes || 0 })} · ${items.length} ${t('guidePoint')}`
        : `${t('routeMinutes', { minutes: data.total_duration_minutes || 0 })} · ${items.length} ${t('guidePoint')}`;
    const planMeta = [
        routePlan.visit_minutes ? `${t('routeVisitTime')} ${t('routeMinutes', { minutes: routePlan.visit_minutes })}` : '',
        routePlan.transfer_minutes ? `${t('routeTransferTime')} ${t('routeMinutes', { minutes: routePlan.transfer_minutes })}` : ''
    ].filter(Boolean).join(' · ');
    const mainCount = items.filter(item => item.route_line_role !== 'support').length;
    const supportCount = Math.max(0, items.length - mainCount);
    const overviewStats = [
        { label: t('routeMinutes', { minutes: data.total_duration_minutes || 0 }), value: t('routeVisitTime') },
        { label: `${items.length} ${t('guidePoint')}`, value: routePlan.feasibility || t('routeFeasibility') },
        { label: routePlan.focus_label || t('routeFocusAuto'), value: t('routeFocusLabel') }
    ];
    const overviewText = [
        mainCount ? `${mainCount} 个主线点` : '',
        supportCount ? `${supportCount} 个辅助点` : '',
        planMeta || t('routeTrustHint')
    ].filter(Boolean).join(' · ');
    result.innerHTML = `
        <div class="smart-result-head">
            <span>${t('routeResult')}</span>
            <h2>${escapeHtml(data.route_title || t('recommendedRoute'))}</h2>
            <p>${escapeHtml(resultSummary)}${routePlan.focus_label ? ` · ${escapeHtml(routePlan.focus_label)}` : ''}</p>
            <div class="smart-result-meta">
                <b>${escapeHtml(planMeta || t('routeCardHint'))}</b>
            </div>
        </div>
        <div class="smart-result-overview">
            <span>${t('routeOverviewCard')}</span>
            <div class="smart-overview-stats">
                ${overviewStats.map(stat => `
                    <div>
                        <strong>${escapeHtml(stat.label)}</strong>
                        <small>${escapeHtml(stat.value)}</small>
                    </div>
                `).join('')}
            </div>
            <p>${escapeHtml(overviewText)}</p>
            <small>${t('routeTrustHint')}</small>
        </div>
        <div class="smart-tune-panel">
            <span>${t('routeTuneTitle')}</span>
            <div>
                <button type="button" onclick="tuneSmartRoute('relaxed')">${t('routeTuneRelaxed')}</button>
                <button type="button" onclick="tuneSmartRoute('deeper')">${t('routeTuneDeeper')}</button>
                <button type="button" onclick="tuneSmartRoute('heritage')">${t('routeTuneHeritage')}</button>
                <button type="button" onclick="tuneSmartRoute('photo')">${t('routeTunePhoto')}</button>
                <button type="button" onclick="tuneSmartRoute('lessWalk')">${t('routeTuneLessWalk')}</button>
            </div>
        </div>
        <div class="smart-route-card-list">
            ${items.map((item, index) => renderSmartRouteItem(item, index)).join('')}
        </div>
    `;
}

function compactSmartRouteText(text, maxLength = 58) {
    const normalized = String(text || '').replace(/\s+/g, ' ').trim();
    if (!normalized) return '';
    const sentence = normalized.split(/[。！？.!?]/)[0];
    const brief = sentence && sentence.length >= 12 ? sentence : normalized;
    return brief.length > maxLength ? `${brief.slice(0, maxLength)}...` : brief;
}

function renderSmartRouteItem(item, index) {
    const isGuide = item.type === 'guide_post';
    const title = item.title || item.name || t('recommendedRoute');
    const roleLabel = item.route_line_role === 'support' ? t('routeSupportStop') : t('routeMainStop');
    const action = compactSmartRouteText(item.visit_action || item.description || '');
    return `
        <article class="smart-route-item" data-route-index="${index}" role="button" tabindex="0" onclick="openSmartRouteDetail(${index})" onkeydown="if(event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openSmartRouteDetail(${index}); }">
            <div class="smart-route-index">${index + 1}</div>
            <img src="${escapeHtml(item.cover_image || '/assets/categories/culture.jpg')}" alt="${escapeHtml(title)}" onerror="this.onerror=null;this.src='/assets/categories/culture.jpg';">
            <div class="smart-route-body">
                <div class="smart-route-title-row">
                    <span>${escapeHtml(roleLabel)} · ${escapeHtml(item.category || (isGuide ? t('cityGuide') : ''))}</span>
                    <strong>${t('routeMinutes', { minutes: item.estimated_minutes || 60 })}</strong>
                </div>
                <h3>${escapeHtml(title)}</h3>
                ${action ? `<p class="smart-action-line">${escapeHtml(action)}</p>` : ''}
                <p>${escapeHtml(item.location_name || item.city || '')}</p>
                <div class="smart-item-footer">
                    <span>${t('viewRouteDetail')}</span>
                </div>
            </div>
        </article>
    `;
}

function openSmartRouteDetail(index) {
    const item = smartRouteState.currentRouteItems[index];
    const detail = document.getElementById('smartRouteDetail');
    if (!item || !detail) return;
    smartRouteState.detailReturnIndex = index;
    const isGuide = item.type === 'guide_post';
    const title = item.title || item.name || t('recommendedRoute');
    const tags = Array.isArray(item.tags) ? item.tags : [];
    const action = item.visit_action || item.description || '';
    const description = item.description || item.inheritor_intro || item.historical_background || '';
    const otherPlaces = Array.isArray(item.other_experience_places) ? item.other_experience_places : [];
    const placeList = otherPlaces.length ? `
        <div class="smart-detail-list">
            <p><b>${t('moreExperiencePlaces')}</b></p>
            ${otherPlaces.slice(0, 6).map(place => `
                <p>${escapeHtml(place.name || '')}${place.best_time ? ` · ${escapeHtml(place.best_time)}` : ''}${place.experience ? `：${escapeHtml(place.experience)}` : ''}</p>
            `).join('')}
        </div>
    ` : '';
    const guideAction = isGuide && item.id
        ? `<button type="button" onclick="openPostDetail(${Number(item.id)})">${t('openGuide')}</button>`
        : '';
    const mapAction = item.navigation_url
        ? `<button type="button" onclick="window.open('${escapeHtml(item.navigation_url)}', '_blank', 'noopener')">${t('routeOpenMap')}</button>`
        : '';
    const coverImage = item.cover_image || '/assets/categories/culture.jpg';
    detail.hidden = false;
    detail.innerHTML = `
        <div class="smart-detail-card">
            <button class="smart-detail-close" type="button" onclick="closeSmartRouteDetail({ restore: true })">${t('closeDetail')}</button>
            <button class="smart-detail-image-button" type="button" onclick="openImageViewerFromElement(this)" data-image-src="${escapeHtml(coverImage)}" data-image-alt="${escapeHtml(title)}" aria-label="${escapeHtml(title)}">
                <img src="${escapeHtml(coverImage)}" alt="${escapeHtml(title)}" onerror="this.onerror=null;this.src='/assets/categories/culture.jpg';this.closest('button').dataset.imageSrc='/assets/categories/culture.jpg';">
            </button>
            <div class="smart-detail-body">
                <span>${escapeHtml(item.category || (isGuide ? t('cityGuide') : ''))}</span>
                <h2>${escapeHtml(title)}</h2>
                ${action ? `<p class="smart-action-line"><b>${t('whatToDo')}：</b>${escapeHtml(action)}</p>` : ''}
                ${description && description !== action ? `<p>${escapeHtml(description)}</p>` : ''}
                <div class="smart-detail-list">
                    <p><b>${t('routeMinutes', { minutes: item.estimated_minutes || 60 })}</b></p>
                    <p>${escapeHtml(item.location_name || item.city || '')}</p>
                    ${item.from_name ? `<p><b>${t('routeArrival')}：</b>${escapeHtml(item.from_name)} → ${escapeHtml(title)}，${escapeHtml(item.distance_from_previous_label || '')}。${escapeHtml(item.arrival_guidance || '')}</p>` : ''}
                    ${item.next_stop_hint ? `<p><b>${t('routeNextStop')}：</b>${escapeHtml(item.next_stop_hint)}</p>` : ''}
                    ${item.reason ? `<p><b>${t('routeReason')}：</b>${escapeHtml(item.reason)}</p>` : ''}
                    ${item.inheritor ? `<p><b>${t('heritageInheritor')}：</b>${escapeHtml(item.inheritor)}</p>` : ''}
                    ${item.activity_time ? `<p><b>${t('heritageActivity')}：</b>${escapeHtml(item.activity_time)}</p>` : ''}
                    ${item.historical_background ? `<p><b>${t('heritageHistory')}：</b>${escapeHtml(item.historical_background)}</p>` : ''}
                </div>
                ${placeList}
                <div class="smart-tag-row">${tags.map(tag => `<span>${escapeHtml(tag)}</span>`).join('')}</div>
                ${mapAction}
                ${guideAction}
            </div>
        </div>
    `;
    detail.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function scrollToSmartRouteCard(index) {
    if (!Number.isFinite(Number(index))) return;
    const card = document.querySelector(`.smart-route-item[data-route-index="${Number(index)}"]`);
    if (!card) return;
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    card.classList.add('smart-route-return-highlight');
    setTimeout(() => card.classList.remove('smart-route-return-highlight'), 900);
}

function closeSmartRouteDetail(options = {}) {
    const detail = document.getElementById('smartRouteDetail');
    if (!detail) return;
    const returnIndex = smartRouteState.detailReturnIndex;
    detail.hidden = true;
    detail.innerHTML = '';
    smartRouteState.detailReturnIndex = null;
    if (options.restore) {
        requestAnimationFrame(() => scrollToSmartRouteCard(returnIndex));
    }
}

function ensureImageViewer() {
    let viewer = document.getElementById('imageViewerOverlay');
    if (viewer) return viewer;
    viewer = document.createElement('div');
    viewer.id = 'imageViewerOverlay';
    viewer.className = 'image-viewer-overlay';
    viewer.hidden = true;
    viewer.innerHTML = `
        <button class="image-viewer-close" type="button" onclick="closeImageViewer()">${t('closeDetail')}</button>
        <img class="image-viewer-img" src="" alt="">
    `;
    viewer.addEventListener('click', (event) => {
        if (event.target === viewer) closeImageViewer();
    });
    document.body.appendChild(viewer);
    return viewer;
}

function openImageViewer(src, alt = '') {
    if (!src) return;
    const viewer = ensureImageViewer();
    const image = viewer.querySelector('.image-viewer-img');
    if (!image) return;
    image.src = src;
    image.alt = alt || t('guideImage');
    viewer.hidden = false;
    document.body.classList.add('image-viewer-open');
}

function openImageViewerFromElement(element) {
    if (!element) return;
    const src = element.dataset?.imageSrc || element.currentSrc || element.src;
    const alt = element.dataset?.imageAlt || element.alt || '';
    openImageViewer(src, alt);
}

function closeImageViewer() {
    const viewer = document.getElementById('imageViewerOverlay');
    if (!viewer) return;
    viewer.hidden = true;
    const image = viewer.querySelector('.image-viewer-img');
    if (image) image.removeAttribute('src');
    document.body.classList.remove('image-viewer-open');
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeImageViewer();
});

Object.assign(window, {
    smartRouteState,
    renderHeritagePreview,
    toggleHeritageData,
    handleSmartCityChange,
    toggleSmartRoutePreference,
    toggleSmartRouteTag,
    toggleSmartAdvancedSettings,
    applySmartRoutePreset,
    markSmartRouteCustom,
    tuneSmartRoute,
    openSmartRoutePage,
    closeSmartRoutePage,
    generateSmartRoute,
    openSmartRouteDetail,
    closeSmartRouteDetail,
    openImageViewer,
    openImageViewerFromElement,
    closeImageViewer
});

function commonsFile(fileName, width = 1200) {
    return `https://commons.wikimedia.org/wiki/Special:Redirect/file/${encodeURIComponent(fileName)}?width=${width}`;
}

const EXPERIENCE_SPOTS = [
    {
        id: 'dongjiaominxiang',
        title: '东交民巷',
        kicker: '北京老城里的西洋街影',
        subtitle: '不急着赶路，沿着树影、砖墙和旧使馆建筑慢慢走，把北京最特殊的一段近代城市记忆看进细节里。',
        cover: commonsFile('15 Dongjiaomin Alley (Former French Embassy in China) 20240527.jpg', 1400),
        cardImage: commonsFile('15 Dongjiaomin Alley.jpeg', 900),
        liteVrImage: '/assets/guides/beijing/dongjiaominxiang/vr-panorama-generated.png',
        sphereImage: '/assets/guides/beijing/dongjiaominxiang/vr-panorama-generated.png',
        meta: [
            { label: '建议时长', value: '60-90 分钟' },
            { label: '最佳时间', value: '工作日上午 / 傍晚' },
            { label: '适合人群', value: '建筑爱好者、欧美游客、City walk' },
            { label: '体验方式', value: '慢走、看立面、读街道气质' }
        ],
        intro: [
            '东交民巷不是那种一眼就把情绪推到最高点的景点。它更像北京城里一段安静的夹层：一边是天安门和前门的宏大叙事，一边是胡同、教堂、旧使馆与近代金融建筑留下的细部。',
            '这里最值得体验的不是“打卡到了”，而是把步速放慢。你会发现北京并不只有红墙、琉璃瓦和中轴线，也有拱窗、山花、砖墙、院门和近代城市秩序留下的痕迹。'
        ],
        story: [
            {
                title: '第一眼：它不像传统想象里的北京',
                image: '/assets/guides/beijing/dongjiaominxiang/street-first-impression.png',
                text: '进入东交民巷时，最先感受到的是比例变化。街道不算宽，树荫压低了天空，建筑立面贴近行人，拱形窗、灰砖墙和院墙让这里有一种“边走边读”的节奏。它不像故宫那样要求仰望，也不像商业街那样推着你消费，而是让你把目光停在门楣、窗框和墙面的纹理上。'
            },
            {
                title: '建筑细节：近代北京的另一种表情',
                image: '/assets/guides/beijing/dongjiaominxiang/architecture-details.png',
                text: '东交民巷的魅力在于混合感。西式立面、老树、北京街巷尺度被压在同一条街里，形成一种不太喧哗的异质感。看这些建筑时，不必急着背年代，更适合观察它们怎样面对街道：有的退到院墙后，有的用立面和拱窗直接回应行人视线。'
            },
            {
                title: '圣弥厄尔教堂：街巷里的垂直瞬间',
                image: commonsFile('Dongjiaominxiang Cathedral 20160825.jpg', 1200),
                text: '走到圣弥厄尔教堂附近，街道突然有了一个向上的焦点。尖顶、立面和街边树影叠在一起，让这段路从“看建筑”变成“感受空间”。如果天气好，可以站远一点看它和街道的关系；如果傍晚来，光线会让墙面层次更柔和。'
            },
            {
                title: '真正的体验：把声音和速度降下来',
                image: '/assets/guides/beijing/dongjiaominxiang/street-scale.png',
                text: '东交民巷适合慢游。不要只盯着单个建筑名，也不要把它走成路线任务。更好的方式是每隔几十米停一次：听车辆和脚步声怎样被树荫吸掉，看旧址铭牌如何把宏大历史缩成一块石碑，再回头看看刚刚经过的街道，感受北京老城里少见的近代层次。'
            }
        ],
        liteHotspots: [
            { x: 18, y: 56, title: '街巷入口', dossierId: 'street-scale', text: '从街道尺度进入东交民巷，先看树影、路面和两侧建筑之间的距离。' },
            { x: 50, y: 46, title: '近代立面', dossierId: 'legation-facade', text: '把视线停在窗框、墙面和院门上，读出这条街区别于传统北京景点的近代气质。' },
            { x: 82, y: 58, title: '慢行方向', dossierId: 'quiet-walk', text: '顺着街巷继续向前，边走边停比固定在一个门口拍照更接近真实游览。' }
        ],
        vrCaption: '全景预览：拖动画面模拟沿东交民巷慢慢转头观察，重点是街巷空间、树影和近代建筑立面。',
        vrInstructions: {
            lite: '拖动画面转头，点击编号会切换中文讲解。第一档不是普通图片，而是把街心、立面、慢行方向拆成可阅读的观察点。',
            sphere: '第二档会进入 360 环视：拖动转身，滚轮或按钮缩放。建议先看树冠压下来的街道尺度，再把视线落到灰砖和拱窗。'
        },
        timeTravel: {
            beforeLabel: '约 1900s',
            afterLabel: '现在',
            title: '把东交民巷切成两层时间',
            beforeImage: commonsFile('Peking. Legation quarter, British, Russian (on left), Japanese (on right) LCCN2006689697.jpg', 1200),
            beforeText: '曾经的使馆区、银行、教堂和近代机构，让这条街不只是通行道路，而是一段被国际关系、城市建设和近代制度反复书写过的北京街区。',
            afterText: '今天走在这里，喧闹已经退到远处。留下来的不是戏剧化的废墟，而是院墙、树影、铭牌和建筑立面共同组成的低声叙事。',
            detail: '拖动滑块，从旧日使馆区的街面、院墙和建筑轮廓，过渡到今天树影下的东交民巷，感受同一片街区在不同时代里的空间气质。'
        },
        dossiers: [
            {
                id: 'street-scale',
                title: '街道尺度',
                tag: '入口感',
                text: '东交民巷高级的地方不在“大”，而在比例：建筑、树、院墙和行人都保持在可以被近距离阅读的尺度里。',
                focus: '先看街宽和树冠，再看两侧建筑离人的距离。'
            },
            {
                id: 'legation-facade',
                title: '旧使馆立面',
                tag: '近代建筑',
                text: '拱窗、砖墙、山花、柱式和院门让这里从传统胡同语汇里偏移出来。游客不需要背建筑史，也能感到它的“不像北京”。',
                focus: '找窗框、砖缝、门楣和墙面的时间痕迹。'
            },
            {
                id: 'church-vertical',
                title: '圣弥厄尔教堂',
                tag: '垂直焦点',
                text: '教堂让街巷出现向上的视线。它不是孤立打卡点，而是把整条街的空间节奏突然抬高的一瞬。',
                focus: '站远一点，看尖顶和树影如何一起进入画面。'
            },
            {
                id: 'quiet-walk',
                title: '慢行节奏',
                tag: 'City walk',
                text: '这条街最怕被走成任务清单。真正的体验来自停顿：停在铭牌前、转身回看、听脚步声从树下穿过去。',
                focus: '每 80 米停一次，比一路拍过去更有记忆。'
            }
        ],
        walkRhythm: [
            { time: '0-10 min', title: '降速进入', text: '先不要拍照，观察街道比例和树荫，让身体先适应这里的安静。' },
            { time: '10-35 min', title: '看建筑表情', text: '挑三处立面细看：门、窗、墙。每一处都比完整大景更容易留下记忆。' },
            { time: '35-55 min', title: '寻找垂直焦点', text: '走到教堂或开阔处，把视线从街面抬到屋顶线，体验空间突然变高。' },
            { time: '55-90 min', title: '回头再走一遍', text: '换方向慢走一次，刚才没注意的铭牌、院门和树影会重新出现。' }
        ],
        stamp: {
            title: '东交民巷体验完成',
            text: '你不是“经过”了这条街，而是读完了一段北京老城里少见的近代层次。',
            code: '东交民巷 · 北京近代街影'
        },
        practical: [
            { title: '从哪里开始', text: '建议从台基厂大街或正义路一侧进入，沿街慢慢向东或向西走，最后顺到前门、王府井或天安门周边。' },
            { title: '怎么拍更有感觉', text: '少拍大合影，多拍立面、树影、门牌和窗框。傍晚斜光会让墙面更有层次，雨后则更适合拍砖墙和路面反光。' },
            { title: '和普通游客怎么不同', text: '不要把这里当成“顺路经过”的点。给它至少一小时，把它当作一条可以读的街，而不是一个需要证明自己来过的地名。' }
        ]
    }
];

const GUIDE_AUTHORS = [
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
];

function isGuidePost(post) {
    return post?.post_type === 'guide' || (
        GUIDE_AUTHORS.includes(post?.author) &&
        Array.isArray(post?.guide_items) &&
        post.guide_items.length > 0
    );
}

function stableHash(value) {
    const text = String(value || '');
    let hash = 2166136261;
    for (let i = 0; i < text.length; i += 1) {
        hash ^= text.charCodeAt(i);
        hash = Math.imul(hash, 16777619);
    }
    return hash >>> 0;
}

function getGuideDisplayPublishTime(post) {
    if (!isGuidePost(post)) return post?.publish_time || '';
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 1, 9, 0, 0);
    const spanMs = Math.max(1, now.getTime() - start.getTime());
    const seed = stableHash(`${post?.id || ''}|${post?.title || ''}|${post?.author || ''}`);
    const offset = Math.floor((seed / 0xFFFFFFFF) * spanMs);
    const hourOffset = (seed % 10) * 60 * 60 * 1000;
    const minuteOffset = ((seed >> 5) % 60) * 60 * 1000;
    const published = new Date(start.getTime() + offset - hourOffset + minuteOffset);
    if (published > now) return now.toISOString();
    if (published < start) return start.toISOString();
    return published.toISOString();
}

function withGuideDisplayPublishTime(post) {
    if (!post || !isGuidePost(post)) return post;
    return {
        ...post,
        publish_time: getGuideDisplayPublishTime(post)
    };
}

function normalizeGuideDisplayPublishTimes(posts) {
    return (posts || []).map(withGuideDisplayPublishTime);
}

function capturePageState() {
    const pages = {};
    navigationPageIds.forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        pages[id] = {
            display: el.style.display || getComputedStyle(el).display,
            opacity: el.style.opacity || '',
            scrollTop: el.scrollTop || 0,
            active: el.classList.contains('active')
        };
    });

    const bottomNav = document.getElementById('bottomNav');
    const activeTopNav = Array.from(document.querySelectorAll('.nav-tabs button')).findIndex(tab => tab.classList.contains('active'));
    return {
        pages,
        activeTopNav,
        bottomNav: bottomNav ? {
            display: bottomNav.style.display || getComputedStyle(bottomNav).display,
            transform: bottomNav.style.transform || ''
        } : null
    };
}

function restorePageState(state) {
    if (!state) return false;

    navigationPageIds.forEach(id => {
        const el = document.getElementById(id);
        const saved = state.pages[id];
        if (!el || !saved) return;
        el.style.display = saved.display;
        el.style.opacity = saved.opacity;
        el.classList.toggle('active', Boolean(saved.active));
        el.scrollTop = saved.scrollTop || 0;
        requestAnimationFrame(() => {
            el.scrollTop = saved.scrollTop || 0;
        });
    });

    const bottomNav = document.getElementById('bottomNav');
    if (bottomNav && state.bottomNav) {
        bottomNav.style.display = state.bottomNav.display;
        bottomNav.style.transform = state.bottomNav.transform;
    }

    if (Number.isInteger(state.activeTopNav) && state.activeTopNav >= 0) {
        setTopNavActive(state.activeTopNav);
    }

    return true;
}

function clearTransientOverlays() {
    ['locationPickerOverlay', 'locationPicker', 'mapSelectorOverlay', 'mapSelector', 'searchResults'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.classList.remove('active');
    });
}

function fetchWithTimeout(url, options = {}, timeoutMs = 3500) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);

    return fetch(url, {
        ...options,
        signal: controller.signal
    }).finally(() => clearTimeout(timer));
}

function hideNavigationPages() {
    navigationPageIds.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });
    document.getElementById('chatPage')?.classList.remove('active');
}

function setTopNavActive(index) {
    const tabs = document.querySelectorAll('.nav-tabs button');
    tabs.forEach(tab => tab.classList.remove('active'));
    if (tabs[index]) tabs[index].classList.add('active');
}

function showSinglePage(pageId, options = {}) {
    clearTransientOverlays();
    hideNavigationPages();
    const page = document.getElementById(pageId);
    if (page) {
        page.style.display = options.display || 'block';
        page.scrollTop = 0;
        requestAnimationFrame(() => {
            page.scrollTop = 0;
        });
    }

    const bottomNav = document.getElementById('bottomNav');
    if (bottomNav) {
        bottomNav.style.display = options.showBottomNav ? 'block' : 'none';
        bottomNav.style.transform = options.showBottomNav ? 'translateY(0)' : 'translateY(150%)';
    }

    const mainPage = document.getElementById('mainPage');
    const discoverPage = document.getElementById('discoverPage');
    if (mainPage) mainPage.style.opacity = '1';
    if (discoverPage) discoverPage.style.opacity = '1';
}

function getVisibleNavigationPageId() {
    return navigationPageIds.find(id => {
        const el = document.getElementById(id);
        return el && getComputedStyle(el).display !== 'none';
    }) || 'mainPage';
}

function openDetailPage() {
    ensureDetailFloatingLayers();
    if (!document.getElementById('detailPage').classList.contains('active')) {
        detailReturnState = capturePageState();
    }
    document.getElementById('detailPage').classList.add('active');
    document.getElementById('mainPage').style.opacity = '0.3';
    document.getElementById('discoverPage').style.opacity = '0.3';
    document.getElementById('bottomNav').style.transform = 'translateY(150%)'; 
}

function closeDetailPage() {
    document.getElementById('detailPage').classList.remove('active');
    closeGuideDetail();
    stopGuideAudio();
    if (!restorePageState(detailReturnState)) {
        showSinglePage('mainPage', { showBottomNav: true });
        setTopNavActive(0);
    }
    detailReturnState = null;
}

let isLoginMode = true; 
let selectedAvatar = null;
let pendingPublishAfterAuth = false;
let pendingAuthAction = null;

function avatarHtml(avatarJson, username, className, id = '') {
    const idAttr = id ? ` id="${id}"` : '';
    const fallback = `https://picsum.photos/100/100?random=${encodeURIComponent(username || 'user')}`;

    if (!avatarJson) {
        return `<img${idAttr} src="${fallback}" alt="${username || 'avatar'}" class="${className}">`;
    }

    try {
        const avatarData = typeof avatarJson === 'string' ? JSON.parse(avatarJson) : avatarJson;

        if (avatarData.type === 'preset') {
            return `<div${idAttr} class="${className} emoji-avatar">${avatarData.emoji}</div>`;
        }

        if (avatarData.data) {
            return `<img${idAttr} src="${avatarData.data}" alt="${username || 'avatar'}" class="${className}">`;
        }
    } catch (e) {
        console.error('头像解析失败:', e);
    }

    return `<img${idAttr} src="${fallback}" alt="${username || 'avatar'}" class="${className}">`;
}

// 页面加载完成后绑定事件
document.addEventListener('DOMContentLoaded', function() {
    applyLanguage();
    showLanguageGateIfNeeded();
    renderExperienceFeatures();

    const avatarFileInput = document.getElementById('avatarFile');
    if (avatarFileInput) {
        // 移除旧的事件监听，避免重复绑定
        avatarFileInput.removeEventListener('change', handleAvatarUpload);
        // 添加事件监听
        avatarFileInput.addEventListener('change', handleAvatarUpload);
        console.log('Avatar file input event listener bound');
    } else {
        console.error('avatarFile input element not found');
    }
}); 

// 头像裁剪相关变量
let cropImage = null;
let cropCanvas = null;
let ctx = null;
let scale = 1;
let minCropScale = 1;
let offsetX = 0;
let offsetY = 0;
let isDragging = false;
let lastX = 0;
let lastY = 0;

// 预选头像列表（QQ风格）- 使用中文名称
const presetAvatars = [
    { id: 1, emoji: '👨‍💼', name: '商务人士' },
    { id: 2, emoji: '👩‍🎨', name: '艺术家' },
    { id: 3, emoji: '🧑‍✈️', name: '飞行员' },
    { id: 4, emoji: '👨‍⚕️', name: '医生' },
    { id: 5, emoji: '👩‍🏫', name: '老师' },
    { id: 6, emoji: '🧑‍🔧', name: '工程师' },
    { id: 7, emoji: '👨‍🚀', name: '宇航员' },
    { id: 8, emoji: '👩‍🔬', name: '科学家' },
    { id: 9, emoji: '👨‍🍳', name: '厨师' },
    { id: 10, emoji: '👩‍🎤', name: '歌手' },
];

function openAuthModal() {
    document.getElementById('authModal').classList.add('active');
}

function closeAuthModal() {
    document.getElementById('authModal').classList.remove('active');
    pendingPublishAfterAuth = false;
    pendingAuthAction = null;
}

function toggleAuthMode(refreshOnly = false) {
    if (!refreshOnly) {
        isLoginMode = !isLoginMode;
    }
    const title = document.getElementById('authTitle');
    const submitBtn = document.getElementById('submitBtn');
    const switchText = document.getElementById('switchText');
    const switchLink = document.querySelector('.auth-switch a');

    // 清空账号密码输入框
    if (!refreshOnly) {
        document.getElementById('usernameInput').value = '';
        document.getElementById('passwordInput').value = '';
    }

    if (isLoginMode) {
        title.innerText = t('authWelcome');
        submitBtn.innerText = t('login');
        switchText.innerText = t('noAccount');
        switchLink.innerText = t('signUp');
    } else {
        title.innerText = t('authCreate');
        submitBtn.innerText = t('register');
        switchText.innerText = t('haveAccount');
        switchLink.innerText = t('signIn');
    }
}

// ==================== 头像选择功能 ====================
function openAvatarSelector() {
    document.getElementById('avatarModal').classList.add('active');
    renderPresetAvatars();
}

function closeAvatarSelector() {
    document.getElementById('avatarModal').classList.remove('active');
}

function renderPresetAvatars() {
    const container = document.getElementById('presetAvatars');
    container.innerHTML = '';
    
    presetAvatars.forEach(avatar => {
        const avatarItem = document.createElement('div');
        avatarItem.className = 'avatar-item';
        avatarItem.innerHTML = `
            <div class="avatar-emoji">${avatar.emoji}</div>
            <span class="avatar-name">${avatar.name}</span>
        `;
        avatarItem.onclick = () => selectPresetAvatar(avatar);
        container.appendChild(avatarItem);
    });
}

function selectPresetAvatar(avatar) {
    selectedAvatar = { type: 'preset', emoji: avatar.emoji, name: avatar.name };
    updateAvatarPreview(avatar.emoji);
    
    // 保存到本地存储
    localStorage.setItem('avatar', JSON.stringify(selectedAvatar));
    
    // 更新服务器（如果已登录）
    updateAvatarOnServer(selectedAvatar);
    
    // 同步到个人中心
    syncProfileAvatar();
    
    closeAvatarSelector();
}

function triggerFileInput() {
    const fileInput = document.getElementById('avatarFile');
    if (!fileInput) {
        alert('头像上传控件未找到，请刷新页面后重试');
        return;
    }
    // 重置文件输入，允许再次选择同一文件
    fileInput.value = '';
    fileInput.click();
}

function handleAvatarUpload(event) {
    console.log('handleAvatarUpload called');
    const file = event.target.files[0];
    console.log('Selected file:', file);
    if (file) {
        // 检查文件类型
        if (!file.type.startsWith('image/')) {
            alert('请选择图片文件');
            return;
        }
        
        // 检查文件大小（限制为5MB）
        if (file.size > 5 * 1024 * 1024) {
            alert('图片大小不能超过5MB');
            return;
        }
        
        const reader = new FileReader();
        reader.onload = function(e) {
            console.log('File read successfully, opening crop modal');
            // 打开裁剪界面
            openCropModal(e.target.result);
        };
        reader.onerror = function() {
            console.error('File read error');
            alert('图片读取失败，请重试');
        };
        reader.readAsDataURL(file);
    } else {
        console.log('未选择文件');
    }
}

function updateAvatarPreview(src) {
    const preview = document.getElementById('avatarPreview');
    if (typeof src === 'string' && src.includes('data:image')) {
        preview.innerHTML = `<img src="${src}" alt="User Avatar" class="default-avatar">`;
    } else {
        preview.innerHTML = `<div class="avatar-emoji-preview">${src}</div>`;
    }
}

// ==================== 头像裁剪功能 ====================
function openCropModal(imageSrc) {
    closeAvatarSelector();
    
    const modal = document.getElementById('cropModal');
    if (modal.parentElement !== document.body) {
        document.body.appendChild(modal);
    }
    modal.classList.add('active');
    
    cropImage = new Image();
    cropImage.onload = function() {
        initCrop();
    };
    cropImage.src = imageSrc;
    
    cropCanvas = document.getElementById('cropCanvas');
    ctx = cropCanvas.getContext('2d');
}

function closeCropModal() {
    const modal = document.getElementById('cropModal');
    modal.classList.remove('active');
    cropImage = null;
    scale = 1;
    minCropScale = 1;
    offsetX = 0;
    offsetY = 0;
    isDragging = false;
}

function initCrop() {
    const container = document.getElementById('cropContainer');
    const frame = document.getElementById('cropFrame');
    const frameSize = Math.min(container.clientWidth - 40, container.clientHeight - 40, 250);
    
    cropCanvas.width = container.clientWidth;
    cropCanvas.height = container.clientHeight;
    frame.style.width = frameSize + 'px';
    frame.style.height = frameSize + 'px';
    frame.style.left = (container.clientWidth - frameSize) / 2 + 'px';
    frame.style.top = (container.clientHeight - frameSize) / 2 + 'px';
    
    const scaleX = frameSize / cropImage.width;
    const scaleY = frameSize / cropImage.height;
    minCropScale = Math.max(scaleX, scaleY);
    scale = minCropScale;
    
    // 居中显示（确保裁剪框内显示图片中心部分）
    offsetX = (cropCanvas.width - cropImage.width * scale) / 2;
    offsetY = (cropCanvas.height - cropImage.height * scale) / 2;
    
    updateZoomDisplay();
    drawCrop();
}

function drawCrop() {
    if (!cropImage || !ctx) return;
    
    ctx.clearRect(0, 0, cropCanvas.width, cropCanvas.height);
    ctx.drawImage(cropImage, offsetX, offsetY, cropImage.width * scale, cropImage.height * scale);
}

function zoomIn() {
    if (scale < 3) {
        scale += 0.2;
        updateZoomDisplay();
        drawCrop();
    }
}

function zoomOut() {
    if (!cropImage) return;
    
    if (scale > minCropScale) {
        scale = Math.max(minCropScale, scale - 0.2);
        updateZoomDisplay();
        drawCrop();
    }
}

function updateZoomDisplay() {
    document.getElementById('zoomLevel').textContent = Math.round(scale * 100) + '%';
}

function confirmCrop() {
    const frame = document.getElementById('cropFrame');
    const frameRect = frame.getBoundingClientRect();
    const containerRect = document.getElementById('cropContainer').getBoundingClientRect();
    
    // 计算裁剪区域在图片上的位置
    const cropX = (frameRect.left - containerRect.left - offsetX) / scale;
    const cropY = (frameRect.top - containerRect.top - offsetY) / scale;
    const cropSize = frameRect.width / scale;
    
    // 创建新画布进行裁剪
    const outputCanvas = document.createElement('canvas');
    outputCanvas.width = 200;
    outputCanvas.height = 200;
    const outputCtx = outputCanvas.getContext('2d');
    
    outputCtx.drawImage(
        cropImage,
        cropX, cropY, cropSize, cropSize,
        0, 0, 200, 200
    );
    
    // 获取裁剪后的图片数据
    const croppedImage = outputCanvas.toDataURL('image/png');
    
    // 设置为选中的头像
    selectedAvatar = { type: 'custom', data: croppedImage };
    updateAvatarPreview(croppedImage);
    
    // 保存到本地存储
    localStorage.setItem('avatar', JSON.stringify(selectedAvatar));
    
    // 更新服务器（如果已登录）
    updateAvatarOnServer(selectedAvatar);
    
    // 同步到个人中心
    syncProfileAvatar();
    
    closeCropModal();
}

// ==================== 添加拖拽功能 - 修复拖拽逻辑 ==================== 
 function startDrag(e) { 
     isDragging = true; 
     const point = getEventPoint(e); 
     lastX = point.x; 
     lastY = point.y; 
 } 
 
 function onDrag(e) { 
     if (!isDragging || !cropImage || !cropCanvas) return; 
     e.preventDefault(); 
     
     const point = getEventPoint(e); 
     const deltaX = point.x - lastX; 
     const deltaY = point.y - lastY; 
     
     // 计算新的偏移量 - 无边界限制，可以随意移动 
     let newOffsetX = offsetX + deltaX; 
     let newOffsetY = offsetY + deltaY; 
     
     // 更新偏移量 
     offsetX = newOffsetX; 
     offsetY = newOffsetY; 
     
     // 更新最后一次的鼠标/触摸位置 
     lastX = point.x; 
     lastY = point.y; 
     
     // 重新绘制图片 
     drawCrop(); 
 } 
 
 function stopDrag() { 
     isDragging = false; 
 } 
 
 function getEventPoint(e) { 
     if (e.touches && e.touches.length > 0) { 
         return { x: e.touches[0].clientX, y: e.touches[0].clientY }; 
     } 
     return { x: e.clientX, y: e.clientY }; 
 }

// 初始化拖拽事件监听
function initCropEvents() {
    const container = document.getElementById('cropContainer');
    
    // 移除旧事件（避免重复绑定）
    container.removeEventListener('mousedown', startDrag);
    container.removeEventListener('touchstart', startDrag);
    
    // 鼠标事件
    container.addEventListener('mousedown', startDrag);
    
    // 使用容器级别的移动和释放事件，避免拖拽时鼠标离开容器就停止
    container.addEventListener('mousemove', function(e) {
        if (isDragging) {
            onDrag(e);
        }
    });
    
    container.addEventListener('mouseup', stopDrag);
    container.addEventListener('mouseleave', stopDrag);
    
    // 触摸事件
    container.addEventListener('touchstart', startDrag);
    
    container.addEventListener('touchmove', function(e) {
        if (isDragging) {
            onDrag(e);
        }
    });
    
    container.addEventListener('touchend', stopDrag);
}

// 页面加载完成后初始化事件
document.addEventListener('DOMContentLoaded', function() {
    initCropEvents();
    console.log('DOM加载完成，开始加载帖子...');
    loadMyPosts().catch(err => {
        console.error('加载帖子时发生错误:', err);
    });
});

// ==================== 登录/注册请求 ====================
async function handleAuth(event) {
    event.preventDefault();

    const usernameInput = document.getElementById('usernameInput').value;
    const passwordInput = document.getElementById('passwordInput').value;

    const endpoint = isLoginMode ? '/login' : '/register';

    const requestData = {
        username: usernameInput,
        password: passwordInput
    };

    // 将头像数据转换为 JSON 字符串发送给后端
    if (selectedAvatar) {
        requestData.avatar = JSON.stringify(selectedAvatar);
    }

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);
            
            // 注册和登录都设置登录状态
            localStorage.setItem('username', data.username);
            localStorage.setItem('isLoggedIn', 'true');
            
            // 如果后端返回了头像，使用后端的头像
            if (data.avatar) {
                const avatarData = JSON.parse(data.avatar);
                localStorage.setItem('avatar', data.avatar);
                updateAvatarPreview(avatarData.type === 'preset' ? avatarData.emoji : avatarData.data);
            } else if (selectedAvatar) {
                // 如果没有后端头像但有选中的头像，保存到本地并更新后端
                localStorage.setItem('avatar', JSON.stringify(selectedAvatar));
                updateAvatarOnServer(selectedAvatar);
            }
            
            const shouldOpenPublish = pendingPublishAfterAuth;
            const actionAfterAuth = pendingAuthAction;
            
            // 登录/注册成功后关闭弹窗，停留在当前页面或继续之前的发布动作
            closeAuthModal();
            if (actionAfterAuth) {
                actionAfterAuth();
            } else if (shouldOpenPublish) {
                openPublishPage();
            }
        } else {
            alert(t('requestFailed', { detail: data.detail }));
        }
    } catch (error) {
        alert(t('serverUnavailable'));
        console.error("请求报错:", error);
    }
}

function checkLoginStatus() {
    // 检查是否已有登录状态
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const username = localStorage.getItem('username');
    const avatar = localStorage.getItem('avatar');
    
    // 如果已有登录状态，保持不变
    if (isLoggedIn === 'true' && username) {
        // 更新头像显示
        if (avatar) {
            const avatarData = JSON.parse(avatar);
            const avatarSrc = avatarData.type === 'preset' ? avatarData.emoji : avatarData.data;
            
            const avatarPreview = document.getElementById('avatarPreview');
            if (avatarPreview) {
                if (avatarSrc.includes('http') || avatarSrc.includes('data:')) {
                    avatarPreview.innerHTML = `<img src="${avatarSrc}" alt="User Avatar" class="default-avatar">`;
                } else {
                    avatarPreview.innerHTML = `<div class="avatar-emoji-preview">${avatarSrc}</div>`;
                }
            }
            
            const profileAvatar = document.getElementById('profileAvatar');
            if (profileAvatar) {
                if (avatarSrc.includes('http') || avatarSrc.includes('data:')) {
                    profileAvatar.innerHTML = `<img src="${avatarSrc}" alt="Avatar">`;
                } else {
                    profileAvatar.innerHTML = `<div class="emoji-avatar">${avatarSrc}</div>`;
                }
            }
        }
        
        const profileName = document.getElementById('profileName');
        if (profileName) {
            profileName.textContent = username;
        }
    } else {
        // 没有登录状态，设置默认头像
        const avatarPreview = document.getElementById('avatarPreview');
        if (avatarPreview) {
            avatarPreview.innerHTML = '<img src="https://picsum.photos/100/100?random=1" alt="User Avatar" class="default-avatar">';
        }
        
        const profileAvatar = document.getElementById('profileAvatar');
        if (profileAvatar) {
            profileAvatar.innerHTML = '<img src="https://picsum.photos/100/100?random=1" alt="Avatar" class="default-avatar">';
        }
        
        const profileName = document.getElementById('profileName');
        if (profileName) {
            profileName.textContent = t('username');
        }
    }
}

// 更新头像到服务器
async function updateAvatarOnServer(avatar) {
    const username = localStorage.getItem('username');
    if (!username) return;
    
    try {
        const response = await fetch('/update-avatar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                avatar: JSON.stringify(avatar)
            })
        });
        
        const data = await response.json();
        if (response.ok) {
            console.log(data.message);
        }
    } catch (error) {
        console.error("更新头像失败:", error);
    }
}

// ==================== 个人中心页面 ==================== 

// 登录成功后跳转到个人中心
function goToProfile() {
    showSinglePage('profilePage', { showBottomNav: true });
    updateProfileInfo();
}

// 更新个人中心统计数据
async function updateProfileStats() {
    // 更新关注数
    const followers = await getFollowers();
    document.getElementById('followCount').textContent = followers.length || 0;
    
    // 更新获赞数（需要从服务器获取）
    updateLikeCount();
}

// 获取并更新获赞数
function updateLikeCount() {
    const username = localStorage.getItem('username');
    fetch(`/get_user_likes?username=${encodeURIComponent(username)}`)
        .then(response => response.json())
        .then(data => {
            const likeCount = data.likes || 0;
            document.getElementById('likeCount').textContent = likeCount;
        })
        .catch(err => {
            console.error('获取获赞数失败:', err);
        });
}

// 更新个人中心信息
function updateProfileInfo() {
    const username = localStorage.getItem('username');
    const avatar = localStorage.getItem('avatar');
    
    if (username) {
        document.getElementById('profileName').textContent = username;
    }
    
    if (avatar) {
        const avatarData = JSON.parse(avatar);
        const avatarSrc = avatarData.type === 'preset' ? avatarData.emoji : avatarData.data;
        updateProfileAvatar(avatarSrc);
    }
    
    // 更新统计数据
    updateProfileStats();
}

// 更新个人中心头像
function updateProfileAvatar(src) {
    const profileAvatar = document.getElementById('profileAvatar');
    
    if (src.includes('http') || src.includes('data:')) {
        // 图片URL
        profileAvatar.innerHTML = `<img src="${src}" alt="Avatar">`;
    } else {
        // emoji头像
        profileAvatar.innerHTML = `<div class="emoji-avatar">${src}</div>`;
    }
}

// 返回首页
function goBack() {
    showSinglePage('mainPage', { showBottomNav: true });
}

// 显示菜单点击提示
function showSection(name) {
    if (name === '头像') {
        // 打开头像选择弹窗
        openAvatarSelector();
    } else {
        alert(`"我的${name}"功能开发中...`);
    }
}

// 打开修改密码弹窗
function openChangePassword() {
    document.getElementById('changePwdModal').classList.add('active');
}

// 关闭修改密码弹窗
function closeChangePwd() {
    document.getElementById('changePwdModal').classList.remove('active');
    document.getElementById('changePwdForm').reset();
}

// 处理修改密码
async function handleChangePassword(event) {
    event.preventDefault();
    
    const oldPwd = document.getElementById('oldPwd').value;
    const newPwd = document.getElementById('newPwd').value;
    const confirmPwd = document.getElementById('confirmPwd').value;
    const username = localStorage.getItem('username');
    
    // 验证密码
    if (newPwd !== confirmPwd) {
        alert(t('passwordMismatch'));
        return;
    }
    
    if (newPwd.length < 6) {
        alert(t('passwordTooShort'));
        return;
    }
    
    try {
        const response = await fetch('/change-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                old_password: oldPwd,
                new_password: newPwd
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            alert(data.message);
            closeChangePwd();
        } else {
            alert(t('requestFailed', { detail: data.detail }));
        }
    } catch (error) {
        alert(t('serverUnavailable'));
        console.error("修改密码失败:", error);
    }
}

// 退出登录
function logout() {
    if (confirm(t('logoutConfirm'))) {
        localStorage.removeItem('username');
        localStorage.removeItem('isLoggedIn');
        localStorage.removeItem('avatar');
        
        // 重置头像显示
        const avatarPreview = document.getElementById('avatarPreview');
        avatarPreview.innerHTML = '<img src="https://picsum.photos/100/100?random=1" alt="User Avatar" class="default-avatar">';
        
        const profileAvatar = document.getElementById('profileAvatar');
        if (profileAvatar) {
            profileAvatar.innerHTML = '<img src="https://picsum.photos/100/100?random=1" alt="Avatar" class="default-avatar">';
        }
        
        // 返回首页并打开登录弹窗
        showSinglePage('mainPage', { showBottomNav: true });
        openAuthModal();
    }
}

// 更新头像后同步到个人中心
function syncProfileAvatar() {
    const avatar = localStorage.getItem('avatar');
    if (avatar) {
        const avatarData = JSON.parse(avatar);
        const avatarSrc = avatarData.type === 'preset' ? avatarData.emoji : avatarData.data;
        updateProfileAvatar(avatarSrc);
    }
}

// 处理底部导航"我的"按钮点击
function handleMyClick() {
    if (isUserLoggedIn()) {
        // 已登录，跳转到个人中心
        goToProfile();
    } else {
        // 未登录，打开登录弹窗
        requireLogin(() => goToProfile());
    }
}

// ==================== 我的帖子功能 ====================
async function showMyPosts() {
    showSinglePage('myPostsPage', { showBottomNav: false });
    
    const currentUser = localStorage.getItem('username');
    
    // 设置页面标题为"用户名 的帖子"
    const pageTitle = document.querySelector('#myPostsPage .posts-header h1');
    pageTitle.textContent = t('myPostsTitle', { user: currentUser });
    document.getElementById('myPostsContainer').innerHTML = `<div class="empty-state"><p>${t('loading')}</p></div>`;
    
    loadMyPostsForProfile(currentUser);
}

function backToProfile() {
    showSinglePage('profilePage', { showBottomNav: true });
}

// ==================== 我的关注功能 ====================
// 处理关注列表点击事件（使用事件委托）
function handleFollowingClick(event) {
    const target = event.target;
    const item = target.closest('.following-item');
    
    if (item) {
        const username = item.getAttribute('data-username');
        if (username) {
            console.log("handleFollowingClick called with:", username);
            viewUserPosts(username);
        }
    }
}

function showFollowingList() {
    showSinglePage('followingPage', { showBottomNav: false });
    renderFollowingList();
}

function backToFollowing() {
    document.getElementById('userPostsPage').style.display = 'none';
    
    // 根据来源页面返回正确的页面
    if (userPostsSource === 'detail') {
        // 从帖子详情页进入的，返回帖子详情页
        document.getElementById('detailPage').classList.add('active');
        document.getElementById('bottomNav').style.transform = 'translateY(150%)';
    } else {
        // 默认从关注列表进入的，返回关注列表
        document.getElementById('followingPage').style.display = 'block';
        // 重新渲染关注列表，确保点击事件绑定正确
        renderFollowingList();
    }
    
    currentViewingUser = '';
    userPostsSource = '';
}

async function renderFollowingList() {
    const followers = await getFollowers();
    const container = document.getElementById('followingList');
    
    if (!followers || followers.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
                <p>${t('noFollowing')}</p>
                <p style="font-size: 14px; margin-top: 5px;">${t('followingHint')}</p>
            </div>
        `;
        return;
    }
    
    let html = '';
    for (const follower of followers) {
        let avatarContent = `<img src="https://picsum.photos/100/100?random=${follower.charCodeAt(0)}" alt="${follower}" class="following-avatar">`;
        
        try {
            const response = await fetch(`/users/${follower}`);
            if (response.ok) {
                const userData = await response.json();
                if (userData.avatar) {
                    const avatarData = JSON.parse(userData.avatar);
                    if (avatarData.type === 'preset') {
                        avatarContent = `<div class="emoji-avatar">${avatarData.emoji}</div>`;
                    } else if (avatarData.data) {
                        avatarContent = `<img src="${avatarData.data}" alt="${follower}" class="following-avatar">`;
                    }
                }
            }
        } catch (error) {
            console.error('获取用户头像失败:', error);
        }
        
        html += `
            <div class="following-item" data-username="${follower}">
                ${avatarContent}
                <div class="following-info">
                    <div class="following-name">${follower}</div>
                </div>
                <svg class="following-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 18l6-6-6-6"/>
                </svg>
            </div>
        `;
    }
    
    container.innerHTML = html;
    
    // 使用事件委托绑定点击事件
    container.removeEventListener('click', handleFollowingClick);
    container.addEventListener('click', handleFollowingClick);
}

// ==================== 消息功能 ====================
let currentChatUser = '';

// 获取当前用户的消息数据 - 从服务器获取
async function getMessages() {
    const currentUser = localStorage.getItem('username');
    if (!currentUser) return {};
    
    try {
        const response = await fetchWithTimeout(`/messages/${encodeURIComponent(currentUser)}`);
        if (response.ok) {
            const data = await response.json();
            // 将服务器数据转换为本地格式
            const cachedMessages = getCachedMessages(currentUser);
            const messages = {};
            data.messages.forEach(item => {
                messages[item.username] = {
                    list: cachedMessages[item.username]?.list || [],
                    unread: item.unread,
                    avatar: item.avatar
                };
            });
            // 同时保存到本地存储作为缓存
            const allMessages = localStorage.getItem('allMessages');
            const messagesData = allMessages ? JSON.parse(allMessages) : {};
            messagesData[currentUser] = messages;
            localStorage.setItem('allMessages', JSON.stringify(messagesData));
            return messages;
        }
    } catch (error) {
        console.error("获取消息失败:", error);
    }
    
    // 降级到本地存储
    return getCachedMessages(currentUser);
}

function getCachedMessages(username = localStorage.getItem('username')) {
    if (!username) return {};

    const allMessages = localStorage.getItem('allMessages');
    try {
        const messagesData = allMessages ? JSON.parse(allMessages) : {};
        return messagesData[username] || {};
    } catch (error) {
        console.error("读取本地消息缓存失败:", error);
        return {};
    }
}

// 保存当前用户的消息数据
function saveMessages(messages) {
    const currentUser = localStorage.getItem('username');
    if (!currentUser) return;
    
    const allMessages = localStorage.getItem('allMessages');
    let messagesData = {};
    try {
        messagesData = allMessages ? JSON.parse(allMessages) : {};
    } catch (error) {
        console.error("本地消息缓存已损坏，正在重建:", error);
    }
    messagesData[currentUser] = messages;
    localStorage.setItem('allMessages', JSON.stringify(messagesData));
}

// 获取未读消息计数
async function getUnreadCount() {
    const messages = await getMessages();
    let count = 0;
    for (const user in messages) {
        if (messages[user] && messages[user].unread) {
            count += messages[user].unread;
        }
    }
    return count;
}

// 更新消息徽章
async function updateMessageBadge() {
    const badge = document.getElementById('messageBadge');
    if (!badge) return;

    const count = await getUnreadCount();
    
    if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'flex';
    } else {
        badge.style.display = 'none';
    }
}

// 消息页面来源（'home' 或 'profile'）
let messagesSource = 'home';
let chatReturnState = null;

// 显示消息页面
function showMessages(source = 'home') {
    // 检查登录状态
    if (!requireLogin(() => showMessages(source))) return;
    
    // 记录来源
    messagesSource = source;
    
    showSinglePage('messagesPage', { showBottomNav: false });
    renderMessagesList();
}

// 关闭消息页面（根据来源返回）
function closeMessages() {
    if (messagesSource === 'profile') {
        // 从个人中心进入，返回个人中心
        showSinglePage('profilePage', { showBottomNav: true });
    } else if (messagesSource === 'discover') {
        showSinglePage('discoverPage', { showBottomNav: false });
    } else {
        // 默认返回首页
        showSinglePage('mainPage', { showBottomNav: true });
    }
}

// 返回消息列表
function backToMessages() {
    const returnState = chatReturnState || { type: 'messages' };
    hideChatPage();
    chatReturnState = null;

    if (returnState.type === 'userPosts') {
        const userPostsPage = document.getElementById('userPostsPage');
        if (userPostsPage) {
            userPostsPage.style.display = 'block';
            userPostsPage.style.zIndex = '700';
            userPostsPage.style.opacity = '1';
        }
        return;
    }

    if (returnState.type === 'detail') {
        document.getElementById('detailPage')?.classList.add('active');
        const bottomNav = document.getElementById('bottomNav');
        if (bottomNav) bottomNav.style.transform = 'translateY(150%)';
        return;
    }

    document.getElementById('messagesPage').style.display = 'block';
    renderMessagesList();
}

function getChatReturnState() {
    const messagesPage = document.getElementById('messagesPage');
    const userPostsPage = document.getElementById('userPostsPage');
    const detailPage = document.getElementById('detailPage');

    if (messagesPage && getComputedStyle(messagesPage).display !== 'none') {
        return { type: 'messages' };
    }
    if (userPostsPage && getComputedStyle(userPostsPage).display !== 'none') {
        return { type: 'userPosts' };
    }
    if (detailPage?.classList.contains('active')) {
        return { type: 'detail' };
    }
    return { type: 'messages' };
}

function hideChatPage() {
    const chatPage = document.getElementById('chatPage');
    if (!chatPage) return;
    chatPage.classList.remove('active');
    chatPage.style.display = 'none';
    currentChatUser = '';
    const input = document.getElementById('chatInput');
    if (input) {
        input.value = '';
        input.disabled = false;
    }
    const sendBtn = document.querySelector('.chat-send-btn');
    if (sendBtn) sendBtn.disabled = false;
}

// 渲染消息列表
async function renderMessagesList() {
    const container = document.getElementById('messagesList');
    if (!container) return;

    container.innerHTML = `<div class="empty-state"><p>${t('loading')}</p></div>`;

    let messages = {};
    let followers = [];

    try {
        [messages, followers] = await Promise.all([
            getMessages(),
            getFollowers()
        ]);
    } catch (error) {
        console.error("渲染消息列表失败:", error);
        messages = getCachedMessages();
    }
    
    // 创建消息列表（包含关注的用户）
    const messageUsers = new Set([...Object.keys(messages), ...followers]);
    const userList = Array.from(messageUsers);
    
    if (userList.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
                <p>${t('noMessages')}</p>
                <p style="font-size: 14px; margin-top: 5px;">${t('messageHint')}</p>
            </div>
        `;
        return;
    }
    
    let html = '';
    for (const user of userList) {
        const userMessages = messages[user] || { list: [], unread: 0 };
        const lastMessage = userMessages.list.length > 0 
            ? userMessages.list[userMessages.list.length - 1] 
            : null;
        const preview = lastMessage ? lastMessage.content : t('startChat');
        const unread = userMessages.unread || 0;
        
        let avatarContent = avatarHtml(userMessages.avatar, user, 'message-avatar');
        
        html += `
            <div class="message-item" onclick='openChat(${JSON.stringify(user)})'>
                ${avatarContent}
                <div class="message-info">
                    <div class="message-name">${escapeHtml(user)}</div>
                    <div class="message-preview">${escapeHtml(preview)}</div>
                </div>
                ${unread > 0 ? `<span class="message-badge">${unread}</span>` : ''}
            </div>
        `;
    }
    
    container.innerHTML = html;
}

// 打开聊天页面
function openChat(username) {
    currentChatUser = username;
    chatReturnState = getChatReturnState();
    hideNavigationPages();
    document.getElementById('detailPage')?.classList.remove('active');

    const bottomNav = document.getElementById('bottomNav');
    if (bottomNav) {
        bottomNav.style.display = 'none';
        bottomNav.style.transform = 'translateY(150%)';
    }

    const chatPage = document.getElementById('chatPage');
    chatPage.style.display = '';
    chatPage.classList.add('active');
    document.getElementById('chatTitle').textContent = username;
    renderChatLoading();
    
    // 标记为已读
    markAsRead(username);
    
    // 加载聊天记录
    loadChatMessages(username);
}

// 标记消息为已读
async function markAsRead(username) {
    const messages = await getMessages();
    if (messages[username]) {
        messages[username].unread = 0;
        saveMessages(messages);
        await updateMessageBadge();
    }
}

// 加载聊天消息
async function loadChatMessages(username) {
    const container = document.getElementById('chatMessages');
    if (!container) return;

    const currentUser = localStorage.getItem('username');
    let chatList = [];

    try {
        const response = await fetchWithTimeout(`/chat-history/${encodeURIComponent(currentUser)}/${encodeURIComponent(username)}`, {}, 4500);
        if (!response.ok) {
            throw new Error(`chat-history ${response.status}`);
        }

        const data = await response.json();
        chatList = (data.history || []).map(msg => ({
            sender: msg.sender,
            content: msg.content,
            time: msg.time
        }));
        cacheChatMessages(username, chatList);
    } catch (error) {
        console.error("加载聊天记录失败，使用本地缓存:", error);
        const messages = getCachedMessages(currentUser);
        chatList = messages[username]?.list || [];
    }
    
    renderChatMessages(chatList);
}

function cacheChatMessages(username, chatList) {
    const messages = getCachedMessages();
    const previous = messages[username] || { unread: 0 };
    messages[username] = {
        ...previous,
        list: chatList,
        unread: 0
    };
    saveMessages(messages);
}

function renderChatLoading() {
    const container = document.getElementById('chatMessages');
    if (!container) return;

    container.innerHTML = `<div class="chat-state">${t('loading')}</div>`;
}

function renderChatMessages(chatList) {
    const container = document.getElementById('chatMessages');
    if (!container) return;

    if (!chatList.length) {
        container.innerHTML = `<div class="chat-state">${t('startChat')}</div>`;
        return;
    }

    const currentUser = localStorage.getItem('username');
    const html = chatList.map(msg => {
        const isSent = msg.sender === currentUser;
        return `
            <div class="chat-message ${isSent ? 'sent' : 'received'}">
                ${escapeHtml(msg.content)}
                <div class="chat-message-time">${formatTime(msg.time)}</div>
            </div>
        `;
    }).join('');
    
    container.innerHTML = html;
    container.scrollTop = container.scrollHeight;
}

// 格式化时间
function formatTime(timestamp) {
    const date = new Date(timestamp);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

// 发送消息 - 同步到服务器
async function sendMessage() {
    // 检查登录状态
    if (!requireLogin(() => sendMessage())) return;
    
    const input = document.getElementById('chatInput');
    const sendBtn = document.querySelector('.chat-send-btn');
    const content = input.value.trim();
    
    if (!content || !currentChatUser) return;
    
    const currentUser = localStorage.getItem('username');
    input.value = '';
    input.disabled = true;
    if (sendBtn) sendBtn.disabled = true;
    
    // 先同步到服务器
    try {
        const response = await fetchWithTimeout('/send-message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sender: currentUser,
                receiver: currentChatUser,
                content: content
            })
        });
        
        if (!response.ok) {
            const data = await response.json();
            input.value = content;
            alert(t('requestFailed', { detail: data.detail || t('unknownTime') }));
            return;
        }
    } catch (error) {
        console.error("发送消息失败:", error);
        input.value = content;
        alert(t('requestFailed', { detail: t('send') }));
        return;
    } finally {
        input.disabled = false;
        if (sendBtn) sendBtn.disabled = false;
        input.focus();
    }
    
    // 更新本地消息数据
    const newMessage = {
        sender: currentUser,
        content: content,
        time: Date.now()
    };
    
    const messages = await getMessages();
    if (!messages[currentChatUser]) {
        messages[currentChatUser] = { list: [], unread: 0 };
    }
    messages[currentChatUser].list.push(newMessage);
    saveMessages(messages);
    
    // 重新加载聊天记录
    loadChatMessages(currentChatUser);
}

// 模拟收到消息（测试用）
async function simulateReceiveMessage(sender, content) {
    const messages = await getMessages();
    if (!messages[sender]) {
        messages[sender] = { list: [], unread: 0 };
    }
    messages[sender].list.push({
        sender: sender,
        content: content,
        time: Date.now()
    });
    messages[sender].unread = (messages[sender].unread || 0) + 1;
    saveMessages(messages);
    await updateMessageBadge();
}

// ==================== 查看他人帖子 ====================
let currentViewingUser = '';
let userPostsSource = ''; // 记录进入用户主页的来源页面

function viewUserPosts(username, source = 'following') {
    console.log("viewUserPosts called with:", username, "from:", source);
    
    // 更新当前查看的用户和来源
    currentViewingUser = username;
    userPostsSource = source;
    
    // 获取所有页面元素
    const followingPage = document.getElementById('followingPage');
    const myPostsPage = document.getElementById('myPostsPage');
    const profilePage = document.getElementById('profilePage');
    const detailPage = document.getElementById('detailPage');
    const userPostsPage = document.getElementById('userPostsPage');
    const container = document.getElementById('userPostsContainer');
    
    // 确保所有其他页面都被隐藏
    followingPage.style.display = 'none';
    myPostsPage.style.display = 'none';
    profilePage.style.display = 'none';
    detailPage.classList.remove('active');
    
    // 确保 userPostsPage 在最上层且可见
    userPostsPage.style.display = 'block';
    userPostsPage.style.zIndex = '700';
    userPostsPage.style.opacity = '1';
    
    // 更新标题
    document.getElementById('userPostsTitle').textContent = t('myPostsTitle', { user: username });
    
    // 清空容器并显示加载状态
    container.innerHTML = `<div style="text-align:center; padding:20px;">${t('loading')}</div>`;
    
    // 确保重新加载数据
    loadUserPosts(username);
}

async function loadUserPosts(username) {
    try {
        const response = await fetch(`/posts/${encodeURIComponent(username)}`);
        const posts = await response.json();
        
        if (response.ok && posts.length > 0) {
            await renderUserPosts(posts);
        } else {
            showUserEmptyState();
        }
    } catch (error) {
        console.error("加载帖子失败:", error);
        showUserEmptyState();
    }
}

async function renderUserPosts(posts) {
    const container = document.getElementById('userPostsContainer');
    let html = '';
    const displayPosts = await Promise.all((posts || []).map(post => localizePostSummary(post)));
    
    displayPosts.forEach(post => {
        html += renderProfilePostCard(post, { showAuthor: false });
    });
    
    container.innerHTML = html;
}

function renderProfilePostCard(post, options = {}) {
    const { editable = false, showAuthor = true, showContent = false } = options;
    const photoSrc = post.photos && post.photos.length > 0
        ? post.photos[0]
        : `https://picsum.photos/400/300?random=${post.id}`;
    const displayPublishTime = getGuideDisplayPublishTime(post) || post.publish_time;
    const dateStr = displayPublishTime ? formatPostDate(displayPublishTime) : '';
    const safeTitle = escapeHtml(post.title || t('title'));
    const safeAuthor = escapeHtml(post.author || t('anonymousUser'));
    const safeLocation = escapeHtml(post.location || t('unknownLocation'));
    const safeContent = escapeHtml(post.content || '');
    const metaParts = [
        showAuthor ? safeAuthor : '',
        dateStr ? escapeHtml(dateStr) : ''
    ].filter(Boolean);
    const actionsHtml = editable ? `
        <div class="post-actions">
            <button class="post-action-btn edit-btn" onclick="event.stopPropagation(); editPost(${post.id})">
                <svg viewBox="0 0 24 24" width="16" height="16"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                <span>${t('edit')}</span>
            </button>
            <button class="post-action-btn delete-btn" onclick="event.stopPropagation(); deletePost(${post.id})">
                <svg viewBox="0 0 24 24" width="16" height="16"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>
                <span>${t('delete')}</span>
            </button>
        </div>
    ` : '';

    return `
        <div class="post-card profile-post-card" onclick="openPostDetail(${post.id})">
            <div class="post-image-wrapper">
                <img src="${photoSrc}" alt="${safeTitle}" class="post-image">
                <div class="profile-post-like">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    <span>${post.likes || 0}</span>
                </div>
            </div>
            <div class="post-info">
                <div class="profile-post-main">
                    <h3 class="post-title-text">${safeTitle}</h3>
                    ${metaParts.length ? `<p class="post-author">${metaParts.join(' · ')}</p>` : ''}
                    ${showContent && safeContent ? `<p class="post-content-preview">${safeContent}</p>` : ''}
                    <p class="post-location">📍 ${safeLocation}</p>
                </div>
                <div class="post-stats-row">
                    <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 14.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg> ${post.views || 0}</span>
                    <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg> ${post.likes || 0}</span>
                    <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> ${post.comments || 0}</span>
                </div>
                ${actionsHtml}
            </div>
        </div>
    `;
}

function showUserEmptyState() {
    const container = document.getElementById('userPostsContainer');
    const canChat = currentViewingUser && currentViewingUser !== localStorage.getItem('username');
    container.innerHTML = `
        <div class="empty-state">
            <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
            </svg>
            <p>${t('noUserPosts', { user: currentViewingUser })}</p>
            ${canChat ? `<button class="empty-chat-btn" type="button" onclick='openChat(${JSON.stringify(currentViewingUser)})'>${t('startChat')}</button>` : ''}
        </div>
    `;
}

// 获取指定用户的帖子（用于个人中心）
async function loadMyPostsForProfile(username) {
    try {
        const response = await fetchWithTimeout(`/posts/${encodeURIComponent(username)}`);
        const posts = await response.json();
        
        const postsContainer = document.getElementById('myPostsContainer');
        
        if (response.ok && posts.length > 0) {
            // 渲染用户帖子列表
            let html = '';
            const displayPosts = await Promise.all(posts.map(post => localizePostSummary(post, { includeContent: true })));
            displayPosts.forEach(post => {
                html += renderProfilePostCard(post, { editable: true, showContent: true });
            });
            postsContainer.innerHTML = html;
        } else {
            postsContainer.innerHTML = `
                <div class="empty-state">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    </svg>
                    <p>${t('noPosts')}</p>
                    <p style="font-size: 14px; margin-top: 5px;">${t('publishFirstHint')}</p>
                </div>
            `;
        }
    } catch (error) {
        console.error("加载用户帖子失败:", error);
        document.getElementById('myPostsContainer').innerHTML = `
            <div class="empty-state">
                <p>${t('requestFailed', { detail: t('loading') })}</p>
            </div>
        `;
    }
}

async function loadMyPosts() {
    try {
        console.log('开始请求 /all-posts API...');
        const url = '/all-posts?post_type=guide';
        const response = await fetchWithTimeout(url);
        console.log('API响应状态:', response.status);
        const posts = sortGuidePostsByDistance(normalizeGuideDisplayPublishTimes(await response.json()));
        console.log('获取到的帖子数量:', posts.length);
        
        if (response.ok && posts.length > 0) {
            console.log('开始渲染推荐卡片...');
            const heroPosts = posts.slice(0, 4);
            const listPosts = posts.slice(heroPosts.length);
            await renderHeroCards(heroPosts);
            console.log('开始渲染帖子列表...');
            renderPosts(listPosts);
        } else {
            console.log('没有帖子数据，显示空状态');
            showEmptyState();
        }
    } catch (error) {
        console.error("加载帖子失败:", error);
        showEmptyState();
    }
}

function calculateDistanceKm(origin, target) {
    const lat1 = Number(origin?.latitude);
    const lon1 = Number(origin?.longitude);
    const lat2 = Number(target?.latitude);
    const lon2 = Number(target?.longitude);
    if (![lat1, lon1, lat2, lon2].every(Number.isFinite)) return Number.POSITIVE_INFINITY;

    const toRad = value => value * Math.PI / 180;
    const earthRadiusKm = 6371;
    const dLat = toRad(lat2 - lat1);
    const dLon = toRad(lon2 - lon1);
    const a = Math.sin(dLat / 2) ** 2 +
        Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
    return earthRadiusKm * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

function sortGuidePostsByDistance(posts) {
    const origin = LocationService.getDiscoverOrigin();
    return [...(posts || [])].sort((a, b) => {
        const distanceA = calculateDistanceKm(origin, a);
        const distanceB = calculateDistanceKm(origin, b);
        if (Math.abs(distanceA - distanceB) > 1) return distanceA - distanceB;

        const engagementA = Number(a.likes || 0) * 2 + Number(a.comments || 0) * 3 + Number(a.views || 0) * 0.02;
        const engagementB = Number(b.likes || 0) * 2 + Number(b.comments || 0) * 3 + Number(b.views || 0) * 0.02;
        return engagementB - engagementA;
    });
}

function refreshHomeGuidesIfVisible() {
    const mainPage = document.getElementById('mainPage');
    if (mainPage && getComputedStyle(mainPage).display !== 'none') {
        loadMyPosts().catch(error => console.error('刷新首页导览推荐失败:', error));
    }
}

function renderHotCategories() {
    const container = document.getElementById('hotCategories');
    if (!container) return;

    container.innerHTML = POST_TAGS.map(tag => `
        <button class="hot-category" type="button" style="background-image: url('${tag.image}');" onclick="openTagCategory('${tag.id}')">
            <span>${getTagLabel(tag.id)}</span>
        </button>
    `).join('');
}

function closeTagResults() {
    const section = document.getElementById('tagResultsSection');
    const posts = document.getElementById('tagResultsPosts');
    const empty = document.getElementById('tagResultsEmpty');
    if (section) section.hidden = true;
    if (posts) posts.innerHTML = '';
    if (empty) empty.style.display = 'none';
}

async function openTagCategory(tagId) {
    const tag = POST_TAGS.find(item => item.id === tagId);
    if (!tag) return;

    const section = document.getElementById('tagResultsSection');
    const title = document.getElementById('tagResultsTitle');
    const postsContainer = document.getElementById('tagResultsPosts');
    const empty = document.getElementById('tagResultsEmpty');

    if (!section || !title || !postsContainer || !empty) return;

    section.hidden = false;
    title.textContent = t('categoryResultTitle', { category: getTagLabel(tag.id) });
    postsContainer.innerHTML = `<div class="empty-state"><p>${t('loadingCategory')}</p></div>`;
    empty.style.display = 'none';

    try {
        const origin = await getCurrentLocationForNearby();
        const url = `/nearby-posts?latitude=${origin.latitude}&longitude=${origin.longitude}&radius=1000&post_type=user&tag=${encodeURIComponent(tagId)}`;
        const response = await fetchWithTimeout(url);
        const posts = response.ok ? await response.json() : [];
        renderTagResults(posts);
    } catch (error) {
        console.error('加载分类推荐失败:', error);
        renderTagResults([]);
    }
}

async function renderTagResults(posts) {
    const postsContainer = document.getElementById('tagResultsPosts');
    const empty = document.getElementById('tagResultsEmpty');
    if (!postsContainer || !empty) return;

    if (!posts || posts.length === 0) {
        postsContainer.innerHTML = '';
        empty.style.display = 'flex';
        return;
    }

    empty.style.display = 'none';
    await renderDiscoverPostsInto(postsContainer, posts);
}

function getExperienceSpot(spotId) {
    return EXPERIENCE_SPOTS.find(spot => spot.id === spotId) || EXPERIENCE_SPOTS[0];
}

async function renderExperienceFeatures() {
    const container = document.getElementById('experienceFeatureList');
    if (!container) return;

    const spots = await Promise.all(EXPERIENCE_SPOTS.map(spot => localizeExperienceSpot(spot, { summaryOnly: true })));

    container.innerHTML = spots.map(spot => `
        <article class="experience-feature-card" onclick="openExperiencePage('${escapeHtml(spot.id)}')">
            <img src="${escapeHtml(spot.cardImage || spot.cover)}" alt="${escapeHtml(spot.title)}">
            <div class="experience-feature-card-body">
                <span>${escapeHtml(spot.kicker)}</span>
                <h3>${escapeHtml(spot.title)}</h3>
                <p>${escapeHtml(spot.subtitle)}</p>
                <div class="experience-feature-meta">
                    <b>${t('featureMetaDeepDive')}</b>
                </div>
            </div>
        </article>
    `).join('');
}

let experienceReturnState = null;
let currentExperienceSpot = null;
let currentExperienceSpotSource = null;
let liteVrState = { dragging: false, startX: 0, startOffset: 0, offset: -18 };
let sphereVrRuntime = null;
let sphereVrStarted = false;
let experienceStoryObserver = null;

async function renderExperiencePageFromSource(sourceSpot) {
    const spot = await localizeExperienceSpot(sourceSpot);
    currentExperienceSpot = spot;
    renderExperiencePage(spot);
}

async function openExperiencePage(spotId) {
    const spot = getExperienceSpot(spotId);
    currentExperienceSpotSource = spot;
    stopGuideAudio();
    closeGuideDetail();
    await renderExperiencePageFromSource(spot);

    const page = document.getElementById('experiencePage');
    if (page && !page.classList.contains('active')) {
        experienceReturnState = capturePageState();
    }

    page?.classList.add('active');
    const mainPage = document.getElementById('mainPage');
    const discoverPage = document.getElementById('discoverPage');
    const bottomNav = document.getElementById('bottomNav');
    if (mainPage) mainPage.style.opacity = '0.3';
    if (discoverPage) discoverPage.style.opacity = '0.3';
    if (bottomNav) bottomNav.style.transform = 'translateY(150%)';

    const scroll = document.getElementById('experienceScroll');
    if (scroll) scroll.scrollTop = 0;
    requestAnimationFrame(() => bindLiteVr(currentExperienceSpot));
}

function closeExperiencePage() {
    document.getElementById('experiencePage')?.classList.remove('active');
    destroySphereVr();
    sphereVrStarted = false;
    if (!restorePageState(experienceReturnState)) {
        showSinglePage('mainPage', { showBottomNav: true });
        setTopNavActive(0);
    }
    experienceReturnState = null;
}

function scrollExperienceToStory() {
    document.getElementById('experienceStory')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function scrollExperienceToVr() {
    document.getElementById('experienceVrSection')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function scrollExperienceToPractical() {
    document.getElementById('experiencePractical')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function renderExperienceQuickNav() {
    return `
        <nav class="experience-quick-nav" aria-label="${t('quickGuideNav')}">
            <button type="button" onclick="scrollExperienceToStory()">${t('storyEntry')}</button>
            <button type="button" onclick="scrollExperienceToVr()">${t('vrEntry')}</button>
            <button type="button" onclick="scrollExperienceToPractical()">${t('adviceEntry')}</button>
        </nav>
    `;
}

function renderExperiencePage(spot) {
    const hero = document.getElementById('experienceHero');
    if (hero) hero.style.backgroundImage = `linear-gradient(180deg, rgba(0,0,0,.14), rgba(0,0,0,.72)), url('${spot.cover}')`;

    document.getElementById('experienceHeroKicker').textContent = spot.kicker;
    document.getElementById('experienceTitle').textContent = spot.title;
    document.getElementById('experienceSubtitle').textContent = spot.subtitle;

    document.getElementById('experienceInfoStrip').innerHTML = spot.meta.map(item => `
        <div class="experience-info-item">
            <span>${escapeHtml(item.label)}</span>
            <strong>${escapeHtml(item.value)}</strong>
        </div>
    `).join('') + renderExperienceQuickNav();

    document.getElementById('experienceIntro').innerHTML = `
        <div class="experience-section-heading">
            <span>${t('travelFeeling')}</span>
            <h2>${t('travelFeelingTitle')}</h2>
        </div>
        ${spot.intro.map(text => `<p>${escapeHtml(text)}</p>`).join('')}
        ${renderExperienceTimeTravel(spot)}
        ${renderExperienceDossiers(spot)}
    `;

    document.getElementById('experienceStory').innerHTML = spot.story.map((item, index) => `
        <article class="experience-story-block ${index % 2 ? 'is-reverse' : ''}">
            <img src="${escapeHtml(item.image)}" alt="${escapeHtml(item.title)}">
            <div>
                <span>${t('sceneLabel', { index: index + 1 })}</span>
                <h3>${escapeHtml(item.title)}</h3>
                <p>${escapeHtml(item.text)}</p>
            </div>
        </article>
    `).join('');

    document.getElementById('liteVrImage').src = spot.liteVrImage;
    document.getElementById('liteVrHotspots').innerHTML = spot.liteHotspots.map((hotspot, index) => `
        <button type="button" class="lite-vr-hotspot" style="left:${Number(hotspot.x)}%; top:${Number(hotspot.y)}%;" data-hotspot-index="${index}">
            <span>${index + 1}</span>
        </button>
    `).join('');
    document.getElementById('liteVrCaption').textContent = spot.vrCaption;
    document.getElementById('sphereVrCaption').textContent = spot.vrInstructions?.sphere || spot.vrCaption;

    document.getElementById('experiencePractical').innerHTML = `
        <div class="experience-section-heading">
            <span>${t('practicalAdvice')}</span>
            <h2>${t('practicalAdviceTitle')}</h2>
        </div>
        ${renderExperienceWalkRhythm(spot)}
        <div class="experience-practical-grid">
            ${spot.practical.map(item => `
                <article>
                    <h3>${escapeHtml(item.title)}</h3>
                    <p>${escapeHtml(item.text)}</p>
                </article>
            `).join('')}
        </div>
        ${renderExperienceStamp(spot)}
    `;

    switchExperienceVr('lite');
    bindExperienceAdvancedControls(spot);
    observeExperienceStoryBlocks();
}

function renderExperienceTimeTravel(spot) {
    const item = spot.timeTravel;
    if (!item) return '';

    return `
        <section class="experience-time-machine">
            <div class="time-machine-visual">
                <img class="time-machine-now-image" src="${escapeHtml(spot.liteVrImage)}" alt="东交民巷现在街景">
                <div class="time-machine-before-image" id="timeMachineBefore">
                    <img src="${escapeHtml(item.beforeImage || spot.liteVrImage)}" alt="北京使馆区历史旧影">
                    <div class="time-machine-before-label">
                        <span>${escapeHtml(item.beforeLabel)}</span>
                        <strong>${t('timeMachineBeforeTitle')}</strong>
                        <small>${t('timeMachineBeforeDesc')}</small>
                    </div>
                </div>
                <div class="time-machine-divider" id="timeMachineDivider"></div>
                <div class="time-machine-now">
                    <span>${escapeHtml(item.afterLabel)}</span>
                </div>
            </div>
            <div class="time-machine-copy">
                <span>${t('timeTravel')}</span>
                <h3>${escapeHtml(item.title)}</h3>
                <p id="timeMachineText">${escapeHtml(item.afterText)}</p>
                <input type="range" min="0" max="100" value="64" class="time-machine-slider" id="timeMachineSlider" aria-label="${t('timeTravel')}">
                <small>${escapeHtml(item.detail)}</small>
            </div>
        </section>
    `;
}

function renderExperienceDossiers(spot) {
    const dossiers = Array.isArray(spot.dossiers) ? spot.dossiers : [];
    if (dossiers.length === 0) return '';

    return `
        <section class="experience-dossiers">
            <div class="experience-section-heading">
                <span>${t('dossierHeading')}</span>
                <h2>${t('dossierTitle')}</h2>
            </div>
            <div class="dossier-grid">
                ${dossiers.map(item => `
                    <button type="button" class="dossier-card" onclick="openExperienceDossier('${escapeHtml(item.id)}')">
                        <span>${escapeHtml(item.tag)}</span>
                        <strong>${escapeHtml(item.title)}</strong>
                        <small>${escapeHtml(item.focus)}</small>
                    </button>
                `).join('')}
            </div>
        </section>
    `;
}

function renderExperienceWalkRhythm(spot) {
    const items = Array.isArray(spot.walkRhythm) ? spot.walkRhythm : [];
    if (items.length === 0) return '';

    return `
        <section class="experience-walk-rhythm">
            <div class="experience-section-heading">
                <span>${t('walkRhythm')}</span>
                <h2>${t('walkRhythmTitle')}</h2>
            </div>
            <div class="walk-rhythm-track">
                ${items.map((item, index) => `
                    <article class="walk-rhythm-step">
                        <b>${index + 1}</b>
                        <div>
                            <span>${escapeHtml(item.time)}</span>
                            <h3>${escapeHtml(item.title)}</h3>
                            <p>${escapeHtml(item.text)}</p>
                        </div>
                    </article>
                `).join('')}
            </div>
        </section>
    `;
}

function renderExperienceStamp(spot) {
    if (!spot.stamp) return '';

    return `
        <section class="experience-stamp">
            <div>
                <span>${t('stampHeading')}</span>
                <h3>${escapeHtml(spot.stamp.title)}</h3>
                <p>${escapeHtml(spot.stamp.text)}</p>
            </div>
            <button type="button" onclick="stampExperiencePassport()">${escapeHtml(spot.stamp.code)}</button>
        </section>
    `;
}

function bindExperienceAdvancedControls(spot) {
    const slider = document.getElementById('timeMachineSlider');
    if (slider) {
        slider.oninput = () => updateExperienceTimeTravel(spot, Number(slider.value));
        updateExperienceTimeTravel(spot, Number(slider.value));
    }
}

function updateExperienceTimeTravel(spot, value) {
    const before = document.getElementById('timeMachineBefore');
    const divider = document.getElementById('timeMachineDivider');
    const text = document.getElementById('timeMachineText');
    const travel = spot.timeTravel;
    if (!before || !divider || !text || !travel) return;

    const progress = Math.max(0, Math.min(100, value));
    const visualWidth = before.parentElement?.getBoundingClientRect().width || 760;
    before.style.setProperty('--time-machine-width', `${Math.round(visualWidth)}px`);
    before.style.width = `${progress}%`;
    divider.style.left = `${progress}%`;
    text.textContent = progress < 48 ? travel.beforeText : travel.afterText;
}

function getExperienceDossier(dossierId) {
    const dossiers = Array.isArray(currentExperienceSpot?.dossiers) ? currentExperienceSpot.dossiers : [];
    return dossiers.find(item => item.id === dossierId) || dossiers[0] || null;
}

function openExperienceDossier(dossierId) {
    const dossier = getExperienceDossier(dossierId);
    if (!dossier) return;

    const existing = document.getElementById('experienceDossierModal');
    if (existing) existing.remove();

    const modal = document.createElement('div');
    modal.className = 'experience-dossier-modal active';
    modal.id = 'experienceDossierModal';
    modal.innerHTML = `
        <div class="experience-dossier-card">
            <button type="button" class="experience-dossier-close" onclick="closeExperienceDossier()" aria-label="关闭">×</button>
            <span>${escapeHtml(dossier.tag)}</span>
            <h3>${escapeHtml(dossier.title)}</h3>
            <p>${escapeHtml(dossier.text)}</p>
            <strong>${escapeHtml(dossier.focus)}</strong>
        </div>
    `;
    document.getElementById('experiencePage')?.appendChild(modal);
}

function closeExperienceDossier() {
    document.getElementById('experienceDossierModal')?.remove();
}

function stampExperiencePassport() {
    const button = document.querySelector('.experience-stamp button');
    if (!button) return;
    button.classList.add('stamped');
    button.textContent = t('stampedDone');
}

function observeExperienceStoryBlocks() {
    if (experienceStoryObserver) {
        experienceStoryObserver.disconnect();
        experienceStoryObserver = null;
    }

    const blocks = document.querySelectorAll('.experience-story-block');
    if (!('IntersectionObserver' in window) || blocks.length === 0) {
        blocks.forEach(block => block.classList.add('in-view'));
        return;
    }

    experienceStoryObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, { threshold: 0.22 });

    blocks.forEach(block => experienceStoryObserver.observe(block));
}

function applyLiteVrTransform() {
    const image = document.getElementById('liteVrImage');
    const hotspots = document.getElementById('liteVrHotspots');
    const transform = `translate3d(${liteVrState.offset}%, 0, 0)`;
    if (image) image.style.transform = transform;
    if (hotspots) hotspots.style.transform = transform;
}

function clampLiteVrOffset(value) {
    return Math.max(-42, Math.min(0, value));
}

function bindLiteVr(spot) {
    const stage = document.getElementById('liteVrStage');
    if (!stage) return;

    liteVrState = { dragging: false, startX: 0, startOffset: -18, offset: -18 };
    applyLiteVrTransform();

    stage.onpointerdown = event => {
        liteVrState.dragging = true;
        liteVrState.startX = event.clientX;
        liteVrState.startOffset = liteVrState.offset;
        stage.classList.add('dragging');
        stage.setPointerCapture?.(event.pointerId);
    };

    stage.onpointermove = event => {
        if (!liteVrState.dragging) return;
        const rect = stage.getBoundingClientRect();
        const deltaPercent = ((event.clientX - liteVrState.startX) / Math.max(1, rect.width)) * 42;
        liteVrState.offset = clampLiteVrOffset(liteVrState.startOffset + deltaPercent);
        applyLiteVrTransform();
    };

    stage.onpointerup = () => {
        liteVrState.dragging = false;
        stage.classList.remove('dragging');
    };

    stage.onpointercancel = stage.onpointerup;

    stage.querySelectorAll('.lite-vr-hotspot').forEach(button => {
        button.onclick = event => {
            event.stopPropagation();
            const hotspot = spot.liteHotspots[Number(button.dataset.hotspotIndex)];
            if (!hotspot) return;
            stage.querySelectorAll('.lite-vr-hotspot').forEach(item => item.classList.remove('active'));
            button.classList.add('active');
            document.getElementById('liteVrCaption').textContent = `${hotspot.title}：${hotspot.text}`;
            if (hotspot.dossierId) openExperienceDossier(hotspot.dossierId);
        };
    });
}

function switchExperienceVr(mode) {
    const litePanel = document.getElementById('vrLitePanel');
    const spherePanel = document.getElementById('vrSpherePanel');
    document.querySelectorAll('.vr-tabs button').forEach(button => {
        button.classList.toggle('active', button.dataset.vrTab === mode);
    });

    litePanel?.classList.toggle('active', mode === 'lite');
    spherePanel?.classList.toggle('active', mode === 'sphere');

    if (mode === 'sphere' && !sphereVrStarted) {
        sphereVrStarted = true;
        initSphereVr(currentExperienceSpot).catch(error => {
            console.error('360 VR 初始化失败:', error);
            const loading = document.getElementById('sphereVrLoading');
            if (loading) loading.textContent = '360 全景加载失败，当前环境可能无法访问 Three.js。';
        });
    }
}

function resetSphereVrView() {
    if (!sphereVrRuntime) return;
    sphereVrRuntime.yaw = 0;
    sphereVrRuntime.pitch = 0;
    if (sphereVrRuntime.camera) {
        sphereVrRuntime.camera.fov = 70;
        sphereVrRuntime.camera.updateProjectionMatrix();
    }
    updateSphereVrHud();
}

function zoomSphereVr(direction) {
    if (!sphereVrRuntime?.camera) return;
    sphereVrRuntime.camera.fov = Math.max(45, Math.min(88, sphereVrRuntime.camera.fov + direction * 5));
    sphereVrRuntime.camera.updateProjectionMatrix();
    updateSphereVrHud();
}

function updateSphereVrHud() {
    const direction = document.getElementById('sphereVrDirection');
    if (!direction || !sphereVrRuntime?.camera) return;

    const yaw = Math.round((((sphereVrRuntime.yaw % 360) + 540) % 360) - 180);
    const label = Math.abs(yaw) < 12 ? '正前方' : yaw > 0 ? '向右环视' : '向左环视';
    direction.textContent = `${label} ${Math.abs(yaw)}° · 视野 ${Math.round(sphereVrRuntime.camera.fov)}°`;
}

function destroySphereVr() {
    if (!sphereVrRuntime) return;
    sphereVrRuntime.stop = true;
    sphereVrRuntime.renderer?.dispose?.();
    sphereVrRuntime.geometry?.dispose?.();
    sphereVrRuntime.material?.dispose?.();
    sphereVrRuntime.texture?.dispose?.();
    sphereVrRuntime = null;
}

async function initSphereVr(spot) {
    if (!spot) return;
    destroySphereVr();

    const canvas = document.getElementById('sphereVrCanvas');
    const stage = document.getElementById('sphereVrStage');
    const loading = document.getElementById('sphereVrLoading');
    if (!canvas || !stage) return;

    const THREE = await import('https://unpkg.com/three@0.164.1/build/three.module.js');
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(70, 1, 0.1, 1000);
    camera.position.set(0, 0, 0.01);

    const geometry = new THREE.SphereGeometry(500, 64, 40);
    geometry.scale(-1, 1, 1);
    const texture = await new THREE.TextureLoader().loadAsync(spot.sphereImage);
    texture.colorSpace = THREE.SRGBColorSpace;
    const material = new THREE.MeshBasicMaterial({ map: texture });
    scene.add(new THREE.Mesh(geometry, material));

    const runtime = {
        renderer,
        geometry,
        material,
        texture,
        stop: false,
        dragging: false,
        yaw: 0,
        pitch: 0,
        startX: 0,
        startY: 0,
        startYaw: 0,
        startPitch: 0,
        camera
    };
    sphereVrRuntime = runtime;
    if (loading) loading.style.display = 'none';

    function resizeSphere() {
        const rect = stage.getBoundingClientRect();
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
        renderer.setSize(rect.width, rect.height, false);
        camera.aspect = rect.width / Math.max(1, rect.height);
        camera.updateProjectionMatrix();
    }

    function renderSphere() {
        if (runtime.stop) return;
        const phi = THREE.MathUtils.degToRad(90 - runtime.pitch);
        const theta = THREE.MathUtils.degToRad(runtime.yaw);
        camera.lookAt(
            Math.sin(phi) * Math.cos(theta),
            Math.cos(phi),
            Math.sin(phi) * Math.sin(theta)
        );
        renderer.render(scene, camera);
        requestAnimationFrame(renderSphere);
    }

    stage.onpointerdown = event => {
        runtime.dragging = true;
        runtime.startX = event.clientX;
        runtime.startY = event.clientY;
        runtime.startYaw = runtime.yaw;
        runtime.startPitch = runtime.pitch;
        stage.classList.add('dragging');
        stage.setPointerCapture?.(event.pointerId);
    };

    stage.onpointermove = event => {
        if (!runtime.dragging) return;
        runtime.yaw = runtime.startYaw - (event.clientX - runtime.startX) * 0.16;
        runtime.pitch = Math.max(-62, Math.min(62, runtime.startPitch + (event.clientY - runtime.startY) * 0.12));
        updateSphereVrHud();
    };

    stage.onpointerup = () => {
        runtime.dragging = false;
        stage.classList.remove('dragging');
    };
    stage.onpointercancel = stage.onpointerup;

    stage.onwheel = event => {
        event.preventDefault();
        camera.fov = Math.max(45, Math.min(88, camera.fov + Math.sign(event.deltaY) * 3));
        camera.updateProjectionMatrix();
        updateSphereVrHud();
    };

    window.addEventListener('resize', resizeSphere, { passive: true });
    resizeSphere();
    updateSphereVrHud();
    renderSphere();
}

// 渲染顶部推荐卡片（4个）
async function renderHeroCards(posts) {
    const container = document.getElementById('heroScroll');
    console.log('heroScroll容器:', container);
    if (!container) {
        console.error('heroScroll容器不存在！');
        return;
    }
    
    let html = '';
    const displayPosts = await Promise.all((posts || []).map(post => localizePostSummary(post)));
    console.log('要渲染的推荐帖子数量:', displayPosts.length);
    
    displayPosts.forEach(post => {
        const photoSrc = post.photos && post.photos.length > 0 
            ? post.photos[0] 
            : `https://picsum.photos/400/600?random=${post.id}`;
        
        html += `
            <div class="hero-card" style="background-image: url('${photoSrc}');" onclick="openPostDetail(${post.id})">
                <div class="card-text-top">
                    <p>${escapeHtml(formatPostDate(post.publish_time))}</p>
                </div>
                <div class="card-bottom-glass">
                    <h2>${post.title}</h2>
                    <span>👥 ${post.likes || 0} ${t('likes')}</span>
                </div>
            </div>
        `;
    });
    
    console.log('生成的HTML长度:', html.length);
    container.innerHTML = html;
    console.log('推荐卡片渲染完成');
}

// 渲染帖子列表
async function renderPosts(posts) {
    const container = document.getElementById('postsContainer');
    console.log('postsContainer容器:', container);
    if (!container) {
        console.error('postsContainer容器不存在！');
        return;
    }
    
    let html = '';
    const displayPosts = await Promise.all((posts || []).map(post => localizePostSummary(post)));
    console.log('要渲染的帖子列表数量:', displayPosts.length);
    
    // 获取当前用户的关注列表
    const followers = await getFollowers();
    
    displayPosts.forEach(post => {
        const photoSrc = post.photos && post.photos.length > 0 
            ? post.photos[0] 
            : `https://picsum.photos/400/300?random=${post.id}`;
        
        // 解析作者头像
        let authorAvatar = '👤';
        if (post.author_avatar) {
            try {
                const avatarData = JSON.parse(post.author_avatar);
                authorAvatar = avatarData.type === 'preset' ? avatarData.emoji : avatarData.data;
            } catch (e) {
                authorAvatar = '👤';
            }
        }
        
        const isImageAvatar = typeof authorAvatar === 'string' && (authorAvatar.includes('http') || authorAvatar.includes('data:'));
        
        html += `
            <div class="post-card" onclick="openPostDetail(${post.id})" role="button" tabindex="0" onkeydown="if(event.currentTarget === event.target && (event.key === 'Enter' || event.key === ' ')) { event.preventDefault(); openPostDetail(${post.id}); }">
                <div class="post-image-wrapper">
                    <img src="${photoSrc}" alt="${post.title}" class="post-image">
                </div>
                <div class="post-info">
                    <h3 class="post-title-text">${post.title}</h3>
                    <div class="post-author-row">
                            ${isImageAvatar ? `<img src="${authorAvatar}" alt="${post.author}" class="post-author-avatar">` : `<span class="post-author-emoji">${authorAvatar}</span>`}
                            <div class="post-author-info">
                                <p class="post-author">${post.author}</p>
                            </div>
                            <button class="follow-btn ${followers.includes(post.author) ? 'following' : ''}" onclick="event.stopPropagation(); handleFollowFromHome('${post.author}', this)">
                                ${followers.includes(post.author) ? t('following') : t('follow')}
                            </button>
                        </div>
                    <p class="post-location">📍 ${post.location}</p>
                    <div class="post-stats-row">
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 14.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg> ${post.views || 0}</span>
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg> ${post.likes || 0}</span>
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> ${post.comments || 0}</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    console.log('帖子列表HTML长度:', html.length);
    container.innerHTML = html;
    console.log('帖子列表渲染完成');
}

// 回到顶部函数
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function showEmptyState() {
    const container = document.getElementById('postsContainer');
    container.innerHTML = renderEmptyState(t('noPosts'), t('publishFirstHint'));
}

// 编辑帖子
async function editPost(postId) {
    try {
        const response = await fetchWithTimeout(`/post/${postId}`);
        const post = await response.json();
        
        if (response.ok) {
            // 打开编辑弹窗
            openEditModal(post);
        }
    } catch (error) {
        console.error("获取帖子失败:", error);
        alert(t('requestFailed', { detail: t('editPost') }));
    }
}

// 删除帖子
async function deletePost(postId) {
    if (!confirm(t('deleteConfirm'))) {
        return;
    }
    
    try {
        const response = await fetch(`/post/${postId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            alert(t('deleteSuccess'));
            loadMyPosts();
        } else {
            alert(t('deleteFailed'));
        }
    } catch (error) {
        console.error("删除失败:", error);
        alert(t('deleteFailed'));
    }
}

// 打开编辑弹窗
function openEditModal(post) {
    const editModal = document.createElement('div');
    editModal.className = 'edit-modal';
    editModal.id = 'editModal';
    editModal.innerHTML = `
        <div class="edit-modal-wrapper">
            <div class="edit-header">
                <h2>${t('editPost')}</h2>
                <button class="edit-close" onclick="closeEditModal()">
                    <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <div class="edit-content">
                <input type="text" id="editTitle" placeholder="${t('postTitle')}" value="${post.title}">
                <input type="text" id="editLocation" placeholder="${t('place')}" value="${post.location || ''}">
                <input type="number" id="editDuration" placeholder="${t('duration')}" value="${post.duration || 1}">
                <input type="number" id="editPeople" placeholder="${t('peoplePlaceholder')}" value="${post.people || 1}">
            </div>
            <div class="edit-actions">
                <button class="edit-cancel-btn" onclick="closeEditModal()">${t('cancel')}</button>
                <button class="edit-save-btn" onclick="saveEdit(${post.id})">${t('saveChanges')}</button>
            </div>
        </div>
    `;
    document.body.appendChild(editModal);
    setTimeout(() => {
        editModal.classList.add('active');
    }, 10);
}

// 关闭编辑弹窗
function closeEditModal() {
    const editModal = document.getElementById('editModal');
    if (editModal) {
        editModal.classList.remove('active');
        setTimeout(() => {
            editModal.remove();
        }, 300);
    }
}

// 保存编辑
async function saveEdit(postId) {
    const title = document.getElementById('editTitle').value.trim();
    const location = document.getElementById('editLocation').value.trim();
    const duration = parseInt(document.getElementById('editDuration').value) || 1;
    const people = parseInt(document.getElementById('editPeople').value) || 1;
    
    if (!title) {
        alert(t('inputPostTitle'));
        return;
    }
    
    try {
        const response = await fetch(`/post/${postId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title,
                location,
                duration,
                people
            })
        });
        
        if (response.ok) {
            alert(t('saveSuccess'));
            closeEditModal();
            loadMyPosts();
        } else {
            alert(t('requestFailed', { detail: t('saveChanges') }));
        }
    } catch (error) {
        console.error("保存失败:", error);
        alert(t('requestFailed', { detail: t('saveChanges') }));
    }
}

function formatPostDate(dateStr) {
    const date = new Date(dateStr);
    const today = new Date();
    const yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 1);
    
    if (date.toDateString() === today.toDateString()) {
        return t('today');
    } else if (date.toDateString() === yesterday.toDateString()) {
        return t('yesterday');
    } else {
        return t('monthDay', { month: date.getMonth() + 1, day: date.getDate() });
    }
}

// ==================== 帖子详情页功能 ====================
let currentPost = null;
let currentPostSource = null;

function heartSvg() {
    return '<svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.08C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>';
}

function renderLikeButton(likeBtn, likes, isLiked) {
    if (!likeBtn) return;
    likeBtn.innerHTML = `
        ${heartSvg()}
        <span>${likes || 0}</span>
    `;
    likeBtn.classList.toggle('liked', Boolean(isLiked));
}

function openPostDetail(postId) {
    loadPostDetail(postId);
}

let activeGuideAudio = null;
let activeGuideUtterance = null;
let activeGuideAudioTarget = null;
let activeGuideSpeechTimer = null;
let activeGuideSpeechSession = 0;
let currentGuideDetailIndex = null;
let currentGuideDetailDisplayIndex = null;
let guideCompletionMode = false;
let commentSubmitting = false;
let activeGuideRouteId = null;
let guideUserLocation = null;
let guideLocationStatus = 'idle';
let guideLocationRequested = false;
let routeMapViewState = { scale: 1, x: 0, y: 0 };

function ensureDetailFloatingLayers() {
    const detailPage = document.getElementById('detailPage');
    const actionBar = document.querySelector('.action-bar');
    if (detailPage && actionBar && actionBar.parentElement !== detailPage) {
        detailPage.appendChild(actionBar);
    }
}

function isSameGuideAudioTarget(target) {
    if (!activeGuideAudioTarget || !target) return false;
    return activeGuideAudioTarget.type === target.type && activeGuideAudioTarget.index === target.index;
}

function getLanguageAudioUrl(source, key) {
    if (!source) return '';
    const englishKey = `${key}_en`;
    if (currentLanguage === 'en' && source[englishKey] && !source[englishKey].includes('placeholder')) {
        return source[englishKey];
    }
    return source[key] && !source[key].includes('placeholder') ? source[key] : '';
}

function normalizeGuideSpeechText(text) {
    return String(text || '')
        .replace(/\s+/g, ' ')
        .replace(/([。！？；.!?])\s*/g, '$1 ')
        .replace(/([，、：,:])\s*/g, '$1 ')
        .trim();
}

function splitGuideSpeechText(text) {
    const normalized = normalizeGuideSpeechText(text);
    if (!normalized) return [];
    const sentences = normalized.match(/[^。！？；.!?]+[。！？；.!?]?/g) || [normalized];
    const chunks = [];
    let current = '';
    sentences.forEach(sentence => {
        const next = `${current}${sentence}`.trim();
        if (next.length > 140 && current) {
            chunks.push(current.trim());
            current = sentence.trim();
        } else {
            current = next;
        }
    });
    if (current) chunks.push(current.trim());
    return chunks;
}

function getFallbackVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices?.() || [];
    const langPrefix = currentLanguage === 'en' ? 'en' : 'zh';
    return voices.find(voice => (voice.lang || '').toLowerCase().startsWith(langPrefix))
        || voices.find(voice => (voice.lang || '').toLowerCase().startsWith('zh'))
        || voices[0]
        || null;
}

function createFallbackUtterance(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = currentLanguage === 'en' ? 'en-US' : 'zh-CN';
    utterance.rate = currentLanguage === 'en' ? 0.9 : 0.86;
    utterance.pitch = currentLanguage === 'en' ? 1 : 1.08;
    const voice = getFallbackVoice();
    if (voice) utterance.voice = voice;
    return utterance;
}

function getGuideItemSpeechText(item) {
    if (!item) return t('noGuideText');
    return [
        item.title,
        item.time,
        item.detail || item.text || t('noGuideText')
    ].filter(Boolean).join('。');
}

function getPostGuideSpeechText(post) {
    if (!post) return t('noGuideText');
    const guideItems = Array.isArray(post.guide_items) ? post.guide_items : [];
    const activeRoute = getActiveGuideRoute(getRouteMap(post));
    const orderedItems = getRouteGuideItemsOnly(guideItems, activeRoute)
        .map(({ item }, index) => `${currentLanguage === 'en' ? `Stop ${index + 1}` : `第${index + 1}站`}，${item.title || t('guidePoint')}。${item.text || ''}`);

    return [
        post.title,
        post.content || t('noGuideText'),
        activeRoute?.title,
        activeRoute?.description || activeRoute?.estimate_note,
        orderedItems.join('。')
    ].filter(Boolean).join('。');
}

function updateGuideAudioControls() {
    const isPostPlaying = activeGuideAudioTarget?.type === 'post';
    document.querySelectorAll('.guide-main-play').forEach(button => {
        button.classList.toggle('playing', isPostPlaying);
        button.innerHTML = isPostPlaying
            ? `<span>Ⅱ</span>${t('pauseAudio')}`
            : `<span>▶</span>${t('playGuide')}`;
    });

    const centerPlay = document.querySelector('.play-btn');
    if (centerPlay) {
        centerPlay.classList.toggle('playing', isPostPlaying);
        centerPlay.innerHTML = isPostPlaying
            ? `<span class="pause-icon">Ⅱ</span>`
            : `<svg width="20" height="20" viewBox="0 0 24 24" fill="#e6b85c"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>`;
    }

    document.querySelectorAll('.guide-audio-btn').forEach(button => {
        const index = Number(button.dataset.guideAudioIndex);
        const isPlaying = activeGuideAudioTarget?.type === 'guide' && activeGuideAudioTarget.index === index;
        button.classList.toggle('playing', isPlaying);
        button.textContent = isPlaying ? 'Ⅱ' : '▶';
        button.setAttribute('aria-label', isPlaying ? t('pauseAudio') : t('playAudio'));
    });

    const detailPlay = document.getElementById('guideDetailPlay');
    if (detailPlay) {
        if (guideCompletionMode) {
            updateGuideCompletionStampState();
            return;
        }
        const isDetailPlaying = activeGuideAudioTarget?.type === 'guide' && activeGuideAudioTarget.index === currentGuideDetailIndex;
        detailPlay.classList.toggle('playing', isDetailPlaying);
        detailPlay.textContent = isDetailPlaying ? t('pauseAudio') : t('playAudio');
    }
}

function stopGuideAudio() {
    activeGuideSpeechSession += 1;
    if (activeGuideSpeechTimer) {
        clearTimeout(activeGuideSpeechTimer);
        activeGuideSpeechTimer = null;
    }

    if (activeGuideAudio) {
        activeGuideAudio.pause();
        activeGuideAudio.currentTime = 0;
        activeGuideAudio = null;
    }

    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    activeGuideUtterance = null;
    activeGuideAudioTarget = null;
    updateGuideAudioControls();
}

function speakGuideFallback(text, target = null) {
    if (!('speechSynthesis' in window)) {
        stopGuideAudio();
        alert(t('speechUnsupported'));
        return;
    }

    stopGuideAudio();
    const chunks = splitGuideSpeechText(text);
    if (chunks.length === 0) {
        alert(t('speechUnsupported'));
        return;
    }

    showToast(t('speechFallback'), { type: 'warning' });
    const session = activeGuideSpeechSession + 1;
    activeGuideSpeechSession = session;
    activeGuideAudioTarget = target;

    const speakChunk = index => {
        if (activeGuideSpeechSession !== session) return;
        const utterance = createFallbackUtterance(chunks[index]);
        activeGuideUtterance = utterance;
        utterance.onend = () => {
            if (activeGuideSpeechSession !== session) return;
            if (index < chunks.length - 1) {
                activeGuideSpeechTimer = setTimeout(() => speakChunk(index + 1), 180);
                return;
            }
            activeGuideUtterance = null;
            activeGuideAudioTarget = null;
            updateGuideAudioControls();
        };
        utterance.onerror = utterance.onend;
        window.speechSynthesis.speak(utterance);
    };

    updateGuideAudioControls();
    speakChunk(0);
}

function handleGuideAudioError(text = '', target = null) {
    stopGuideAudio();
    speakGuideFallback(text, target);
}

function playGuideAudio(index) {
    const item = currentPost?.guide_items?.[index];
    if (!item) return;
    const target = { type: 'guide', index };

    if (isSameGuideAudioTarget(target)) {
        stopGuideAudio();
        return;
    }

    const audioUrl = getLanguageAudioUrl(item, 'audio');
    if (audioUrl) {
        stopGuideAudio();
        activeGuideAudio = new Audio(audioUrl);
        activeGuideAudioTarget = target;
        activeGuideAudio.onended = stopGuideAudio;
        activeGuideAudio.onerror = () => handleGuideAudioError(getGuideItemSpeechText(item), target);
        updateGuideAudioControls();
        activeGuideAudio.play().catch(() => handleGuideAudioError(getGuideItemSpeechText(item), target));
        return;
    }

    speakGuideFallback(getGuideItemSpeechText(item), target);
}

function getGuideItem(index) {
    const guideItems = Array.isArray(currentPost?.guide_items) ? currentPost.guide_items : [];
    return guideItems[index] || null;
}

function formatGuideDistance(km) {
    if (!Number.isFinite(km)) return '--';
    if (km < 1) return `${Math.max(20, Math.round(km * 1000 / 10) * 10)}m`;
    return `${km.toFixed(km < 10 ? 1 : 0)}km`;
}

function getCurrentGuideRouteContext() {
    const guideItems = Array.isArray(currentPost?.guide_items) ? currentPost.guide_items : [];
    const routeMap = getRouteMap(currentPost);
    const activeRoute = getActiveGuideRoute(routeMap);
    const ordered = getRouteGuideItemsOnly(guideItems, activeRoute);
    const position = getCurrentGuideRoutePosition();
    return { guideItems, routeMap, activeRoute, ordered, position };
}

function calculateRemainingGuideDistance(ordered, position) {
    if (!Array.isArray(ordered) || position < 0) return Number.POSITIVE_INFINITY;
    let total = 0;
    for (let i = position; i < ordered.length - 1; i += 1) {
        const from = ordered[i]?.item;
        const to = ordered[i + 1]?.item;
        const distance = calculateDistanceKm(from, to);
        if (Number.isFinite(distance)) total += distance;
    }
    return total;
}

function findNearestGuideRoutePosition(ordered) {
    if (!guideUserLocation || !Array.isArray(ordered) || ordered.length === 0) return 0;
    let nearestIndex = 0;
    let nearestDistance = Number.POSITIVE_INFINITY;
    ordered.forEach(({ item }, index) => {
        const distance = calculateDistanceKm(guideUserLocation, item);
        if (distance < nearestDistance) {
            nearestDistance = distance;
            nearestIndex = index;
        }
    });
    return nearestIndex;
}

function renderGuideProgressStrip(ordered, position) {
    const stops = Array.isArray(ordered) ? ordered : [];
    if (stops.length === 0) return '';

    return `
        <div class="guide-progress-strip" aria-label="${t('routeStops')}">
            <div class="guide-progress-text">${Math.max(1, position + 1)} / ${stops.length}</div>
            <div class="guide-progress-dots">
                ${stops.map(({ item, index }, stopIndex) => `
                    <button type="button" class="guide-progress-dot ${stopIndex < position ? 'done' : ''} ${stopIndex === position ? 'active' : ''}" onclick="openGuideDetail(${Number(index)}, ${stopIndex})" aria-label="${escapeHtml(item?.title || t('guidePoint'))}">
                        ${stopIndex + 1}
                    </button>
                `).join('')}
            </div>
        </div>
    `;
}

function renderGuideLiveStatus() {
    const container = document.getElementById('guideDetailLive');
    if (!container) return;
    if (guideCompletionMode || currentGuideDetailIndex === null) {
        container.innerHTML = '';
        container.hidden = true;
        return;
    }

    const { activeRoute, ordered, position } = getCurrentGuideRouteContext();
    const current = ordered[position]?.item || getGuideItem(currentGuideDetailIndex);
    const next = ordered[position + 1]?.item || null;
    const distanceToCurrent = guideUserLocation ? calculateDistanceKm(guideUserLocation, current) : Number.POSITIVE_INFINITY;
    const remainingDistance = calculateRemainingGuideDistance(ordered, Math.max(0, position));
    const isOffRoute = Number.isFinite(distanceToCurrent) && distanceToCurrent > 0.8;
    const locationText = guideUserLocation
        ? t('distanceToStop', { distance: formatGuideDistance(distanceToCurrent) })
        : (guideLocationStatus === 'locating' ? t('locatingUser') : t('locationDeniedHint'));

    container.hidden = false;
    container.innerHTML = `
        <section class="guide-live-card">
            <div class="guide-live-heading">
                <span>${t('liveRoute')}</span>
                <strong>${escapeHtml(activeRoute?.title || t('recommendedRoute'))}</strong>
            </div>
            <div class="guide-live-grid">
                <div>
                    <span>${t('currentStopLabel')}</span>
                    <strong>${escapeHtml(current?.title || t('guidePoint'))}</strong>
                    <small>${locationText}</small>
                </div>
                <div>
                    <span>${t('nextTargetLabel')}</span>
                    <strong>${escapeHtml(next?.title || t('completionStamp'))}</strong>
                    <small>${Number.isFinite(remainingDistance) ? t('remainingEstimate', { distance: formatGuideDistance(remainingDistance) }) : t('routeActionHint')}</small>
                </div>
            </div>
            <div class="guide-route-alert ${isOffRoute ? 'off' : 'on'}">${isOffRoute ? t('offRouteHint') : t('onRouteHint')}</div>
            ${renderGuideProgressStrip(ordered, Math.max(0, position))}
            <div class="guide-live-actions">
                <button type="button" onclick="skipCurrentGuideStop()" ${position >= ordered.length - 1 ? 'disabled' : ''}>${t('skipStop')}</button>
                <button type="button" onclick="switchToShortGuideRoute()">${t('switchShortRoute')}</button>
                <button type="button" onclick="returnToNearestGuideRoute()">${t('returnToRoute')}</button>
            </div>
        </section>
    `;
}

function requestGuideUserLocation({ force = false } = {}) {
    if (!navigator.geolocation) {
        guideLocationStatus = 'unavailable';
        renderGuideLiveStatus();
        return;
    }
    if (guideLocationRequested && !force) return;
    guideLocationRequested = true;
    guideLocationStatus = 'locating';
    renderGuideLiveStatus();

    navigator.geolocation.getCurrentPosition(
        position => {
            guideUserLocation = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude
            };
            guideLocationStatus = 'ready';
            renderGuideLiveStatus();
        },
        () => {
            guideLocationStatus = 'denied';
            renderGuideLiveStatus();
        },
        { timeout: 5000, maximumAge: 30000, enableHighAccuracy: true }
    );
}

function skipCurrentGuideStop() {
    moveGuideDetail(1);
}

function getShortestGuideRoute(routeMap) {
    const routes = Array.isArray(routeMap?.routes) ? routeMap.routes : [];
    if (routes.length === 0) return null;
    return [...routes].sort((a, b) => {
        const aStops = Array.isArray(a.stops) ? a.stops.length : Number.POSITIVE_INFINITY;
        const bStops = Array.isArray(b.stops) ? b.stops.length : Number.POSITIVE_INFINITY;
        return aStops - bStops;
    })[0];
}

function switchToShortGuideRoute() {
    if (!currentPost) return;
    const guideItems = Array.isArray(currentPost.guide_items) ? currentPost.guide_items : [];
    const routeMap = getRouteMap(currentPost);
    const shortest = getShortestGuideRoute(routeMap);
    const activeRoute = getActiveGuideRoute(routeMap);
    if (!shortest || shortest.id === activeRoute?.id) {
        showToast(t('noShortRoute'), { type: 'warning' });
        return;
    }

    activeGuideRouteId = shortest.id;
    const ordered = getRouteGuideItemsOnly(guideItems, shortest);
    const nearestPosition = findNearestGuideRoutePosition(ordered);
    const target = ordered[nearestPosition] || ordered[0];
    showToast(t('shortRouteApplied'), { detail: shortest.title || t('recommendedRoute') });
    if (currentPost) renderGuideSection(currentPost);
    if (target) openGuideDetail(target.index, nearestPosition);
}

function returnToNearestGuideRoute() {
    const { ordered } = getCurrentGuideRouteContext();
    if (!ordered.length) return;
    const nearestPosition = findNearestGuideRoutePosition(ordered);
    const target = ordered[nearestPosition] || ordered[0];
    showToast(t('routeReturned'), { detail: target?.item?.title || t('guidePoint') });
    if (target) openGuideDetail(target.index, nearestPosition);
}

function openGuideDetail(index, displayIndex = null) {
    const item = getGuideItem(index);
    if (!item) return;
    ensureDetailFloatingLayers();
    guideCompletionMode = false;

    currentGuideDetailIndex = index;
    currentGuideDetailDisplayIndex = Number.isFinite(displayIndex) ? displayIndex : index;
    const panel = document.getElementById('guideDetailPanel');
    const title = document.getElementById('guideDetailTitle');
    const indexEl = document.getElementById('guideDetailIndex');
    const text = document.getElementById('guideDetailText');
    const images = document.getElementById('guideDetailImages');
    const itemImages = Array.isArray(item.images) && item.images.length > 0
        ? item.images
        : [item.image].filter(Boolean);

    title.textContent = item.title || `${t('guidePoint')} ${index + 1}`;
    indexEl.textContent = item.time
        ? `${t('stopLabel', { index: currentGuideDetailDisplayIndex + 1 })} · ${item.time}`
        : t('stopLabel', { index: currentGuideDetailDisplayIndex + 1 });
    text.textContent = item.detail || item.text || t('noGuideDetail');
    images.innerHTML = itemImages.map((src, imageIndex) => `
        <img src="${escapeHtml(src)}" alt="${escapeHtml(item.title || t('guideImage'))} ${imageIndex + 1}" onclick="openImageViewerFromElement(this)" onkeydown="if(event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openImageViewerFromElement(this); }" tabindex="0" role="button" data-image-src="${escapeHtml(src)}" data-image-alt="${escapeHtml(item.title || t('guideImage'))} ${imageIndex + 1}">
    `).join('');
    renderGuideLiveStatus();
    requestGuideUserLocation();
    const nav = document.getElementById('guideDetailNav');
    if (nav) nav.textContent = t('navigateThere');
    const play = document.getElementById('guideDetailPlay');
    if (play) play.classList.remove('stamped');
    updateGuideDetailStepButtons();
    updateGuideAudioControls();

    panel.classList.remove('completion-mode');
    panel.classList.add('active');
    panel.scrollTop = 0;
    stopGuideAudio();
}

function closeGuideDetail() {
    document.getElementById('guideDetailPanel')?.classList.remove('active');
    document.getElementById('guideDetailPanel')?.classList.remove('completion-mode');
    const live = document.getElementById('guideDetailLive');
    if (live) {
        live.innerHTML = '';
        live.hidden = true;
    }
    currentGuideDetailIndex = null;
    currentGuideDetailDisplayIndex = null;
    guideCompletionMode = false;
    updateGuideAudioControls();
}

function playCurrentGuideDetail() {
    if (guideCompletionMode) {
        stampCurrentGuide();
        return;
    }
    if (currentGuideDetailIndex === null) return;
    playGuideAudio(currentGuideDetailIndex);
}

function navigateCurrentGuide() {
    if (guideCompletionMode) {
        showMyGuideStamps();
        return;
    }
    const item = getGuideItem(currentGuideDetailIndex);
    if (!item || item.latitude === undefined || item.longitude === undefined) {
        alert('当前导览点暂未设置导航坐标。');
        return;
    }

    const label = encodeURIComponent(item.title || t('guidePoint'));
    const url = `https://maps.apple.com/?ll=${item.latitude},${item.longitude}&q=${label}`;
    window.open(url, '_blank');
}

function navigatePostLocation() {
    if (!currentPost) return;
    const lat = Number(currentPost.latitude);
    const lng = Number(currentPost.longitude);
    const label = encodeURIComponent(currentPost.location || currentPost.title || t('attractionGuide'));
    const url = Number.isFinite(lat) && Number.isFinite(lng)
        ? `https://maps.apple.com/?ll=${lat},${lng}&q=${label}`
        : `https://maps.apple.com/?q=${label}`;
    window.open(url, '_blank');
}

window.openGuideDetail = openGuideDetail;
window.closeGuideDetail = closeGuideDetail;
window.playCurrentGuideDetail = playCurrentGuideDetail;
window.navigateCurrentGuide = navigateCurrentGuide;
window.playGuideAudio = playGuideAudio;
window.playPostAudio = playPostAudio;
window.navigatePostLocation = navigatePostLocation;
window.startGuideRoute = startGuideRoute;
window.saveCurrentGuideRoute = saveCurrentGuideRoute;
window.shareCurrentGuideRoute = shareCurrentGuideRoute;
window.stampCurrentGuide = stampCurrentGuide;
window.showMyGuideStamps = showMyGuideStamps;
window.skipCurrentGuideStop = skipCurrentGuideStop;
window.switchToShortGuideRoute = switchToShortGuideRoute;
window.returnToNearestGuideRoute = returnToNearestGuideRoute;

function getRouteMap(post) {
    if (!post || !post.route_map || Array.isArray(post.route_map)) return null;
    const routes = Array.isArray(post.route_map.routes) ? post.route_map.routes : [];
    return routes.length > 0 ? post.route_map : null;
}

function getActiveGuideRoute(routeMap) {
    const routes = Array.isArray(routeMap?.routes) ? routeMap.routes : [];
    if (routes.length === 0) return null;
    return routes.find(route => route.id === activeGuideRouteId)
        || routes.find(route => route.id === routeMap.default_route)
        || routes[0];
}

function getOrderedGuideItemsForRoute(guideItems, route) {
    const ordered = [];
    const usedIndexes = new Set();
    const routeStops = Array.isArray(route?.stops) ? route.stops : [];

    routeStops.forEach(index => {
        const numericIndex = Number(index);
        if (!Number.isInteger(numericIndex) || numericIndex < 0 || numericIndex >= guideItems.length) return;
        if (usedIndexes.has(numericIndex)) return;
        usedIndexes.add(numericIndex);
        ordered.push({
            item: guideItems[numericIndex],
            index: numericIndex,
            inActiveRoute: true,
        });
    });

    guideItems.forEach((item, index) => {
        if (usedIndexes.has(index)) return;
        ordered.push({
            item,
            index,
            inActiveRoute: false,
        });
    });

    return ordered;
}

function getRouteGuideItemsOnly(guideItems, route) {
    const routeStops = Array.isArray(route?.stops) ? route.stops : [];
    const ordered = routeStops
        .map(index => Number(index))
        .filter((index, position, list) => Number.isInteger(index) && list.indexOf(index) === position)
        .filter(index => index >= 0 && index < guideItems.length)
        .map(index => ({
            item: guideItems[index],
            index,
            inActiveRoute: true
        }));

    return ordered.length > 0
        ? ordered
        : guideItems.map((item, index) => ({ item, index, inActiveRoute: true }));
}

function getCurrentOrderedGuideItems() {
    const guideItems = Array.isArray(currentPost?.guide_items) ? currentPost.guide_items : [];
    const activeRoute = getActiveGuideRoute(getRouteMap(currentPost));
    return getRouteGuideItemsOnly(guideItems, activeRoute);
}

function getCurrentGuideRoutePosition() {
    if (currentGuideDetailIndex === null) return -1;
    const ordered = getCurrentOrderedGuideItems();
    const byDisplayIndex = Number.isInteger(currentGuideDetailDisplayIndex)
        ? ordered[currentGuideDetailDisplayIndex]
        : null;
    if (byDisplayIndex && byDisplayIndex.index === currentGuideDetailIndex) {
        return currentGuideDetailDisplayIndex;
    }
    return ordered.findIndex(({ index }) => index === currentGuideDetailIndex);
}

function getStampStorageKey() {
    const username = localStorage.getItem('username') || 'guest';
    return `guideStamps_${username}`;
}

function cleanStampTitle(value) {
    return String(value || t('attractionGuide'))
        .replace(t('stampPostfix'), '')
        .split(/[：:｜|,·-]/)[0]
        .replace(/(导览|路线|游览|体验)$/g, '')
        .trim() || t('attractionGuide');
}

function cleanStoredRouteTitle(stamp) {
    const routeTitle = String(stamp?.routeTitle || '').trim();
    if (routeTitle) return cleanStampTitle(routeTitle);
    const code = String(stamp?.stampCode || '');
    const codeRoute = code.includes('·') ? code.split('·').pop() : code;
    return cleanStampTitle(codeRoute || stamp?.title);
}

function normalizeGuideStamp(stamp) {
    if (!stamp || typeof stamp !== 'object') return stamp;
    const baseTitle = cleanStampTitle(stamp.title || stamp.stampTitle);
    const routeTitle = cleanStoredRouteTitle(stamp);
    const city = getStampCityLabel(stamp);
    const text = String(stamp.text || '');
    const shouldRegenerateText = !text || text.length > 86 || /建议|进入|参观|最后|依次|路线/.test(text);

    return {
        ...stamp,
        title: baseTitle,
        routeTitle,
        stampTitle: stamp.stampTitle && stamp.stampTitle.length <= 24
            ? stamp.stampTitle
            : `${baseTitle}${t('stampPostfix')}`,
        stampCode: stamp.stampCode && stamp.stampCode.length <= 30
            ? stamp.stampCode
            : `${baseTitle} · ${routeTitle}`,
        text: shouldRegenerateText
            ? `你不是“经过”了${baseTitle}，而是读完了一段${city}值得停留的文化记忆。`
            : text
    };
}

function getGuideStamps() {
    try {
        const stamps = JSON.parse(localStorage.getItem(getStampStorageKey()) || '[]');
        return Array.isArray(stamps) ? stamps.map(normalizeGuideStamp) : [];
    } catch (error) {
        return [];
    }
}

function saveGuideStamps(stamps) {
    localStorage.setItem(getStampStorageKey(), JSON.stringify(stamps));
}

function getStampBaseTitle(post) {
    const rawTitle = post?.stamp?.place || post?.title || t('attractionGuide');
    return String(rawTitle)
        .split(/[：:｜|,-]/)[0]
        .replace(/(导览|路线|游览|体验)$/g, '')
        .trim() || t('attractionGuide');
}

function getStampRouteTitle(route, post) {
    const rawTitle = route?.stampTitle || route?.title || post?.route_map?.title || t('routeOverview');
    return String(rawTitle)
        .replace(/^(推荐|经典|精选)?路线[：:]/, '')
        .replace(/(游览|导览|路线)$/g, '')
        .trim() || t('routeOverview');
}

function getStampCityLabel(post) {
    const rawCity = String(post?.city || post?.location || '').trim();
    const city = rawCity
        .split(/[，,·\s]/)[0]
        .replace(/市$/, '')
        .trim();
    return city ? `${city}城里` : '城市里';
}

function buildGuideStampText(post, route, baseTitle, routeTitle) {
    if (post?.stamp?.text) return post.stamp.text;
    const city = getStampCityLabel(post);
    if (routeTitle && routeTitle !== baseTitle) {
        return `你不是“经过”了${baseTitle}，而是跟着「${routeTitle}」读完了一段${city}值得停留的文化记忆。`;
    }
    return `你不是“经过”了${baseTitle}，而是读完了一段${city}值得停留的文化记忆。`;
}

function getCurrentStampData() {
    const activeRoute = getActiveGuideRoute(getRouteMap(currentPost));
    const baseTitle = getStampBaseTitle(currentPost);
    const routeTitle = getStampRouteTitle(activeRoute, currentPost);
    const stampTitle = currentPost?.stamp?.title || `${baseTitle}${t('stampPostfix')}`;
    const stampCode = currentPost?.stamp?.code || `${baseTitle} · ${routeTitle}`;
    return {
        id: `${currentPost?.id || 'guide'}:${activeRoute?.id || 'default'}`,
        postId: currentPost?.id,
        title: baseTitle,
        routeTitle,
        city: currentPost?.city || currentPost?.location || '',
        stampTitle,
        stampCode,
        text: buildGuideStampText(currentPost, activeRoute, baseTitle, routeTitle),
        stampedAt: new Date().toISOString()
    };
}

function hasGuideStamp(stampId) {
    return getGuideStamps().some(stamp => stamp.id === stampId);
}

function stampCurrentGuide() {
    if (!currentPost) return;
    const stamp = getCurrentStampData();
    const stamps = getGuideStamps();
    if (stamps.some(item => item.id === stamp.id)) {
        showToast(t('stampAlreadySaved'), {
            actionText: t('viewStamps'),
            onAction: showMyGuideStamps
        });
        updateGuideCompletionStampState(true);
        return;
    }

    saveGuideStamps([stamp, ...stamps]);
    updateGuideCompletionStampState(true);
    showToast(t('stampSaved'), {
        actionText: t('viewStamps'),
        onAction: showMyGuideStamps
    });
}

function updateGuideCompletionStampState(isStamped = null) {
    const stampButton = document.getElementById('guideDetailPlay');
    if (!stampButton || !guideCompletionMode) return;
    const stamped = isStamped ?? hasGuideStamp(getCurrentStampData().id);
    const stampTicket = document.querySelector('.guide-stamp-ticket');
    stampButton.textContent = stamped ? t('stamped') : t('stampIt');
    stampButton.classList.remove('playing');
    stampButton.classList.toggle('stamped', stamped);
    if (stampTicket) {
        stampTicket.classList.toggle('stamped', stamped);
        stampTicket.textContent = stamped ? t('stampedDone') : getCurrentStampData().stampCode;
        if ('disabled' in stampTicket) stampTicket.disabled = stamped;
    }
}

function updateGuideDetailStepButtons() {
    const prev = document.getElementById('guideDetailPrev');
    const next = document.getElementById('guideDetailNext');
    if (!prev || !next) return;

    const ordered = getCurrentOrderedGuideItems();
    const position = getCurrentGuideRoutePosition();
    prev.textContent = t('previousStop');
    next.textContent = guideCompletionMode || position >= ordered.length - 1 ? t('completionStamp') : t('nextStop');
    prev.disabled = position <= 0;
    next.disabled = guideCompletionMode || position < 0;
}

function moveGuideDetail(delta) {
    const ordered = getCurrentOrderedGuideItems();
    const position = getCurrentGuideRoutePosition();
    if (guideCompletionMode && delta < 0) {
        const lastPosition = Math.max(0, ordered.length - 1);
        if (ordered[lastPosition]) openGuideDetail(ordered[lastPosition].index, lastPosition);
        return;
    }
    const nextPosition = position + delta;
    if (!ordered[nextPosition]) {
        if (delta > 0) showGuideCompletionStamp();
        return;
    }
    openGuideDetail(ordered[nextPosition].index, nextPosition);
}

function showGuideCompletionStamp() {
    if (!currentPost) return;
    const ordered = getCurrentOrderedGuideItems();
    const lastPosition = Math.max(0, ordered.length - 1);
    const lastStop = ordered[lastPosition];
    if (lastStop) {
        currentGuideDetailIndex = lastStop.index;
        currentGuideDetailDisplayIndex = lastPosition;
    }
    guideCompletionMode = true;
    stopGuideAudio();

    const stamp = getCurrentStampData();
    const panel = document.getElementById('guideDetailPanel');
    const title = document.getElementById('guideDetailTitle');
    const indexEl = document.getElementById('guideDetailIndex');
    const text = document.getElementById('guideDetailText');
    const images = document.getElementById('guideDetailImages');
    const live = document.getElementById('guideDetailLive');

    title.textContent = stamp.stampTitle;
    indexEl.textContent = t('completionStamp');
    text.textContent = '';
    if (live) {
        live.innerHTML = '';
        live.hidden = true;
    }
    images.innerHTML = `
        <section class="guide-completion-card">
            <span>${t('completionStamp')}</span>
            <h3>${escapeHtml(stamp.stampTitle)}</h3>
            <p>${escapeHtml(getGuidePreviewText(stamp.text, 74) || t('stampDefaultText'))}</p>
            <button class="guide-stamp-ticket" type="button" onclick="stampCurrentGuide()">${escapeHtml(stamp.stampCode)}</button>
        </section>
    `;

    panel.classList.add('active', 'completion-mode');
    panel.scrollTop = 0;
    updateGuideDetailStepButtons();
    const play = document.getElementById('guideDetailPlay');
    const nav = document.getElementById('guideDetailNav');
    if (play) play.textContent = t('stampIt');
    if (nav) nav.textContent = t('viewStamps');
    updateGuideCompletionStampState();
}

function getGuideRouteSummary(route, orderedGuideItems) {
    const routeStopCount = Array.isArray(route?.stops) && route.stops.length > 0
        ? route.stops.length
        : orderedGuideItems.filter(({ inActiveRoute }) => inActiveRoute).length || orderedGuideItems.length;

    return [
        route?.duration ? `⏱ ${escapeHtml(route.duration)}` : '',
        route?.distance ? `🚶 ${escapeHtml(route.distance)}` : '',
        routeStopCount ? `${routeStopCount} ${t('guidePoint')}` : ''
    ].filter(Boolean).join(' · ');
}

function getGuidePreviewText(text, maxLength = 92) {
    const compact = String(text || '').replace(/\s+/g, ' ').trim();
    if (compact.length <= maxLength) return compact;
    return `${compact.slice(0, maxLength)}...`;
}

function scrollGuideSectionTo(sectionId) {
    document.getElementById(sectionId)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function scrollGuideToStop(index) {
    const card = document.querySelector(`.guide-card[data-guide-index="${Number(index)}"]`);
    if (!card) return;
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    card.classList.add('guide-card-pulse');
    setTimeout(() => card.classList.remove('guide-card-pulse'), 900);
}

function renderGuideQuickNav() {
    return `
        <nav class="guide-quick-nav" aria-label="${t('quickGuideNav')}">
            <span>${t('quickGuideNav')}</span>
            <button type="button" onclick="scrollGuideSectionTo('guideIntroSection')">${t('guideIntro')}</button>
            <button type="button" onclick="scrollGuideSectionTo('guideRouteSection')">${t('routeOverview')}</button>
            <button type="button" onclick="scrollGuideSectionTo('guideStopsSection')">${t('routeStops')}</button>
        </nav>
    `;
}

function renderGuideJourneyHero(post, activeRoute, orderedGuideItems) {
    const summary = getGuideRouteSummary(activeRoute, orderedGuideItems);
    const firstStops = orderedGuideItems
        .map((entry, displayIndex) => ({ ...entry, displayIndex }))
        .filter(({ inActiveRoute }) => inActiveRoute)
        .map(({ item, index, displayIndex }) => `
            <button type="button" onclick="scrollGuideToStop(${Number(index)})">
                ${displayIndex + 1}. ${escapeHtml(item.title || t('guidePoint'))}
            </button>
        `)
        .join('');

    return `
        <section class="guide-journey-hero">
            <span class="guide-journey-kicker">${t('chooseRouteFirst')}</span>
            <h3>${escapeHtml(activeRoute?.title || post.title || t('recommendedRoute'))}</h3>
            <p>${escapeHtml(getGuidePreviewText(activeRoute?.description || t('chooseRouteHint')))}</p>
            <div class="guide-journey-meta">${summary || t('routeActionHint')}</div>
            ${firstStops ? `<div class="guide-journey-stops">${firstStops}</div>` : ''}
            <div class="guide-journey-actions">
                <button type="button" class="guide-start-btn" onclick="startGuideRoute()">${t('startGuide')}</button>
                <button type="button" class="guide-secondary-btn" onclick="saveCurrentGuideRoute()">${t('saveRoute')}</button>
                <button type="button" class="guide-secondary-btn" onclick="shareCurrentGuideRoute()">${t('shareRoute')}</button>
            </div>
        </section>
    `;
}

function startGuideRoute() {
    if (!currentPost || !isGuidePost(currentPost)) return;
    const guideItems = Array.isArray(currentPost.guide_items) ? currentPost.guide_items : [];
    const activeRoute = getActiveGuideRoute(getRouteMap(currentPost));
    const firstRouteIndex = Array.isArray(activeRoute?.stops) && activeRoute.stops.length > 0
        ? Number(activeRoute.stops[0])
        : 0;
    const firstIndex = Number.isInteger(firstRouteIndex) && guideItems[firstRouteIndex] ? firstRouteIndex : 0;

    document.querySelector('.guide-route-step-list')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    setTimeout(() => openGuideDetail(firstIndex, 0), 260);
}

async function saveCurrentGuideRoute() {
    if (!currentPost) return;
    const isBookmarked = await checkFavorite(currentPost.id);
    if (isBookmarked) {
        showToast(t('routeAlreadySaved'), {
            detail: t('routeSavedHint'),
            actionText: t('viewNow'),
            onAction: openFavoritesFromToast
        });
        return;
    }
    await toggleBookmark();
}

async function shareCurrentGuideRoute() {
    if (!currentPost) return;
    const activeRoute = getActiveGuideRoute(getRouteMap(currentPost));
    const shareText = `${currentPost.title || t('attractionGuide')} · ${activeRoute?.title || t('recommendedRoute')}`;

    try {
        if (navigator.share) {
            await navigator.share({ title: currentPost.title, text: shareText });
        } else if (navigator.clipboard) {
            await navigator.clipboard.writeText(shareText);
        }
        showToast(t('shareReady'), { detail: t('shareReadyHint') });
    } catch (error) {
        console.warn('分享导览失败:', error);
    }
}

function getRouteViewBox(route, guideItems) {
    if (!route || !Array.isArray(route.stops)) return '0 0 100 100';
    const points = route.stops
        .map(index => guideItems[index])
        .filter(item => item && item.map_x !== undefined && item.map_y !== undefined)
        .map(item => [Number(item.map_x), Number(item.map_y)]);

    if (points.length === 0) return '0 0 100 100';

    const xs = points.map(point => point[0]);
    const ys = points.map(point => point[1]);
    const minX = Math.max(0, Math.min(...xs) - 9);
    const maxX = Math.min(100, Math.max(...xs) + 9);
    const minY = Math.max(0, Math.min(...ys) - 9);
    const maxY = Math.min(100, Math.max(...ys) + 9);
    return `${minX} ${minY} ${Math.max(22, maxX - minX)} ${Math.max(22, maxY - minY)}`;
}

function renderRouteSvg(route, guideItems) {
    if (!route || !Array.isArray(route.stops)) return '';

    const points = route.stops
        .map(index => guideItems[index])
        .filter(item => item && item.map_x !== undefined && item.map_y !== undefined)
        .map(item => `${Number(item.map_x)},${Number(item.map_y)}`)
        .join(' ');

    if (!points) return '';

    return `
        <svg class="route-map-line" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
            <polyline points="${points}" />
        </svg>
    `;
}

function renderGuideRouteMap(post, guideItems) {
    const routeMap = getRouteMap(post);
    if (!routeMap) return '';

    const routes = routeMap.routes;
    const activeRoute = getActiveGuideRoute(routeMap);
    const stopSet = new Set(Array.isArray(activeRoute?.stops) ? activeRoute.stops : []);
    const visibleStops = guideItems
        .map((item, index) => ({ item, index }))
        .filter(({ item, index }) => item.map_x !== undefined && item.map_y !== undefined && stopSet.has(index));

    return `
        <section class="route-map-section">
            <div class="route-map-heading">
                <div>
                    <span class="guide-eyebrow">${escapeHtml(routeMap.subtitle || t('routeMap'))}</span>
                    <h3>${escapeHtml(routeMap.title || t('routeSelection'))}</h3>
                </div>
                <button class="guide-main-play" onclick="playPostAudio()">
                    <span>▶</span>
                    ${t('playGuide')}
                </button>
            </div>
            <div class="route-map-layout">
                <div class="route-map-viewport">
                    <div class="route-map-tools" aria-label="${t('routeMap')}">
                        <button type="button" class="route-map-tool" data-map-tool="zoom-in">+</button>
                        <button type="button" class="route-map-tool" data-map-tool="zoom-out">−</button>
                        <button type="button" class="route-map-reset" data-map-tool="reset">${t('reset')}</button>
                    </div>
                    <div class="route-map-canvas">
                        <img src="${escapeHtml(routeMap.map_image || '')}" alt="${escapeHtml(routeMap.title || t('routeMap'))}" class="route-map-image">
                        ${renderRouteSvg(activeRoute, guideItems)}
                        ${visibleStops.map(({ item, index }, stopIndex) => `
                            <button class="route-map-marker" style="left:${Number(item.map_x)}%; top:${Number(item.map_y)}%;" data-guide-index="${index}" data-guide-display-index="${stopIndex}" aria-label="${t('viewDetailNav')}">
                                <span class="route-marker-icon">${stopIndex + 1}</span>
                                <span class="route-marker-label">${escapeHtml(item.title || `${t('guidePoint')} ${stopIndex + 1}`)}</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
                <div class="route-options">
                    ${routes.map((route, routeIndex) => `
                        <button class="route-option ${route.id === activeRoute?.id ? 'active' : ''}" data-route-id="${escapeHtml(route.id)}">
                            <span class="route-option-icon">${routeIndex + 1}</span>
                            <span class="route-option-body">
                                <strong>${escapeHtml(route.title || t('recommendedRoute'))}</strong>
                                <span class="route-option-meta">⏱ ${escapeHtml(route.duration || '-')} · 🚶 ${escapeHtml(route.distance || '-')}</span>
                                <span class="route-option-desc">${escapeHtml(route.description || '')}</span>
                            </span>
                        </button>
                    `).join('')}
                </div>
            </div>
        </section>
    `;
}

function applyRouteMapTransform(viewport) {
    const canvas = viewport.querySelector('.route-map-canvas');
    if (!canvas) return;
    canvas.style.transform = `translate3d(${routeMapViewState.x}px, ${routeMapViewState.y}px, 0) scale(${routeMapViewState.scale})`;
}

function clampRouteMapState(viewport = null) {
    routeMapViewState.scale = Math.min(3, Math.max(1, routeMapViewState.scale));
    const canvas = viewport?.querySelector?.('.route-map-canvas');
    const viewportRect = viewport?.getBoundingClientRect?.();
    const baseWidth = canvas?.offsetWidth || viewportRect?.width || 0;
    const baseHeight = canvas?.offsetHeight || viewportRect?.height || 0;
    const scaledWidth = baseWidth * routeMapViewState.scale;
    const scaledHeight = baseHeight * routeMapViewState.scale;
    const minX = Math.min(0, (viewportRect?.width || baseWidth) - scaledWidth);
    const minY = Math.min(0, (viewportRect?.height || baseHeight) - scaledHeight);

    if (routeMapViewState.scale === 1 || scaledWidth <= (viewportRect?.width || baseWidth)) {
        routeMapViewState.x = 0;
    } else {
        routeMapViewState.x = Math.min(0, Math.max(minX, routeMapViewState.x));
    }

    if (routeMapViewState.scale === 1 || scaledHeight <= (viewportRect?.height || baseHeight)) {
        routeMapViewState.y = 0;
    } else {
        routeMapViewState.y = Math.min(0, Math.max(minY, routeMapViewState.y));
    }
}

function zoomRouteMap(viewport, delta, clientX = null, clientY = null) {
    const oldScale = routeMapViewState.scale;
    const nextScale = Math.min(3, Math.max(1, oldScale + delta));
    if (nextScale === oldScale) return;

    const viewportRect = viewport.getBoundingClientRect();
    const focusX = clientX === null ? viewportRect.width / 2 : clientX - viewportRect.left;
    const focusY = clientY === null ? viewportRect.height / 2 : clientY - viewportRect.top;
    const contentX = (focusX - routeMapViewState.x) / oldScale;
    const contentY = (focusY - routeMapViewState.y) / oldScale;

    routeMapViewState.scale = nextScale;
    routeMapViewState.x = focusX - contentX * nextScale;
    routeMapViewState.y = focusY - contentY * nextScale;
    clampRouteMapState(viewport);
    applyRouteMapTransform(viewport);
}

function resetRouteMap(viewport, route, guideItems) {
    routeMapViewState = { scale: 1, x: 0, y: 0 };
    const canvas = viewport.querySelector('.route-map-canvas');
    if (canvas) canvas.style.transformOrigin = '0 0';

    const img = viewport.querySelector('.route-map-image');
    if (img) {
        img.style.objectPosition = 'center center';
    }

    viewport.dataset.routeViewBox = getRouteViewBox(route, guideItems);
    clampRouteMapState(viewport);
    applyRouteMapTransform(viewport);
}

function initInteractiveRouteMap(guideSection) {
    const viewport = guideSection.querySelector('.route-map-viewport');
    const routeMap = getRouteMap(currentPost);
    const guideItems = Array.isArray(currentPost?.guide_items) ? currentPost.guide_items : [];
    const activeRoute = getActiveGuideRoute(routeMap);
    if (!viewport || !activeRoute) return;

    resetRouteMap(viewport, activeRoute, guideItems);

    viewport.querySelectorAll('[data-map-tool]').forEach(button => {
        button.addEventListener('click', event => {
            event.stopPropagation();
            const tool = button.dataset.mapTool;
            if (tool === 'zoom-in') zoomRouteMap(viewport, 0.25);
            if (tool === 'zoom-out') zoomRouteMap(viewport, -0.25);
            if (tool === 'reset') resetRouteMap(viewport, activeRoute, guideItems);
        });
    });

    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let originX = 0;
    let originY = 0;

    viewport.addEventListener('pointerdown', event => {
        if (event.target.closest('.route-map-marker, .route-map-tools')) return;
        isDragging = true;
        viewport.classList.add('dragging');
        startX = event.clientX;
        startY = event.clientY;
        originX = routeMapViewState.x;
        originY = routeMapViewState.y;
        viewport.setPointerCapture?.(event.pointerId);
    });

    viewport.addEventListener('pointermove', event => {
        if (!isDragging) return;
        routeMapViewState.x = originX + event.clientX - startX;
        routeMapViewState.y = originY + event.clientY - startY;
        clampRouteMapState(viewport);
        applyRouteMapTransform(viewport);
    });

    viewport.addEventListener('pointerup', () => {
        isDragging = false;
        viewport.classList.remove('dragging');
    });

    viewport.addEventListener('pointercancel', () => {
        isDragging = false;
        viewport.classList.remove('dragging');
    });

    viewport.addEventListener('wheel', event => {
        event.preventDefault();
        zoomRouteMap(viewport, event.deltaY < 0 ? 0.18 : -0.18, event.clientX, event.clientY);
    }, { passive: false });

    viewport.addEventListener('dblclick', event => {
        if (event.target.closest('.route-map-marker, .route-map-tools')) return;
        event.preventDefault();
        zoomRouteMap(viewport, 0.35, event.clientX, event.clientY);
    });
}

function bindGuideRouteMap(guideSection) {
    guideSection.querySelectorAll('.route-option').forEach(option => {
        option.addEventListener('click', event => {
            event.stopPropagation();
            activeGuideRouteId = option.dataset.routeId;
            routeMapViewState = { scale: 1, x: 0, y: 0 };
            if (currentPost) renderGuideSection(currentPost);
        });
    });

    guideSection.querySelectorAll('.route-map-marker').forEach(marker => {
        marker.addEventListener('click', event => {
            event.stopPropagation();
            openGuideDetail(Number(marker.dataset.guideIndex), Number(marker.dataset.guideDisplayIndex));
        });
    });

    initInteractiveRouteMap(guideSection);
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('guideDetailBack')?.addEventListener('click', closeGuideDetail);
    document.getElementById('guideDetailPrev')?.addEventListener('click', () => moveGuideDetail(-1));
    document.getElementById('guideDetailNext')?.addEventListener('click', () => moveGuideDetail(1));
    document.getElementById('guideDetailPlay')?.addEventListener('click', playCurrentGuideDetail);
    document.getElementById('guideDetailNav')?.addEventListener('click', navigateCurrentGuide);
});

document.addEventListener('click', function(event) {
    const audioButton = event.target.closest?.('.guide-audio-btn');
    if (audioButton) {
        event.stopPropagation();
        playGuideAudio(Number(audioButton.dataset.guideAudioIndex));
        return;
    }

    const guideCard = event.target.closest?.('.guide-card');
    if (guideCard) {
        openGuideDetail(Number(guideCard.dataset.guideIndex), Number(guideCard.dataset.guideDisplayIndex));
    }
});

function playPostAudio() {
    if (!currentPost || !isGuidePost(currentPost)) return;
    const target = { type: 'post', index: null };

    if (isSameGuideAudioTarget(target)) {
        stopGuideAudio();
        return;
    }

    const audioUrl = getLanguageAudioUrl(currentPost, 'audio_url');
    if (audioUrl) {
        stopGuideAudio();
        activeGuideAudio = new Audio(audioUrl);
        activeGuideAudioTarget = target;
        activeGuideAudio.onended = stopGuideAudio;
        activeGuideAudio.onerror = () => handleGuideAudioError(getPostGuideSpeechText(currentPost), target);
        updateGuideAudioControls();
        activeGuideAudio.play().catch(() => handleGuideAudioError(getPostGuideSpeechText(currentPost), target));
        return;
    }

    speakGuideFallback(getPostGuideSpeechText(currentPost), target);
}

function renderGuideSection(post) {
    const guideSection = document.getElementById('guideSection');
    if (!guideSection) return;

    const guideItems = Array.isArray(post.guide_items) ? post.guide_items : [];
    if (!isGuidePost(post) || guideItems.length === 0) {
        guideSection.innerHTML = '';
        return;
    }

    const routeMapHtml = renderGuideRouteMap(post, guideItems);
    const activeRoute = getActiveGuideRoute(getRouteMap(post));
    const orderedGuideItems = getOrderedGuideItemsForRoute(guideItems, activeRoute);

    guideSection.innerHTML = `
        ${renderGuideQuickNav()}
        <section class="guide-flow-section" id="guideIntroSection">
            <div class="guide-flow-heading">
                <span>01</span>
                <div>
                    <b>${t('guideIntro')}</b>
                    <p>${escapeHtml(post.content || t('routeActionHint'))}</p>
                </div>
            </div>
        </section>
        <section class="guide-flow-section" id="guideRouteSection">
            <div class="guide-flow-heading">
                <span>02</span>
                <div>
                    <b>${t('routeOverview')}</b>
                    <p>${escapeHtml(activeRoute?.estimate_note || activeRoute?.description || t('routeActionHint'))}</p>
                </div>
            </div>
            ${routeMapHtml}
            ${renderGuideJourneyHero(post, activeRoute, orderedGuideItems)}
        </section>
        <section class="guide-flow-section guide-route-step-list" id="guideStopsSection">
            <div class="guide-flow-heading">
                <span>03</span>
                <div>
                    <b>${t('routeStops')}</b>
                    <p>${t('routeActionHint')}</p>
                </div>
            </div>
            <div class="guide-list">
            ${orderedGuideItems.map(({ item, index, inActiveRoute }, displayIndex) => `
                <article class="guide-card ${inActiveRoute ? 'in-active-route' : 'route-extra-stop'}" data-guide-index="${index}" data-guide-display-index="${displayIndex}">
                    <img src="${escapeHtml(item.image || '')}" alt="${escapeHtml(item.title || t('guideImage'))}" class="guide-card-image" onclick="event.stopPropagation();openImageViewerFromElement(this);" onkeydown="if(event.key === 'Enter' || event.key === ' ') { event.preventDefault(); event.stopPropagation(); openImageViewerFromElement(this); }" tabindex="0" role="button" data-image-src="${escapeHtml(item.image || '')}" data-image-alt="${escapeHtml(item.title || t('guideImage'))}">
                    <div class="guide-card-body">
                        <div class="guide-card-title-row">
                            <div>
                                <span class="guide-stop-label">${t('stopLabel', { index: displayIndex + 1 })}${item.time ? ` · ${escapeHtml(item.time)}` : ''}</span>
                                <h4>${escapeHtml(item.title || `${t('guidePoint')} ${displayIndex + 1}`)}</h4>
                            </div>
                            <button class="guide-audio-btn" data-guide-audio-index="${index}" aria-label="${t('playAudio')}">▶</button>
                        </div>
                        <p>${escapeHtml(item.text || t('noGuideText'))}</p>
                        <span class="guide-card-more">${t('viewDetailNav')}</span>
                    </div>
                </article>
            `).join('')}
            </div>
        </section>
    `;

    bindGuideRouteMap(guideSection);
    updateGuideAudioControls();
}

async function loadPostDetail(postId) {
    try {
        const response = await fetch(`/post/${postId}`);
        const post = await response.json();
        
        if (response.ok) {
            currentPostSource = post;
            showPostDetail(post);
        } else {
            alert(t('requestFailed', { detail: post.detail }));
        }
    } catch (error) {
        console.error("加载帖子详情失败:", error);
        alert(t('requestFailed', { detail: t('loading') }));
    }
}

async function showPostDetail(post) {
    const displayPost = await localizePost(withGuideDisplayPublishTime(post));
    currentPost = displayPost;
    post = displayPost;
    stopGuideAudio();
    activeGuideRouteId = null;
    ensureDetailFloatingLayers();
    
    const photoSrc = post.photos && post.photos.length > 0 
        ? post.photos[0] 
        : `https://picsum.photos/600/1000?random=${post.id}`;
    
    const detailImage = document.getElementById('detailImage');
    detailImage.src = photoSrc;
    detailImage.dataset.imageSrc = photoSrc;
    detailImage.dataset.imageAlt = post.title || t('guideImage');
    detailImage.onclick = () => openImageViewer(photoSrc, post.title || t('guideImage'));
    detailImage.onkeydown = (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            openImageViewer(photoSrc, post.title || t('guideImage'));
        }
    };
    detailImage.tabIndex = 0;
    detailImage.setAttribute('role', 'button');

    const detailPlayButton = document.querySelector('.play-btn-wrapper');
    if (detailPlayButton) {
        detailPlayButton.style.display = isGuidePost(post) ? 'flex' : 'none';
    }

    const bottomSheet = document.querySelector('.detail-bottom-sheet');
    if (bottomSheet) {
        bottomSheet.classList.toggle('guide-detail-mode', isGuidePost(post));
    }
    
    document.querySelector('.detail-title').textContent = post.title;
    document.getElementById('detailContent').textContent = post.content || t('authorNoContent');
    renderGuideSection(post);
    document.querySelector('.location-tag').textContent = `📍 ${post.location || t('unknownLocation')}`;
    document.querySelector('.author-name').textContent = post.author || t('anonymousUser');
    
    // 修复时间显示
    let timeText = t('unknownTime');
    const displayPublishTime = getGuideDisplayPublishTime(post) || post.publish_time;
    if (displayPublishTime) {
        try {
            const date = new Date(displayPublishTime);
            if (!isNaN(date.getTime())) {
                timeText = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
            }
        } catch (e) {
            timeText = displayPublishTime;
        }
    }
    document.querySelector('.publish-date').textContent = t('publishedAt', { date: timeText });
    
    // 显示统计信息（只显示数字）
    document.querySelectorAll('.stat-value')[0].innerHTML = `${post.duration || 0}`;
    document.querySelectorAll('.stat-value')[1].innerHTML = `${post.people || 0}`;
    
    // 更新浏览量（只显示数字）
    document.getElementById('detailViews').textContent = `${post.views || 0}`;
    
    // 更新点赞按钮（只显示数字）
    const likeBtn = document.querySelectorAll('.action-item')[1];
    renderLikeButton(likeBtn, post.likes || 0, getLikedPosts().includes(post.id));
    likeBtn.onclick = handleLike;
    checkLike(post.id).then(isLiked => {
        renderLikeButton(likeBtn, currentPost.likes || post.likes || 0, isLiked);
    });
    
    // 更新评论按钮（只显示数字）
    const commentBtn = document.querySelectorAll('.action-item')[2];
    commentBtn.innerHTML = `
        <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        <span>${post.comments || 0}</span>
    `;
    commentBtn.onclick = openCommentModal;
    
    // 更新收藏按钮状态 - 从服务器检查
    const bookmarkBtn = document.getElementById('detailBookmark');
    const bookmarkText = document.getElementById('detailBookmarkText');
    const isBookmarked = await checkFavorite(post.id);
    if (isBookmarked) {
        bookmarkBtn.classList.add('bookmarked');
        bookmarkText.textContent = isGuidePost(post) ? t('routeSaved') : t('bookmarked');
    } else {
        bookmarkBtn.classList.remove('bookmarked');
        bookmarkText.textContent = isGuidePost(post) ? t('saveRoute') : t('bookmark');
    }
    
    // 设置作者头像
    const oldAvatar = document.getElementById('authorAvatar');
    oldAvatar.outerHTML = avatarHtml(post.author_avatar, post.author || t('anonymousUser'), 'author-avatar', 'authorAvatar');
    
    const authorAvatar = document.getElementById('authorAvatar');
    authorAvatar.onclick = function() {
        viewUserPosts(post.author || t('anonymousUser'), 'detail');
    };
    authorAvatar.style.cursor = 'pointer';
    
    // 更新关注按钮状态（异步）
    updateFollowButton(post.author || t('anonymousUser'));
    
    loadComments(post.id);
    openDetailPage();
    const detailScroll = document.getElementById('detailScroll');
    if (detailScroll) detailScroll.scrollTop = 0;
}

// 更新关注按钮状态 - 从服务器获取
async function updateFollowButton(author) {
    const followBtn = document.getElementById('followBtn');
    if (!followBtn) return;
    const currentUser = localStorage.getItem('username');

    if (currentUser === author) {
        followBtn.style.display = 'none';
        return;
    }

    followBtn.style.display = '';
    
    const followers = await getFollowers();
    
    if (followers.includes(author)) {
        followBtn.textContent = t('following');
        followBtn.classList.add('following');
    } else {
        followBtn.textContent = t('follow');
        followBtn.classList.remove('following');
    }
}

// 获取关注列表 - 从服务器获取
async function getFollowers() {
    const username = localStorage.getItem('username');
    if (!username) {
        return [];
    }
    
    const storageKey = `followers_${username}`;
    
    try {
        const response = await fetchWithTimeout(`/followers/${encodeURIComponent(username)}`);
        if (response.ok) {
            const data = await response.json();
            // 使用用户独立的 key 保存到本地存储
            localStorage.setItem(storageKey, JSON.stringify(data.following || []));
            return data.following || [];
        }
    } catch (error) {
        console.error("获取关注列表失败:", error);
    }
    
    // 降级到用户独立的本地存储
    const followers = localStorage.getItem(storageKey);
    return followers ? JSON.parse(followers) : [];
}

// 保存关注列表
function saveFollowers(followers) {
    const username = localStorage.getItem('username');
    if (!username) return;
    const storageKey = `followers_${username}`;
    localStorage.setItem(storageKey, JSON.stringify(followers));
}

// 获取收藏列表 - 从服务器获取
async function getFavorites() {
    const username = localStorage.getItem('username');
    if (!username) {
        const favorites = localStorage.getItem('favorites');
        return favorites ? JSON.parse(favorites) : [];
    }
    
    try {
        const response = await fetch(`/favorites/${encodeURIComponent(username)}`);
        if (response.ok) {
            const data = await response.json();
            // 同时保存到本地存储作为缓存
            localStorage.setItem('favorites', JSON.stringify(data));
            return data;
        }
    } catch (error) {
        console.error("获取收藏列表失败:", error);
    }
    
    // 降级到本地存储
    const favorites = localStorage.getItem('favorites');
    return favorites ? JSON.parse(favorites) : [];
}

// 保存收藏列表到服务器
async function saveFavoritesToServer(postId, isAdd) {
    const username = localStorage.getItem('username');
    if (!username) return;
    
    try {
        if (isAdd) {
            const response = await fetch('/favorite', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    post_id: postId
                })
            });
            if (response.ok) {
                console.log('收藏已同步到服务器');
            }
        } else {
            const response = await fetch('/favorite', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    post_id: postId
                })
            });
            if (response.ok) {
                console.log('取消收藏已同步到服务器');
            }
        }
    } catch (error) {
        console.error("同步收藏失败:", error);
    }
}

// 检查帖子是否已收藏
async function checkFavorite(postId) {
    const username = localStorage.getItem('username');
    if (!username) {
        // 未登录时检查本地存储
        const favorites = localStorage.getItem('favorites');
        if (favorites) {
            const favList = JSON.parse(favorites);
            return favList.some(fav => fav.id === postId);
        }
        return false;
    }
    
    try {
        const response = await fetch(`/check-favorite?username=${encodeURIComponent(username)}&post_id=${postId}`);
        if (response.ok) {
            const data = await response.json();
            return data.is_favorited;
        }
    } catch (error) {
        console.error("检查收藏状态失败:", error);
    }
    
    return false;
}

// 显示我的收藏页面
async function showMyFavorites() {
    const favorites = await getFavorites();
    
    showSinglePage('myPostsPage', { showBottomNav: false });
    
    // 修改页面标题（找到正确的标题元素）
    const pageTitle = document.querySelector('#myPostsPage .posts-header h1');
    pageTitle.textContent = t('myFavorites');
    
    // 使用正确的容器ID
    const postsContainer = document.getElementById('myPostsContainer');
    
    if (favorites.length === 0) {
        postsContainer.innerHTML = `
            <div class="empty-state">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
                <p>${t('noFavorites')}</p>
                <p style="font-size: 14px; margin-top: 5px;">${t('favoritesHint')}</p>
            </div>
        `;
    } else {
        let html = '';
        const displayFavorites = await Promise.all(favorites.map(post => localizePostSummary(post)));
        displayFavorites.forEach(post => {
            const photoSrc = post.photos && post.photos.length > 0 
                ? post.photos[0] 
                : `https://picsum.photos/400/300?random=${post.id}`;
            
            html += `
                <div class="post-card" onclick="openPostDetail(${post.id})">
                    <div class="post-image-wrapper">
                        <img src="${photoSrc}" alt="${post.title}" class="post-image">
                    </div>
                    <div class="post-info">
                        <h3 class="post-title-text">${post.title}</h3>
                        <p class="post-author">${post.author}</p>
                        <p class="post-location">📍 ${post.location}</p>
                        <div class="post-stats-row">
                            <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 14.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg> ${post.views || 0}</span>
                            <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg> ${post.likes || 0}</span>
                            <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> ${post.comments || 0}</span>
                        </div>
                    </div>
                </div>
            `;
        });
        postsContainer.innerHTML = html;
    }
    
}

function formatStampDate(value) {
    if (!value) return '';
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return '';
    return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
}

function prepareGuideStampsPage() {
    stopGuideAudio();
    closeGuideDetail();
    document.getElementById('detailPage')?.classList.remove('active');
    document.getElementById('experiencePage')?.classList.remove('active');
    document.getElementById('chatPage')?.classList.remove('active');
    document.getElementById('appToast')?.remove();
    detailReturnState = null;
}

function showMyGuideStamps() {
    prepareGuideStampsPage();
    showSinglePage('myPostsPage', { showBottomNav: false });
    const pageTitle = document.querySelector('#myPostsPage .posts-header h1');
    if (pageTitle) pageTitle.textContent = t('myStamps');

    const postsContainer = document.getElementById('myPostsContainer');
    const stamps = getGuideStamps();
    if (!postsContainer) return;

    if (stamps.length === 0) {
        postsContainer.innerHTML = `
            <div class="empty-state">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M7 4h10l1 7a5 5 0 0 1-4 4.9V19h4v2H6v-2h4v-3.1A5 5 0 0 1 6 11l1-7Z"></path>
                </svg>
                <p>${t('noStamps')}</p>
                <p style="font-size: 14px; margin-top: 5px;">${t('stampsHint')}</p>
            </div>
        `;
        return;
    }

    postsContainer.innerHTML = `
        <div class="stamp-collection">
            ${stamps.map(stamp => `
                <article class="stamp-card" ${stamp.postId ? `onclick="openPostDetail(${Number(stamp.postId)})"` : ''}>
                    <span>${escapeHtml(stamp.city || t('cityGuide'))}</span>
                    <h3>${escapeHtml(stamp.stampTitle || stamp.title)}</h3>
                    <p>${escapeHtml(getGuidePreviewText(stamp.text || t('stampDefaultText'), 72))}</p>
                    <div class="stamp-ticket">${escapeHtml(stamp.stampCode || stamp.routeTitle || stamp.title)}</div>
                    <small>${formatStampDate(stamp.stampedAt)}</small>
                </article>
            `).join('')}
        </div>
    `;
}

// 切换收藏状态
async function toggleBookmark() {
    if (!currentPost) return;
    if (!requireLogin(() => toggleBookmark())) return;
    
    const postId = currentPost.id;
    const bookmarkBtn = document.getElementById('detailBookmark');
    const bookmarkText = document.getElementById('detailBookmarkText');
    
    // 检查当前是否已收藏
    const isFavorited = await checkFavorite(postId);
    
    if (isFavorited) {
        // 取消收藏
        bookmarkBtn.classList.remove('bookmarked');
        bookmarkText.textContent = isGuidePost(currentPost) ? t('saveRoute') : t('bookmark');
        
        // 更新本地存储
        let favorites = await getFavorites();
        const index = favorites.findIndex(fav => fav.id === postId);
        if (index > -1) {
            favorites.splice(index, 1);
        }
        localStorage.setItem('favorites', JSON.stringify(favorites));
        
        // 同步到服务器
        await saveFavoritesToServer(postId, false);
        
        showToast(t('bookmarkRemoved'));
    } else {
        // 添加收藏
        const newFavorite = {
            id: currentPost.id,
            title: currentPost.title,
            author: currentPost.author,
            photos: currentPost.photos,
            location: currentPost.location,
            publish_time: currentPost.publish_time,
            likes: currentPost.likes,
            comments: currentPost.comments,
            views: currentPost.views
        };
        
        bookmarkBtn.classList.add('bookmarked');
        bookmarkText.textContent = isGuidePost(currentPost) ? t('routeSaved') : t('bookmarked');
        
        // 更新本地存储
        let favorites = await getFavorites();
        favorites.push(newFavorite);
        localStorage.setItem('favorites', JSON.stringify(favorites));
        
        // 同步到服务器
        await saveFavoritesToServer(postId, true);
        
        showToast(isGuidePost(currentPost) ? t('routeSaved') : t('bookmarkSuccess'), {
            detail: isGuidePost(currentPost) ? t('routeSavedHint') : t('savedHint'),
            actionText: t('viewNow'),
            onAction: openFavoritesFromToast
        });
    }
}

// 从服务器同步关注列表
async function syncFollowersFromServer() {
    const username = localStorage.getItem('username');
    if (!username) return;
    
    try {
        const response = await fetch(`/followers/${encodeURIComponent(username)}`);
        if (response.ok) {
            const data = await response.json();
            saveFollowers(data.following || []);
        }
    } catch (error) {
        console.error("同步关注列表失败:", error);
    }
}

// 处理首页帖子的关注操作
async function handleFollowFromHome(author, btnElement) {
    if (!requireLogin(() => handleFollowFromHome(author, btnElement))) return;
    
    const followers = await getFollowers();
    const currentUser = localStorage.getItem('username');
    if (currentUser === author) {
        showToast(t('cannotFollowSelf'), { type: 'warning' });
        return;
    }
    
    if (followers.includes(author)) {
        // 取消关注
        try {
            const response = await fetch('/unfollow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    follower: currentUser,
                    following: author
                })
            });
            
            if (response.ok) {
                const index = followers.indexOf(author);
                followers.splice(index, 1);
                btnElement.textContent = t('follow');
                btnElement.classList.remove('following');
                saveFollowers(followers);
                showToast(t('unfollowed'));
            } else {
                const data = await response.json();
                alert(t('requestFailed', { detail: data.detail || t('unknownTime') }));
            }
        } catch (error) {
            console.error("取消关注失败:", error);
            alert(t('requestFailed', { detail: t('follow') }));
        }
    } else {
        // 添加关注
        try {
            const response = await fetch('/follow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    follower: currentUser,
                    following: author
                })
            });
            
            if (response.ok) {
                followers.push(author);
                btnElement.textContent = t('following');
                btnElement.classList.add('following');
                saveFollowers(followers);
                showToast(t('followed'), {
                    detail: t('followHint'),
                    actionText: t('viewNow'),
                    onAction: openFollowingFromToast
                });
            } else {
                const data = await response.json();
                alert(t('requestFailed', { detail: data.detail || t('unknownTime') }));
            }
        } catch (error) {
            console.error("关注失败:", error);
            alert(t('requestFailed', { detail: t('follow') }));
        }
    }
}

// 切换关注状态
async function toggleFollow() {
    if (!requireLogin(() => toggleFollow())) return;
    
    const author = currentPost.author;
    const followers = await getFollowers();
    const followBtn = document.getElementById('followBtn');
    const currentUser = localStorage.getItem('username');
    if (currentUser === author) {
        return;
    }
    
    if (followers.includes(author)) {
        // 取消关注
        try {
            const response = await fetch('/unfollow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    follower: currentUser,
                    following: author
                })
            });
            
            if (response.ok) {
                const index = followers.indexOf(author);
                followers.splice(index, 1);
                followBtn.textContent = t('follow');
                followBtn.classList.remove('following');
                saveFollowers(followers);
                showToast(t('unfollowed'));
            } else {
                const data = await response.json();
                alert(t('requestFailed', { detail: data.detail }));
            }
        } catch (error) {
            console.error("取消关注失败:", error);
            alert(t('requestFailed', { detail: t('follow') }));
        }
    } else {
        // 关注
        try {
            const response = await fetch('/follow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    follower: currentUser,
                    following: author
                })
            });
            
            if (response.ok) {
                followers.push(author);
                followBtn.textContent = t('following');
                followBtn.classList.add('following');
                saveFollowers(followers);
                showToast(t('followed'), {
                    detail: t('followHint'),
                    actionText: t('viewNow'),
                    onAction: openFollowingFromToast
                });
            } else {
                const data = await response.json();
                alert(t('requestFailed', { detail: data.detail }));
            }
        } catch (error) {
            console.error("关注失败:", error);
            alert(t('requestFailed', { detail: t('follow') }));
        }
    }
    
    // 更新个人中心统计数据
    updateProfileStats();
}

// 获取已点赞的帖子列表
function getLikedPosts() {
    const username = localStorage.getItem('username') || 'guest';
    const liked = localStorage.getItem(`likedPosts_${username}`) || localStorage.getItem('likedPosts');
    return liked ? JSON.parse(liked) : [];
}

// 保存已点赞的帖子列表
function saveLikedPosts(likedPosts) {
    const username = localStorage.getItem('username') || 'guest';
    localStorage.setItem(`likedPosts_${username}`, JSON.stringify(likedPosts));
}

async function checkLike(postId) {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    const username = localStorage.getItem('username');
    if (isLoggedIn !== 'true' || !username) {
        return getLikedPosts().includes(postId);
    }

    try {
        const response = await fetch(`/post/${postId}/check-like?username=${encodeURIComponent(username)}`);
        if (!response.ok) {
            return getLikedPosts().includes(postId);
        }

        const data = await response.json();
        const likedPosts = getLikedPosts();
        const localIndex = likedPosts.indexOf(postId);
        if (data.is_liked && localIndex === -1) {
            likedPosts.push(postId);
            saveLikedPosts(likedPosts);
        } else if (!data.is_liked && localIndex !== -1) {
            likedPosts.splice(localIndex, 1);
            saveLikedPosts(likedPosts);
        }
        return data.is_liked;
    } catch (error) {
        console.error("检查点赞状态失败:", error);
        return getLikedPosts().includes(postId);
    }
}

async function handleLike() {
    if (!currentPost) return;
    
    if (!requireLogin(() => handleLike())) return;
    
    const likedPosts = getLikedPosts();
    const wasLiked = likedPosts.includes(currentPost.id);
    const likeBtn = document.querySelectorAll('.action-item')[1];
    const username = localStorage.getItem('username');
    
    try {
        const response = await fetch(`/post/${currentPost.id}/like`, {
            method: wasLiked ? 'DELETE' : 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            renderLikeButton(likeBtn, data.likes, data.is_liked);
            currentPost.likes = data.likes;
            
            if (data.is_liked && !likedPosts.includes(currentPost.id)) {
                likedPosts.push(currentPost.id);
            } else if (!data.is_liked) {
                const likedIndex = likedPosts.indexOf(currentPost.id);
                if (likedIndex !== -1) {
                    likedPosts.splice(likedIndex, 1);
                }
            }
            saveLikedPosts(likedPosts);
            
            // 更新个人中心获赞数（如果是自己的帖子）
            updateProfileStats();
            showToast(data.is_liked ? t('likedToast') : t('unlikedToast'), {
                detail: data.is_liked ? t('likedHint') : ''
            });
        } else {
            const data = await response.json();
            alert(t('requestFailed', { detail: data.detail || t('likes') }));
        }
    } catch (error) {
        console.error("点赞操作失败:", error);
        alert(t('requestFailed', { detail: t('likes') }));
    }
}

function openCommentModal() {
    const existing = document.getElementById('commentModal');
    if (existing) {
        existing.classList.add('active');
        if (currentPost) loadComments(currentPost.id);
        return;
    }

    const commentModal = document.createElement('div');
    commentModal.className = 'comment-modal';
    commentModal.id = 'commentModal';
    commentModal.innerHTML = `
        <div class="comment-modal-wrapper">
            <div class="comment-header">
                <div class="back-btn" onclick="closeCommentModal()">
                    <svg viewBox="0 0 24 24" width="20" height="20"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg>
                </div>
                <h2>${t('comments')}</h2>
                <div class="placeholder"></div>
            </div>
            <div class="comment-list" id="commentList">
                <!-- 评论列表 -->
            </div>
            <div class="comment-input-wrapper">
                <input type="text" id="commentInput" placeholder="${t('writeComment')}" />
                <button class="comment-submit-btn" onclick="submitComment()">${t('send')}</button>
            </div>
        </div>
    `;
    document.body.appendChild(commentModal);
    commentModal.classList.add('active');
    
    // 加载该帖子的所有评论
    if (currentPost) {
        loadComments(currentPost.id);
    }
}

function closeCommentModal() {
    const commentModal = document.getElementById('commentModal');
    if (commentModal) {
        commentModal.remove();
    }
}

async function loadComments(postId) {
    const commentList = document.getElementById('commentList');
    if (!commentList) return;
    
    try {
        const response = await fetch(`/post/${postId}/comments`);
        const comments = await response.json();
        
        if (response.ok && comments.length > 0) {
            let html = '';
            comments.forEach(comment => {
                const date = new Date(comment.publish_time);
                html += `
                    <div class="comment-item">
                        <div class="comment-avatar"></div>
                        <div class="comment-content">
                            <div class="comment-header">
                                <span class="comment-author">${comment.author}</span>
                                <span class="comment-time">${date.getMonth() + 1}/${date.getDate()}</span>
                            </div>
                            <p class="comment-text">${comment.content}</p>
                        </div>
                    </div>
                `;
            });
            commentList.innerHTML = html;
        } else {
            commentList.innerHTML = `<div class="no-comments">${t('noComments')}</div>`;
        }
    } catch (error) {
        console.error("加载评论失败:", error);
    }
}

async function submitComment() {
    if (!currentPost) return;
    if (commentSubmitting) return;
    
    if (!requireLogin(() => submitComment())) return;
    
    const input = document.getElementById('commentInput');
    const submitBtn = document.querySelector('.comment-submit-btn');
    const content = input?.value.trim() || '';
    if (!content) {
        showToast(t('inputCommentRequired'), { type: 'warning' });
        return;
    }
    
    const username = localStorage.getItem('username');
    commentSubmitting = true;
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.classList.add('submitting');
    }
    
    try {
        const response = await fetch(`/post/${currentPost.id}/comment`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                author: username,
                content: content
            })
        });
        
        if (response.ok) {
            input.value = '';
            loadComments(currentPost.id);
            
            const commentBtn = document.querySelectorAll('.action-item')[2];
            currentPost.comments = (currentPost.comments || 0) + 1;
            commentBtn.innerHTML = `
                <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                <span>${currentPost.comments}</span>
            `;
            showToast(t('commentPosted'), { detail: t('commentHint') });
        } else {
            const data = await response.json();
            alert(t('requestFailed', { detail: data.detail }));
        }
    } catch (error) {
        console.error("评论失败:", error);
        alert(t('requestFailed', { detail: t('comments') }));
    } finally {
        commentSubmitting = false;
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.classList.remove('submitting');
        }
    }
}

// ==================== 搜索功能 ====================
function openSearch() {
    // 创建搜索弹窗
    const searchModal = document.createElement('div');
    searchModal.className = 'search-modal';
    searchModal.id = 'searchModal';
    searchModal.onclick = (e) => {
        if (e.target === searchModal) {
            closeSearch();
        }
    };
    searchModal.innerHTML = `
        <div class="search-modal-wrapper">
            <div class="search-header-fixed">
                <div class="search-bar">
                    <input type="text" id="searchInput" placeholder="${t('searchPosts')}" autofocus>
                    <button class="search-submit-btn" onclick="handleSearch()">${t('search')}</button>
                    <button class="search-cancel-btn" onclick="closeSearch()">✕</button>
                </div>
            </div>
            <div class="post-search-results" id="postSearchResults"></div>
        </div>
    `;
    document.body.appendChild(searchModal);
    searchModal.classList.add('active');
    
    // 绑定搜索事件
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', debounce(handleSearch, 300));
    
    // 初始加载所有帖子
    handleSearch();
}

function closeSearch() {
    const searchModal = document.getElementById('searchModal');
    if (searchModal) {
        searchModal.classList.remove('active');
        setTimeout(() => {
            searchModal.remove();
        }, 0.3);
    }
}

function debounce(func, delay) {
    let timer = null;
    return function() {
        clearTimeout(timer);
        timer = setTimeout(func, delay);
    };
}

async function handleSearch() {
    const query = document.getElementById('searchInput').value.trim();
    
    try {
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const posts = await response.json();
        
        if (response.ok) {
            await renderSearchResults(posts);
        }
    } catch (error) {
        console.error("搜索失败:", error);
    }
}

async function renderSearchResults(posts) {
    const container = document.getElementById('postSearchResults');
    if (!container) return;
    
    if (!posts || posts.length === 0) {
        container.innerHTML = `
            <div class="search-empty">
                <svg viewBox="0 0 24 24" fill="currentColor" width="48" height="48">
                    <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.77l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                </svg>
                <p>${t('noSearchResults')}</p>
            </div>
        `;
        return;
    }
    
    let html = '';
    const displayPosts = await Promise.all(posts.map(post => localizePostSummary(post)));
    displayPosts.forEach(post => {
        const photoSrc = post.photos && post.photos.length > 0 
            ? post.photos[0] 
            : `https://picsum.photos/400/300?random=${post.id}`;
        
        html += `
            <div class="search-result-item" onclick="searchResultClick(${post.id})">
                <img src="${photoSrc}" alt="${post.title}" class="search-result-image">
                <div class="search-result-info">
                    <h4 class="search-result-title">${post.title}</h4>
                    <p class="search-result-author">${post.author}</p>
                    <p class="search-result-location">📍 ${post.location}</p>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

function searchResultClick(postId) {
    closeSearch();
    openPostDetail(postId);
}

// 绑定搜索按钮点击事件
document.addEventListener('DOMContentLoaded', function() {
    renderHotCategories();
});

// ==================== 发布页面功能 ====================
const DEFAULT_LOCATION = {
    name: '北京市',
    address: '北京市',
    city: '北京市',
    latitude: 39.9042,
    longitude: 116.4074,
    source: 'default'
};

let currentUserLocation = { latitude: DEFAULT_LOCATION.latitude, longitude: DEFAULT_LOCATION.longitude };
let activeLocationPickerTarget = 'discover';
let locationFallbackNotifiedAt = 0;

function notifyLocationFallback() {
    const now = Date.now();
    if (now - locationFallbackNotifiedAt < 5000) return;
    locationFallbackNotifiedAt = now;
    showToast(t('locationFallbackTitle'), {
        type: 'warning',
        detail: t('locationFallbackHint'),
        actionText: t('retry'),
        onAction: () => {
            if (document.getElementById('discoverPage') && getComputedStyle(document.getElementById('discoverPage')).display !== 'none') {
                loadNearbyPosts({ forceLocation: true });
            } else {
                showLocationPicker({ target: 'discover' });
            }
        },
        duration: 5200
    });
}

const LocationService = {
    state: {
        currentCity: { ...DEFAULT_LOCATION },
        currentCoords: null,
        discoverLocation: { ...DEFAULT_LOCATION },
        publishLocation: null,
        mapDraftLocation: null
    },

    normalize(location, defaults = {}) {
        if (!location) return null;
        const latitude = Number(location.latitude ?? location.lat ?? defaults.latitude);
        const longitude = Number(location.longitude ?? location.lng ?? location.lon ?? defaults.longitude);
        if (!Number.isFinite(latitude) || !Number.isFinite(longitude)) return null;

        const rawName = String(location.name || location.location || location.address || defaults.name || '').trim();
        const address = String(location.address || rawName || defaults.address || '').trim();
        const city = String(location.city || extractCityName(address || rawName) || defaults.city || '').trim();
        const name = rawName || city || address || `位置 (${latitude.toFixed(4)}, ${longitude.toFixed(4)})`;

        return {
            name,
            address,
            city,
            latitude,
            longitude,
            source: location.source || defaults.source || 'manual',
            updatedAt: location.updatedAt || Date.now()
        };
    },

    setCurrentCity(location) {
        const normalized = this.normalize(location, DEFAULT_LOCATION);
        if (!normalized) return null;
        this.state.currentCity = normalized;
        return normalized;
    },

    setCurrentCoords(location) {
        const normalized = this.normalize(location, { ...DEFAULT_LOCATION, source: 'gps' });
        if (!normalized) return null;
        this.state.currentCoords = normalized;
        currentUserLocation = {
            latitude: normalized.latitude,
            longitude: normalized.longitude
        };
        return normalized;
    },

    setDiscoverLocation(location, options = {}) {
        const normalized = this.normalize(location, DEFAULT_LOCATION);
        if (!normalized) return null;
        this.state.discoverLocation = normalized;
        this.setCurrentCity(normalized);
        currentUserLocation = {
            latitude: normalized.latitude,
            longitude: normalized.longitude
        };

        const locationEl = document.getElementById('discoverLocation');
        if (locationEl) {
            locationEl.innerHTML = `📍 ${normalized.city || normalized.name}`;
        }

        if (options.persist !== false) {
            saveToRecentLocations(normalized);
        }

        if (options.refreshHome !== false) {
            refreshHomeGuidesIfVisible();
        }

        const discoverPage = document.getElementById('discoverPage');
        if (options.reload !== false && discoverPage && getComputedStyle(discoverPage).display !== 'none') {
            loadNearbyPosts();
        }

        return normalized;
    },

    setPublishLocation(location, options = {}) {
        const normalized = this.normalize(location, DEFAULT_LOCATION);
        if (!normalized) return null;
        this.state.publishLocation = normalized;
        currentLocation = normalized;

        const publishLocationEl = document.getElementById('locationValue');
        if (publishLocationEl) {
            publishLocationEl.textContent = normalized.name || normalized.city || normalized.address;
        }

        const locationBtn = document.getElementById('locationBtn');
        if (locationBtn) locationBtn.disabled = false;

        if (options.persist !== false) {
            saveToRecentLocations(normalized);
        }

        if (options.saveDraft !== false) {
            schedulePublishDraftSave();
        }

        return normalized;
    },

    setMapDraftLocation(location) {
        const normalized = this.normalize(location, this.getPickerBaseLocation());
        if (!normalized) return null;
        this.state.mapDraftLocation = normalized;
        selectedMapLocation = {
            latitude: normalized.latitude,
            longitude: normalized.longitude
        };
        mapAddress = normalized.address || normalized.name;
        return normalized;
    },

    getPickerBaseLocation() {
        if (activeLocationPickerTarget === 'publish') {
            return this.state.publishLocation || this.state.discoverLocation || DEFAULT_LOCATION;
        }
        return this.state.discoverLocation || this.state.currentCoords || DEFAULT_LOCATION;
    },

    getDiscoverOrigin() {
        return this.state.discoverLocation || this.state.currentCoords || DEFAULT_LOCATION;
    },

    getPublishLocation() {
        return this.state.publishLocation || currentLocation || DEFAULT_LOCATION;
    },

    applyPickerSelection(location, options = {}) {
        if (activeLocationPickerTarget === 'publish') {
            return this.setPublishLocation(location, options);
        }
        return this.setDiscoverLocation(location, options);
    }
};

let uploadedPhotos = [];
let currentLocation = null;
let editingPostId = null;
let publishReturnPage = 'home';
let publishReturnState = null;
let selectedPublishTags = [];
let publishDraftTimer = null;

function getPublishDraftKey() {
    const username = localStorage.getItem('username') || 'guest';
    return `publishDraft_${username}`;
}

function showPublishFeedback(message, type = 'info') {
    const feedback = document.getElementById('publishFeedback');
    if (!feedback) return;
    feedback.textContent = message;
    feedback.className = `publish-feedback ${type}`;
    feedback.hidden = false;
}

function clearPublishFeedback() {
    const feedback = document.getElementById('publishFeedback');
    if (!feedback) return;
    feedback.hidden = true;
    feedback.textContent = '';
    feedback.className = 'publish-feedback';
}

function buildGeneratedTitle(content) {
    const compact = String(content || '').replace(/\s+/g, ' ').trim();
    return compact ? compact.slice(0, 24) : t('postTitle');
}

function getPublishFormState() {
    const publishLocation = LocationService.getPublishLocation();
    return {
        title: document.getElementById('publishTitle')?.value || '',
        content: document.getElementById('publishContent')?.value || '',
        locationText: document.getElementById('locationValue')?.textContent || publishLocation.name || t('defaultCity'),
        location: publishLocation,
        duration: document.getElementById('durationInput')?.value || '',
        people: document.getElementById('peopleInput')?.value || '',
        photos: uploadedPhotos.map(photo => photo.src),
        tags: selectedPublishTags,
        savedAt: new Date().toISOString()
    };
}

function hasPublishDraftContent(draft) {
    return Boolean(
        draft &&
        (
            String(draft.title || '').trim() ||
            String(draft.content || '').trim() ||
            (Array.isArray(draft.photos) && draft.photos.length > 0) ||
            (Array.isArray(draft.tags) && draft.tags.length > 0)
        )
    );
}

function savePublishDraft({ quiet = true } = {}) {
    if (editingPostId !== null) return;
    const draft = getPublishFormState();
    if (!hasPublishDraftContent(draft)) {
        localStorage.removeItem(getPublishDraftKey());
        return;
    }
    localStorage.setItem(getPublishDraftKey(), JSON.stringify(draft));
    if (!quiet) showPublishFeedback(t('draftSaved'), 'success');
}

function schedulePublishDraftSave() {
    if (editingPostId !== null) return;
    clearTimeout(publishDraftTimer);
    publishDraftTimer = setTimeout(() => {
        savePublishDraft();
        const title = document.getElementById('publishTitle')?.value.trim();
        const content = document.getElementById('publishContent')?.value.trim();
        if (title || content || uploadedPhotos.length > 0) {
            showPublishFeedback(t('draftSaved'), 'success');
        }
    }, 600);
}

function clearPublishDraft() {
    localStorage.removeItem(getPublishDraftKey());
    clearTimeout(publishDraftTimer);
}

function loadPublishDraft() {
    try {
        return JSON.parse(localStorage.getItem(getPublishDraftKey()) || 'null');
    } catch (error) {
        return null;
    }
}

function applyPublishDraft(draft) {
    if (!hasPublishDraftContent(draft)) return false;
    document.getElementById('publishTitle').value = draft.title || '';
    document.getElementById('publishContent').value = draft.content || '';
    document.getElementById('durationInput').value = draft.duration || '';
    document.getElementById('peopleInput').value = draft.people || '';
    document.getElementById('locationValue').textContent = draft.locationText || t('defaultCity');
    LocationService.setPublishLocation(
        draft.location || { ...DEFAULT_LOCATION, name: draft.locationText || t('defaultCity') },
        { persist: false, saveDraft: false }
    );
    uploadedPhotos = Array.isArray(draft.photos)
        ? draft.photos.map((src, index) => ({ id: `draft-${index}-${Date.now()}`, src }))
        : [];
    selectedPublishTags = Array.isArray(draft.tags) ? draft.tags : [];
    renderPhotoGrid();
    renderPublishTags();
    showPublishFeedback(t('draftRestored'), 'success');
    return true;
}

function bindPublishDraftInputs() {
    ['publishTitle', 'publishContent', 'durationInput', 'peopleInput'].forEach(id => {
        const el = document.getElementById(id);
        if (!el || el.dataset.draftBound === 'true') return;
        el.dataset.draftBound = 'true';
        el.addEventListener('input', schedulePublishDraftSave);
    });
}

function renderPublishTags() {
    const container = document.getElementById('publishTagGrid');
    if (!container) return;

    container.innerHTML = POST_TAGS.map(tag => {
        const active = selectedPublishTags.includes(tag.id) ? ' active' : '';
        return `<button type="button" class="publish-tag-btn${active}" onclick="togglePublishTag('${tag.id}')">${getTagLabel(tag.id)}</button>`;
    }).join('');
}

function togglePublishTag(tagId) {
    if (selectedPublishTags.includes(tagId)) {
        selectedPublishTags = selectedPublishTags.filter(id => id !== tagId);
    } else {
        selectedPublishTags = [...selectedPublishTags, tagId];
    }
    renderPublishTags();
    schedulePublishDraftSave();
}

// 打开发布页面
function openPublishPage(options = {}) {
    const restoreDraft = options.restoreDraft !== false;
    if (!isUserLoggedIn()) {
        pendingPublishAfterAuth = true;
        pendingAuthAction = () => openPublishPage(options);
        document.getElementById('publishPage').style.display = 'none';
        requireLogin(pendingAuthAction);
        return;
    }
    
    // 重置发布表单
    publishReturnState = capturePageState();
    publishReturnPage = getVisibleNavigationPageId();
    uploadedPhotos = [];
    selectedPublishTags = [];
    LocationService.setPublishLocation(DEFAULT_LOCATION, { persist: false, saveDraft: false });
    document.getElementById('publishTitle').value = '';
    document.getElementById('publishContent').value = '';
    document.getElementById('publishBtn').disabled = false;
    document.getElementById('publishBtn').textContent = t('publish');
    clearPublishFeedback();
    document.getElementById('locationValue').textContent = t('defaultCity');
    document.getElementById('durationInput').value = '';
    document.getElementById('peopleInput').value = '';
    document.getElementById('photoGrid').innerHTML = `
        <div class="photo-add-btn" onclick="triggerPhotoUpload()">
            <svg viewBox="0 0 24 24" width="32" height="32"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"></path></svg>
        </div>
    `;
    renderPublishTags();
    bindPublishDraftInputs();
    if (!restoreDraft || !applyPublishDraft(loadPublishDraft())) {
        showPublishFeedback(t('publishReadyHint'), 'info');
    }
    
    showSinglePage('publishPage', { showBottomNav: false });
}

// 关闭发布页面
async function closePublishPage(options = {}) {
    const shouldSaveDraft = options.saveDraft !== false;
    const shouldRefresh = options.refreshAfterClose === true;
    if (shouldSaveDraft && editingPostId === null) {
        savePublishDraft();
    }
    document.getElementById('publishPage').style.display = 'none';
    if (!restorePageState(publishReturnState)) {
        showSinglePage('mainPage', { showBottomNav: true });
        setTopNavActive(0);
    }
    
    if (shouldRefresh && publishReturnPage === 'myPostsPage') {
        const currentUser = localStorage.getItem('username');
        if (currentUser) {
            await loadMyPostsForProfile(currentUser);
        }
    } else if (shouldRefresh && publishReturnPage === 'mainPage') {
        await loadMyPosts();
    }
    
    // 重置编辑状态
    editingPostId = null;
    publishReturnPage = 'home';
    publishReturnState = null;
}

// 触发照片上传
function triggerPhotoUpload() {
    const fileInput = document.getElementById('photoFile');
    fileInput.value = '';
    fileInput.click();
}

// 处理照片上传
function handlePhotoUpload(event) {
    const files = event.target.files;
    if (!files || files.length === 0) return;
    
    const maxPhotos = 9;
    const remainingSlots = maxPhotos - uploadedPhotos.length;
    const photosToAdd = Math.min(files.length, remainingSlots);
    showPublishFeedback(t('loading'), 'info');
    
    for (let i = 0; i < photosToAdd; i++) {
        const file = files[i];
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const photoData = {
                id: Date.now() + i,
                src: e.target.result,
                file: file
            };
            uploadedPhotos.push(photoData);
            renderPhotoGrid();
            schedulePublishDraftSave();
            showPublishFeedback(t('draftSaved'), 'success');
        };
        
        reader.readAsDataURL(file);
    }
}

// 渲染照片网格
function renderPhotoGrid() {
    const grid = document.getElementById('photoGrid');
    const hasAddButton = uploadedPhotos.length < 9;
    
    let html = '';
    uploadedPhotos.forEach((photo, index) => {
        html += `
            <div class="photo-item" style="order: ${index}">
                <img src="${photo.src}" alt="照片">
                <div class="photo-remove" onclick="removePhoto('${String(photo.id).replace(/'/g, "\\'")}')">×</div>
            </div>
        `;
    });
    
    if (hasAddButton) {
        html += `
            <div class="photo-add-btn" onclick="triggerPhotoUpload()" style="order: ${uploadedPhotos.length}">
                <svg viewBox="0 0 24 24" width="32" height="32"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"></path></svg>
            </div>
        `;
    }
    
    grid.innerHTML = html;
}

// 删除照片
function removePhoto(id) {
    uploadedPhotos = uploadedPhotos.filter(photo => photo.id !== id);
    renderPhotoGrid();
    schedulePublishDraftSave();
}

// 获取当前位置
function getLocation() {
    if (!navigator.geolocation) {
        showToast(t('locationFallbackTitle'), { type: 'warning', detail: t('locationFallbackHint') });
        LocationService.setPublishLocation(DEFAULT_LOCATION, { persist: false });
        return;
    }
    
    document.getElementById('locationBtn').disabled = true;
    document.getElementById('locationValue').textContent = t('gettingLocation');
    
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            LocationService.setCurrentCoords({
                name: '当前位置',
                latitude,
                longitude,
                source: 'gps'
            });
            
            // 使用逆地理编码获取地址（这里使用一个模拟地址）
            getAddressFromCoords(latitude, longitude);
        },
        function(error) {
            document.getElementById('locationBtn').disabled = false;
            LocationService.setPublishLocation(DEFAULT_LOCATION, { persist: false });
            notifyLocationFallback();
        },
        { timeout: 10000 }
    );
}

// 根据坐标获取地址（模拟）
function getAddressFromCoords(lat, lng) {
    // 先尝试使用位置选择器中的位置
    // 如果没有，才使用模拟地址
    const mockAddresses = [
        '北京市朝阳区',
        '上海市浦东新区',
        '广州市天河区',
        '深圳市南山区',
        '杭州市西湖区',
        '成都市锦江区',
        '武汉市江汉区',
        '南京市玄武区'
    ];
    
    // 根据坐标生成一个固定的地址索引
    const index = Math.abs(Math.floor((lat + lng) * 100)) % mockAddresses.length;
    const address = mockAddresses[index];
    
    LocationService.setPublishLocation({
        name: address,
        address,
        city: extractCityName(address),
        latitude: lat,
        longitude: lng,
        source: 'gps'
    });
}

// 处理发布
async function handlePublish() {
    const publishBtn = document.getElementById('publishBtn');
    
    // 防止重复提交
    if (publishBtn.disabled) {
        return;
    }
    
    const rawTitle = document.getElementById('publishTitle').value.trim();
    const content = document.getElementById('publishContent').value.trim();
    const duration = document.getElementById('durationInput').value;
    const people = document.getElementById('peopleInput').value;
    const isEditing = editingPostId !== null;
    const title = rawTitle || buildGeneratedTitle(content);
    
    // 调试日志
    console.log("发布按钮点击");
    console.log("照片数量:", uploadedPhotos.length);
    console.log("标题:", rawTitle);
    console.log("位置:", LocationService.getPublishLocation());
    
    // 验证
    if (!rawTitle && !content) {
        showPublishFeedback(t('publishNeedText'), 'error');
        showToast(t('publishNeedText'), { type: 'warning' });
        return;
    }
    
    const publishLocation = LocationService.getPublishLocation();
    
    // 禁用按钮防止重复提交
    publishBtn.disabled = true;
    publishBtn.textContent = isEditing ? t('saving') : t('publishLoading');
    showPublishFeedback(isEditing ? t('saving') : t('publishLoading'), 'info');
    savePublishDraft();
    
    // 准备发布数据
    const publishData = {
        title: title,
        content: content,
        photos: uploadedPhotos.map(p => p.src), // 这里应该上传到服务器，简化处理只传base64
        location: publishLocation.name || document.getElementById('locationValue').textContent,
        city: publishLocation.city || extractCityName(publishLocation.name || publishLocation.address || ''),
        latitude: publishLocation.latitude,
        longitude: publishLocation.longitude,
        duration: duration ? parseInt(duration) : 1,
        people: people ? parseInt(people) : 1,
        tags: selectedPublishTags,
        author: localStorage.getItem('username'),
        publishTime: new Date().toISOString()
    };
    
    try {
        let response, data;
        
        if (isEditing) {
            // 更新现有帖子
            response = await fetch(`/post/${editingPostId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(publishData)
            });
            data = await response.json();
            
            if (response.ok) {
                showToast(t('editSuccess'));
                clearPublishFeedback();
            } else {
                showPublishFeedback(t('requestFailed', { detail: data.detail || t('saveChanges') }), 'error');
                showToast(t('draftKept'), { type: 'warning' });
                return;
            }
        } else {
            // 发布新帖子
            response = await fetch('/publish', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(publishData)
            });
            data = await response.json();
            
            if (response.ok) {
                clearPublishDraft();
                clearPublishFeedback();
                showToast(t('publishSuccess'));
            } else {
                showPublishFeedback(t('requestFailed', { detail: data.detail || t('publish') }), 'error');
                showToast(t('draftKept'), { type: 'warning' });
                return;
            }
        }
        
        closePublishPage({ saveDraft: false, refreshAfterClose: true });
    } catch (error) {
        savePublishDraft({ quiet: false });
        showPublishFeedback(t('draftKept'), 'error');
        showToast(t('draftKept'), { type: 'warning' });
        console.error("操作失败:", error);
    } finally {
        // 恢复按钮状态
        publishBtn.disabled = false;
        publishBtn.textContent = isEditing ? t('saveChanges') : t('publish');
    }
}

// 编辑帖子
async function editPost(postId) {
    try {
        openPublishPage({ restoreDraft: false });
        publishReturnPage = 'myPostsPage';
        editingPostId = postId;
        document.getElementById('publishBtn').textContent = t('saveChanges');
        document.getElementById('publishTitle').value = t('loading');
        document.getElementById('publishContent').value = '';
        clearPublishFeedback();

        const response = await fetchWithTimeout(`/post/${postId}`);
        const post = await response.json();
        
        if (!response.ok) {
            showPublishFeedback(t('requestFailed', { detail: t('editPost') }), 'error');
            showToast(t('requestFailed', { detail: t('editPost') }), { type: 'warning' });
            closePublishPage();
            return;
        }
        
        // 填充现有数据
        document.getElementById('publishTitle').value = post.title;
        document.getElementById('publishContent').value = post.content || '';
        document.getElementById('locationValue').textContent = post.location;
        document.getElementById('durationInput').value = post.duration || '';
        document.getElementById('peopleInput').value = post.people || '';
        selectedPublishTags = Array.isArray(post.tags) ? post.tags : [];
        renderPublishTags();
        
        // 设置位置坐标
        LocationService.setPublishLocation({
            name: post.location,
            address: post.location,
            city: post.city || extractCityName(post.location),
            latitude: post.latitude,
            longitude: post.longitude,
            source: 'edit'
        }, { persist: false, saveDraft: false });
        
        // 设置帖子ID用于更新
        editingPostId = postId;
        
        // 修改按钮文字
        document.getElementById('publishBtn').textContent = t('saveChanges');
        
        // 如果有照片，加载照片
        if (post.photos && post.photos.length > 0) {
            uploadedPhotos = post.photos.map((src, index) => ({
                id: `photo-${index}`,
                src: src
            }));
            renderPhotoGrid();
        }
        showPublishFeedback(t('publishReadyHint'), 'info');
        
    } catch (error) {
        console.error("编辑帖子失败:", error);
        showPublishFeedback(t('requestFailed', { detail: t('editPost') }), 'error');
        showToast(t('requestFailed', { detail: t('editPost') }), { type: 'warning' });
    }
}

// 删除帖子
async function deletePost(postId) {
    if (!confirm(t('deleteConfirm'))) {
        return;
    }
    
    try {
        const response = await fetch(`/post/${postId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            alert(t('deleteSuccess'));
            // 刷新帖子列表
            const currentUser = localStorage.getItem('username');
            await loadMyPostsForProfile(currentUser);
        } else {
            const data = await response.json();
            alert(t('requestFailed', { detail: data.detail }));
        }
    } catch (error) {
        console.error("删除帖子失败:", error);
        alert(t('deleteFailed'));
    }
}

// 绑定底部导航加号按钮
document.addEventListener('DOMContentLoaded', function() {
    const navCenterBtn = document.querySelector('.nav-center-btn');
    if (navCenterBtn) {
        navCenterBtn.addEventListener('click', openPublishPage);
    }

});

window.addEventListener('load', checkLoginStatus);

// 显示位置选择器（修改GPS定位）- 新界面
function showLocationPicker(options = {}) {
    console.log('=== 显示位置选择器 ===');
    activeLocationPickerTarget = options.target || inferLocationPickerTarget();
    const overlay = document.getElementById('locationPickerOverlay');
    const picker = document.getElementById('locationPicker');
    
    console.log('overlay元素:', overlay);
    console.log('picker元素:', picker);
    
    if (overlay) {
        overlay.classList.add('active');
        console.log('overlay已添加active类');
    } else {
        console.error('locationPickerOverlay元素未找到！');
    }
    
    if (picker) {
        picker.classList.add('active');
        console.log('picker已添加active类');
    } else {
        console.error('locationPicker元素未找到！');
    }
    
    loadRecentLocations();
    console.log('最近位置已加载');
}

// 关闭位置选择器
function closeLocationPicker() {
    console.log('=== 关闭位置选择器 ===');
    const overlay = document.getElementById('locationPickerOverlay');
    const picker = document.getElementById('locationPicker');
    
    console.log('overlay:', overlay);
    console.log('picker:', picker);
    
    if (overlay) {
        overlay.classList.remove('active');
        console.log('overlay active类已移除');
    }
    
    if (picker) {
        picker.classList.remove('active');
        console.log('picker active类已移除');
    }
    
    const input = document.getElementById('locationSearchInput');
    if (input) {
        input.value = '';
        console.log('搜索框已清空');
    }
}

// 确保位置选择器内部点击正常工作
document.addEventListener('DOMContentLoaded', function() {
    // 绑定城市标签点击事件
    const cityTags = document.querySelectorAll('.city-tag');
    cityTags.forEach(tag => {
        tag.addEventListener('click', function(e) {
            e.stopPropagation(); // 防止事件冒泡到overlay
            const name = this.dataset.name;
            const lat = parseFloat(this.dataset.lat);
            const lng = parseFloat(this.dataset.lng);
            console.log('城市标签被点击:', name, lat, lng);
            if (name && !isNaN(lat) && !isNaN(lng)) {
                selectLocation({ name, address: name, city: name, latitude: lat, longitude: lng, source: 'manual-city' });
            }
        });
    });
    
    // 绑定当前位置项点击事件
    const currentLocationItem = document.querySelector('.current-location');
    if (currentLocationItem) {
        currentLocationItem.addEventListener('click', function(e) {
            e.stopPropagation();
            console.log('当前位置项被点击');
            locateCurrentUserFromPicker();
        });
    }
});

// 从地址中提取市名
function extractCityName(fullAddress) {
    if (!fullAddress) return '未选择位置';
    
    // 匹配省/自治区/直辖市 + 市 的模式
    const patterns = [
        /([\u4e00-\u9fa5]+省)([\u4e00-\u9fa5]+市)/,    // 某某省某某市
        /([\u4e00-\u9fa5]+自治区)([\u4e00-\u9fa5]+市)/, // 某某自治区某某市
        /([\u4e00-\u9fa5]+市)([\u4e00-\u9fa5]+区)/,    // 某某市某某区（直辖市）
        /([\u4e00-\u9fa5]+市)/                          // 单独的市名
    ];
    
    for (let index = 0; index < patterns.length; index++) {
        const pattern = patterns[index];
        const match = fullAddress.match(pattern);
        if (match) {
            // 如果是 "北京市东城区" 这种模式，返回 "北京市"
            if (index === 2) {
                return match[1];
            }
            // 如果是 "广东省深圳市" 这种模式，返回 "深圳市"
            if (match[2]) {
                return match[2];
            }
            // 如果只有市名，直接返回
            return match[1];
        }
    }
    
    // 如果都匹配不到，返回原地址
    return fullAddress;
}

// 选择位置
function inferLocationPickerTarget() {
    const publishPage = document.getElementById('publishPage');
    if (publishPage && getComputedStyle(publishPage).display !== 'none') {
        return 'publish';
    }
    return 'discover';
}

function selectLocation(locationOrName, latitude, longitude) {
    console.log('=== 选择位置函数被调用 ===');
    const location = typeof locationOrName === 'object'
        ? locationOrName
        : {
            name: locationOrName,
            address: locationOrName,
            city: extractCityName(locationOrName),
            latitude,
            longitude
        };
    console.log('位置信息:', location);

    LocationService.applyPickerSelection(location);
    closeLocationPicker();
    console.log('位置选择器已关闭');
}

// 地图选点相关变量
let mapInstance = null;
let selectedMapLocation = null;
let mapAddress = '';
let mapSearchTimeout = null;

// 地图搜索数据库（包含城市、景点、商圈等）
const mapSearchDatabase = [
    { name: '北京', address: '北京市', latitude: 39.9042, longitude: 116.4074 },
    { name: '故宫博物院', address: '北京市东城区景山前街4号', latitude: 39.9163, longitude: 116.3972 },
    { name: '天安门广场', address: '北京市东城区天安门广场', latitude: 39.9042, longitude: 116.4074 },
    { name: '八达岭长城', address: '北京市延庆区八达岭镇', latitude: 40.3607, longitude: 116.0147 },
    { name: '颐和园', address: '北京市海淀区新建宫门路19号', latitude: 39.9999, longitude: 116.2755 },
    { name: '三里屯', address: '北京市朝阳区三里屯路', latitude: 39.9371, longitude: 116.4477 },
    { name: '上海', address: '上海市', latitude: 31.2304, longitude: 121.4737 },
    { name: '外滩', address: '上海市黄浦区中山东一路', latitude: 31.2304, longitude: 121.4998 },
    { name: '东方明珠', address: '上海市浦东新区世纪大道1号', latitude: 31.2397, longitude: 121.4998 },
    { name: '南京路', address: '上海市黄浦区南京东路', latitude: 31.2397, longitude: 121.4742 },
    { name: '广州', address: '广州市', latitude: 23.1291, longitude: 113.2644 },
    { name: '广州塔', address: '广州市海珠区阅江西路222号', latitude: 23.1060, longitude: 113.3245 },
    { name: '深圳', address: '深圳市', latitude: 22.5431, longitude: 114.0579 },
    { name: '深圳湾', address: '深圳市南山区滨海大道', latitude: 22.4955, longitude: 113.9172 },
    { name: '杭州', address: '杭州市', latitude: 30.2741, longitude: 120.1552 },
    { name: '西湖', address: '杭州市西湖区', latitude: 30.2741, longitude: 120.1552 },
    { name: '成都', address: '成都市', latitude: 30.5728, longitude: 104.0668 },
    { name: '宽窄巷子', address: '成都市青羊区金河宾馆旁', latitude: 30.6633, longitude: 104.0355 },
    { name: '锦里', address: '成都市武侯区武侯祠大街231号', latitude: 30.6571, longitude: 104.0360 },
    { name: '重庆', address: '重庆市', latitude: 29.4316, longitude: 106.9123 },
    { name: '洪崖洞', address: '重庆市渝中区嘉陵江滨江路88号', latitude: 29.4419, longitude: 106.9148 },
    { name: '解放碑', address: '重庆市渝中区民族路177号', latitude: 29.4316, longitude: 106.9123 },
    { name: '武汉', address: '武汉市', latitude: 30.5928, longitude: 114.3055 },
    { name: '黄鹤楼', address: '武汉市武昌区蛇山西山坡特1号', latitude: 30.5852, longitude: 114.3051 },
    { name: '西安', address: '西安市', latitude: 34.2619, longitude: 108.9463 },
    { name: '兵马俑', address: '西安市临潼区秦俑馆公路', latitude: 34.3835, longitude: 109.2741 },
    { name: '大雁塔', address: '西安市雁塔区慈恩路1号', latitude: 34.2252, longitude: 108.9536 },
    { name: '南京', address: '南京市', latitude: 32.0603, longitude: 118.7969 },
    { name: '夫子庙', address: '南京市秦淮区贡院街152号', latitude: 32.0350, longitude: 118.7919 },
    { name: '苏州', address: '苏州市', latitude: 31.3251, longitude: 120.6265 },
    { name: '拙政园', address: '苏州市姑苏区东北街178号', latitude: 31.3230, longitude: 120.6360 },
    { name: '天津', address: '天津市', latitude: 39.0842, longitude: 117.2009 },
    { name: '天津之眼', address: '天津市河北区李公祠大街', latitude: 39.1322, longitude: 117.2065 }
];

// 防抖搜索
function debounceMapSearch() {
    clearTimeout(mapSearchTimeout);
    mapSearchTimeout = setTimeout(() => {
        const searchInput = document.getElementById('mapSearchInput');
        const keyword = searchInput.value.trim();
        
        // 显示/隐藏清除按钮
        const cancelBtn = document.getElementById('mapSearchCancel');
        cancelBtn.style.display = keyword ? 'block' : 'none';
        
        if (!keyword) {
            clearMapSearchResults();
            return;
        }
        
        // 执行搜索
        performMapSearch(keyword);
    }, 300);
}

// 执行搜索
function performMapSearch(keyword) {
    console.log('地图搜索:', keyword);
    
    // 过滤匹配的地点
    const results = mapSearchDatabase.filter(item => 
        item.name.includes(keyword) || 
        item.address.includes(keyword)
    );
    
    console.log('搜索结果:', results.length, '个');
    
    // 同时使用Nominatim搜索（外部API）
    fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(keyword)}&format=json&limit=10&accept-language=zh-CN`)
        .then(response => response.json())
        .then(data => {
            if (data && data.length > 0) {
                // 合并结果（去重）
                const externalResults = data.map(item => ({
                    name: item.display_name.split(',')[0],
                    address: item.display_name,
                    latitude: parseFloat(item.lat),
                    longitude: parseFloat(item.lon)
                }));
                
                // 合并并去重
                const allResults = [...results];
                externalResults.forEach(external => {
                    const exists = allResults.some(r => 
                        Math.abs(r.latitude - external.latitude) < 0.01 && 
                        Math.abs(r.longitude - external.longitude) < 0.01
                    );
                    if (!exists) {
                        allResults.push(external);
                    }
                });
                
                displayMapSearchResults(allResults.slice(0, 10));
            } else {
                displayMapSearchResults(results.slice(0, 10));
            }
        })
        .catch(error => {
            console.error('外部搜索失败:', error);
            displayMapSearchResults(results.slice(0, 10));
        });
}

// 显示搜索结果
function displayMapSearchResults(results) {
    const resultsContainer = document.getElementById('mapSearchResults');
    
    if (!results || results.length === 0) {
        resultsContainer.innerHTML = `<div style="padding: 20px; text-align: center; color: #999;">${t('noMapResults')}</div>`;
        return;
    }
    
        resultsContainer.innerHTML = results.map(item => `
        <div class="map-search-item" onclick="selectMapSearchResult(${item.latitude}, ${item.longitude}, '${escapeJsString(item.name)}', '${escapeJsString(item.address)}')">
            <div class="result-icon">📍</div>
            <div class="result-info">
                <p class="result-title">${escapeHtml(item.name)}</p>
                <p class="result-address">${escapeHtml(item.address)}</p>
            </div>
        </div>
    `).join('');
}

// 选择搜索结果
function selectMapSearchResult(latitude, longitude, name, address) {
    console.log('选择搜索结果:', name, latitude, longitude);
    
    LocationService.setMapDraftLocation({
        name,
        address: address || name,
        city: extractCityName(address || name),
        latitude,
        longitude,
        source: 'search'
    });
    
    // 更新地图
    if (mapInstance && typeof mapInstance.setView === 'function') {
        mapInstance.setView([latitude, longitude], 16);
    }
    
    // 更新地址显示
    const addressEl = document.getElementById('mapAddress');
    if (addressEl) {
        addressEl.textContent = mapAddress;
    }
    
    // 清空搜索
    clearMapSearch();
    
    // 保存到最近使用
    saveToRecentLocations(LocationService.state.mapDraftLocation);
}

// 清除搜索
function clearMapSearch() {
    const searchInput = document.getElementById('mapSearchInput');
    const cancelBtn = document.getElementById('mapSearchCancel');
    const resultsContainer = document.getElementById('mapSearchResults');
    
    searchInput.value = '';
    cancelBtn.style.display = 'none';
    resultsContainer.innerHTML = '';
}

// 清除搜索结果
function clearMapSearchResults() {
    const resultsContainer = document.getElementById('mapSearchResults');
    resultsContainer.innerHTML = '';
}

// HTML转义
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function escapeJsString(text) {
    return String(text || '').replace(/\\/g, '\\\\').replace(/'/g, "\\'");
}

// 显示地图选点器
function showMapSelector() {
    console.log('=== 显示地图选点器 ===');
    
    // 关闭位置选择器
    closeLocationPicker();
    
    // 显示地图选点器
    const overlay = document.getElementById('mapSelectorOverlay');
    const selector = document.getElementById('mapSelector');
    
    if (overlay) overlay.classList.add('active');
    if (selector) selector.classList.add('active');
    
    // 初始化地图
    const baseLocation = LocationService.getPickerBaseLocation();
    selectedMapLocation = {
        latitude: baseLocation.latitude,
        longitude: baseLocation.longitude
    };
    mapAddress = baseLocation.address || baseLocation.name || '';
    LocationService.state.mapDraftLocation = { ...baseLocation };
    initMap();
}

// 关闭地图选点器
function closeMapSelector() {
    console.log('=== 关闭地图选点器 ===');
    
    const overlay = document.getElementById('mapSelectorOverlay');
    const selector = document.getElementById('mapSelector');
    
    if (overlay) overlay.classList.remove('active');
    if (selector) selector.classList.remove('active');
}

// 确认地图选择
function confirmMapSelection() {
    console.log('=== 确认地图选择 ===');
    console.log('选中的位置:', selectedMapLocation);
    
    if (selectedMapLocation) {
        const draft = LocationService.state.mapDraftLocation || {
            name: mapAddress || `位置 (${selectedMapLocation.latitude.toFixed(4)}, ${selectedMapLocation.longitude.toFixed(4)})`,
            address: mapAddress,
            latitude: selectedMapLocation.latitude,
            longitude: selectedMapLocation.longitude,
            source: 'map'
        };
        selectLocation(draft);
    }
    
    closeMapSelector();
}

// 初始化地图
function initMap() {
    console.log('=== 初始化地图 ===');
    
    const mapContainer = document.getElementById('mapContainer');
    if (!mapContainer) {
        console.error('地图容器未找到');
        return;
    }
    
    // 如果地图已初始化，直接返回
    if (mapInstance) {
        console.log('地图已初始化');
        const baseLocation = LocationService.getPickerBaseLocation();
        if (typeof mapInstance.setView === 'function') {
            mapInstance.setView([baseLocation.latitude, baseLocation.longitude], 15);
        }
        if (window.mapCenterMarker) {
            window.mapCenterMarker.setLatLng([baseLocation.latitude, baseLocation.longitude]);
        }
        updateAddress(baseLocation.longitude, baseLocation.latitude);
        return;
    }
    
    // 先清空容器
    mapContainer.innerHTML = '';
    
    // 检查Leaflet是否加载
    if (typeof L === 'undefined') {
        console.error('Leaflet地图库未加载，使用简单地图模式');
        initSimpleMap();
        return;
    }
    
    try {
        // 创建Leaflet地图实例
        const baseLocation = LocationService.getPickerBaseLocation();
        mapInstance = L.map('mapContainer').setView(
            [baseLocation.latitude, baseLocation.longitude], 
            15
        );
        
        // 添加OpenStreetMap图层
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(mapInstance);
        
        // 添加缩放控件
        L.control.zoom({ position: 'bottomright' }).addTo(mapInstance);
        
        // 创建中心点标记（可拖动）
        const centerMarker = L.marker(
            [baseLocation.latitude, baseLocation.longitude],
            {
                icon: L.divIcon({
                    className: 'map-center-icon',
                    html: '<div class="marker-pin"></div>',
                    iconSize: [40, 40],
                    iconAnchor: [20, 40]
                }),
                draggable: true  // 允许拖动
            }
        ).addTo(mapInstance);
        
        // 保存标记引用用于更新
        window.mapCenterMarker = centerMarker;
        
        // 监听标记拖动事件（拖动图标时更新地址）
        centerMarker.on('drag', function(e) {
            const latlng = e.target.getLatLng();
            selectedMapLocation = {
                latitude: latlng.lat,
                longitude: latlng.lng
            };
            LocationService.setMapDraftLocation({
                name: mapAddress,
                address: mapAddress,
                latitude: latlng.lat,
                longitude: latlng.lng,
                source: 'map'
            });
        });
        
        // 监听标记拖动结束事件（拖动完成后更新地址）
        centerMarker.on('dragend', function(e) {
            const latlng = e.target.getLatLng();
            updateAddress(latlng.lng, latlng.lat);
        });
        
        // 监听地图移动事件（拖动地图时图标位置不变，只有用户拖动图标才会移动）
        // 移除：不再让图标跟随地图中心移动
        
        // 监听地图点击事件（点击地图时更新标记位置和地址）
        mapInstance.on('click', function(e) {
            selectedMapLocation = {
                latitude: e.latlng.lat,
                longitude: e.latlng.lng
            };
            LocationService.setMapDraftLocation({
                name: mapAddress,
                address: mapAddress,
                latitude: e.latlng.lat,
                longitude: e.latlng.lng,
                source: 'map'
            });
            
            // 更新中心点标记位置
            centerMarker.setLatLng(e.latlng);
            
            // 更新地址（点击时才更新）
            updateAddress(e.latlng.lng, e.latlng.lat);
        });
        
        // 初始更新地址
        updateAddress(baseLocation.longitude, baseLocation.latitude);
        
        console.log('Leaflet地图初始化成功');
    } catch (error) {
        console.error('Leaflet地图初始化失败:', error);
        initSimpleMap();
    }
}

// 简单地图模式（备用方案）
function initSimpleMap() {
    console.log('=== 使用简单地图模式 ===');
    
    const mapContainer = document.getElementById('mapContainer');
    if (!mapContainer) return;
    let simpleMapDraftLocation = { ...LocationService.getPickerBaseLocation() };
    
    // 创建简单地图界面
    mapContainer.innerHTML = `
        <div class="simple-map">
            <div class="simple-map-grid"></div>
            <div class="simple-map-marker" id="simpleMapMarker" style="cursor: grab;">
                <svg viewBox="0 0 24 24" width="40" height="40" fill="#ff6b6b">
                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                </svg>
            </div>
            <div class="simple-map-info">
                <p>📍 ${simpleMapDraftLocation.latitude.toFixed(4)}, ${simpleMapDraftLocation.longitude.toFixed(4)}</p>
                <p class="hint">拖动红色图标选择位置，拖动背景移动地图</p>
            </div>
        </div>
    `;
    
    const simpleMap = document.querySelector('.simple-map');
    const marker = document.getElementById('simpleMapMarker');
    let isDraggingMap = false;
    let isDraggingMarker = false;
    let startX, startY;
    
    // 拖动地图（背景）- 不更新地址
    simpleMap.addEventListener('mousedown', function(e) {
        // 如果点击的是标记，不拖动地图
        if (e.target === marker || marker.contains(e.target)) {
            return;
        }
        isDraggingMap = true;
        startX = e.clientX;
        startY = e.clientY;
    });
    
    document.addEventListener('mousemove', function(e) {
        // 拖动地图 - 图标位置不变，只有背景移动
        if (isDraggingMap) {
            const deltaX = e.clientX - startX;
            const deltaY = e.clientY - startY;
            
            // 更新位置（模拟地图移动）
            simpleMapDraftLocation.longitude += deltaX * 0.0001;
            simpleMapDraftLocation.latitude -= deltaY * 0.0001;
            
            // 更新显示坐标（仅显示）
            const infoEl = document.querySelector('.simple-map-info p:first-child');
            if (infoEl) {
                infoEl.textContent = `📍 ${simpleMapDraftLocation.latitude.toFixed(4)}, ${simpleMapDraftLocation.longitude.toFixed(4)}`;
            }
            
            startX = e.clientX;
            startY = e.clientY;
        }
        
        // 拖动标记 - 只有拖动图标时才更新位置
        if (isDraggingMarker) {
            const deltaX = e.clientX - startX;
            const deltaY = e.clientY - startY;
            
            // 更新位置
            simpleMapDraftLocation.longitude += deltaX * 0.0001;
            simpleMapDraftLocation.latitude -= deltaY * 0.0001;
            
            // 更新显示坐标
            const infoEl = document.querySelector('.simple-map-info p:first-child');
            if (infoEl) {
                infoEl.textContent = `📍 ${simpleMapDraftLocation.latitude.toFixed(4)}, ${simpleMapDraftLocation.longitude.toFixed(4)}`;
            }
            
            startX = e.clientX;
            startY = e.clientY;
        }
    });
    
    document.addEventListener('mouseup', function() {
        // 拖动标记结束时更新地址
        if (isDraggingMarker) {
            LocationService.setMapDraftLocation({ ...simpleMapDraftLocation, source: 'map' });
            updateAddress(simpleMapDraftLocation.longitude, simpleMapDraftLocation.latitude);
        }
        isDraggingMap = false;
        isDraggingMarker = false;
    });
    
    // 拖动红色标记
    marker.addEventListener('mousedown', function(e) {
        e.stopPropagation(); // 阻止事件冒泡到地图
        isDraggingMarker = true;
        startX = e.clientX;
        startY = e.clientY;
        marker.style.cursor = 'grabbing';
    });
    
    marker.addEventListener('mouseup', function() {
        marker.style.cursor = 'grab';
    });
    
    // 点击地图更新位置（点击时更新地址）
    simpleMap.addEventListener('click', function(e) {
        if (!isDraggingMap && !isDraggingMarker) {
            LocationService.setMapDraftLocation({ ...simpleMapDraftLocation, source: 'map' });
            updateAddress(simpleMapDraftLocation.longitude, simpleMapDraftLocation.latitude);
        }
    });
    
    // 初始更新地址
    updateAddress(simpleMapDraftLocation.longitude, simpleMapDraftLocation.latitude);
    
    console.log('简单地图模式初始化成功');
}

// 显示地图加载错误
function showMapError() {
    const mapContainer = document.getElementById('mapContainer');
    if (mapContainer) {
        mapContainer.innerHTML = `
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center; padding: 20px;">
                <div style="font-size: 48px; margin-bottom: 15px;">🗺️</div>
                <p style="color: #666; margin-bottom: 10px;">地图加载失败</p>
                <p style="color: #999; font-size: 14px;">请检查网络连接或刷新页面重试</p>
                <button onclick="initMap()" style="margin-top: 15px; padding: 10px 20px; background: #ff6b6b; color: white; border: none; border-radius: 20px; cursor: pointer;">
                    重新加载
                </button>
            </div>
        `;
    }
}

// 更新地图中心位置（仅更新标记，不更新地址）
function updateMapCenterLocation() {
    if (!mapInstance) return;
    
    const center = mapInstance.getCenter();
    
    // 更新中心点标记位置（跟随地图移动）
    if (window.mapCenterMarker) {
        window.mapCenterMarker.setLatLng(center);
    }
}

// 更新地址信息（使用OpenStreetMap的Nominatim服务）
function updateAddress(lng, lat) {
    console.log('=== 更新地址信息 ===', lng, lat);
    
    // 使用Nominatim逆地理编码服务
    const url = `https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lng}&format=json&accept-language=zh-CN`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data && data.display_name) {
                mapAddress = data.display_name;
                LocationService.setMapDraftLocation({
                    name: mapAddress,
                    address: mapAddress,
                    city: extractCityName(mapAddress),
                    latitude: lat,
                    longitude: lng,
                    source: 'map'
                });
                
                const addressEl = document.getElementById('mapAddress');
                if (addressEl) {
                    addressEl.textContent = mapAddress;
                }
                
                console.log('地址解析成功:', mapAddress);
            } else {
                mapAddress = '';
                LocationService.setMapDraftLocation({
                    name: `位置 (${lat.toFixed(4)}, ${lng.toFixed(4)})`,
                    latitude: lat,
                    longitude: lng,
                    source: 'map'
                });
                const addressEl = document.getElementById('mapAddress');
                if (addressEl) {
                    addressEl.textContent = `(${lat.toFixed(4)}, ${lng.toFixed(4)})`;
                }
                console.log('地址解析失败');
            }
        })
        .catch(error => {
            console.error('地址解析请求失败:', error);
            mapAddress = '';
            LocationService.setMapDraftLocation({
                name: `位置 (${lat.toFixed(4)}, ${lng.toFixed(4)})`,
                latitude: lat,
                longitude: lng,
                source: 'map'
            });
            const addressEl = document.getElementById('mapAddress');
            if (addressEl) {
                addressEl.textContent = `(${lat.toFixed(4)}, ${lng.toFixed(4)})`;
            }
        });
}

// 在地图上获取当前位置
function getCurrentLocationOnMap() {
    console.log('=== 在地图上获取当前位置 ===');
    
    if (!navigator.geolocation) {
        alert('您的浏览器不支持地理位置功能');
        return;
    }
    
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            
            console.log('定位成功:', latitude, longitude);
            
            LocationService.setCurrentCoords({
                name: '当前位置',
                latitude,
                longitude,
                source: 'gps'
            });
            LocationService.setMapDraftLocation({
                name: '当前位置',
                latitude,
                longitude,
                source: 'gps'
            });
            
            // 移动地图到当前位置（Leaflet格式）
            if (mapInstance) {
                mapInstance.setView([latitude, longitude], 18);
            }
            
            // 更新地址信息
            updateAddress(longitude, latitude);
            
        },
        function(error) {
            console.error('定位失败:', error.code, error.message);
            
            let errorMsg = '';
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMsg = '您拒绝了位置权限，请在浏览器设置中允许定位权限';
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMsg = '位置信息不可用';
                    break;
                case error.TIMEOUT:
                    errorMsg = '获取位置超时，请稍后重试';
                    break;
                default:
                    errorMsg = '获取位置失败';
            }
            
            alert(errorMsg);
        },
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        }
    );
}

// 放大地图
function zoomInMap() {
    if (mapInstance) {
        const currentZoom = mapInstance.getZoom();
        if (currentZoom < 18) {
            mapInstance.setZoom(currentZoom + 1);
        }
    }
}

// 缩小地图
function zoomOutMap() {
    if (mapInstance) {
        const currentZoom = mapInstance.getZoom();
        if (currentZoom > 3) {
            mapInstance.setZoom(currentZoom - 1);
        }
    }
}

// 获取当前位置
function locateCurrentUserFromPicker() {
    console.log('=== 获取当前位置 ===');
    
    // 检查是否支持定位
    if (!navigator.geolocation) {
        alert('您的浏览器不支持地理位置功能');
        return;
    }
    
    // 检查是否是安全上下文（HTTPS或localhost）
    if (!window.isSecureContext) {
        console.warn('非安全上下文，可能无法获取位置');
        // 非安全上下文也尝试获取，但提示用户可能失败
    }
    
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const accuracy = position.coords.accuracy;
            
            console.log('定位成功:', latitude, longitude, '精度:', accuracy + 'm');
            
            // 根据精度估算位置名称
            let locationName = '当前位置';
            if (accuracy < 100) {
                locationName = '精确位置';
            } else if (accuracy < 1000) {
                locationName = '附近区域';
            }

            const located = LocationService.setCurrentCoords({
                name: locationName,
                address: locationName,
                latitude,
                longitude,
                source: 'gps'
            });
            LocationService.applyPickerSelection(located || {
                name: locationName,
                address: locationName,
                latitude,
                longitude,
                source: 'gps'
            });
            
            closeLocationPicker();
        },
        function(error) {
            console.error('定位失败:', error.code, error.message);
            
            let errorMsg = '';
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMsg = '您拒绝了位置权限，请在浏览器设置中允许定位权限';
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMsg = '位置信息不可用';
                    break;
                case error.TIMEOUT:
                    errorMsg = '获取位置超时，请稍后重试';
                    break;
                case error.UNKNOWN_ERROR:
                    errorMsg = '未知错误，无法获取位置';
                    break;
                default:
                    errorMsg = '获取位置失败，请选择其他城市';
            }
            
            alert(errorMsg);
        },
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        }
    );
}

// 模拟地点数据库（像美团一样包含各种类型的地点）
const locationDatabase = [
    // 北京
    { name: '故宫博物院', address: '北京市东城区景山前街4号', latitude: 39.9163, longitude: 116.3972, type: '景点' },
    { name: '天安门广场', address: '北京市东城区天安门广场', latitude: 39.9042, longitude: 116.4074, type: '景点' },
    { name: '八达岭长城', address: '北京市延庆区八达岭镇', latitude: 40.3607, longitude: 116.0147, type: '景点' },
    { name: '颐和园', address: '北京市海淀区新建宫门路19号', latitude: 39.9999, longitude: 116.2755, type: '景点' },
    { name: '三里屯', address: '北京市朝阳区三里屯路', latitude: 39.9371, longitude: 116.4477, type: '商圈' },
    { name: '望京SOHO', address: '北京市朝阳区望京街10号', latitude: 39.9962, longitude: 116.4707, type: '写字楼' },
    { name: '簋街', address: '北京市东城区东直门内大街', latitude: 39.9318, longitude: 116.4146, type: '美食街' },
    { name: '北京大学', address: '北京市海淀区颐和园路5号', latitude: 39.9999, longitude: 116.2755, type: '学校' },
    // 上海
    { name: '外滩', address: '上海市黄浦区中山东一路', latitude: 31.2304, longitude: 121.4737, type: '景点' },
    { name: '东方明珠', address: '上海市浦东新区世纪大道1号', latitude: 31.2397, longitude: 121.4998, type: '景点' },
    { name: '南京路步行街', address: '上海市黄浦区南京东路', latitude: 31.2397, longitude: 121.4998, type: '商圈' },
    { name: '陆家嘴', address: '上海市浦东新区陆家嘴环路', latitude: 31.2397, longitude: 121.5058, type: '商圈' },
    { name: '静安寺', address: '上海市静安区静安寺路', latitude: 31.2304, longitude: 121.4477, type: '景点' },
    { name: '徐家汇', address: '上海市徐汇区虹桥路', latitude: 31.1934, longitude: 121.4362, type: '商圈' },
    // 深圳
    { name: '深圳湾公园', address: '深圳市南山区滨海大道', latitude: 22.4936, longitude: 113.9145, type: '景点' },
    { name: '东门老街', address: '深圳市罗湖区东门步行街', latitude: 22.5431, longitude: 114.0579, type: '商圈' },
    { name: '福田CBD', address: '深圳市福田区中心三路', latitude: 22.5431, longitude: 114.0579, type: '商圈' },
    { name: '华侨城', address: '深圳市南山区深南大道', latitude: 22.5431, longitude: 113.9766, type: '景点' },
    // 广州
    { name: '广州塔', address: '广州市海珠区阅江西路222号', latitude: 23.1291, longitude: 113.3245, type: '景点' },
    { name: '北京路', address: '广州市越秀区北京路', latitude: 23.1291, longitude: 113.2644, type: '商圈' },
    { name: '天河城', address: '广州市天河区天河路208号', latitude: 23.1291, longitude: 113.3245, type: '商圈' },
    // 杭州
    { name: '西湖', address: '杭州市西湖区西湖风景区', latitude: 30.2741, longitude: 120.1552, type: '景点' },
    { name: '河坊街', address: '杭州市上城区河坊街', latitude: 30.2741, longitude: 120.1552, type: '商圈' },
    { name: '西溪湿地', address: '杭州市西湖区天目山路', latitude: 30.2741, longitude: 120.0852, type: '景点' },
    // 成都
    { name: '宽窄巷子', address: '成都市青羊区宽窄巷子', latitude: 30.6631, longitude: 104.0347, type: '景点' },
    { name: '锦里', address: '成都市武侯区武侯祠大街', latitude: 30.6447, longitude: 104.0388, type: '景点' },
    { name: '春熙路', address: '成都市锦江区春熙路', latitude: 30.6594, longitude: 104.0425, type: '商圈' },
];

// 防抖函数
let searchTimeout = null;
function debounceSearch() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        const searchInput = document.getElementById('locationSearchInput');
        const keyword = searchInput.value.trim();
        
        if (!keyword) {
            // 清空搜索结果，显示热门城市
            hideSearchResults();
            showHotCities();
            return;
        }
        
        // 执行搜索
        performSearch(keyword);
    }, 300);
}

// 执行搜索
function performSearch(keyword) {
    console.log('搜索关键词:', keyword);
    
    // 过滤匹配的地点
    const results = locationDatabase.filter(item => 
        item.name.includes(keyword) || 
        item.address.includes(keyword)
    );
    
    console.log('搜索结果:', results.length, '个');
    
    if (results.length > 0) {
        showSearchResults(results);
        hideHotCities();
    } else {
        // 没有找到结果，显示热门城市
        hideSearchResults();
        showHotCities();
    }
}

// 显示搜索结果
function showSearchResults(results) {
    const container = document.getElementById('searchResults');
    if (!container) return;
    
    let html = '';
    results.forEach(item => {
        html += `
            <div class="search-result-item" onclick="selectLocation({ name: '${escapeJsString(item.name)}', address: '${escapeJsString(item.address)}', city: '${escapeJsString(extractCityName(item.address || item.name))}', latitude: ${item.latitude}, longitude: ${item.longitude}, source: 'search' })">
                <div class="result-icon">📍</div>
                <div class="result-info">
                    <p class="result-title">${escapeHtml(item.name)}</p>
                    <p class="result-address">${escapeHtml(item.address)}</p>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
    container.classList.add('active');
}

// 隐藏搜索结果
function hideSearchResults() {
    const container = document.getElementById('searchResults');
    if (container) {
        container.classList.remove('active');
        container.innerHTML = '';
    }
}

// 显示热门城市
function showHotCities() {
    const hotCities = document.querySelector('.hot-cities');
    if (hotCities) {
        hotCities.style.display = 'flex';
    }
}

// 隐藏热门城市
function hideHotCities() {
    const hotCities = document.querySelector('.hot-cities');
    if (hotCities) {
        hotCities.style.display = 'none';
    }
}

// 保存到最近使用
function saveToRecentLocations(locationOrName, latitude, longitude) {
    const location = typeof locationOrName === 'object'
        ? LocationService.normalize(locationOrName, DEFAULT_LOCATION)
        : LocationService.normalize({
            name: locationOrName,
            address: locationOrName,
            latitude,
            longitude
        }, DEFAULT_LOCATION);
    if (!location) return;

    let recentLocations = JSON.parse(localStorage.getItem('recentLocations') || '[]');
    
    // 移除已存在的相同位置
    recentLocations = recentLocations.filter(loc => {
        const recent = LocationService.normalize(loc, DEFAULT_LOCATION);
        return !recent || (
            recent.name !== location.name &&
            (Math.abs(recent.latitude - location.latitude) > 0.0001 ||
                Math.abs(recent.longitude - location.longitude) > 0.0001)
        );
    });
    
    // 添加到开头
    recentLocations.unshift(location);
    
    // 只保留最近10个
    recentLocations = recentLocations.slice(0, 10);
    
    localStorage.setItem('recentLocations', JSON.stringify(recentLocations));
}

// 加载最近使用的位置
function loadRecentLocations() {
    const recentLocations = JSON.parse(localStorage.getItem('recentLocations') || '[]');
    const container = document.getElementById('recentLocations');
    
    if (recentLocations.length === 0) {
        container.innerHTML = `<p class="empty-text">${t('noRecentLocations')}</p>`;
        return;
    }
    
    let html = '';
    recentLocations.forEach(rawLoc => {
        const loc = LocationService.normalize(rawLoc, DEFAULT_LOCATION);
        if (!loc) return;
        const name = String(loc.name || loc.city || loc.address).replace(/\\/g, '\\\\').replace(/'/g, "\\'");
        const address = String(loc.address || loc.name).replace(/\\/g, '\\\\').replace(/'/g, "\\'");
        const city = String(loc.city || '').replace(/\\/g, '\\\\').replace(/'/g, "\\'");
        html += `
            <div class="location-tag" onclick="selectLocation({ name: '${name}', address: '${address}', city: '${city}', latitude: ${loc.latitude}, longitude: ${loc.longitude}, source: 'recent' })">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/>
                </svg>
                ${escapeHtml(loc.name || loc.city || loc.address)}
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// 打开 Discover 页面
function openDiscoverPage() {
    console.log('打开 Discover 页面');
    
    showSinglePage('discoverPage', { showBottomNav: false });
    setTopNavActive(1);
    
    // 关闭详情页（如果打开的话）
    document.getElementById('detailPage').classList.remove('active');
    detailReturnState = null;
    
    // 获取当前位置并加载附近帖子
    loadNearbyPosts();
}

// 返回首页
function backToHome() {
    showSinglePage('mainPage', { showBottomNav: true });
    setTopNavActive(0);
}

// 获取当前位置
function getCurrentLocationForNearby({ force = false } = {}) {
    return new Promise((resolve, reject) => {
        let settled = false;
        const resolveOnce = (location) => {
            if (settled) return;
            settled = true;
            resolve(location);
        };
        const selectedDiscoverLocation = LocationService.state.discoverLocation;
        if (!force && selectedDiscoverLocation && selectedDiscoverLocation.source !== 'default') {
            resolveOnce(selectedDiscoverLocation);
            return;
        }

        if (!navigator.geolocation) {
            notifyLocationFallback();
            resolveOnce(LocationService.getDiscoverOrigin());
            return;
        }

        const fallbackTimer = setTimeout(() => {
            notifyLocationFallback();
            resolveOnce(LocationService.getDiscoverOrigin());
        }, 800);
        
        navigator.geolocation.getCurrentPosition(
            function(position) {
                if (settled) return;
                clearTimeout(fallbackTimer);
                const located = LocationService.setCurrentCoords({
                    name: '当前位置',
                    address: '当前位置',
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    source: 'gps'
                });
                if (selectedDiscoverLocation?.source === 'default') {
                    LocationService.setDiscoverLocation(located, { persist: false, reload: false, refreshHome: false });
                }
                resolveOnce(LocationService.getDiscoverOrigin());
            },
            function() {
                if (settled) return;
                clearTimeout(fallbackTimer);
                notifyLocationFallback();
                resolveOnce(LocationService.getDiscoverOrigin());
            },
            { timeout: 1200, maximumAge: 60000 }
        );
    });
}

// 加载附近帖子
async function loadNearbyPosts(options = {}) {
    console.log('开始加载附近帖子');
    const container = document.getElementById('discoverPosts');
    const emptyState = document.getElementById('discoverEmpty');
    if (container) container.innerHTML = renderEmptyState(t('loadingNearby'));
    if (emptyState) emptyState.style.display = 'none';

    try {
        const origin = await getCurrentLocationForNearby({ force: options.forceLocation === true });
        console.log('当前位置:', origin);
        
        const response = await fetchWithTimeout(`/nearby-posts?latitude=${origin.latitude}&longitude=${origin.longitude}&radius=1000&post_type=user`);
        console.log('API响应状态:', response.status);
        
        if (response.ok) {
            const posts = await response.json();
            console.log('从API获取的帖子数:', posts.length);
            renderDiscoverPosts(posts);
        } else {
            console.log('API响应失败，显示空状态');
            renderDiscoverErrorState();
        }
    } catch (error) {
        console.error("加载附近帖子失败:", error);
        console.log('加载失败，显示空状态');
        renderDiscoverErrorState();
    }
}

function renderDiscoverErrorState() {
    const container = document.getElementById('discoverPosts');
    const emptyState = document.getElementById('discoverEmpty');
    if (emptyState) emptyState.style.display = 'none';
    if (!container) return;
    container.innerHTML = `
        ${renderEmptyState(t('loadingFailed'), t('loadingFailedHint'))}
        <button type="button" class="empty-action-btn" onclick="loadNearbyPosts({ forceLocation: true })">${t('retry')}</button>
    `;
}

// 渲染 Discover 帖子列表
async function renderDiscoverPosts(posts) {
    console.log('开始渲染帖子列表，帖子数:', posts ? posts.length : 0);
    const container = document.getElementById('discoverPosts');
    const emptyState = document.getElementById('discoverEmpty');
    
    console.log('容器元素:', container);
    console.log('空状态元素:', emptyState);
    
    if (!posts || posts.length === 0) {
        container.innerHTML = '';
        if (emptyState) {
            emptyState.innerHTML = renderEmptyState(t('nearbyNoPosts'), t('nearbyHint'), 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z');
            emptyState.style.display = 'flex';
        }
        console.log('显示空状态');
        return;
    }
    
    if (emptyState) emptyState.style.display = 'none';
    await renderDiscoverPostsInto(container, posts);
}

async function renderDiscoverPostsInto(container, posts) {
    if (!container) return;
    const sortedPosts = sortDiscoverPosts(posts || []);
    const displayPosts = await Promise.all(sortedPosts.map(post => localizePostSummary(post)));
    const followers = await getFollowers();

    let html = '';
    displayPosts.forEach(post => {
        const photoSrc = post.photos && post.photos.length > 0 
            ? post.photos[0] 
            : `https://picsum.photos/400/300?random=${post.id}`;
        
        const distanceText = post.distance ? `${post.distance}km` : t('locationNearby');
        let authorAvatar = '👤';
        if (post.author_avatar) {
            try {
                const avatarData = JSON.parse(post.author_avatar);
                authorAvatar = avatarData.type === 'preset' ? avatarData.emoji : avatarData.data;
            } catch (e) {
                authorAvatar = '👤';
            }
        }
        const isImageAvatar = typeof authorAvatar === 'string' && (authorAvatar.includes('http') || authorAvatar.includes('data:'));
        const author = post.author || t('anonymousUser');
        const isFollowing = followers.includes(author);
        const authorArg = author.replace(/\\/g, '\\\\').replace(/'/g, "\\'");
        
        html += `
            <div class="post-card discover-post-card">
                <div class="post-image-wrapper" onclick="openPostDetail(${post.id})">
                    <img src="${photoSrc}" alt="${post.title}" class="post-image">
                </div>
                <div class="post-info">
                    <h3 class="post-title-text" onclick="openPostDetail(${post.id})">${post.title}</h3>
                    <div class="post-author-row">
                        ${isImageAvatar ? `<img src="${authorAvatar}" alt="${author}" class="post-author-avatar">` : `<span class="post-author-emoji">${authorAvatar}</span>`}
                        <div class="post-author-info">
                            <p class="post-author">${author}</p>
                        </div>
                        <button class="follow-btn ${isFollowing ? 'following' : ''}" onclick="event.stopPropagation(); handleFollowFromHome('${authorArg}', this)">
                            ${isFollowing ? t('following') : t('follow')}
                        </button>
                    </div>
                    <p class="post-location">📍 ${post.location || t('locationNearby')} · ${distanceText}</p>
                    <div class="post-stats-row">
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zm0 14.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg> ${post.views || 0}</span>
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg> ${post.likes || 0}</span>
                        <span class="post-stat"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> ${post.comments || 0}</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

function sortDiscoverPosts(posts) {
    return [...posts].sort((a, b) => {
        const score = (post) => {
            if (typeof post.recommendation_score === 'number') {
                return post.recommendation_score;
            }
            const distance = Number(post.distance || 0);
            const likes = Number(post.likes || 0);
            const views = Math.max(Number(post.views || 0), 1);
            const comments = Number(post.comments || 0);
            const likeRate = likes / views;
            const distanceScore = 1 / (1 + distance / 10);
            const engagement = Math.log1p(likes * 2 + comments * 3);
            return likeRate * 0.45 + distanceScore * 0.35 + engagement * 0.20;
        };
        return score(b) - score(a);
    });
}

// 模拟附近帖子数据
function getMockNearbyPosts() {
    return [
        {
            id: 1,
            title: '周末一起去爬山吧',
            photos: ['https://picsum.photos/400/300?random=1'],
            location: '北京市海淀区',
            latitude: 39.9902,
            longitude: 116.3068,
            author: '户外达人',
            views: 1256,
            likes: 234,
            comments: 45,
            distance: 2.5
        },
        {
            id: 2,
            title: '发现一家超棒的咖啡馆',
            photos: ['https://picsum.photos/400/300?random=2'],
            location: '北京市朝阳区',
            latitude: 39.9391,
            longitude: 116.4753,
            author: '美食探索者',
            views: 892,
            likes: 156,
            comments: 23,
            distance: 5.2
        },
        {
            id: 3,
            title: '傍晚的湖边散步',
            photos: ['https://picsum.photos/400/300?random=3'],
            location: '北京市西城区',
            latitude: 39.9142,
            longitude: 116.3654,
            author: '生活记录者',
            views: 678,
            likes: 89,
            comments: 12,
            distance: 3.8
        },
        {
            id: 4,
            title: '城市夜景真美',
            photos: ['https://picsum.photos/400/300?random=4'],
            location: '北京市东城区',
            latitude: 39.9289,
            longitude: 116.4133,
            author: '摄影爱好者',
            views: 2134,
            likes: 456,
            comments: 78,
            distance: 4.1
        },
        {
            id: 5,
            title: '今日份下午茶',
            photos: ['https://picsum.photos/400/300?random=5'],
            location: '北京市丰台区',
            latitude: 39.8566,
            longitude: 116.2871,
            author: '甜品控',
            views: 543,
            likes: 123,
            comments: 18,
            distance: 8.3
        }
    ];
}
