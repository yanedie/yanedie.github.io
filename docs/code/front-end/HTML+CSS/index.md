---
categories:
  - HTML
  - CSS
tags:
  - HTML
  - CSS
date: 2023-05-10 23:29:54
created: 2023-09-19T01:30
updated: 2024-02-15T23:10
---
# HTML + CSS

## EMMET 语法

1. 生成标签直接输入标签名按`tab`键即可，比如`div`然后`tab`键，就可以生成`<div></div>`
2. 如果想要生成多个相同标签加上*就可以，比如`div*3`就可以快速生成3个div
3. 如果有父子级关系的标签，可以用`>`，比如`ul>li`
4. 如果有兄弟关系的标签，用`+`就可以，比如`div+p`
5. 如果生成带有类名或者id名字的，直接写`.demo`或者`#two` + `tab`键就可以了
6. 如果生成的div类名是有顺序的，可以用自增符号`$`: `.class$*5`
7. 如果想要在生成的标签内部写内容可以用{}表示：`div{$}*5, div{lorem}`

## 块（Block）元素和内联（Inline）元素

the heading and paragraph elements start on new lines. That is because by default, headings and paragraphs display as block elements.
Browsers treat block elements as though they are in little rectangular boxes, stacked up in the page. Each block element begins on a new line, and some space is also usually added above and below the entire element by default.

The text we marked up as emphasized `<em>`. It does not start a new line, but rather stays in the flow of the paragraph. That is because the em element is an **inline** element (also called a **text-level semantic** element or **phrasing** element). *Inline elements do not start new lines; they just go with the flow.*

## Empty Elements

Attributes are instructions that clarify or modify an element.

The syntax for an attribute is as follows:
    attributename="value"

Attributes go after the element name, separated by a space.
    <element attributename="value">

In non-empty elements, attributes go in the opening tag only.
    <element attributename="value">Content</element>

You can also put more than one attribute in an element in any order. Just keep them separated with spaces.
    <element attribute1="value" attribute2="value">
    E.g. <img src="" alt=""> <!--Attributes' order is not important.-->s

## 标记文本

### 段落

`<p></p>`

### 标题

```html
<h1></h1>
...
<h6></h6>
```

### 主题中断

`<hr>`

### 列表

#### 有序列表

```html
<ol>
    <li>...</li>
</ol>
```

#### 无序列表

```html
<ul>
    <li>...</li>
</ul>
```

> 列表编号不从1开始，可以用`start`属性来指定起始编号。
> `<ol start="17">`

#### 定义列表

```html
<dl>
    <dt>...</dt> <!--term 表项-->
    <dd>...</dd> <!--description 定义-->
    <dd>...</dd> <!--一个表项允许有多个定义-->
</dl>
```

## 更多内容元素

### 长引用

`<blockquote>...</blockquote>`<br />
Also see: a inline element - `<q>`

### 预格式化文本

对于空白元素在语义上很重要的内容，请使用预格式化文本`<pre>`元素。它是唯一的显示与拼写完全一致的元素，所有的回车和多个字符空格都保留。
`white-space: pre` CSS属性也可用于保留源文档中的空格和回车。

### Figure

**figure** 元素用于给文本添加图像或者阐明文本中的某些内容。一个 figure 可能包含一个图像、一段视频、一段代码 (a code snippet) 、文本或者一个表格——pretty much anything that can go in the flow of web content. Content in a figure element should be treated and referenced as a **self-contained unit**. That means if a figure is removed from its original placement in the main flow (to a sidebar or appendix, for example), both the figure and the main flow should continue to make sense.

```html
<figure>
    <pre>
        <code>
        ...
        </code>
    </pre>
    <figcaption>Sample CSS rule</figcaption><!--位于内容上方和下方都可以-->
</figure>
```

## 组织网页内容

- 主内容（main）
  main 元素的内容应该是该页的唯一内容。W3C HTML5 规范规定，页面应该只有一个 main 区段，并且不应该嵌套在其它区段中。
- 页眉（header）
- 页脚（footer）
- 区段/章节（section）
- 文章（article）
- 导航（nav）
- 无光或互补内容（aside）

