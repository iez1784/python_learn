### 第4章 介绍Python对象类型 (P120 - P149)
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


#### 列表解析
- 处理序列的操作和列表的方法中，Python还包括了一个更高级的操作，称作列表解析表达式(list comprehension expression), 从而提供了一种处理像矩阵这样结构的强大工具

###### 从列举的矩阵中提取出第二列，因为矩阵是按照行进行存储的，所以通过简单的索引即可获取行
```python
>>> col2 = [row[1] fro row in M]              # Collect the items in column 2
>>> col2
[2, 5, 8]

>>> M
[[1,2,3],[4,5,6],[7,8,9]]                     # The matrix is unchanged
```
- 列表解析源自集合的概念
- 它是一种通过对序列中的每一项运行一个表达式来创建一个新列表的方法，每次一个，从左至右
- 列表解析是编写在方括号中的(提醒你在创建列表这个事实)，并且由使用了同一个变量名的(这里是row)表达式和循环结构组成
- 之前的这个列表解析表达基本上就是它字面上所讲的: "把矩阵M的每个row中的row[1]，放在一个新的列表中"。其结果就是一个包含了矩阵的第二列的新列表

##### 实际应用中的列表解析可以更复杂:
```python
>>> [row[1] + 1 for row in M]                # Add 1 to each item in column 2
[3, 6, 9]

>>> [row[1] for row in M if row[1] % 2 == 0]     # Filter out odd items
[2, 8]
```
- 第一个操作: 把它搜集到的每一个元素都加了1
- 第二个使用了一个if条件语句，通过使用%求余表达式(取余数)过滤了结果中的奇数
- 列表解析创建了新的列表作为结果，但是能够在任何迭代的对象上进行迭代

##### 列表解析去步进坐标的一个硬编码表表和一个字符串:
```python
>>> diag = [M[i][i] for i in [0, 1, 2]]             # Collect a diagonal from matrix
>>> diag
[1, 5, 9]

>>> doubles = [c * 2 for c in 'spam']               # Repeat characters in a string
>>> doubles
['ss', 'pp', 'aa', 'mm']
```

##### 括号中的解析语法也可以用来创建产生所需要结果的生成器
- 例如: 内置的sum函数， 按一种顺序汇总各项
```python
>>> G = (sum(row) for row in M)
>>> next(G)
6
>>> next(G)
15
```
- 内置函数map可以做类似的事情，产生对各项运行一个函数的结果
```python
>>> list(map(sum, M))                             # Map sum over iteams in M
[6, 15, 24]
```
- 解析语法也可以用来创建集合和字典
```python
>>> {sum(row) for row in M}                      # Create a set of row sums
{24, 6, 15}

>>> {i : sum(M[i] for i in range(3)}             # Creates key/value table of row sums
{0: 6, 1: 15, 2: 24}
```

##### 实际上， Python 3.0中， 列表、 集合和字典都可以用来解析来创建:
```python
>>> [ord(x) for x in 'spaam']                  # List of character ordinals
[115, 112, 97, 97, 109]

>>> {ord(x) for x in 'spaam'}                  # Sets remove duplicates
{112, 97, 115, 109}

>>> {x: ord(x) for x in 'spaam'}               # Dictionary keys are unique
{'a': 97, 'p': 112, 's': 115, 'm': 109}

### 字典
- Python中的字典是完全不同的东西
  - 它们不是序列，而是一种映射(mapping)
  - 映射是一个其他对象的集合，但是它们是通过键而不是相对位置来存储的
  - 映射并没有任何可靠的从左至右的顺序
  - 它们简单地将键映射到值
  - 字典是Python核心对象集合中的唯一的一种映射类型，也具有可变性--可以就地改变，并可以随需求增大或减小，就像列表那样

#### 映射操作
- 作为常量编写时，字典编写在大括号中，并包含一系列的"键:值"
- 我们需要将键与一系列值相关联(例如，为了表述某物的某属性)的时候，字典是很有用的

```python
>>> D = {'food': 'Spam', 'quantity':4, 'color': 'pink'}
```
- 可以通过键对这个字典进行索引来读取或改变键所关联的值
- 字典的索引操作使用的是和序列相同的语法，但是在方括号中的元素是键，而不是相对位置

```python
>>> D['food']                   # Fetch value of key 'food'
'Spam'

