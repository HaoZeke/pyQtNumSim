#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
GUI Portion of the Numerical Swissknife
"""

import sys
from sympy import *
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QWidget, qApp, QDesktopWidget, 
    QMessageBox, QPushButton, QToolTip, QMainWindow)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from modules import *

qtCreatorFile = "testUI.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def out():
    print("Hi")

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnQuit.clicked.connect(qApp.quit)
        self.btnCalcRoot.clicked.connect(self.calcRootNR)


    def calcRootNR(self):
        f = self.funcInpRoot.text()
        gX = self.guessX.value()
        x,niter,xval = roots.newtonRaphson(f,gX)
        self.outTextRoot.append(" For the function " + self.funcInpRoot.text())
        self.outTextRoot.append(" The root is approximately " + repr(x))
        self.outTextRoot.append(" After " + str(niter) + " iterations.")
        self.outTextRoot.append(" At the approximate root, the function is " \
         + repr(xval))

    def calc(self):
        sym_x = Symbol('x')
        try:
            fx = S(self.funcInp.text())
        except:
            sys.exit('Unable to convert.')

        try:
            dfdx = diff(fx, Symbol('x'))
        except:
            sys.exit('Can\'t Diff')
        self.outText.append(" test " + repr(dfdx))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())