### 内联元素综述

#### 文本级别元素

强调文本

使用em元素来强调**句子的一部分**。em 元素的位置会影响句子的意思。 强调文本总是默认显示为斜体。屏幕阅读器会用不同的声调来表示强调文本，所以使用 em 元素只是为了表达意义，并不是要使文本成为斜体。

```html
<p><em>Arlo</em> is very smart. </p>
<p>Arlo is <em>very</em> smart. </p>
```

第一句强凋的是谁很聪明，第二句强调的是多么聪明。

重要文本

strong 表示**一个词或短语**是重要的、严重的或紧急的。strong 元素不会改变句子的意思，它只会引起对重要部分的注意。浏览器通常默认把 strong 文本显示为粗体。屏幕阅读器可以用不同的声调来读重要内容，所以把文本标记为strong 是为了意义上的明确，并不是为了把它变为粗体。

语义元素：

<table><thead><tr><th>元素</th><th>描述</th></tr></thead><tbody><tr><td>a</td><td>超链接</td></tr><tr><td>abbr</td><td>缩写</td></tr><tr><td>b</td><td>引起视觉注意，如关键字（粗体）</td></tr><tr><td>bdi</td><td>指示可能有方向性需求的文本</td></tr><tr><td>bdo</td><td>双向重写；显式指示文本方向（由左到右1t工，从右到左rt1</td></tr><tr><td>br</td><td>换行</td></tr><tr><td>cite</td><td>引用，可以引用某个标题，如书的标题</td></tr><tr><td>code</td><td>计算机代码示例</td></tr><tr><td>data</td><td>机器可读的日期、时间、权重和其他测量值</td></tr><tr><td>del</td><td>删除文本，表明是对文档的编辑</td></tr><tr><td>dfn</td><td>术语的定义实例或者第一次出现</td></tr><tr><td>em</td><td>强调文本</td></tr><tr><td>i</td><td>替代语音（斜体）或替代语言</td></tr><tr><td>ins</td><td>插入文本；表明是对文档的插入</td></tr><tr><td>kbd</td><td>键盘，由用户输入的文本（技术文档使用）</td></tr><tr><td>mark</td><td>前后相关的文本</td></tr><tr><td>q</td><td>短的内联引用</td></tr><tr><td>ruby, rt, rp</td><td>使用东亚文本和文字提供解释或发音帮助</td></tr><tr><td>s</td><td>不正确的文本（加删除线）</td></tr><tr><td>samp</td><td>程序的示例输出</td></tr><tr><td>small</td><td>小字显示，如法律或者版权提示（用小一点尺寸的学体</td></tr><tr><td>span</td><td>泛型分段内容</td></tr><tr><td>strong</td><td>非常重要的内容</td></tr><tr><td>sub</td><td>下标</td></tr><tr><td>sup</td><td>上标</td></tr><tr><td>time</td><td>机器可读的时间数据</td></tr><tr><td>u</td><td>表示要加下划线的正式名称、拼错的单词或文本</td></tr><tr><td>var</td><td>变量或程序参数（技术文档使用）</td></tr><tr><td>wbr</td><td>单词换行</td></tr></tbody></table>

表示性元素：

```html
<b> -> font-weight: bold
<i> -> font-style: italic
<s>  -> text-decoration: line-through
<u> -> text-decoration: underline
<small> -> font-size:80%
```

短引用 `<q>`

根据 HTML 规范，浏览器应该在 q 元素两侧自动添加引号。

缩写和首字母简写

用 abbr 元素标记首字母简写和缩写。缩写是以句点结束的单词（Connection -> Conn.）。首字母简写是由短语中单词的首字母组成的缩写形式（NASA或者USA）。title 属性可以用于缩写：

```html
<abbr title="Points">pts.</abbr>
<abbr title="American Type Founders">ATF</abbr>
```

引用`<cite>`

表示对其它文档的引用，如书、杂、文章标题等。引用默认以斜体显示。

```html
<p>Passages of this article were inspired by <cite>The Complete Manual
of Typography</cite> by James Felici.</p>
```

