#### 第二章 Python如何运行程序 (P70 - P80)

- 应该如何开始编码以及Python如何运行代码
- Python解释器
______________________________________
##### Python解释器简介
- 大多数时候Python作为一门编程语言来介绍的
- Python也是一个名为解释器的软件包
- 解释器是一种让其他程序运行起来的程序。当你编写了一段Python程序，Python解释器将读取程序，并按照其中的命令执行，得出结果。实际上，解释器是代码与机器的计算机硬件之间的软件逻辑层
  - 当Python包安装在机器上后，它包含了一些最小化的组件: 一个解释器和支持的库。
  - 根据使用情况的不同，Python解释器可能采取可执行程序的形式，或是作为链接到另一个程序的一系列库
  - 根据选用的Python版本的不同，解释器本身可以用C程序实现，或一些Java类实现，或者其他的形式。无论采取何种形式，编写的Python代码必须在解释器上运行。当然，为了实现这一点，首先必须要在计算机上安装Python解释器
- 平台的不同，Python的安装细节不同
  - Windows用户通过获取并运行自安装的可执行文件
  - Linux和Mac OS X用户也许己经拥有了一个可用的Python预先安装在了计算机上
  - 一些Linux用户和Mac OS X用户(和大多数UNIX用户一样)可从Python的完整源代码分发包中编译安装
  - Linux用户也可以找到RPM文件，Mac OS X用户可以找到各种特定于Mac的安装包
  - 其他平台有着对应其平台的不同的安装技术
