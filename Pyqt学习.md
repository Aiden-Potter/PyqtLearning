# Pyqt学习

## QT Designer配置

照着教程配好ui界面和ui转换成py代码的两个插件

之后生成一个qt的ui类

再写一个MyMainForm类继承QMainWindow和UI布局，把自己这个对象传到setupUi方法中

接下来就可以在MyMainForm写窗口逻辑了

简单来说就是绑定按钮方法执行

## 关于消息显示

### QMessageBox：弹出消息对话框控件

 QMessageBox是一种通用的弹出式对话框，用于显示消息，允许用户通过单击不同的标准按钮对消息进行反馈。弹出式对话框有很多类型，如提示、警告、错误、询问、关于等对话框。这些不同类型的QMessageBox对话框只是显示时图标不同，其他功能一样。

 **QMessageBox类中常用方法**

  information(QWdiget parent,title,text,buttons,defaultButton)：弹出消息对话框。

  question(QWidget parent,title,text,buttons,defaultButton)：弹出问答对话框

  warning(QWidget parent,title,text,buttons,defaultButton)：弹出警告对话框

  critical(QWidget parent,title,text,buttons,defaultButton)：弹出严重错误对话框

  about(QWidget parent,title,text)：弹出关于对话

 **参数解释如下：**

  parent：指定的父窗口控件。

  title：表示对话框标题。

  text：表示对话框文本。

  buttons：表示多个标准按钮，默认为ok按钮。

  defaultButton表示默认选中的标准按钮，默认选中第一个标准按钮。

 **其他方法如下：**

  setTitle()：设置标题

  setText()：设置正文消息

  setIcon()：设置弹出对话框的图片

 **QMessageBox的标准按钮类型**

  QMessage.Ok 同意操作、QMessage.Cancel 取消操作、QMessage.Yes 同意操作、QMessage.No 取消操作、QMessage.Abort 终止操作、QMessage.Retry 重试操作、QMessage.Ignore 忽略操作

 **5种常用的消息对话框及其显示效果**

  提前说明：from PyQt5.QtWidgets import **QMessageBox** 导入直接使用

 （1）消息对话框，用来告诉用户关于提示信息

  QMessageBox.information(self, '信息提示对话框','前方右拐到达目的地',QMessageBox.Yes | QMessageBox.No)

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803130840952-562264456.png)

 （2）提问对话框，用来告诉用户关于提问消息。

 QMessageBox.question(self, "提问对话框", "你要继续搞测试吗？", QMessageBox.Yes | QMessageBox.No)

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803130929590-2126905760.png)

 **特别注意Tips：** **对于提问对话框，需要根据用户选择Yes或者No进行下一步判断，可以获取按钮点击的返回值进行判断，选择NO的返回值为65536，选择Yes的返回值为其他**。。示例如下：

![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901073917520-232369572.png)

（3）警告对话框，用来告诉用户关于不寻常的错误消息。

 QMessageBox.warning(self, "警告对话框", "继续执行会导致系统重启，你确定要继续？", QMessageBox.Yes | QMessageBox.No)

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803131029955-1482217950.png)

 （4）严重错误对话框，用来告诉用户关于程序执行失败的严重的错误消息。

 QMessageBox.critical(self, "严重错误对话框", "数组越界，程序异常退出", QMessageBox.Yes | QMessageBox.No)

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803131109046-1975905633.png)

 （5）关于对话框

 QMessageBox.about(self, "关于对话框", "你的Windows系统是DOS1.0")

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803131147405-359711040.png)

**上述程序完整代码如下：**



```python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 166)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("YaHei Consolas Hybrid")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "对话框"))
        self.pushButton.setText(_translate("Form", "弹出对话框"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMsg)

    def showMsg(self):
        QMessageBox.information(self, '信息提示对话框','前方右拐到达目的地',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        QMessageBox.question(self, "提问对话框", "你要继续搞测试吗？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.warning(self, "警告对话框", "继续执行会导致系统重启，你确定要继续？", QMessageBox.Yes | QMessageBox.No)
        QMessageBox.critical(self, "严重错误对话框", "数组越界，程序异常退出", QMessageBox.Yes | QMessageBox.No,)
        QMessageBox.about(self, "关于对话框", "你的Windows系统是DOS1.0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```



#### 运行结果（顺序弹出以下消息框）。

![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901072756356-1584337759.png)

#### 关键代码

![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901072139245-486019548.png)

### QInputDialog标准对话框控件

 QInputDialog控件是一个标准对话框，用于获取用户输入信息，QInputDialog控件可以提供数字、字符串输入或提供下拉列表选择。

 针对QInputDialog对话框控件的使用，**我们主要考虑2个问题**：1、如何在弹出对话框供用户输入，2、如何获取用户输入。

 **QInputDialog常用方法：**

  getint()：从输入控件中获得标准整数输入

  getDouble()：从输入控件中获得标准浮点数输入

  getText()：从输入控件中获得标准字符串的输入

  getItem() ：从输入控件中获得列表里的选项输入