定义术语 `<dfn>`

在出版界，单词或术语的第一次出现和定义实例，经常会以特殊的风格标示。在 HTML 中，可以用 dfn 元素标识它们。使用样式表在视觉上格式化它们。

程序代码元素 `<code>,<var>，<samp>`

代码、示例和键盘元素通常默认显示为等宽字体。变量通常显示为斜体。

下标和上标`<sub>, <sup>`

突出显示的文本 `<mark>`
新的 mark 元素表示一个字可能被认为与读者特别有关。有人可能会使用它在结果页面中动态突出搜索项，或者引起对文本的注意，或者表明当前页面都属于一个系列。一些设计师（和浏览器）会给标记文本浅色背景，就像是用荧光笔标记的。

日期和时间 `<time>`

time 元素显示日期、时间或日期 - 时间的组合，能够以机器可读的方式对日期和时间进行编码。用户代理能够把生日提醒或排定的事件添加到用户日程表中，搜索引擎也能够生成更智能的搜索结果，用于查找近期公布的文章。或者，它可能用来重新设计时间信息的格式（18:00 -> 6 p.m.）

datetime 属性以标准时间格式来指定日期或时间的信息。完整的时间格式以日期开始（年 - 月 - 日）。时间部分以字母 T 开头，并列出小时（24小时制）、分钟、秒（可选）以及毫秒（可选）。最后，对于时区，由符号 - 或 + 后的数字来表示落后或领先格林尼治标准时间（GMT）多少小时。例如，“-05:00”表示，这是东部标准时区，比 GMT 落后 5 小时。当只识别日期和时间时，可以省略其他部分。比如，<code>2016-12-25T15:00-8:00</code> 显示为 3pm PST on December 25, 2016

下面是几个 datetime 有效值的例子：

• Time only: 9:30 p.m.

    `<time datetime="21:30">9:30p.m.</time>`

• Date only: June 19, 2016

    `<time datetime="2016-06-19">June 19, 2016</time>`

• Date and time: Sept. 5, 1970, 1:11a.m.

    `<time datetime="1970-09-05T01:11:00">Sept. 5, 1970, 1:11a.m.</time>`

• Date and time, with time zone information: 8:00am on July 19, 2015, in
Providence, RI

    `<time datetime="2015-07-19T08:00:00-05:00">July 19, 2015, 8am, Providence RI</time>`

> 你也可以使用不带 datetime 属性的 time 元素.但其内容必须是有效的日期，时间字符串：`<time>2O16-O6-19</time>`

机器可读的信息 `<data>`

`<data>` 标签用于添加给定内容的机器可读翻译。它可以用于各种类型的数据,包括日期、计量、权重、微数据等。

该元素既为数据处理器提供了机器可读的值，又为浏览器中的渲染提供了人类可读的值。

提示：如果内容与时间或日期相关，请改用 `<time>` 元素。

下示显示产品名称，同时将每个名称与产品编号相关联：

```html
<ul>
  <li><data value="21053">圣女果</data></li>
  <li><data value="21054">牛肉番茄</data></li>
  <li><data value="21055">零食番茄</data></li>
</ul>
```

插入和删除文本

ins 和 del 元素用来标记一个文档的编辑部分，即那些插入或者删除的部分。大多数浏览器会改写为删除文本和下划线文本。一些老式的浏览器会把删除文本和下划线文本显示为普通文本。

#### 添加空行

换行符 `<br>`

单词换行 `<wbr>`

Word Break Opportunity (`<wbr>`) 规定在文本中的何处适合添加换行符。如果单词太长，或者您担心浏览器会在错误的位置换行，那么您可以使用 <wbr> 元素。注意，当单词分为两行时，浏览器不会添加连字符。

### 泛型（generic）元素 div 和 span

`<div>` 是块级元素，表示内容的分隔，而`<span>` 是内联元素，表示当前没有文本级别元素适用的词和短语。可以用 id 或 class 属性为泛型元素命名。

#### 使用 div 分区

