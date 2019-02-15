### 第4章 介绍Python对象类型 (P120 - P150)
- 从非正式的角度来说
  - 在Python中，我们使用一些东西在做事情
  - "事情"采用的是像加法以及连接这样的操作形式，而"东西"指的变是我们操作的对象
- 从更正式的角度来讲
  - 在Python中，数据以对象的形式出现--无论是Python提供的内置对象，还是使用Python或是像C扩展库这样的扩展语言工具创建的对象
  - 对象无非是内存中的一部分，包含数值和相关操作的集合
- 对象是Python中最基本的概念
- 从更具体的视角来看
  - Python程序可以分解成模块、语句、表达式以及对象
  1. 程序由模块构成
  2. 模块包含语句
  3. 语句包含表达式
  4. 表达式建立并处理对象
______________________________________________________
### 为什么使用内置类型
- 底层语言
  - 如果使用过底层语言C或C++，应该知道很大一部分工作集中于用对象(或者叫做数据结构)去表现应用领域的组件。
  - 需要部置内存结构、管理内存分配、实现搜索和读取例程

- Python程序
  - 提供了强大的对象类型作为语言的组成部分
  - 除非有内置类型无法提供的特殊对象要处理，最好总是使用内置对象而不是使用自己的实现
    - 原因
    1. 内置对象使程序更容易编写
    2. 内置对象是扩展的组件
    3. 内置对象往往比定制的数据结构更有效率
    4. 内置对象是语言的标准的一部分
_______________________________________________________
### Python的核心数据类型
- 表4-1是Python的内置对象类型和一些统写其常量(literal)所使用到的语法，也就是能够生成这些对象的表达式

#### 表4-1: 内置对像

对象类型 | 例子 常量/创建
:------ | :------
数字 | 1234， 3.1415， 3+4j， Decimal， Fraction 
字符串 | 'spam', "guio's"， b'a\xolc' 
列表 | [1,[2,'three'],4] 
字典 | {'food':'spam', 'taste':'yum'} 
元组 | (1, 'spam', 4, 'U') 
文件 | myfile=open('eggs','r') 
集合 | set('abc')，{'a', 'b', 'c'} 
其他类型 | 类型、None、布尔型 
编程单元类型 | 函数、模块、类 
与实现相关的类型 | 编译的代码堆栈跟踪 
_______________________________________________________

- 表4-1中所列内容并不完整，因为在Python程序中处理的每样东西都是一种对象
- 其他类型的对象往往都是通过导入或使用模块来建立的，而且它们都有各自的行为
- 后面部分介绍的像函数、模块和类这样的编程单元在Python中也是对象，它们由def、class、import和lambda这样的语句和表达式创建，并且可以在脚本间自由地传递，存储在其他对象中等
- Python还提供了一组与实现相关的类型，例如编译过的代码对象，它们通常更多地关系到工具生成器而不是应用程序开发者
- 我们通常把表4-1中的对相类型称作是核心数据类型，因为它们是在Python语言内部高效创建的，也就是说，有一些特定语法可以生成它们

```python
>>> 'spam'
```
- 从技术上讲，正在运行一个常量表达式，这个表达式生成并返回一个新的字符串对象
  - 这是Python用来生成这个对象的一个特定语法
  - 类似地，一个方括号中的表达式会生成一个列表，大括号中的表达式会建立一个字典
- Python中没有类型声明，运行的表达式的语法决定了创建的使用的对象的类型
- 一旦创建了一个对象、它就和操作集合绑定了--只可以对字符串进行字符串相关的操作，对列表进行列表相关的操作
- Python是动态类型的(它自动跟踪你的类型而不是要求声明代码)，它也是强类型语言(你只能对一个对象进行适合该类型的有效的操作)
- 列表提供了其他对象的有序集合，而字典是通过键存储对象的
- 列表和字典都可以嵌套，可以随需求扩展和删减，并能够包含任意类型的对象
_______________________________________________________
#### 数字
- Python的核心对象集合包括常规的类型:
  - 整数(没有小数部分的数字)
  - 浮点数(概括地讲，就是后边有小数部分的数字)
  - 少见的类型(有虚部的复数、固定精度的十进制数、带分子和分母的有理分数以及集合等)