**完整代码如下（代码可直接复制运行）：**



```python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 190)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.GetIntlineEdit = QtWidgets.QLineEdit(Form)
        self.GetIntlineEdit.setGeometry(QtCore.QRect(150, 30, 150, 31))
        self.GetIntlineEdit.setText("")
        self.GetIntlineEdit.setObjectName("GetIntlineEdit")
        self.GetstrlineEdit = QtWidgets.QLineEdit(Form)
        self.GetstrlineEdit.setGeometry(QtCore.QRect(150, 80, 150, 31))
        self.GetstrlineEdit.setObjectName("GetstrlineEdit")
        self.GetItemlineEdit = QtWidgets.QLineEdit(Form)
        self.GetItemlineEdit.setGeometry(QtCore.QRect(150, 130, 150, 31))
        self.GetItemlineEdit.setObjectName("GetItemlineEdit")
        self.getIntButton = QtWidgets.QPushButton(Form)
        self.getIntButton.setGeometry(QtCore.QRect(50, 30, 80, 31))
        self.getIntButton.setObjectName("getIntButton")
        self.getStrButton = QtWidgets.QPushButton(Form)
        self.getStrButton.setGeometry(QtCore.QRect(50, 80, 80, 31))
        self.getStrButton.setObjectName("getStrButton")
        self.getItemButton = QtWidgets.QPushButton(Form)
        self.getItemButton.setGeometry(QtCore.QRect(50, 130, 80, 31))
        self.getItemButton.setObjectName("getItemButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QInputDialog例子"))
        self.getIntButton.setText(_translate("Form", "获取整数"))
        self.getStrButton.setText(_translate("Form", "获取字符串"))
        self.getItemButton.setText(_translate("Form", "获取列表选项"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.getIntButton.clicked.connect(self.getInt)
        self.getStrButton.clicked.connect(self.getStr)
        self.getItemButton.clicked.connect(self.getItem)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, 'Integer input dialog', '输入数字')
        if ok and num:
           self.GetIntlineEdit.setText(str(num))

    def getStr(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：')
        if ok and text:
            self.GetstrlineEdit.setText(str(text))

    def getItem(self):
        items=('C', 'C++', 'C#', 'JAva', 'Python')
        item, ok=QInputDialog.getItem(self, "select input dialog", '语言列表', items, 0, False)
        if ok and item:
            self.GetItemlineEdit.setText(str(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```



**运行结果如下（会陆续弹出三个输入对话框）：**

**![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901065443937-1853977653.png)**

 ![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901065533274-1778836533.png)

 ![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901065559664-1721651095.png)

**关键代码介绍：**

 **QInputDialog.getInt(self, 'Integer input dialog', '输入数字')** -> 输入整数对话框

 **QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：')** -> 输入字符串对话框

 **QInputDialog.getItem(self, "select input dialog", '语言列表', items, 0, False)** -> 下拉列表选择对话框

### QFileDialog 文件/目录选择对话框

 QFileDialog是用于打开和保存文件的标准对话框。使用QFileDialog控件**主要考虑2个场景**：使用该控件提供用户选择目录或文件，并保存选择目录或文件的路径。简单说就是实现类似word/Notepad++文件打开功能。如下