使用 div 元素来创建页面元素或者内容的逻辑分组。它表明它们同属干一个概念单元或应被 CSS 或JavaScript 视为一个单元。通过把相关内容标记为一个 div， 并赋予它一个唯一的 id 标识，或者指明它是 class 的一部分，就可以对元素进行分组。

FAQ

What is the difference between `<section>` and `<div>`?

`<section>` means that the content inside is grouped (i.e. relates to a single theme), and should appear as an entry in an outline of the page.

`<div>`, on the other hand, does not convey any meaning, aside from any found in its class, lang and title attributes.

So no: using a `<div>` does not define a section in HTML.

#### 使用 span 定义短语

span 与 div 元素有一样的优点，只不过它用于不引入换行的短语元素。因为 span 是内联元素，所以可能只包含文本和其它内联元素（换句话说,，不能将标题、列表、内容分组元素等放入 span）

虽然没 telephone 元素，但是能够用 span 来赋予其电话号码的意义。本例中，每个电话号码都标记为 span ，并归类为 tel ：

```html
<ul>
<li>John: <span class="tel">999.8282</span></li>
<li>Paul: <span class="tel">888.4889</span></li>
<li>George: <span class="tel">888.1628</span></li>
<li>Ringo: <span class="tel">999.3220</span></li>
</ul>
```

你可以看到，加了标签的 span 给其中的文本添加了意义，否则，这些文本只是由数字组成的随机字符串。而且 spa n元素允许我们在整个站点对电话号码应用相同的样式（比如，可以使用CSS white-space：nowrap 声明来确保不出现换行）。这样信息不仅能为人所识别，而且、（理论上）也能为计算机程序所识别，程序知道如何处理“tel”类的信息。事实上，一些值（包括“tel”）已经在
名为微格式的标记系统中标准化了，这也使得网页内容对软件更有用。

#### id 和 class 属性

在 HTML5 中，id 和 class 属性的值必须包含一个字符（也就是说，它们不能为空），也可能不包含任何空白字符。你可以在值中使用几乎任何字符。早期版本的 HTML 对 id 值有限制（例如，它们需要以字母开头），但是这些限制在 HTML5 中被删除了。

id 属性用于给文档中的元素指派一个唯一的标识符。换句活说，id 的值在文档中必须只能使用一次。

class 属性用于组合相似的元素，因此，不同干 id 属性，多个元素可以共用一个 class 名，通过让多个元素使用同一个类，你可以借助单一样式规则一次性将样式应用到所有定义了标签的元素中，或者可以使用一个脚本来控制全部元素。

```html
<div id="ISBN0321127307" class="listing book">
    <img src="felici-cover.gif" alt="CMT cover">
    <p><cite>The Complete Manual of Typography</cite>, James Felici</p>
    <p class="description">A combination of type history and examples of good and bad type.</p>
</div>

<div id="ISBN0881792063" class="listing book">
    <img src="bringhurst-cover.gif" alt="ETS cover">
    <p><cite>The Elements of Typographic Style</cite>, Robert Bringhurst
    </p>
    <p class="description">This lovely, well-written book is concerned foremost with creating beautiful typography.</p>
</div>
```

注意，一个元素也可以同时属于多个类。当有多个 class 值时，可以用空格将它们分隔开。

#### 识别和分类所有元素

id 和 class 属性不局限于 div 和 span，它们是 HTML 中的两个全局属性。这意味着你可以将它们与所有 HTML 元素一起使用。

### 使用 ARIA 提高可访问性

像 div 和 span 这样的泛型元素则缺乏辅助设备所必需的语义。在富 Web 应用程序中，特别是那此严重依赖 JavaScript 和 AJAX 的应用程序中，标记本身并不能提供足够的线索来说明元素是如何使用的，以及当前的表单控件是否被选中，是否必需或者是处于其他状态。
而 ARIA （Accessible Rich Internet Application，可访问的富 Internet 应用程序），这是一组角色和属性，定义了使 Web 内容和 Web 应用程序（尤其是那些使用 JavaScript 开发的）更容易被残疾人访问的方法。该规范由 Web 可访问性倡议（WAI）的一个工作组创建并维护，这就是你也听到它被称为 WAI - ARIA 的原因。ARIA 定义了角色、状态和属性，开发人员可以将它们添加到标记和脚本中，以提供更丰富的语义信息。

