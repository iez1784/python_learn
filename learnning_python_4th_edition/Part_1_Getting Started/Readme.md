#### 第三章 如何运行程序 (P81 - P117)

- 当前常用的启动技术
- 如何交互地输入程序代码
- 如何将其保存至一个文件从而以后可以在系统命令中运行、图标点击、模块导入，以及IDLE这样的GUI中的菜单选项等内容
- 模块导入的内容，理解Python程序架构的基础
- 浏览一下IDLE和其他IDE的部分，从而了解什么样的工具更适合
_____________________________________________________________________
##### 交互提示模式下编写代码
- 解释器己经作为一个可执行程序安装在系统中了，开始交互解释对话的平台无关的方法，往旆就是在操作系统的提示环境下输入python，不需要任何参数
- C:\ python
  >>>
- Windows中，可以在DOS终端窗口中输入python
- UNIX、Linux以及Mac OS X中，在shell窗口或终端窗口中(xterm或终端中运行的ksh或csh这样的shell)输入pyhton
- 其他的系统可以采用类似的方法或平台特定的工具
- 如果你没有设置系统中shell的PATH环境变量，使其包含了Python的安装目录，你也许需要将"python"改为机器上Python可执行文件的完整路径。在UNIX或Linux上，可以输入 /usr/local/bin/python(或 /usr/bin/python)；在Windows上，可以尝试输入 C:\ Python30\python (3.0版本)
- 在Windows中，除了在shell窗口中输入phton，也可以通过启动IDLE的主窗口或者通过从Python的Start按钮菜单的选项中选择"Python (command line)"来开始类似的交互会话

#### 交互地运行代码