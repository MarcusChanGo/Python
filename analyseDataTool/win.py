#!/usr/bin/python3
# coding: utf-8


from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("mainWindow");
        MainWindow.resize(900,700);
        MainWindow.setWindowTitle("分析数据工具");
        self.centralwidget = QtWidgets.QWidget(MainWindow);
        self.centralwidget.setObjectName("centralwidget");