### 字符转义（CHARACTER ESCAPES）

当浏览器解析 HTML 文档时，一且遇到 < 符号，它便会将其解释为标签的开头。但是，如果文本中只需要一个小于号呢？可能被误解为代码的字符需要在源文档中转义。转义并不意味着输入字符本身，而是用数字或已命名的字符实体引用（character entity reference）来表示它。如果浏览器看到这些字符引用，那么在网页显示时，会将这些地方替换为正确的字符。

有两种方法可用于引用（转义）特殊字符：

使用预定义的字符名简写（称为命名实体）。

> HTML将数百个命名实体定义为标记语言的一部分，也就是说，你不能创建白己的实体。

使用指派的数值，该值对应于其在编码字符集（数值实体）中的位置。数值可以是**十进制**或**十六进制**格式。

所有的字符引用都以 & 开头，以 ; 结尾。

#### 何时使用转义字符 When to Escape Characters

##### HTML 语法字符

在 HTML 中 <、>、&、"和 ' 字符具有特殊的语法意义，可能会被误解为代码。

因此，W3C 建议在内容中转义<、>和 & 字符。如果属性值包含单引号或双引号，则建议转义值中的引号字符。引号在内容中没有问题，不需要转义。

| 字符 |  描述  |  实体名  | 十进制数 | 十六进制数 |
|:----:|:----:|:--------:|:--------:|:----------:|
|  <   | 小于号 |  `&lt;`  | `&#060;` |  `&#x3C;`  |
|  >   | 大于号 |  `&gt;`  | `&#062;` |  `&#x3E;`  |
|  "   |  引号  | `&quot;` | `&#034;` |  `&#x22;`  |
|  '   |  撇号  | `&apos;` | `&#039;` |  `&#x27;`  |
|  &   |  与号  | `&amp;`  | `&#038;` |  `&#x26;`  |

##### 不可见或模糊字符

有些字符没有图形显示，在标记中很难看到。其中包括：

1. 不中断空格（&nbsp；），用于确保行不会在两个单词之间中断。

   例如，如果我把自己的名字标记成这样：

   `Jennifer&nbsp;Robbins`

   我可以肯定我的姓和名将始终保持在一行上。

   不中断空格的另一个用途是将一长串数字分开，比如32 000 000。

2. 零宽度的空格

   可以放在不使用单词间空格来表示应该在哪里换行的语言中。

3. 零宽度非连接符

   防止相邻字符进行连接以形成连字或其他连接形式。

4. 零宽度连接符

   非打印空格，它使相邻学符以连接的形式显示（在阿拉佰语和印度语中很常见）。

<table><thead><tr><th>字符</th><th>描述</th><th>实体名</th><th>十进制数</th><th>十六进制数</th></tr></thead><tbody><tr><td>(non-printing)</td><td>不中断空格</td><td>&amp;nbsp;</td><td>&amp;#160;</td><td>&amp;#xA0;</td></tr><tr><td>(non-printing)</td><td>En空格</td><td>&amp;ensp;</td><td>&amp;#8194;</td><td>&amp;#x2002;</td></tr><tr><td>(non-printing)</td><td>Em空格</td><td>&amp;emsp;</td><td>8#8195;</td><td>&amp;#x2003;</td></tr><tr><td>(non-printing)</td><td>零宽度空格</td><td>(none)</td><td>&amp;#8203;</td><td>&amp;#x200B;</td></tr><tr><td>(non-printing)</td><td>零宽度非连接符</td><td>&amp;zwnj;</td><td>8#8204;</td><td>&amp;#x200C;</td></tr><tr><td>(non-printing)</td><td>零宽度连接符</td><td>&amp;zwj;</td><td>B#8205;</td><td>&amp;#x200D;</td></tr></tbody></table>

## 浮动

### 为什么需要浮动？

实现标准流无法实现的排列方式，比如多个块级元素一行内排列显示以及分别靠左和靠右对齐。如用行内块元素，之间会有大的空白缝隙，很难控制。

