## System Design

## 看这个！！！一个突击的！！
https://www.jyt0532.com/2017/03/27/system-design/

## RAFT
非常好的动图解释
http://thesecretlivesofdata.com/raft/
## CAP
### Consistency
http://thesecretlivesofdata.com/raft/
http://www.importnew.com/20633.html
https://blog.csdn.net/tyrroo/article/details/81514700

## LRU/LFU 的原理好处缺点
https://blog.csdn.net/jake_li/article/details/50659868

## General Web Application
https://msdn.microsoft.com/en-us/library/ee658099.aspx
### Application Request Processing
SOAP: 安全 

[REST](#REST-and-RESTful): 轻量级
### Authentication

### Authorization
### Caching
- In a ready to use format when possible
- Avoid caching volatile data that changes 
- regularly Avoid caching sensitive information unless it is encrypted.

### Exception Management
- user friendly error messages to notify users
- avoid exposing sensitive data in error pages
- Design a global exception handler that displays a global error page. Avoid the use of custom exceptions when not necessary.
- Do not catch exceptions unless you must handle them; Do not use exceptions to control application logic flow??????

### Logging and Instrumentation
用处：
- early indications of an attack
- legal proceedings



### Navigation
### Page Layout
### Page Rendering

### Session Management
考虑： what，where，how long to store it
- 需要存吗
- read-only或者不许session state, to improve performance 

### Validation
防攻击

## Concept
### REST and RESTful[^n]
#### 解释
> URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作。
> 1. REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计 RESTful API（REST风格的网络接口）；
> 2. Server提供的RESTful API中，URL中只使用名词来指定资源，原则上不使用动词。“资源”是REST架构或者说整个网络处理的核心。
> 3. 用HTTP协议里的动词来实现资源的添加，修改，删除等操作。即通过HTTP动词来实现资源的状态扭转：
> * GET    用来获取资源
> * POST  用来新建资源（也可以用于更新资源)
> * PUT    用来更新资源
> * DELETE  用来删除资源。
> 4. Server和Client之间传递某资源的一个表现形式，比如用JSON，XML传输文本，或者用JPG，WebP传输图片等。当然还可以压缩HTTP传输时的数据（on-wire data compression）。
> 5. 用 HTTP Status Code传递Server的状态信息。比如最常用的 200 表示成功，500 表示Server内部错误等。