>>> D['quantity'] += 1          # Add 1 to 'quantity' value
>>> D
{'food': 'Spam', 'color': 'pink', 'quantity': 5}
```

##### 不同的创建字典的方法
###### 1
- 开始一个空的字典，然后每次以一个键来填写它
- 与列表中禁止边界外的赋值不同，对一个新的字典的键赋值会创建该键
```python
>>> D ={}
>>> D['name'] = 'Bob'
>>> D['job'] = 'dev'
>>> D['age'] = 40

>>> D
{'age': 40, 'job': 'dev', 'name': 'Bob'}

>>> print(D['name'])
Bob
```
- 在这里，我们实际上使用字典的键，如描述某人的记录中的名字字段
- 在另一个应用中，字典也可以用来执行搜索
- 通过键索引一个字典往往是Python中编写搜索的最快方法

#### 重访嵌套
- 上例中，我们使用字典去描述一个假设的人物，用了三个键
- 假设信息更复杂一些，也许我们需要去记录名(first name)和姓(last name)，并有多个工作(job)的头衔
- 产生了另一个Python对象嵌套的应用

```python
>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'job': ['dev', 'mgr'],
           'age': 40.5}
```
- 这里，顶层再次使用了三个键的字典(键分别是"name"、"job"和"age")
- 一个嵌套的字典作为name的值，支持了多个部分，并用一个嵌套的列表作为job的值从而支持多个角色和未来的扩展
- 能够获取这个结构的组件，就像之前在矩阵中所做的那样，但是这次索引的是字典的键，而不是列表的偏移量
```python
>>> rec['name']                        # 'name' is a nested dictionary
{'last': 'Smith', 'first': 'Bob'}

>>> rec['name']['last']                # Index the nested dictionary
'Smith'

>>> rec['job']                         # 'job' is a nested list
['dev', 'mgr']
>>> rec['job'][-1]                     # Index the nested list
'mgr'                                           

>>> rec['job'].append('janitor')       # Expand Bob's job description in-place
>>> rec
{'age': 40.5, 'job': ['dev','mgr','janitor'], 'name': {'last': 'Smith', 'first': 'Bob'}}
```
- 注意最后一个操作是如何扩展嵌入job列表的。因为job列表是字典所包含的一部分独立的内存，它可以自由地增加或减少
- Python核心数据类型的灵活性
- 嵌套允许直接并轻松地建立复杂的信息结构
- 使用C这样的底层语言建立一个类似的结构，将会很枯燥并会使用更多的代码-我们将不得不事先安排并且声明结构和数组， 填写值，将每一个都连接起来等，在Python中，这所有的一切都是自动完成的-运行表达式创建了整个的嵌套对象结构
- Python这样的脚本语言的主要优点这一
- 同样重要的是，在底层语言中，当我们不再需要该对象时，必须小心地去释放掉所有对象空间
- 在Python中，当最后一次引用对象后(例如，将这个变量用其他的值进行赋值)，这个对象所占用的内存空间将会自动清理掉:

```python
>>> rec=0                      # Now the object's space is reclaimed
```
- 从技术上讲, Python具有一种叫做垃圾收集的特性，在程序运行时可以清理不再使用的内存，并将你从必须管理代码中这样的细节中解放出来
- 在Python中，一旦一个对象的最后一次引用被移除，空间将会立即回收

### 键的排序: for 循环
- 作为映射，字典仅支持通过键获取元素
- 在各种常见的应用场合，通过调用方法，它们也支持类型特定的操作
- 因为字典不是序列，它们并不包含任何可靠的从左至右的顺序。这意味着如晨我们建立一个字典，并将它打印出来，它的键也许会以与我们输入时不同的顺序出现

```python
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D
{'a': 1, 'c': 3, 'b': 2}
```
- 如果在一个字典的元素中，我们确实需要强调某种顺序的时候，应该怎样做呢？一个常用的解决办法就是通过字典的keys方法收集一个键的列表，使用列表的sort方法进行排序，然后使用Python的for循环逐个进行显示结果

```python
>>> Ks = list(D.keys())              # Unordered keys list
>>> Ks                               # A list in 2.6, "view" in 3.0: use list()
['a', 'c', 'b']

>>> Ks.sort()                        # Sorted keys list
>>> Ks
['a', 'b', 'c']

>>> for key in Ks:                          # Iterate though sorted keys
        print(key, '=>', D[key])            # <== press Enter twice here
a => 1
b => 2
c= > 3
```
- sorted 调用返回结果并对各种对象类型进行排序， 自动对字典的键排序：

##### 打印这个自身是无序的字典的键和值，以排好序的键和顺序输出
```python
>>> D
{'a': 1, 'c': 3, 'b':L 2}

