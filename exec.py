import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ChoiceWhatEat import Ui_MainWindow


class Mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Mywindow,self).__init__(parent)
        self.setupUi(self)
        self.configHelp.triggered.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        text = QTextEdit('', dialog)
        text.resize(800, 480)
        text.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[general]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[food]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mian = 鸡杂面|肥肠面|豌杂面</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mixian = 牛肉米线|郡花米线|豌豆米线</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rou = 泡椒猪肝|糖醋排骨|白菜肉丝</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sucai = 炒白菜|炒豌豆尖|酸辣土豆丝</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tang = 小菜豆腐汤|紫菜蛋花汤|海带蹄花汤</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">out = 串串香|牛尾汤|泰国菜|陈光记|烤肉</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[drink]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">naicha = 珍珠奶茶|丝袜奶茶|豆腐奶茶</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">guocha = 杨枝甘露|葡萄多多|清爽百香果</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">caffee = 南山咖啡|卡布奇诺|猫屎咖啡|雀巢咖啡</p></body></html>")
        dialog.setWindowTitle("请将【config.ini】文件按照如下格式进行填写，并存放到程序同级目录，注意符号均为英文")
        dialog.resize(800, 480)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon("./file/test1.ico"))
    form = Mywindow()
    form.show()
    # time.sleep(20)
    # form.center()
    sys.exit(app.exec_())