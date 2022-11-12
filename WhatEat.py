# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhatEat.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Eattool import Eattool

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(67, 255, 249)")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 75, 150, 50))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(48, 255, 62)")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 480, 60))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 75, 150, 50))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(48, 255, 62)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 75, 150, 50))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(48, 255, 62)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 75, 150, 50))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(48, 255, 62)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 500, 60))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 500, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 200, 750, 290))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #定义按键功能
        self.pushButton.clicked.connect(self.chifan)
        self.pushButton_2.clicked.connect(self.chimian)
        self.pushButton_3.clicked.connect(self.chimixian)
        self.pushButton_4.clicked.connect(self.waimianchi)
        self.pushButton_5.clicked.connect(self.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "吃饭"))
        self.label.setText(_translate("MainWindow", "请点击你今天想要吃的食物类型"))
        self.pushButton_2.setText(_translate("MainWindow", "吃面"))
        self.pushButton_3.setText(_translate("MainWindow", "吃米线"))
        self.pushButton_4.setText(_translate("MainWindow", "外面吃"))
        self.label_2.setText(_translate("MainWindow", "下面是为您推荐的结果"))
        self.pushButton_5.setText(_translate("MainWindow", "关闭"))

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

