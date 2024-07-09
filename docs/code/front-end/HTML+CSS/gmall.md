---
tags:
  - HTML
  - CSS
created: 2023-06-28T22:49
updated: 2024-07-09T00:06
---
# 尚品汇

## 顶部导航条

![](../assets/images/top-nav.png)

---

### 思路

首先确定版心宽度，高度由内容撑开，因此不设高度。  
所有展示内容都要在版心范围内，因此版心内嵌到各个页面区域中，此处嵌套在顶部导航条。  
导航条可初步分为两个`div`，用左右浮动布局。  

=== "Left div"
    一开始的思路是内部再分为两个`div`，再用浮动布局，此方法麻烦。最终实现是通过设置右外边距（margin）。

    !!! info "注意点"
        - 垂直居中通过行高 = 字号实现，注意只对内联元素生效。
        - **登录**和**免费注册**之间的竖线其实是边框（border）。
        - 竖线和文字等高，因此在`<a>`内设置 border 属性。
        - 盒子模型中 margin 在 border 外面，因此调整 margin 对调整 border 和文字之间的距离无效，需要用 padding。

=== "Right div"
    这个一开始的思路是正确的，用列表做导航栏。但列表是块级元素，如果使其内联的思路是改`display`属性。但是最终实现还是通过浮动。

    !!! info "注意点"
        - 由于是列表，直接对`<li>`设置左右外边距。
        - 第一个列表项和最后一个列表项的左边距和右边距不需要。
        - 最后一个列表项的左竖线同样不需要。
        - 竖线的注意点同左`div`。

### 源码

=== "HTML"
    ```html
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>锦盒(JH.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
        <link rel="shortcut icon" href="./images/favicon.ico" type="image/x-icon">
        <link rel="stylesheet" href="./css/reset.css">
        <link rel="stylesheet" href="./css/index.css">
    </head>
    <body>
        <div class="topbar">
            <div class="container clearfix">
                <div class="welcome leftfix">
                    <span class="hello">锦盒欢迎你</span>
                    <span>请</span>
                    <a href="#" class="login">登录</a>
                    <a href="#" class="register">免费注册</a>
                </div>
                <div class="topbar-nav rightfix">
                    <ul class="clearfix">
                        <li><a href="#">我的订单</a></li>
                        <li><a href="#">我的购物车</a></li>
                        <li><a href="#">我的锦盒</a></li>
                        <li><a href="#">锦盒会员</a></li>
                        <li><a href="#">企业采购</a></li>
                        <li><a href="#">关注锦盒</a></li>
                        <li><a href="#">合作招商</a></li>
                        <li><a href="#">商家后台</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
    </html>
    ```

=== "CSS"
    ```css
    /* 基础设置-版心 */
    .container {
        width: 1190px;
        /* 页面水平居中 */
        margin: 0 auto;
    }

    /* 顶部导航条 start */
    .topbar {
        height: 30px;
        background-color: #ececec;
    }

    .welcome {
        height: 30px;
        line-height: 30px;
        font-size: 0;
        color: #666;
    }

    .welcome span, .welcome a {
        font-size: 12px;
    }

    .welcome .hello {
        margin-right: 28px;
    }

    .welcome .login {
        /* 用padding是因为margin在border外面，对border不生效 */
        padding-right: 10px;
        border-right: 1px solid #666;
    }

    .welcome .register {
        padding-left: 10px;
    }

    /* 在div内垂直居中 */
    .topbar-nav ul {
        height: 30px;
        line-height: 30px;
    }

    .topbar-nav ul>li {
        /* display: inline-block; 应改用浮动（左）*/
        /* 垂直居中应找父元素ul定义 */
        float: left;
    }

    .topbar-nav ul>li>a {
        padding: 0 15px;
        border-right: 1px solid #666;
    }

    .topbar-nav ul>li:first-child a {
        padding-left: 0;
    }

    .topbar-nav ul>li:last-child a{
        border-style: none;
        padding-right: 0;
    }
    ```

## 头部

![](../assets/images/header.png)

---

### 思路

两个 div 分别左浮动和右浮动。左 div 内嵌 img，右 div 包含一个输入框和一个按钮（button），均在表单(form)元素内。

