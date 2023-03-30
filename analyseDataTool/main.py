#!/usr/bin/python3
# coding: utf-8


import Ui_test
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv);
    window = QMainWindow();
    ui = Ui_test.Ui_MainWindow();
    ui.setupUi(window);
    window.show();
    sys.exit(app.exec_());