![img](https://img2018.cnblogs.com/blog/774327/201908/774327-20190803091202767-243037863.png)

  针对上述场景，**QFileDialog控件实现的主要方法**：

  QFileDialog.getOpenFileName()：获取单个文件路径

  QFileDialog.getOpenFileNames()：获取多个文件路径

  QFileDialog.getExistingDirectory()：获取文件夹路径

**完整代码如下：**



```python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 120)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 40, 301, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openFileButton = QtWidgets.QPushButton(self.widget)
        self.openFileButton.setObjectName("openFileButton")
        self.horizontalLayout.addWidget(self.openFileButton)
        self.filePathlineEdit = QtWidgets.QLineEdit(self.widget)
        self.filePathlineEdit.setObjectName("filePathlineEdit")
        self.horizontalLayout.addWidget(self.filePathlineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QFileDialog打开文件例子"))
        self.openFileButton.setText(_translate("Form", "打开文件"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.openFileButton.clicked.connect(self.openFile)

    def openFile(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                    "选取指定文件夹",
                                    "C:/")
        self.filePathlineEdit.setText(str(get_directory_path))

        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                    "选取单个文件",
                                   "C:/",
                                    "All Files (*);;Text Files (*.txt)")
        if ok:
            self.filePathlineEdit.setText(str(get_filename_path))

        get_filenames_path, ok = QFileDialog.getOpenFileNames(self,
                                    "选取多个文件",
                                   "C:/",
                                    "All Files (*);;Text Files (*.txt)")
        if ok:
            self.filePathlineEdit.setText(str(' '.join(get_filenames_path)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```



**运行结果如下（会陆续弹出选择文件夹、选择单个文件、选择多个文件）:**

**![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901065852725-1162451707.png)**

 

 ![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901065927411-129188262.png)

 

 

![img](https://img2018.cnblogs.com/blog/774327/201909/774327-20190901070031489-1392611234.png)

**关键代码介绍**

  **QFileDialog.getOpenFileName(self,"选取单个文件","C:/","All Files (\*);;Text Files (\*.txt)")** -> 获取单个指定文件的绝对路径

  getOpenFileName()参数说明：

  第1个参数：用于指定父组件

  第2个参数：对话框标题

  第3个参数：对话框显示时默认打开的目录。"."表示当前程序所在目录，“/”表示当前盘下的根目录。

  第4个参数：对话框中文件扩展名过滤器。All Files (*);;Text Files (*.txt)表示可以选择所有文件类型或者只显示.txt后缀的文件类型。

 **QFileDialog.getExistingDirectory(self,"选取指定文件夹","C:/")** -> 获取指定文件夹的绝对路径

 **QFileDialog.getOpenFileNames(self,"选取多个文件","C:/","All Files (\*);;Text Files (\*.txt)")** -> 获取多个指定文件的绝对路径



## 关于事件

GUI程序都是事件驱动的，事件由用户或者其他方式触发

还有mouse事件、key事件等等

```python
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()
```

### 如何给事件传递参数



信号本身是有类型的，包含一个参数的信号、两个参数的信号等等，这个参数要和槽函数传递的值对应

信号的参数类型要指定，信号的参数可以重载

```python
from PyQt5.QtCore import QObject , pyqtSignal

class CustSignal(QObject):

    #声明无参数的信号
    signal1 = pyqtSignal()

    #声明带一个int类型参数的信号
    signal2 = pyqtSignal(int)

    #声明带int和str类型参数的信号
    signal3 = pyqtSignal(int,str)

    #声明带一个列表类型参数的信号
    signal4 = pyqtSignal(list)

    #声明带一个字典类型参数的信号
    signal5 = pyqtSignal(dict)

    #声明一个多重载版本的信号，包括带int和str类型参数的信号和带str类型参数的信号
    signal6 = pyqtSignal([int,str], [str])

    def __init__(self,parent=None):
        super(CustSignal,self).__init__(parent)

        #将信号连接到指定槽函数
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int,str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6OverLoad)

        #发射信号
        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1,"text")
        self.signal4.emit([1,2,3,4])
        self.signal5.emit({"name":"wangwu","age":"25"})
        self.signal6[int,str].emit(1,"text")
        self.signal6[str].emit("text")

    def signalCall1(self):
        print("signal1 emit")

    def signalCall2(self,val):
        print("signal2 emit,value:",val)

    def signalCall3(self,val,text):
        print("signal3 emit,value:",val,text)

    def signalCall4(self,val):
        print("signal4 emit,value:",val)

    def signalCall5(self,val):
        print("signal5 emit,value:",val)

    def signalCall6(self,val,text):
        print("signal6 emit,value:",val,text)

    def signalCall6OverLoad(self,val):
        print("signal6 overload emit,value:",val)

if __name__ == '__main__':
    custSignal = CustSignal()
```



### TimerEvent

> 何时调用？

### connect

connect 用于绑定

事件有很多，包括

- clicked
- valueChanged







### sender

在被调用的函数里，可以使用sender方法来获得信号发送者进而完成逻辑

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

### emit

控制信号发出的作用，使用到QObject创建一个信号控制对象

类的触发事件，**mouse事件**

```python
    def mouseDoubleClickEvent(self, event) :
        self.c.closeApp.emit()
```

创建的信号控制对象

```python
class Communicate(QObject):
    closeApp =pyqtSignal()
```

完整代码

```python
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp =pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mouseDoubleClickEvent(self, event) :
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

### 自定义信号参数数量

1、使用lambda表达式传递按钮数字给槽函数，当然也可以传递其他任何东西

```python
from PyQt5.QtWidgets import QMainWindow, QPushButton , QWidget , QMessageBox, QApplication, QHBoxLayout
import sys

class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        button1.clicked.connect(lambda: self.onButtonClick(1))
        button2.clicked.connect(lambda: self.onButtonClick(2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        print('Button {0} 被按下了'.format(n))
        QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.setGeometry(300,300,600,400)
    form.show()
    sys.exit(app.exec_())
```

2、另一种解决方法是使用functools中的partial函数

```python
from PyQt5.QtWidgets import QMainWindow, QPushButton , QWidget , QMessageBox, QApplication, QHBoxLayout
import sys
from functools import partial

class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        # button1.clicked.connect(lambda: self.onButtonClick(1))
        # button2.clicked.connect(lambda: self.onButtonClick(2))
        button1.clicked.connect(partial(self.onButtonClick, 1))
        button2.clicked.connect(partial(self.onButtonClick, 2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        print('Button {0} 被按下了'.format(n))
        QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.setGeometry(300,300,600,400)
    form.show()
    sys.exit(app.exec_())
```

### disconnect

断开信号与槽的连接



## 关于轨迹绘制

save 和 restore保存画笔状态