>>> for key in sorted(D):
        print(key, '=>', D[key])

a => 1
b => 2
c => 3
```
- for循环是遍历一个序列中的所有元素并按顺序对每一元素运行一些代码的简单并有效的一种方法
- 一个用户定义的循环变量(这里是key)用作每次运行过程中当前元素的参考量
- for循环以及其作用相近的while循环，是在脚本中编写重复性任务语句的主要方法
- for循环主像列表解析一样是一个序列操作
- 它可以使用在任意一个序列对象，并且就像列表解析一样，甚至可以用在一些不是序列的对象中

##### for循环可以步进循环字符串中的字符，打印每个字符的大写
```python
>>> for c in 'spam':
        print(c.upper())
S
P
A
M
```
- Python的while循环是一种更为常见的排序循环工具，它不仅限于遍历序列
```python
>>> x = 4
>>> while x > 0:
        print('spam!' * x)
        x -= 1
spam!spam!spam!spam!
spam!spam!spam!
spam!spam!
spam!
```

### 迭代和优化
- 如果for循环看起来就像之前介绍的列表解析表达式一样，那也没错。它们都是真正的通用迭代工具
- 事实上，它们都能够工作于遵守迭代协议(这是Python中无处不在的一个概念，表示在内存中物理存储的序列，或一个在迭代操作情况下每次产生一个元素的对象)的任意对象
- 如果一个对象在响应next之前先用一个对象对iter内置函数做出响应，那么它就属于后一种情况.我们在前面所见到的生成器解析表达式就是这样的一个对象
- 从左到右地扫描一个对象的每个Python工具都使用迭代协议

##### 意味着像下面这样的任何列表解析表达式都可以计算一列数字的平方
```python
>>> squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
>>> squares
[1, 4, 9, 16, 25]
```

##### 能够编写成一个等效的for循环，通过在运行时手动增加列表来创建最终的列表
```python
>>> squares = []
>>> for x in [1, 2, 3, 4, 5]:
        squares.append(x ** 2)
>>> squares
[1, 4, 9, 16, 25]
```
- 列表解析和相关的函数编程工具，如map和filter，通常运行得比for循环快(也许快了两倍): 这是对有大数据集合的程序有重大影响的特性这一
- 在Python中性能测试是一个很难应付的任务，因为它在反复地优化
- Python中的一个主要的原则就是，首先为了简单和可读性去编写代码，在程序可以工作，并证明了确实有必要考虑性能后，再考虑该问题
- 如果确实需要提高代码的性能，Python提供了帮助你实现的工具，包括time以及timeit模块和profile模块

### 不存在的键: if 测试
- 尽管我们能够通过给新的键赋值来扩展字典，但是获取一个不存在的键值仍然是一个错误
```python
>>> D
{'a': 1, 'c': 3, 'b': 2}

>>> D['e'] = 99                                  # Assigning new keys grows dictionaries
>>> D
{'a': 1, 'c': 3, 'b': 2, 'e': 99}

>>> D['f']                                       # Referencing a nonexistent key is an error
...error text omitted...
KeyError: 'f'
```
- 获取一个并不存在的东西往往是一个程序错误
- 在一些通用程序中，我们编写程序时并不是总知道当前存在什么键
- 在这种情况下，我们如何处理并避免错误发生呢?
  - 一个技巧是首先进行测试
  - in关系表达式允许我们查询字典中一个键是否存在，并可以通过使用Python的if语句对结果进行分支处理

```python
>>> 'f' in D
False

>>> if not 'f' in D:
       print('missing')

missing
```
- 上例包含关键字if，紧跟着一个其结果为真或假的表达式，如果测试的结果是真的话将运行一些代码
- 其他的方法来创建字典并避免获取不存在的字典键: 
  - get方法(带有一个默认值的条件索引)
  - Python 2.X的has_key方法(Python 3.0中不可用)
  - try语句(一个捕获异常并从异常中恢复的工具)
  - if/else表达式

```python
>>> value = D.get('x', 0)                       # Index but with a default
>>> value
0
>>> value = D['x'] if 'x' in D else 0           # if/else expression form
>>> value
0
```

### 元组
- 元组对象(tuple，发音为"toople" 或"tuhple")，其本上就像一个不可能改变挺不错表
- 像列表一样，元组是序列，但是它具有不可变性，和字符串类似
- 从语法上讲，它们编写在圆括号中而不是方括号中
- 它们支持任意类型、任意嵌套以及常见的序列操作

```python
>>> T = (1, 2, 3, 4)                     # A 4-item tuple
>>> len(T)                               # Length
4