- Python的基本数字类型还是相当基本的。Python中的数字支持一般的数学运算
  - 加号(+)代表加法
  - 星号(*)表示乘法
  - 双星号(**)表示乘方

```python
>>> 123 + 222                 # Integer addition
345
>>> 1.5 * 4                   # Floating-point multiplication
6.0
>>> 2 ** 100                  # 2 to the power 100
1267650600228229401496703205376
```
- 注意这里的最后一个结果: 当需要的时候，Python 3.0的整数类型会自动提供额外的精度，以用于较大的数值
- Python 2.6中，一个单独的长整型会以类的方式来处理那些对于普通整型来说太大的数值

```python
>>> 3.1415 * 2                      # repr: as code
6.2830000000000004
>>> print(3.1415 * 2)               # str: user-friendly
6.283
``` 
- 两个结果不同，这是显示的问题
- 这证明有两种办法打印对象: 
  - 全精度(第一个结果)
  - 用户友好的形式(第二个结果)
- 一般来说，第一种形式看做是对象的代码形式repr
- 第二种是它的用户友好形式str

- 除了表达式外，和Python一起分发的还有一些常用的数学模块，模块只不是我们导入以供使用的一些额外工具包

```python
>>> import math
>>> math.pi
3.1415926535897931
>>> math.sqrt(85)
9.2195444572928871
```
- math模块包括更高级的数学工具，如函数，而random模块可以作为随机数字的生成器和随机选择器

```python
>>> import random
>>> random.random()
0.59268735266273953
>>> random.choice([1,2,3,4])
1
```
- Python还包括了一些较为少见的数字对象，如复数、固定精度士进制数、有理数、集合和布尔值，第三方开源扩展领域甚至包含了更多(矩阵和向量)

#### 字符串
- 像任意字符的集合一样，字符串是用来记录文本信息的
- 序列:一个包含其他对象的有序集合
- 序列中的元素包含了一个从左到右的顺序-序列中的元素根据它们的相对位置进行存储和读取
- 从严格意义上来说: 字符串是单个字符的字符串的序列，其他类型的序列还包括列表和元组

#### 序列的操作
- 作为序列，字符串支持假设其中各个元素包含位置顺序的操作

-例子： 有一个含有四个字符的字符串，我们通过内置的len函数验证其长度并通过索引操作得到其各个元素

```python
>>> S = 'Spam'
>>> len(S)               # Length
4
>>> S[0]                 # The first item in S, indexing by zero-based position
'S'
>>> S[1]                 # The second item from the left
'p'
```
- 在Python中，索引是按照从最前面的偏移量进行编码的，也就是从0开始，第一项索引为0，第二项索引为1，依次类推
- Python变量不需要提前声明
- 当给一个变量赋值的时候就创建了它，可能赋的是任何类型的对象，并且当变量出现在一个表达式中的时候，就会用其值替换它
- 在使用变量的值之前必须对其赋值
- 我们需要把一个对象赋给一个变量以便保存它供随后使用

- Python中，我们能够反向索引，从最后一个开始(正向索引是从左边开始计算，反向索引是从右边开始计算)

```python
>>> S[-1]               # The last item from the end in S
'm'
>>> S[-2]               # The second to last item from the end
'a'
```

-  般来说，负的索引号会简单地与字符串的长度相加，因此，以下两个操作是等效的(尽管第一个要更容易编写并不容易发生错误)
```python
>>> S[-1]                  # The last item in S
'm'
>>> S[len(S)-1]            # Negative indexing, the hard way
'm'
```

- 值得注意的是: 我们能够在方括号中使用任意表达式，而不仅仅是使用数字常量-只要Python需要一个值，我们可以使用一个常量、一个变量或任意表达式

- 序列也支持一种所谓分片 (slice) 的操作，这是一种一步就能够提取整个分片(slice)的方法