### 浮动的排列特性 

1. 脱离标准流，不再保留原先的位置

2. 浮动元素会在一行内显示并且元素顶部对齐

3. 浮动元素具有行内块的特性。


### 常见布局方式

先用标准流的父元素排列上下位置，之后内部元素采取浮动排列左右位置，符合网页布局第一准备。

PC端：

- 标准流（最基本的布局方式）

  1. 块级元素独占一行，从上往下顺序排列。

  2. 行内元素从左到右排列，碰到父元素边缘则自动换行。行内元素给宽高是无效的。  
- 浮动

  1. 浮动元素具有行内块特性。

  2. 如果行内元素有了浮动，可以直接给高度和宽度。

  3. 如果块级元素没有设置宽度，默认和父元素一样宽，但是添加浮动以后，宽度由内容撑开。
- 定位

注意点：

一个元素浮动了，理论上其余兄弟元素也要浮动。

浮动盒子不会影响前面的标准流，只会影响后面的标准流，

### 清除浮动

很多情况下，浮动的父盒子不方便给高度，高度由子盒子撑开，但是子盒子浮动以后不占用位置，父元素的高度会变成零，就会影响下面的标准流盒子，这个时候需要清除浮动。 

- 清除浮动本质是清除浮动元素造成的影响
- 清除浮动策略是**闭合浮动**，只让浮动在父盒子内部影响，不影响父盒子外面的其他盒子。

- 如果父盒子本身有高度，则不需要清除浮动

- 清除浮动以后，父盒子就会根据浮动的子盒子自动检测高度。父级有了高度，就不会影响下面的标准流了。

实际工作中，几乎只用`clear：both`

方法：

1. 额外标签法（隔墙法）

   在浮动元素末尾添加一个空的标签，如`<div style="clear:both"></div>`，或者其它标签，如`<br />`等。

   ```html
   <style>
   	.clear {
   		clear: both;
   	}
   </style>
   </head>
   <body>
   	<div class=box>
   		<div>浮动元素1</div>
   		<div>浮动元素2<div>
   		<div class=clear></div>
       </div>
   </body>
   ```

   优点：通俗易懂，书写方便

   缺点：添加许多无意义的标签，结构化较差

   注意：要求这个新添加的标签必须是块级元素，不能是行内元素。

2. 父级添加`overflow`

   最常见的是`overflow: hidden`

   优点：代码简洁

   缺点：无法显示溢出的部分

3. 父级添加`:after`伪元素

   ```html
   <style>
       .clearfix: after {
           content: "";
           display:"block";
           height: 0;
           clear：both;
           visibility: hidden;
       }
   
       .clearfix { /* IE6、7专有 */
           *zoom: 1;
       }
   </style>
   ```

   优点：没有增加标签，结构更简单

   缺点：照顾低版本浏览器

   代表网站：百度、淘宝、网易等

4. 父级添加双伪元素

    ```html
   <style>
       .clearfix:before,
       .clearfix:after {
           content :"";
           display:table;
       }
       
       .clearfix:after {
           clear: both;
       }
       
       .clearfix {
           *zoom:1；
       }
   </style>
   ```

   优点：代码更简洁

   缺点：照顾低版本浏览器

   代表网站：小米、腾讯等

## 定位

### 为什么需要定位？

定位可以让盒子自由地在某个盒子内移动位置或者固定屏幕中某个位置，并且可以盖住其它盒子。

### 分类

定位=定位模式+边偏移

定位模式：

`position: value` {

- `static` 静态定位（了解）
- `relative` 相对定位（重要）
  1. 移动位置的时候参照点是**自身原来的位置**
  2. 不脱离文档流，文档流的位置继续占有
  3. 最佳实践：给绝对定位当父元素（子绝父相）

- `absolute` 绝对定位（重要）
  1. 移动位置的时候是相对于它的**祖先元素**来说的

- `fixed` 固定定位

}

边偏移：

- `top`
- `bottom`
- `left`
- `right`

### 子绝父相布局



### 轮播图布局