>>> T + (5,6)                            # Concatenation
(1,2,3,4,5,6)

>>> T[0]                                 # Indexing, slicing, and more
1
```

- 在Python 3.0中，元组还有两个专有的可调用方法，但它的专有方法不像列表所拥有的那么多
```python
>>> T.index(4)                           # Tuple methods: 4 appears at offset 3
3
>>> T.count(4)                           # 4 appears once
1
```
- 元组的真正不同之处就在于一旦创建后就不能再改变。元组是不可变的序列
```python
>>> T[0] = 2                             # Tuples are immutable
...error text omitted...
TypeError: 'tuple' object does not support item assignment
```
- 与列表和字典一样，元组支持混合的类型和嵌套，但是不能增长或缩短，它们是不可变的
```python
>>> T = ('spam', 3.0, [11, 22, 33])
>>> T[1]
3.0
>>> T[2][1]
22
>>> T.append(4)
AttributeError: 'tuple' object has no attribute 'append'
```

#### 为会要用元组
- 元组在实际中往往并不像列表这样常用，但是它的关键是不可变性
- 如果在程序中以列表的形式传递一个对象的集合，它可能在任何地方改变;如果使用元组的话，则不能
- 元组提供了一种完整性的约束，这对于我们这里所编写的更大型的程序来说是方便的


### 文件
- 文件对象是Python代码对电脑上外部文件的主要接口
- 文件是核心类型，有些特殊:
  - 没有特定的常量语法创建文件
  - 要创建一个文件对象，需调用内置的open函数以字符串的形式传递给它一个外部的文件名以及一个处理模式的字符吕

##### 创建一个文本输出文件
- 可以传递其文件名
- 以及'w'处理模式字符串以写数据
```python
>>> f = open('data.txt', 'w')          # Make a new file in output mode
>>> f.write('Hello\n')                 # Write strings of bytes to it
6
>>> f.write('world\n')                 # Returns number of bytes written in Python 3.0
6
>>> f.close()                          # Close to flush output buffers to disk
```
- 在当前文件夹下创建了一个文件，并向它写入文本
  - 文件名可以是完整的路径，如果需要读取电脑上其他位置的文件


- 为了读出刚才所写的内容，重新以'r'处理模式打开文件，读取输入
- 之后将文件的内容读至一个字符串，并显示它
- 对脚本而言，文件的内容总是字符串，无论文件包含的数据是什么类型

```PYTHON
>>> f = open('data.txt')              # 'r' is the default processing mode
>>> text = f.read()                   # Read entire file into a string
>>> text
'Hello\nworld\n'

>>> print(text)                       # print interprets control characters
Hello
world

>>> text.split()                      # File content is always a string
['Hello', 'world']
```
- 文件对象提供了多种读和写的方法(read可以接受一个字节大小的选项，readline每次读一行等)，以及其他的工具(seek移动到一个新文件位置)
- 如今读取一个文件的最佳方式就是根本不读它，文件提供了一个迭代器(iterator)， 它在for循环或其他环境中自动地一行一行地读取

##### 快速查看文件方法
- 在任何打开的文件上运行一个dir调用并且在返回的任何方法名上调用一个help
```python
>>> dir(f)
[...many names omitted...
'buffer', 'close','closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 
'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline',
'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writeable', 'write',
'writelines']

>>>help(f.seek)
...tyr it and see...
```

- Python 3.0中的文件在文本和二进制数据之间划出了一条清晰的界限
- 文本文件把内容显示为字符串，并且自动执行Unicode编码和解码
- 二进制文件把内容显示为一个物定的字节字符串类型，并且允许你不修改地访问文件内容

```python
>>> data = open('data.bin', 'rb').read()       # Open binary file
>>> data                                       # bytes string holds binary data
b'\x00\x00\x00\x07spam\x00\x08'
>>> data[4:8]
b'spam
```

### 其他文件类工具
- opoen函数能够实现在Python中编写的绝大多数文件处理
- 更高级的任务，Python还有额外的类文件工具: 
  - 管道
  - 先进先出队列(FIFO)
  - 套接字
  - 通地键访问文件
  - 对象持久
  - 基于描述符的文件
  - 关系数据库和面向对象数据库接口等
- 描述符文件(descriptor file) 支持文件锁定和其他的底层工具
- 套接字提供网络和进程间通信的接口

### 其他核心类型
- 集合是最近增加到这门语言中的类型，它不是映射也不是序列，相反，它们是唯一的不可变的对象的无序集合
- 集合可以通过调用内置set函数而创建，或者使用Python 3.0中新的集合常量和表达式创建，并且它支持一般的数学集合操作
```python
>>> X = set('spam')                 # Make a set out of a sequence in 2.6 and 3.0
>>> Y = {'h', 'a', 'm'}             # Make a set with new 3.0 set literals
>>> X,Y
({'a','p','s','m'},{'a','h','m'})