- [Python下载地址](http://www.python.org)
________________________________________
##### 程序执行
- 编写或运行Python脚本的意义是什么呢?这取决于你是从一个程序员还是Python解释器的角度去看待这个问题

_________________________________________
##### 程序员的视角
- 最简单的形式而言: 一个Python程序仅是一个包含Python语句的文本文件
###### script0.py 简单的python文件
```python
print('hello world')
print(2 ** 100)
```
- 这个文件包含了两个Python打印语句，在输入流中简单地打印一个字符串(引号中的文字)和一个数学表达式的结果($2^100$)
- 可以用任何自己喜欢的文本编辑器编写python语句
- Python文件是以.py结尾的
- Windows DOS命令行窗口运行Python文件： C:\temp> python script0.py

##### Python的视角
- 在文本文件中输入代码，之后在解释器中运行这些代码
- 当Python运行脚本时，在代码开始进行处理之前，Python还会执行一些步骤。确切地说，第一步是编译成所谓的"字节码"，之后将其转发到所谓的"虚拟机"中

##### 字节码编译
- 当程序执行时，Python内部(对大多数用户是完全隐藏的)会先将源代码(文件中的语句)编译成所谓字节码的形式
- 编译是一个简单的翻译步骤，而且字节码是源代码底层的、与平台无关的表现形式
- Python通过把每一条源语句分解为单一步骤来将这些源语句翻译成一组字节码指令。这些字节码可以提高执行速度:比起文本文件中原始的源代码语句，字节码的运行速度要快得多
- 如果Python进程在机器上拥有写入权限，那么它将把程序的字节码保存为一个以.pyc为扩展名的文件(".pyc"就是编译过的".py"源代码)
- Python这样保存字节码是作为一种启动速度的优化。下一次运行程序时，如果你在上次保存字节码之后没有修改过源代码的话，Python将会加载.pyc文件并跳过编译这个步骤。当Python必须重编译时，它会自动检查源文件和字节码文件的时间戳:如果你又保存了源代码，下次程序运行时，字节码将自动重新创建
- 如果Python无法在机器上写入字节码，程序仍然可以工作: 字节码将会在内存中生成并在程序结束时简单地丢弃
- 由于.pyc文件能够加速启动，最好保证在大型程序中可以写入
- 字节码文件同样是分发Python程序的方法这一: 如果Python找到的都是.pyc文件，它也很乐意运行这个程序，尽管这里没有原始的.py源代码文件

##### Python虚拟机(PVM)
- 一旦程序编译成字节码(或字节码从己经存在的.pyc文件中载入)，之后的字节码发送到通常称为Python虚拟机(Python Virtual Machine，简写为PVM)上来执行。
- 它不是一个独立的程序，不需要安装
- PVM就是迭代运行字节码指令的一个大循环，一个接一个地完成操作
- PVM是Python的运行引擎，它时常表现为Python系统的一部分，并且它是实际运行脚本的组件。从技术上讲，它才是所谓"Python解释器"的最后一步
- 运行时的结构
  --> 源代码(m.py) --> 字节码(m.pyc) --> 运行时(PVM)
  Python的传统运行执行模式: 录入的源代码转换为字节码，之后字节码在Python虚拟机中运行。代码自动被编译，之后再解释

- 字节码的编译是自动完成的，而且PVM也仅仅是安装在机器上的Python系统的一部分。再一次说明，程序员只需简单地编写代码并运行包含有语句的文件

##### 性能的含义
- Python模式中的一些不同之处
  - 其中一个是，在Python的工作中通常没有"build"或"make"的步骤: 代码在写好之后立即运行
  - Ptyhon字节码不是机器的二进制代码。字节码是特定于Python的一种表现形式
- PVM循环(而不是CPU芯片)仍然需要解释字节码，并且字节码指令与CPU指令相比需要更多的工作
- Python并不需要反复地重分析和重分解每一行语句。实际的效果就是纯Python代码的运行速度介于传统的编译语言和传统的解释语言之间

##### 开发的含义
- Python执行模块的另一个情况是其开发和执行的环境实际上并没有区别，也就是说，编译和执行源代码的系统是同一个系统
- 在Python中，编译器总是在运行时出现，并且是运行程序系统的一部分
- 这使开发周期大大缩短。在程序开始执行之前不需要预编译和连接kw需要简单地输入并运行代码即可
- 这同样使Python具有更多的动态语言特性: 在运行时，Python程序去构建并执行另一个Python程序是可能的
- 这种结构是Python能够实现产品定制的原因: 因为Python代码可以动态地修改，用户可以改进系统内部的Python部分，而不需要拥有编译整个系统的代码
- 从更基础的角度来说，牢记我们在Python中真正拥有的只有运行时: 完全不需要初始的编译阶段，所有的事情都在程序运行时发生的。这甚至包括了建立函数和类的操作以及连接的模块。这些事情对于静态语言往往是发生在执行之前的，而在Python中是与程序的执行同时进行的

##### 执行模块的变体
- 前一节的内部执行流程反映了如今Python的标准实现形式，并且这实际上并不是Python语言本身所必需的。正是因为这一点，执行模块也在随时间而演变

##### Python实现的替代者
- 本书的过程中，Python语言有三种主要实现方式(CPython、Jython和IronPython)以及一些次要的实现方式, 如 Stackless Python
- CPython是标准的实现;其他的都是有特定的目标和角色的。所有的这些都用来实现Python语言，只是通过不同的形式执行程序而己

###### CPython
- 和Python的其他两种实现方式相比，原始的、标准的Python实现方式通常称作Cpython
- 这个名字根据它是由可移植的ANSI C语言代码编写而成的这个事实而来的
- 从http://www.python.org获取的、从ActivePython分发包中得到的以及从绝大多数Linux和Mac OS X机器上自动安装的Python
- 和其他的替代系统相比来说，它运行速度最快、最完整而且最健全

###### Jython
- Jython系统(最初称为JPython)是一种Python语言的替代实现方式，其目的是为了与java统程语言集成
- Jython包含了Java类，这些类编译Python源代码、形成Java字节码，并将得到的字节码映射到Java虚拟机(JVM)上
- Jython的目标是让Python代码能够脚本化Java应用程序，就好像CPython允许Python脚本化C和C++组件一样。它实现了与Java的无缝集成
- Python代码被翻译成Java字节码，在运行时看起来就像一个真正的Java程序一样
- Jython脚本可以应用于开发Web applet和servlet，建立基于Java的GUI
- Jython具有集成支持的功能，允许导入Python代码或使用Java的类
- Jython要比CPython慢而且也不够健壮，它往往看做是一个主要而向寻找Java代码前端脚本语言的Java开发者的一个有趣的工具

###### IronPython
- 设计目是让Python程序可以与Windows平台上的.NET框架及与之对应的Linux的上开源的Mono编写成的应用相集成
- IronPython允许Python程序既可以用作客户端也可以用作服务器端的组件，还可以与其他.NET的语言进行通信
- IronPython和Jython都由同一个创始人开发的
- 主要为了满足在.NET组件中集成Python的开发者
- 它是由微软公司开发的，IronPython也许能够为了性能实现完成一引起重要的优化工具

###### 执行优化工具
- CPython、Jython和IronPython都是通过同样的方式实现Python语言的，即通过把源代码编译为字节码，然后在适合的虚拟机上执行这些字节码
- 其他的系统，包括Psyco即时编译器以及Shedskin C++转换器，则试着优化了基本执行模块

###### Psyco实时编译器
- Psyco系统并不是Python的另一种实现方式，而是一个扩展字节码执行模块的组件，可以让程序运行得更快
- Psyco是一个PVM的增强工具，这个工具收集并使用信息，在程序运行时，可以将部分程序的字节码转换成底层的真正的二进制机器代码，从而实现更快的执行速度。在开发的过程中，Psyco无需代码的修改或独立的编译步骤即可完成这一转换
- 当程序运行时，Psyco收集了正在传递过程中的对象的类别信息，这些信息可以用来裁剪对象的类型，从而生成高效的机器代码
- 机器代码一旦生成后，就替代了对应的原始字节码，从而加快程序的整体执行速度
- 因为字节码的转换与程序运行同时发生，所以Pysco往往看做是一个即时编译器(JIT)
- Psyco是一个专有的JIT编译器: 它生成机器代码将数据类型精简至你程序实际上所使用的类型。例如，如果程序的一部分在不同的时候采用了不同的数据类型，Psyco可以生成不同版本的机器码用来支持每一个不同的类型组合
- Psyco己经证实能够大大提高Python代码的速度。 官方网站介绍，Psyco提供了"2倍至100倍的速度提升，典型值为4x，在没有改进的Python解释器和不修改的源代码基础上，仅仅依告动态可加载的C扩展模块"
- Psyco目前还不是标准Python的一部分，需要单独获取并安装
- Psyco的最大缺点是它实际上只能够为Inter x86构架的芯片生成机器代码，尽管包括了Windows、Linux以及最新的Mac
- [Psyco](http://psyco.sourceforge.net)

###### Shedskin C++转换器
- Shedskin是一个引擎系统，它采用了一种不同的Python程序执行方法: 尝试将Python代码变为C++代码，然后使用机器中的C++编译器将得到的C++代码编译为机器代码

##### 冻结二进制文件
- 有时候人们需要一个"真正的"Python编译器，实际上他们真正需要的是得到一种能够让Python程序生成独立的可执行二进制代码的简单方法。这是一个比执行流程概念更接近于打包分发概念的东西。通过从网络上获得的一些第三方目具，将Python程序转为可执行程序(在Python世界上称作冻结二进制文件，Frozen Binary)是有可能的
- 冻结二进制文件能够将程序的字节码、PMV(解释器)以及任何程序所需要的Python支持文件捆绑在一起形成一个单儿的文件包。过程会有一些不同，但是实际的结果将会是一个单独的可执行二进制程序(如:Windows系统中的.exe文件)，这个程序可以很容易地向客户分发。
- 将字节码和PVM混合在一起形成一个独立的组件--冻结二进制文件
- 如今，有三种系统能够生成冻结二进制文件: py2exe(Windows下使用)、PyInstaller(和py3exe类似，它能够在Linux及UNIX上使用，并且能够生成自安装的二进制文件)以及freeze(最初始的版本)
- 参考http://www.python.org以及Vaults of Parnassus网站(http://www.vex.net/parnassus/)
- 冻结二进制文件与真实的编译输出结果有所不同: 它们通过虚拟机运行字节码
- 冻结二进制文件并不小(包括PVM)
- 由于代码嵌入在冻结二进制代码之中，对于接收者来说，代码都是隐藏起来的
- 对商业软件的开发者来说，单文件封装的构架特别有吸引力

##### 其他执行选项
- 其他的方案可以用来运行Python程序
  - Stackless Python系统是标准CPython实现的一个变体，它不会在C语言调用栈上保存状态。这使得Python更容易移植到较小的栈架构中，提供了更高效的多处理选项，并且促进了像coroutine这样的新奇的编程结构
  - Cython系统(基于Pyrex项目所完成的工作)是一种混合的语言，它为Python代码结合了调用C函数以及使用变量、参数和类属性的C类型声明的能力。Cython代码可以编译成使用Python/C API的C代码，随后可以再完整地编译。尽管与标准Python并不完全兼容，Cython对于包装外部的C库以及提高Python的C扩展的编码效率都很有用

##### 未来的可能性
- 这里所描述的运行时执行模块事实上是当前Python实现的产品，并不是语言本身
- 未来也许会有新的字节码格式和实现方式的变体将被采用，例如:
  - Parrot项目的目标是提供一种对于多种编程语言通用的字节码格式、虚拟机以及优化技术(http://www.python.org)
  - 项目PyPy尝试在PVM上重新实现Python，以便使新的实现技术成为可能。其目标是产生一个快速而灵的Python实现
- 字节码的可移植性和运行的灵活性对于很多Python系统来说是很重要的特性。此为，为了实现静态编译，而增加类型约束声明将会破坏这种灵活、明了、简单以及所有代表了Python编码精神的特性。由于Python本身的高度动态性，以后的任何实现方式都可能保留许多当前的PVM产品

#### 本章小结
- 介绍了Python的执行模块(Python如何运行程序)
- 探索了这个模块的一些变体(即时编译器以及类似的工具)
- 从一开始编码时就真正理解程序是如何运行的

#### 本章习题
1. 什么是Python解释器
- Python解释器是运行Python程序的程序

2. 什么是源代码
- 源代码是为程序所写的语句: 它包括了文本文件(.py为后缀名)的文本

3. 什么是字节码
- 字节码是Python将程序编译后所得到的底层形式。Python自动将字节码保存到后缀名为.pyc的文件中

4. 什么是PVM
- PVM是Python虚拟机，它是Python的运行时引擎解释编译得到的代码

5. 请列出两个Python标准执行模块的变体的名字 
- Psyco、Shedskin以及forzen binaries是执行模块的所有变体

6. CPython、Jython以及IronPython有什么不同
- CPython是Python语言的标准实现。Jython和IronPython分别是Python程序的Java和.NET的实现；它们都是Python的编译器的替代实现

#### 注1: 
- 从严格的意义上讲，只有文件导入的情况下字节码才保存，并不是对顶层文件
- 当在交互提示模式下所录入的代码也不会保存为字节码

#### 注2: 
- Jpython和Python是完全独立的Python实现，可以为不同的运行构建编译Python源代码
- 标准CPython程序能够获取Java以及.NET软件：例如，JPython以及.NET系统的Python，允许Python调用Java以及.NET组件