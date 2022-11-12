import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon


class Mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Mywindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./file/test1.ico"))
    form = Mywindow()
    form.show()
    # time.sleep(20)
    # form.center()
    sys.exit(app.exec_())

2、设计UI的时候，给主窗口加颜色，background-color:rgb(120, 219, 255)
    图片方法：background-image: url(:/image/background.png);

3、UI文件补充函数内容
        #定义按键功能
        self.pushButton.clicked.connect(self.chifan)
        self.pushButton_2.clicked.connect(self.chimian)
        self.pushButton_3.clicked.connect(self.chimixian)
        self.pushButton_4.clicked.connect(self.waimianchi)
        self.pushButton_5.clicked.connect(self.close)

#定义自定义函数
    def chifan(self):
        tool = Eattool()
        result = tool.eat_fan()
        self.textEdit.setPlainText(result)

    def chimian(self):
        tool = Eattool()
        result = tool.eat_mian()
        self.textEdit.setPlainText(result)

    def chimixian(self):
        tool = Eattool()
        result = tool.eat_mixian()
        self.textEdit.setPlainText(result)

    def waimianchi(self):
        tool = Eattool()
        result = tool.eat_out()
        self.textEdit.setPlainText(result)

2、打包（去命令行模式）
pyinstaller -F -w .\exec.py