=== "Left div"
    这个比较简单。

=== "Right div"
    这里一开始没什么思路，原来是个带边框的输入框 + 带背景图片的按钮。
    !!! info "注意点"
        1. 输入框有 1px 的边框，因此从设计稿得到宽高时各要减去2px。
        2. 输入框与父元素之间的上下边距一致，添加单向外边距可以让输入框居中。
        3. 输入框和按钮之间会有间距，可以通过在父元素`<form>`添加属性`font-size: 0`实现。
            - 按钮本身有固有样式，所以如果在元素内添加文字，即使父元素设置字体大小为零，也不会生效（继承样式的优先级小于自身样式）。
        4. 垂直方向没对齐，90% 是基线（baseline）的问题,可以通过`vertical-align`解决。
        5. 按钮添加图标是通过`background-image`实现。
            - 背景图片重复，设置`background-repeat:no-repeat`
            - 背景图片居中，设置`background-position:center`

### 源码

=== "HTML"
    ```html
        <div class="header">
            <div class="container clearfix">
                <div class="logo leftfix">
                    <img src="./images/logo.png" alt="锦盒商城">
                </div>
                <div class="search rightfix">
                    <form action="#">
                        <input type="text">
                        <!-- <button>搜索</button> -->
                        <button></button>
                    </form>
                </div>
            </div>
        </div>
    ```

=== "CSS"
    ```css
    .header {
        height: 120px;
        /* background-color: papayawhip; */
    }

    .header .search form {
        margin-top: 42px;
        /* 取消元素之间的边距 */
        font-size: 0;
    }

    .header .search input {
        height: 34px;
        width: 508px;
        /* 设置边框 宽高应各自减去边框像素*2 */
        border: 1px solid #DD302D;

    }

    .header .search button {
        height: 36px;
        width: 80px;
        background-color: #DD302D;
        /* input和button没对齐，因为有文字，90%是基线造成的问题。这里采用vertical-align属性解决问题  */
        vertical-align: top;
        background-image: url('../images/serch_icon.png');
        background-repeat: no-repeat;
        background-position: center;
    }
    ```

## 主导航

![](../assets/images/main-nav.png)

---

### 思路

这个一看就是两个左浮动的 div 。其父元素加个下边框。  
左 div 垂直+水平居中分别采用`line-height:$font-size`和`text-align:center`（只对内联元素生效）。  
右 div 为`<ul>`列表，其中`<li>`也要左浮动，列表项才能从竖向排列转为横向排列。同样地使用`line-height:$font-size`垂直居中。

=== "Left div"
    这个没什么细节。

=== "right div"
    !!! info "注意点"
        - `<li>`浮动后，其父元素`<ul>`需要清除浮动，而`<ul>`本身也是处于左浮动，二者可以同时存在。

### 源码

=== "HTML"
    ```html
        <div class="main-nav">
            <div class="container clearfix">
                <div class="all-types leftfix">全部商品分类</div>
                <ul class="main-nav-list leftfix clearfix">
                    <li><a href="#">锦盒超市</a></li>
                    <li><a href="#">优惠券</a></li>
                    <li><a href="#">买啥</a></li>
                    <li><a href="#">锦盒家电</a></li>
                    <li><a href="#">锦盒生鲜</a></li>
                    <li><a href="#">plus会员</a></li>
                    <li><a href="#">进口好物</a></li>
                    <li><a href="#">品牌闪购</a></li>
                    <li><a href="#">拍卖</a></li>
                    <li><a href="#">五金店</a></li>
                </ul>
            </div>
        </div>
    ```

=== "CSS"
    ```css
    .main-nav {
        height: 48px;
        border-bottom: 1px solid #DD302D;
    }

    .main-nav .all-types {
        width: 190px;
        height: 48px;
        background-color: #DD302D;
        color: white;
        font-size: 16px;
        line-height: 48px;
        text-align: center;
    }

    .main-nav .main-nav-list {
        height: 48px;
        line-height: 48px;
    }

    .main-nav .main-nav-list li {
        font-size: 16px;
        float: left;
        margin: 0 10px;
    }
    ```

## 侧边导航

![side-nav](../assets/images/side-nav-1.png)

### 思路