>>> X & Y                           # Intersection
{'a', 'm'}

>>> X | Y                           # Union
{'a', 'p', 's', 'h', 'm'}

>>> X - Y                           # Difference
{'p', 's'}

>>> {x ** 2 for x in [1,2,3,4]}     # Set comprehensions in 3.0
{16, 1, 4, 9}
```

- Python最近添加了一些新的数值类型
  - 十进制数(固定精度浮点数)
  - 分数(有一个分子和一个分母的有理数)
  - 它们都用来解决浮点数学的局限性和内在的不精确性

```python
>>> 1/3                           # Floating-point (use.0 in Python 2.6)
0.33333333333333331

>>> (2/3) + (1/2)         
1.1666666666666665

>>> import decimal                # Decimals: fixed precision 
>>> d = decimal.Decimal('3.141')
>>> d + 1
Decimal('4.141')

>>> decimal.getcontext().prec = 2
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.33')

>>> from fractions import Fraction             # Fractions: numerator + denominator
>>> f = Fraction(2, 3)
>>> f + 1
Fraction(5, 3)
>>> f + Fraction(1,2)
Fraction(7,6)

- Python还添加了布尔值(预定义的True和False对象实际上是定制后以逻辑结果显示的整数1和0)
- 以及长期以来一直支持特殊的占位符对象None(它通常用来初始化名字和对象)
```python
>>> 1 > 2, 1 < 2                     # Booleans
(False, True)
>>> bool('spam')
True

>>> X = None                         # None placeholder
>>> print(X)
None

>>> L = [None] * 100                 # Initialize a list of 100 Nones
>>> L
[None,None,None,None,None,None,None,None,None,None,None,None,None,None,
None,None,None,None,None,None,None,... a lisft of 100 Nones...]
```


### 如何破坏代码的灵活性
- 值得注意：内置函数type返回的类型对象是赋给该类型的另一个对象的一个对象
- 其结果在Python 3.0中略有不同，因为类型己经完全和类结合起来了
```python
# In Python 2.6:

>>> type(L)                # Types: type of L is list type object
<type 'list'>
>>> type(type(L))          # Even types are objects
<type 'type'>

# In Python 3.0: 
>>> type(L)                # 3.0: types are classes, and vice versa
<class 'list'>
>>> type(type(L))          # See Chapter 31 for more on class types
<class 'type'>
```
- 除了允许交互地探究对象，这个函数的实际应用是，允许编写代码来检查它所处理的对象的类型
- 在Python脚本中至少有3种方法可做到这点:

```python
>>> if type(L) == type([]):         # Type testing, if you must...
        print('yes')
yes
>>> if type(L) == list:             # Using the type name
        print('yes')
yes
>>> if isinstance(L, list):         # Object-oriented tests
        print('yes')
yes
```

#### 在代码中检验了特定的类型，实际上破坏了它的灵活性，即限制它只能使用一种类型工作。没有这样的检测，代码也许能够使用整个范围的类型工作
#### 这与前边我们讲到的多态的思想有些关联，它是由Python没有类型声明而发展起来的

- 在Python中，我们编写对象接口(所支持的操作)而不是类型
- 不关注于特定的类型意味着代码会自动地适应它们中的很多类型: 任何具有兼容接口的对象均能够工作，而不管它是什么对象类型
- 尽管支持类型检测(即使在一些极少数的情况下，这是必要的)， 冷饮瘵会看到它并不是一个"Python式"的思维方法
- 多态也是使用Python的关键思想

### 用户定义的类
- 用抽象的术语来说，类定义了新的对象类型，扩展了核心类型

###### 假如你希望有一个对象类型对职员进行建模。尽管Python里没有这样特定的核心类型，下边这个用户定义的类或许符合你的需求:

```python
>>> class Worker:
          def __init__(self, name, pay):              # Initialize when created
              self.name = name                        # self is the new object
              self.pay = pay
          
          def lastName(self):
              return self.name.split()[-1]            # Split string on blanks
          
          def giveRaise(self, percent):        
              self.pay *= (1.0 + percent)             # Update pay in-place
```

