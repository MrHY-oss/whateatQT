from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys
from Eattool import Eattool


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("今天你想吃什么呢，请点击下面四个类型选项")
        self.resize(600, 480)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("吃饭")
        self.btnPress2 = QPushButton("吃面")
        self.btnPress3 = QPushButton("吃米线")
        self.btnPress4 = QPushButton("外面吃")
        layout = QVBoxLayout()

        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)
        layout.addWidget(self.btnPress4)
        layout.addWidget(self.textEdit)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
        self.btnPress4.clicked.connect(self.btnPress4_Clicked)


    def btnPress1_Clicked(self):
        tool = Eattool()
        result = tool.eat_fan()
        self.textEdit.setPlainText(result)

    def btnPress2_Clicked(self):
        tool = Eattool()
        result = tool.eat_mian()
        self.textEdit.setPlainText(result)

    def btnPress3_Clicked(self):
        tool = Eattool()
        result = tool.eat_mixian()
        self.textEdit.setPlainText(result)

    def btnPress4_Clicked(self):
        tool = Eattool()
        result = tool.eat_out()
        self.textEdit.setPlainText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())