# Welcome to Shortcut！
Shortcut is a high-configurable to which integrates most commcon operations to 
improve work efficiency.

##Pre-install
1. [Python3.4](https://www.python.org/downloads/)
2. [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
3. [cx_Freeze](https://pypi.python.org/packages/3.4/c/cx_Freeze/cx_Freeze-4.3.4.win32-py3.4.exe#md5=bd087416c69ced533768a22e5d3414b8)

##User Guide
###Build exe
Go to the root of project and run cmd `python setup.py build`. Or run build.bat directly. Both of them will automatically generate build directory in the root.

###Run
* Run `run.bat` or cmd `python shorcut.py` to check the result of changing code immediately.
* Run `ProjectRoot/build/exe.win32-3.4/Shorcut.exe` in the normal use.

###Config
We could config the common behavior easily in the config file named `config.ini`.

* The `<section:path>` represents the path wrote in the config file.
* [Button] section is required to Shortcut because it will tell Shortcut how to generate 
buttons and what behavior they will get.
* Each option in the [Button] should start with `open`, `edit` or `cmd` (will be more in the future). `Open` means the button will open an application, directory and so on. `Edit` means the button will edit a file. The `edit` keyword always follows two keywords named `from` and `to`, which means a file will be edited from some string to other string. `Cmd` means the button will excuete a command which could be run on Windows cmd.

--------------

# 欢迎来到Shortcut！
Shortcut是一个高度配置化的桌面工具，它旨在集成一些常见的操作，以此来提高工作效率！

##预先安装
1. [Python3.4](https://www.python.org/downloads/)
2. [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
3. [cx_Freeze](https://pypi.python.org/packages/3.4/c/cx_Freeze/cx_Freeze-4.3.4.win32-py3.4.exe#md5=bd087416c69ced533768a22e5d3414b8)

##使用指南
###构建exe
进入项目根目录调用命令行 `python setup.py build`, 或者直接打开build.bat，会在根目录下自动生成build文件夹。

###运行
* 即时查看结果，在项目根目录下，运行 `run.bat` 或打开命令行 `python shorcut.py`。
* 运行exe，直接运行 `项目根目录/build/exe.win32-3.4/Shorcut.exe`。

###配置
我们在 `config.ini` 中方便地配置常见的行为。

* `<section:path>` 代表在配置文件中写好的路径。
* [Button]区块是必须的，因为Shortcut据此来生成具备某种行为的按钮。
* [Button]中的每个项都是以`open` 、 `edit` 、`cmd` 开头（未来还会更多）。`Open` 表示按钮是用来打开一个应用程序、目录或者其他。`Edit` 表示按钮是用来编辑一个文件。 `Edit` 关键字常常跟着 `from` 和 `to` 两个关键字。它们表示文件的编辑会从某些字符串改成另一些字符串。
`Cmd` 表示按钮是用来执行一段命令。