- 这个类定义了一个新的对象的种类，有name和pay两个属性(有时候叫做状态信息)
- 也有两个小的行为编写函数(通常叫做方法)的形式
- 就像函数那样去调用类，会生成我们新类型的实例，并且类的方法调用时，类的方法自动获取被处理的实例(其中的self参数)

```python
>>> bob = Worker('Bob Smith', 50000)                 # Make two instances
>>> sue = Worker('Sue Jones', 60000)                 # Each has name and pay attrs
>>> bob.lastName()                                   # Calle method: bob is self
'Smith'
>>> sue.lastName()                                   # sue is the self subject
'Jones'
>>> sue.giveRaise(.10)                               # Update sue's pay
66000.0
```

- 隐含的"self"对象是我们把这叫做面向对象模型的原因，即一个类中的函数总有一个隐含的对象
- 一般来说，尽管这样，基于类的类型是建立在并使用了核心类型的

### 剩余的内容
- Python脚本能够处理的所有的事情都是某种类型的对象
- 在Python中的每样东西都是一个"对象"， 只有我们目前所见到的那些对象类型才被认为是Python核心类型集合中的一部分
- 其他Python中的类型有的是与程序执行相关的对象(如函数、模块、类和编译过的代码)
- 我们现在学过的对象仅是对象而己，并不一定是面向对象。面向对象是一种往往要求有继承和Python类声明的概念


### 本章小结
- 介绍了Python核心对象类型，以及可以对它们进行的一些操作
- 学习了一些能够用于许多对象类型的一般操作 (比如：索引和分片这样的序列操作)
- 可以作为方法调用的特定类型操作 (比如：字符串分隔和列表增加)
- 在学习的过程中己经定义了一些关键的术语。比如: 不可变性、序列和多态


### 本章习题
1. 列举4个Python核心类型的名称
- 数字、字符串、列表、字典、元组、文件和集合一般被认为是核心对象(数据)类型
- 类型、None和布尔型有时也被定义在这样的分类中
- 还有多种数字类型(整数、浮点数、复数、分数和十进制数)
- 多种字符串类型(Python 2.X中的一般字符串和Unicode字符串，以及Python 3.X中的文本字符串和字节字符串)

2. 为什么我们把它们称作是"核心"数据类型
- 它们被认作是"核心"类型是因为综们是Python语言自身的一部分，并有总是有效的
- 为了建立其他的对象，通常必须调用被导入模块的函数
- 大多数核心类型都有特定的语法去生成其对象:
  - 例如 'spam'是一个创建字符串的表达式，而且决定了可以被应用的操作的集合
- 正是因为这一点，核心类型与Python的语法紧密地结合在一起。与之相比较，必须调用内置的open函数去创建一个文件对象

3. "不可变性" 代表了什么，哪三种Python的核心类型被认为是具有不可变性的
- 一个具有"不可变性"的对象是一个在其创建以后不能够被改变的对象
- Python中的数字、字符串和元组都属于这个分类
- 尽管无法就地改变一个不可变的对象，但是你总是可以通过运行一个表达式创建一个新的对象

4. "序列"是什么意思，哪三种Python的核心类型被认为是这个分类中的
- 一个"序列"是一个对位置进行排序的对象的集合
- 字符串、列表和元组是Python中所有的序列
- 它们共同拥有一般的序列操作，例如: 索引、合并以及分片，但又各自有自己的类型特定的方法调用

5. "映射" 是什么意思，哪种Python的核心类型是映射
- 术语"映射"， 表示将键与相关值相互关联映射的对象
- Python的字典是其核心类型集中唯一的映射类型
- 映射没有从左至右的位置顺序
- 它们支持通过键获取数据，并包含了类型特定的方法调用

6. 什么是"多态"， 为什么我们要关心多态
- "多态" 意味着一个操作符(如 +) 的意义取决于被操作的对象
- 这将变成使用好Python的关键思想之一
- 不要把代码限制在特定的类型上，使代码自动适用于多种类型



### 注1
- 常量(literal)是指其语法会生成对象胡表达式，有时也叫做常数(constant)
- 值得注意的是, "常数"不是指不可变的对象或变量(这个术语与在C++中的const，或Python中的"不可变"这个概念没有什么关系)

### 注2
- 当我们采用Python的对象持久化系统时(在文件或键值数据库中保存Python原生对象的简单方式)， 我们刚刚创建的rec记录，很有可能是数据库记录，可以参考Python的pickle和shelve模块的细节