左边无序列表，右边定义列表。子绝父相。  
左边鼠标悬浮在列表项上，背景占满且左侧有间距，所以要用 padding。  
右边鼠标悬浮出现，相对于`<ul>`绝对定位。`<dt>, <dl>`分别左浮。  

=== "Left div"

    !!! info "注意点"
        - 如果几个元素之间上下间距相等，那么行高可以设为：元素自身高度 ＋（上边距+下边距）➗ 2
        - 如果选中一个`<li>`时背景色铺满，同时要调整间距，应该用 padding，否则背景色会铺不满

=== "Right div"

    !!! info "注意点"
        - 出现 border 属性时，如果要调整内容与边距之间的间距，则需要用 padding 而非 margin

### 源码

=== "HTML"
    ```html
    <div class="main-content">
        <div class="container clearfix">
            <ul class="side-nav leftfix">
                <li>
                    <a href="#">手机/运营商/数码</a>
                    <div class="second-menu">
                        <dl class="clearfix">
                            <dt><a href="#">电子书刊</a></dt>
                            <dd><a href="#">电子书</a></dd>
                            <dd><a href="#">网络原创</a></dd>
                            <dd><a href="#">数字杂志</a></dd>
                            <dd><a href="#">多媒体图书</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">音像</a></dt>
                            <dd><a href="#">音乐</a></dd>
                            <dd><a href="#">影视</a></dd>
                            <dd><a href="#">教育音像</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">英文原版</a></dt>
                            <dd><a href="#">少儿</a></dd>
                            <dd><a href="#">商务投资</a></dd>
                            <dd><a href="#">英语学习考试</a></dd>
                            <dd><a href="#">文学</a></dd>
                            <dd><a href="#">传记</a></dd>
                            <dd><a href="#">励志</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">文艺</a></dt>
                            <dd><a href="#">小说</a></dd>
                            <dd><a href="#">文学</a></dd>
                            <dd><a href="#">青春文学</a></dd>
                            <dd><a href="#">传记</a></dd>
                            <dd><a href="#">艺术</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">少儿</a></dt>
                            <dd><a href="#">胎教</a></dd>
                            <dd><a href="#">0-2岁</a></dd>
                            <dd><a href="#">3-6岁</a></dd>
                            <dd><a href="#">7-10岁</a></dd>
                            <dd><a href="#">11-14岁</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">人文社科</a></dt>
                            <dd><a href="#">历史</a></dd>
                            <dd><a href="#">哲学</a></dd>
                            <dd><a href="#">国学</a></dd>
                            <dd><a href="#">政治/军事</a></dd>
                            <dd><a href="#">法律</a></dd>
                            <dd><a href="#">人文社科</a></dd>
                            <dd><a href="#">心理学</a></dd>
                            <dd><a href="#">文化</a></dd>
                            <dd><a href="#">社会科学</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">经管励志</a></dt>
                            <dd><a href="#">经济</a></dd>
                            <dd><a href="#">金融与投资</a></dd>
                            <dd><a href="#">管理</a></dd>
                            <dd><a href="#">励志与成功</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">生活</a></dt>
                            <dd><a href="#">健康与保健</a></dd>
                            <dd><a href="#">家庭与育儿</a></dd>
                            <dd><a href="#">旅游</a></dd>
                            <dd><a href="#">烹饪美食</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">科技</a></dt>
                            <dd><a href="#">工业技术</a></dd>
                            <dd><a href="#">科普读物</a></dd>
                            <dd><a href="#">建筑</a></dd>
                            <dd><a href="#">医学</a></dd>
                            <dd><a href="#">科学与自然</a></dd>
                            <dd><a href="#">计算机与互联网</a></dd>
                            <dd><a href="#">电子通信</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">教育</a></dt>
                            <dd><a href="#">中小学教辅</a></dd>
                            <dd><a href="#">教育与考试</a></dd>
                            <dd><a href="#">外语学习</a></dd>
                            <dd><a href="#">大中专教材</a></dd>
                            <dd><a href="#">科学与自然</a></dd>
                            <dd><a href="#">字典词典</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">艺术与收藏</a></dt>
                            <dd><a href="#">经济管理</a></dd>
                            <dd><a href="#">文化与艺术</a></dd>
                        </dl>
                        <dl class="clearfix">
                            <dt><a href="#">其他</a></dt>
                            <dd><a href="#">工具书</a></dd>
                            <dd><a href="#">杂志期刊</a></dd>
                            <dd><a href="#">套装书</a></dd>
                            <dd><a href="#">打折图书</a></dd>
                        </dl>
                    </div>
                </li>
    ```

