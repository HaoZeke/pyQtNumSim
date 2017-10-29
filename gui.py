#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
GUI Portion of the Numerical Swissknife
"""

import sys
import numpy as np
from io import StringIO
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
        self.btnCalcRoot.clicked.connect(self.calcRootMenu)
        self.btnCalcLAS.clicked.connect(self.calcLASnGE)


    def calcRootMenu(self):
        try:
            if self.inpNR.isChecked() == true:
                # self.label_22.setEnabled(False)
                # self.upperBound.setEnabled(False)
                # self.label_23.setEnabled(False)
                # self.lowerBound.setEnabled(False)
                self.calcRootNR()
            if self.inpBi.isChecked() == true:
                # self.label_11.setEnabled(False)
                # self.guessX.setEnabled(False)
                self.calcRootBi()
            if self.btnGrpRF.checkedId() == -1:
                QMessageBox.warning(self, "User Warning","Choose a method.")
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass
            

    def calcRootNR(self):
        f = self.funcInpRoot.text()
        if not f:
            QMessageBox.warning(self, "User Warning","Enter an equation.")
        else:
            gX = self.guessX.value()
            if self.precisionRF.text():
                preci = float(self.precisionRF.text())
                x,niter,xval = roots.newtonRaphson(f,gX,preci)
            else:
                x,niter,xval = roots.newtonRaphson(f,gX)
            self.outTextRoot.append("<b> Newton-Raphson Method </b><br> \
                For the function " + self.funcInpRoot.text())
            self.outTextRoot.append(" The root is approximately " + repr(x))
            self.outTextRoot.append(" After " + str(niter) + " iterations.")
            self.outTextRoot.append(" At the approximate root, the function is " \
             + repr(xval))

    def calcRootBi(self):
        f = self.funcInpRoot.text()
        if not f:
            QMessageBox.warning(self, "User Warning","Enter an equation.")
        else:
            lBound = self.lowerBound.value()
            uBound = self.upperBound.value()
            if self.precisionRF.text():
                preci = float(self.precisionRF.text())
                x,niter,xval = roots.bisection(f,lBound,uBound,tol=preci)
            else:
                x,niter,xval = roots.bisection(f,lBound,uBound)
            self.outTextRoot.append("<b> Bisection Method </b><br> \
             For the function " + self.funcInpRoot.text())
            self.outTextRoot.append(" The root is approximately " + repr(x))
            self.outTextRoot.append(" After " + str(niter) + " iterations.")
            self.outTextRoot.append(" At the approximate root, the function is " \
             + repr(xval))


    def calcLASnGE(self):
       A = np.matrix(np.loadtxt(StringIO(self.inpTextLA.toPlainText())))
       b = np.fromstring(self.inpVecB.text(),sep=' ')
       classAns = las.gaussElim(A,b)
       self.outTextLA.append("The matrix A is \n" + str(A))
       self.outTextLA.append("\nThe vector b is \n" + str(b.reshape((-1, 1))))
       self.outTextLA.append("\nThe X vector is \n" + str(classAns.x.reshape((-1,1))))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())