```python
>>> S                    # A 4-character string
'Spam'
>>> S[1:3]               # Slice of S from offsets 1 through 2 (not 3)
'pa'
```
- 认识分片的最简单的办法就是把它们看做是从一个字符串中一步就提取出一部分的方法
- 它们的一般形式为X[I:J], 表示 "取出在X中从偏移量为I，直到但不包括偏移量为J的内容"，结果就是返回一个新的对象
- 上面例子中的最后一个操作，在字符串S中从偏移1到2(也就是，3-1)的所有字符作为一个新的字符串。效果就是切片或"分离出"中间的两个字符
- 在一个分片中，左边界默认为0， 并且右边界默认为分片序列的长度。这引入了一些常用法的变体:

```python
>>> S[1:]             # Everything past the first (1:len(S))
'pam'
>>> S                 # S itself hasn't changed
'Spam'
>>> S[0:3]            # Everything but the last
'Spa'
>>> S[:3]             # Same as S[0:3]
'Spa'
>>> S[:-1]            # Everthing but the last again, but simpler (0:-1)
'Spa'
>>> S[:]              # All of S as a top-level copy (0:len(S))
'Spam'
- 注意负偏移量如何用作分片的边界
- 最后一个操作中如何有效地拷贝整个字符串

- 作为一个序列，字符串也支持使用加号进行合并(将两个字符串合成一个新的字符串)， 或者重复(通过再重复一次创建一个新的字符串)
```python
>>> S
'Spam'
>>> S + 'xyz'         # Concatenation
'Spamxyz' 
>>> S                 # S is unchanged
'Spam'
>>> S * 8             # Repetiton
'SpamSpamSpamSpamSpamSpamSpamSpam'
```

- 注意加号(+)对于不同的对象有不同的意义: 对于数字为加法，对于字符串为合并
- 一个操作的意义取决于被操作的对象
- 由于类型并不受约束，Python编写的操作通常可以自动地适用于不同类型的对象，只要它们支持一种兼容的接口(就像这里的+操作一样)

#### 不可变性
- 注意：在之前的例子中，没有通过任何操作对原始的字符串进行改变
- 每个字符串都被定义为生成新的字符串作为其结果，因为字符串在Python具有不可变性-在创建后不能就地改变
  1. 不能通过对其某一位置进行赋值而改变字符串，但是你总是可以通过建立一个新的字符串并以同一个变量名对其进行赋值
  2. 因为Python在运行过程中会清理旧的对象

```python
>>> S
'Spam'
>>> S[0] = 'z'     # Immutable objects cannot be changed
...error text omitted...
TypeError: 'str' object does not support item assignment

