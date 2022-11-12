import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from WhatEat import Ui_MainWindow

class Mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Mywindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("./file/test1.ico"))
    form = Mywindow()
    form.show()
    # time.sleep(20)
    # form.center()
    sys.exit(app.exec_())