=== "CSS"
    ````css
    .main-content .side-nav {
        width: 190px;
        height: 458px;
        background-color: #f4f4f4;
        position: relative;
    }

    .main-content .side-nav li {
        font-size: 14px;
        color:#333;
        /* 除了使用margin控制边距，还可以计算行高 */
        /* margin: 7px 0 7px 16px; */
        /* height: 28px; */
        line-height: 28px;
        /* 悬浮出现背景色，所以不用margin用padding */
        padding-left: 16px;
    }

    .main-content .side-nav li:hover,
    .main-content .side-nav li:hover>a {
        background-color: #DD302D;
        color: white;
    }

    /* 先定义好尺寸和位置隐藏起来 */
    .main-content .side-nav .second-menu {
        width: 680px;
        height: 458px;
        position: absolute;
        top: 0;
        left: 190px;
        padding-left: 20px;
        background-color: white;
        display: none;
    }

    /* 当鼠标悬浮在<li>上时再出现 */
    .main-content .side-nav li:hover .second-menu {
        display: block;
    }

    .second-menu dl {
        height: 36px;
        line-height: 36px;
    }

    .second-menu dl:first-of-type {
        margin-top: 10px;
    }

    /* 让定义列表横向排列 */
    .second-menu dt {
        float: left;
        width: 70px;
        height: 20px;
        margin-right: 10px;
        font-weight: bold;
    }

    .second-menu dd {
        float: left;
    }

    .second-menu dd a {
        border-left: 1px solid #666;
        /* 小细节 */
        padding: 0 10px;
    }
    ```

## 轮播图

<center>![slide show](../assets/images/slide-show.png){style="zoom:30%"}</center>

### 思路

由于当前只学了 HTML 和 CSS，因此轮播图这类需要用到 JavaScript 的功能，暂时直接用`<img>`替代。

### 源码

=== "HTML"
    ```html
        <div class="main-content">
            <div class="container clearfix">
                <div class="banner leftfix">
                    <img src="./images/banner主图.png" alt="">
                </div>
            </div>
        </div>
    ```

=== "CSS"
    ```css
    /* 不需要 */
    ```

## 右侧内容区

<center>![](../assets/images/side-other.png){style="zoom:30%"}</center>

### 思路

整体可分为上下两个部分，两边各有一定 padding。  
首先是上半部分。  
上半部分又可分为两个区域，第一个区域是标题，第二个区域是列表。  

- 标题
    - 通过设计稿的边框量出距离顶端的高，减去 1 便是容器高度。
    - 容器内分别两个左浮动和右浮动的`<span>`和`<a>`，以及容器底部的边框。

- 列表
    - `<ul>`套`<li>`。因为上下间距相同，所以行高可以设为：元素自身高度 ＋（上边距+下边距）➗ 2

其次是下半部分。
还是老套路，无序列表加浮动，复制3份。  
通过设计稿可以量出图标和文字的高度，二者相加即为父容器的高度，内含`<span>`和`<div>`。  
通过给`<div>`设置背景图像，加上更改`<background-position>`的 X 坐标和 Y 坐标 来实现精灵图的功能。

!!! info "注意点"
    坐标轴以左上角为原点，所以一般坐标值都是负值。

### 源码
=== "HTML"
    ```html
        <div class="main-content">
            <div class="container clearfix">
                <div class="side-other leftfix">
                    <div class="message">
                        <div class="title clearfix">
                            <span class="leftfix">锦盒快报</span>
                            <a class="rightfix" href="#">更多&nbsp;&gt;</a>
                        </div>
                        <ul class="msg-list">
                            <li><a href="#">[特惠] 毛衣+直筒裤，才是YYDS。</a></li>
                            <li><a href="#">[特惠] 毛衣+直筒裤，才是YYDS。</a></li>
                            <li><a href="#">[特惠] 毛衣+直筒裤，才是YYDS。</a></li>
                            <li><a href="#">[特惠] 毛衣+直筒裤，才是YYDS。</a></li>
                        </ul>
                    </div>
                    <div class="other-nav">
                        <ul class="other-nav-list clearfix">
                            <li>
                                <div class="pic"></div>
                                <span>话费</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>火车票</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>加油卡</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>白条</span>
                            </li>
                        </ul>
                        <ul class="other-nav-list clearfix">
                            <li>
                                <div class="pic"></div>
                                <span>电影票</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>酒店</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>理财</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>机票</span>
                            </li>
                        </ul>
                        <ul class="other-nav-list clearfix">
                            <li>
                                <div class="pic"></div>
                                <span>礼品卡</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>彩票</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>游戏</span>
                            </li>
                            <li>
                                <div class="pic"></div>
                                <span>众筹</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    ```

=== "CSS"

    ```css
    .side-other .other-nav {
        margin-top: 10px;
        width: 290px;
        height: 290px;
        /* background-color: cadetblue; */
        /* fix margin collapse for first child */
        overflow: hidden;
    }

    .other-nav .other-nav-list:first-child {
        margin-top: 16px;
    }

    .other-nav .other-nav-list:nth-child(2) {
        /* 踩坑：类忘记加了clearfix 如果第二个ul没有清除浮动，第3个ul外边距不会生效 */
        margin: 17px 0;
    }

    .other-nav .other-nav-list li {
        width: 48px;
        height: 70px;
        float: left;
        margin: 0 11px;
        text-align: center;
        cursor:pointer;
        /* background-color: yellowgreen; */
    }

    .other-nav .other-nav-list li:first-child {
        margin-left: 16px;
    }

    .other-nav .other-nav-list li:last-child {
        margin-right: 16px;
    }

    .other-nav .other-nav-list .pic {
        width: 48px;
        height: 48px;
        background-image: url(../images/精灵图-侧边功能.png);
        background-repeat: no-repeat;
        overflow: hidden;
    }

    /* X轴依次平移-48px，Y轴处于原点 */
    .other-nav .other-nav-list:nth-child(1) li:nth-child(1) .pic {
        background-position: calc(0 * -48px) calc(0 * -48px);
    }

    .other-nav .other-nav-list:nth-child(1) li:nth-child(2) .pic {
        background-position: calc(1 * -48px) calc(0 * -48px);
    }

    .other-nav .other-nav-list:nth-child(1) li:nth-child(3) .pic {
        background-position: calc(2 * -48px) calc(0 * -48px);
    }

    .other-nav .other-nav-list:nth-child(1) li:nth-child(4) .pic {
        background-position: calc(3 * -48px) calc(0 * -48px);
    }

    /* X轴依次平移-48px,y轴每次固定平移-48px */
    .other-nav .other-nav-list:nth-child(2) li:nth-child(1) .pic {
        background-position: calc(0 * -48px) calc(1 * -48px);
    }

    .other-nav .other-nav-list:nth-child(2) li:nth-child(2) .pic {
        background-position: calc(1 * -48px) calc(1 * -48px);
    }

    .other-nav .other-nav-list:nth-child(2) li:nth-child(3) .pic {
        background-position: calc(2 * -48px) calc(1 * -48px);
    }

    .other-nav .other-nav-list:nth-child(2) li:nth-child(4) .pic {
        background-position: calc(3 * -48px) calc(1 * -48px);
    }

    /* X轴依次平移-48px,y轴每次固定平移-96px */
    .other-nav .other-nav-list:nth-child(3) li:nth-child(1) .pic {
        background-position: calc(0 * -48px) calc(2 * -48px);
    }

    .other-nav .other-nav-list:nth-child(3) li:nth-child(2) .pic {
        background-position: calc(1 * -48px) calc(2 * -48px);
    }

    .other-nav .other-nav-list:nth-child(3) li:nth-child(3) .pic {
        background-position: calc(2 * -48px) calc(2 * -48px);
    }

    .other-nav .other-nav-list:nth-child(3) li:nth-child(4) .pic {
        background-position: calc(3 * -48px) calc(2 * -48px);
    }
    ```