>>> S = 'z' + S[1:]          # But we can run expressions to make new objects
>>> S
'zpam'
```

- 在Python中的每一个对象灰可以分为不可变性或者可变性
- 在核心类型中，数字、字符串和元组是不可变的
- 列表和字典可以全完自由地改变
- 在其他方面，这种不可变性可以用来保证在程序中保持一个对象固定不变


#### 类型的特定的方法
- 我们学习过的每一个字符串操作都是一个真正的序列操作。也就是说，这些操作在Python中的其他序列中也会工作，包括列表和元组
- 字符串的find方法是一个基本的子字符串查找的操作(它将返回一个传入子字符串的偏移量，或者没有找到的情况下返回 -1)
- 字符串的replace方法将会对全局进行搜索和替换

```python
>>> S.find('pa')             # Find the offset of a substinrg
1
>>> S
'Spam'
>>> S.replace('pa', 'XYZ')   # Replace occurrences of a substring with another
'SXYZm'
>>> S
'Spam' 
```

- 这些字符串方法的命名有改变的含义，但在这里我们都不会改变原始的字符串，而是会创建一个新的字符串作为结果-因为字符串具有不可变性
- 字符串方法将是Python中文本处理的头号工具
- 其他的方法还能够实现通过分隔符将字符串拆分为子字符串(作为一种解析简单形式)， 大小写变换，测试字符串的内容(字数、字母或其他)， 去掉字符串后的空格字符

```python
>>> line = 'aaa,bbb,cccc,dd'
>>> line.split(',')               # Split on a delimiter into a list of substrings
['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
>>> S.upper()                     # Upper-and lowercase conversions
'SPAM'

>>> S.isalpha()                   # Content tests: isalpha, isdigit,etc.
True

>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line = line.rstrip()         # Remove whitespace characters on the right side
>>> line
'aaa,bbb,ccccc,dd'
```
- 字符串还支持一个叫做格式化的高级替代操作，可以以一个表达式的形式(最初的)和一个字符串方法调用(Python 2.6和Python 3.0中新引入的)形式使用

```python
>>> '%s, eggs, and %s' % ('spam', 'SPAM!')     # Formatting expression(all)
'spam, eggs, and SPAM!'

>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')  # Formatting method(2.6, 3.0)
'spam, eggs, and SPAM!'
```

- 注意: 尽管序列操作是通用的，但方法不通用(虽然某类型共享某些方法名，字符串的方法只用用于字符串)
- 一条简明的法则是: 可作用于多种类型的通用型操作都是以内置函数或表达式的形式出现的 [例如: len(X), X[0]]，但是类型特定的操作是以方法调用的形式出现的 [例如， aString.upper()]

#### 寻求帮助
- 可以调用内置的dir函数，将会返回一个列表，其中包含了对象的所有属性
- 由于方法是函数属性，它们也会在这个列表中出现
- 假设S是一个字符串

```python
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
- 一般来说，以双下划线开头并结尾的变量名是用来表示Python实现细节的命名模式
- 而这个列表中没有下划线的属性是字符串对象能够调用的方法
- dir函数简单地给出了方法的名称。要查询它们是做什么的，你可以将其传递给help函数

```python
>>> help(S.replace)
Help on built-in function replace:

replace(...)
    S.replace (old, new[, count]) -> str
    Return a  copy of S with all occurrences of substring 
    old replaced by new. If the optional argument count is 
    given, only the first count occurrences are replaced.
```

- 就像PyDoc一样(一个从对象中提取文档的工具), help是一个随Python一起分发的面向系统代码的接口
- dir和help是Python文档的首要选择

### 编写字符串的其他方法
- 反斜线转义序列表示特殊的字符

```python
>>> S = 'A\nB\tC'         #\n is end-of-line, \t is tab
>>> len(S)                # Each stands for just one character
5

>>> ord('\n')             # \n is a byte with the binary value 10 in ASCII
10

>>> S = 'A\0B\0C'         # \0, a binary zero byte, does not terminate string
>>> len(S)
5 
```
- Python允许字符串包括在单引号或双引号中(它们代表着相同的东西)
- 允许在三个引号(单引号或双引号)中包括多行字符串常量
- 当采用这种形式的时候，所有的行都合并在一起，并在每一行的末尾增加换行符

```python
>>> msg = """ aaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc"""
>>> msg
'\naaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\nccccccccccccccc'
```
- Python也支持原始(raw)字符串常量，即去掉反斜线转义机制(这样的字符串常是以字母"r"开头的)
- Python还支持Unicode字符串形式从而支持国际化
- 基本的str字符串类型也处理Unicode
- ASCII文本也是一种简单的Unicode
- 用bytes类型表示原始字节字符串
- Python 2.6中，Unicode是一种单独的类型
- str处理8位字符串和二进制数据
- Python 3.0中，文件也改变为返回和接受str，从而处理二进制数据的文本和字节

#### 模式匹配
- 字符串对象的方法能够支持基于模式的文本处理
- 文本的模式匹配是本书范围之外的一个高级工具
- re的模块，这个模块包含了类似搜索、分割和替换等调用，但是因为使用模式去定义子字符串，可以通用一些:

```python
>>> import re
>>> match = re.match('Hello[ \t]*(.*)world','Hello    Python world')
>>> match.group(1)
'Python '
```
- 这个例子的目的是搜索子字符串，这个子字符串以"Hello,"开始，后面跟着零个或几个制表符或空格，接着有任意字符将其保存至匹配的group中，最后以"world."结尾
- 如果找到了这样的子字符串，与模式中括号包含的部分匹配的子字符串的对应部分保存为组

```python
>>> match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
>>> match.grroups()
('usr', 'home', 'lumberjack')
```
- 模式匹配本身是一个相当高级的文本处理工具

### 列表
- Python的列表对象是这个语言提供的最通用的序列
- 列表是一个任意类型的对象的位置相关的有序集合，它没有固定的大小
- 不像字符串，其大小是可变的，通过对偏移量进行赋值以及其他各种列表的方法进行调用，确实能够修改列表的大小

#### 序列操作
- 列表是序列的一种，列表支持所有的我们对字符串所讨论过的序列操作
- 唯一的区别就是其结果往往是列表而不是字符串

```python
>>> L = [123, 'spam', 1.23]          # A list of three different-type objects
>>> len(L)                           # Number of items in the list
3
```
- 我们一样能够对列表进行索引、切片等操作， 就像对字符串所做的操作那样:
```python
>>> L[0]             # Indexing by position
123

>>> L[:-1]           # Slicing a list returns a new list
[123, 'spam']

>>> L + [4,5,6]      # Concatenation makes a new list too
[123, 'spam', 1.23, 4, 5, 6]

>>> L                # We're not changing the original list
[123,  'spam',  1.23]
```

#### 类型特定的操作
- Python的列表与其他语言中的数组有些类似，但是列表要强大得多
  1. 列表没有固定类型的约束，可以包含完全不同的类型的对象
  2. 列表没有因定大小，也就是说能够按照需要增加或减小列表大小

```python
>>> L.append('NI')      # Growing: add object at end of list
>>> L
[123, 'spam', 1.23, 'NI']

>>> L.pop(2)           # Shrinking: delete an item in the middle
1.23

>>> L                  # "del L[2]" deletes from a list too
[123, 'spam', 'NI']
```
- 列表的append方法扩充了列表的大小并在列表的尾部插入一项
- pop方法(或者等效的del语句) 移除给定偏移量的一项，从而让列表减小
- 其他的列表方法可以在任意位置插入(insert)元素，按照值移除(remove)元素
- 因为列表是可变的，大多数列表的方法都会就地改变列表对象，而不是创建一个新的列表:

```python
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']

- 列表sort方法，默认按照升序对列表进行排序
- reverse对列表进行翻转
- 这些方法都直接对列表进行了改变
```

#### 边界检查
- 尽管列表没有固定的大小，Python仍不允许引用不存在的元素
- 超出列表末尾之外的索引总是会导致错误，对列表末尾范围之外赋值也是如此

```python
>>> L
[123, 'spam', 'NI']

>>> L[99]
...error text omitted...
IndexError: list assignment index out of range
```
- 在Python中，并不是默默地增大列表作为响应，而是会提示错误
- 为了让一个列表增大，我们可以调用append这样的列表方法

#### 嵌套
- Python核心数据类型的一个优秀的特性就是它们支持任意的嵌套
- 能够以任意的组合对其进行嵌套，并可以多个层次进行嵌套(比如: 能够让一个列表包含一个字典，并在这个字典中包含另一个列表等)
- 这种特性的一个直接的应用就是实现矩阵，或者Python中的"多维数组"

```python
>>> M = [[1,2,3],          # A 3 x 3  matrix, as nested lists
         [4,5,6],          # Code can spam lines if bracketed
         [7,8,9]]

>>> M
[[1,2,3],[4,5,6],[7,8,9]]
```
- 包含3个其他列表的列表。其效果就是表现了一个3x3的数字矩阵
- 这样的结构可以通过多种方法获取元素

```python
>>> M[1]         # Get row2
[4,5,6]

>>> M[1][2]      # Get row 2, then get item 3 within the row
6
```
- 第一个操作读取了整个第二行
- 第二个操作读取了那行的第三个元素
- 串联起索引操作可以逐层深入地获取嵌套的对象结构




P134








### 注1
- 常量(literal)是指其语法会生成对象胡表达式，有时也叫做常数(constant)
- 值得注意的是, "常数"不是指不可变的对象或变量(这个术语与在C++中的const，或Python中的"不可变"这个概念没有什么关系)