### 怎样才算RESTful
> 1、REST 是面向资源的，这个概念非常重要，而资源是通过 URI 进行暴露。URI 的设计只要负责把资源通过合理方式暴露出来就可以了。对资源的操作与它无关，操作是通过 HTTP动词来体现，所以REST 通过 URI 暴露资源时，会强调不要在 URI 中出现动词。比如：左边是错误的设计，而右边是正确的
> ```
> GET /rest/api/getDogs --> GET /rest/api/dogs 获取所有小狗狗 
> GET /rest/api/addDogs --> POST /rest/api/dogs 添加一个小狗狗 
> GET /rest/api/editDogs/:dog_id --> PUT /rest/api/dogs/:dog_id 修改一个小狗狗 
> GET /rest/api/deleteDogs/:dog_id --> DELETE /rest/api/dogs/:dog_id 删除一个小狗狗
> ```
> 2、REST很好地利用了HTTP本身就有的一些特征，如HTTP动词、HTTP状态码、HTTP报头等等
> ```
> HTTP状态码
> ```
> 200 OK 
> 400 Bad Request 
> 500 Internal Server Error
> ```
> 在 APP 与 API 的交互当中，其结果无非就三种状态：所有事情都按预期正确执行完毕 - 成功APP 发生了一些错误 – 客户端错误API 发生了一些错误 – 服务器端错误这三种状态与上面的状态码是一一对应的。
### 为什么会有REST
> http是目前在互联网上使用最多的协议，没有之一。可是http的创始人一直都觉得，在过去10几年来，所有的人都在错误的使用Http.这句话怎么说呢？
>
> 如果说你要删除一个数据，以往的做法通常是 delete/{id} 如果你要更新一个数据，可能是Post数据放Body，然后方法是 update/{id}， 或者是artichle/{id}?method=update这种做法让Roy Fielding很暴燥，他觉得这个世界不该这样的，所有的人都在误解而且在严重错误的误解Http的设计初衷，好比是发明了火药却只用它来做烟花爆竹。
>
> 那么正确的使用方式是什么呢？如果你要看Rest各种特性，你恐怕真的很难理解Rest，但是如果你看错误的使用http的人倒底儿了哪些错，什么是Rest就特别容易理解了。
>
> 七宗罪的第一条，混乱。一万个人心里有一万个Url的命名规则，Url是统一资源定位符，重点是资源。而很多人却把它当成了万金油，每一个独立的虚拟的网页都可以随意使用，各种操作都能够迭加。这是混乱的来源之一。
>
> 第二条，贪婪。有状态和无状态全部混在一起。特别是在购物车或者是登录的应用中，经常刷新就丢失带来的用户体验简直棒棒哒。每一个请求并不能单独的响应一些功能，很多的功能混杂在一起里。这是人性贪婪的本质，也是各种Hack的起源，只要能够把问题解决掉，总会有人用他认为最方便的方式去解决问题，比如说汽车门把手坏掉了直接系根绳子当把手，emmmm这样确实很棒啊。
>
> 第三条，无序。返回的结果往往是很随意，各种错误信息本来就是用Http的状态码构成的，可是很多人还是喜欢把错误信息返回在返回值中。最常见的就是Code和Message，当然对于这一点，我个人是保留疑问的，我的观点是，Http本身的错误和服务器的内部错误还是需要在不断层面分开的，不能混在一起。可是在大神眼里并非如此，这个再议。
>
> 好了我编不下去了。那么怎么解决这些问题呢？强迫症患者的福音就是先颁规则，第一个规则就是明确Url是什么，该怎么用。就是所有的Url本质来讲，都应该是一种资源。一个独立的Url地址，就是对应一个独一无二的资源。怎么样？这种感觉是不是棒棒哒？一个冰淇淋，一个老师，一间房子，在Url上对应的都是一个资源，不会有多余的Url跟他对应，也不会表示有多个Url地址~~
>
>注意，这里点的是Url地址，并不是单独的参数，他就是一个/room/{room_id}这样的东西，举个栗子,/room/3242 这就表示3242号房间。这是一个清爽的世界啊，你想想，之前的Url是什么都要，我开房，可能是/open/room/3242 我要退房可能是/exit/3242/room，我要打理房间，可能是room/3242?method=clean.
>
> 够了！这些乱七八糟的东西全够了，让世界回归清爽的本质，一间房，就是/room/3242 没有别的Url地址了。
>
> 那我想要对这个资源有操作怎么办？这就是棒棒哒大神想出来的了，http有几种Method来着？get ,put ,post,delete，还有其他隐藏的4种。在过去的混乱世界里，经常用的就是Get和Post。如果不是因为Get不支持大数据传输，我想连Post都会有人使用。（想像一下Roy Fielding在愤怒的对着电脑屏幕喊，Http的Method一共有八个，你们为毛只逮着Get一只羊的毛薅薅薅薅薅）。
>
> 而对资源最常见的操作是什么？CRUD，对不对，就是创建，读，更新，删除。再看Http的Method？是不是非常完美？其实也怪Fielding老爷子一开始命名不准确，如果刚开始就是把Get方法叫做Read，Put方法叫做Update，Post叫做Create这该多好。。。你用一个Get，大家又发现没什么限制没什么所谓，又很难理解Put和Post的差别，法无禁止即可为啊，呃，老爷子不要瞪我，我瞎说的。
>
> 总之，这四种方法够不够你浪？你有本身找出来更多的对资源的操作来啊，我还有4个Method没用过呢。如果这4个真的不够了，有什么问题，大不了我再重新更改http协议啊。
>
> 其实简单说，对于Rest理解到这里就够了。后续的东西，都是在这一条基础上空想出来的，比强迫症更强迫症，当然，无状态我是百分百支持的。以上的各种表述可能不太准确，也纯属是我的意淫和各种小道资料，并未考据，但是凭良心讲，我是早就看不惯黑暗年代里的Url命名风格了，所以当时最早接触到Rest的时候，瞬间就找到了真爱，我靠，这不就是我一直想要的答案吗？
 

[^n]: https://www.zhihu.com/question/28557115


