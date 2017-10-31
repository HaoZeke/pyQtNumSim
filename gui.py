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

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnQuit.clicked.connect(qApp.quit)
        self.btnCalcRoot.clicked.connect(self.calcRootMenu)
        self.btnCalcLAS.clicked.connect(self.calcLASMenu)
        self.btnCalcODE.clicked.connect(self.calcODEMenu)


    def calcRootMenu(self):
        try:
            if self.inpNR.isChecked() == true:
                # self.label_22.setEnabled(False)
                # self.upperBound.setEnabled(False)
                self.calcRootNR()
            if self.inpBi.isChecked() == true:
                self.calcRootBi()
            if self.inpSec.isChecked() == true:
                self.calcRootSec()
            if self.inpRegF.isChecked() == true:
                self.calcRootRegFal()
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
            self.outTextRoot.append("The root is approximately " + repr(x))
            self.outTextRoot.append("After " + str(niter) + " iterations.")
            self.outTextRoot.append("At the approximate root, the function is " \
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
            self.outTextRoot.append("The root is approximately " + repr(x))
            self.outTextRoot.append("After " + str(niter) + " iterations.")
            self.outTextRoot.append("At the approximate root, the function is " \
             + repr(xval))

    def calcRootRegFal(self):
        # Needs user input for max iter.
        f = self.funcInpRoot.text()
        if not f:
            QMessageBox.warning(self, "User Warning","Enter an equation.")
        else:
            approxOne = self.lowerBound.value()
            approxTwo = self.upperBound.value()
            if self.precisionRF.text():
                preci = float(self.precisionRF.text())
                x,niter,xval = roots.regulaFalsi(f,approxOne,approxTwo,tol=preci)
            else:
                x,niter,xval = roots.regulaFalsi(f,approxOne,approxTwo)
            self.outTextRoot.append("<b> Regula Falsi Method </b><br> \
             For the function " + self.funcInpRoot.text())
            self.outTextRoot.append("The root is approximately " + repr(x))
            self.outTextRoot.append("After " + str(niter) + " iterations.")
            self.outTextRoot.append("At the approximate root, the function is " \
             + repr(xval))

    def calcRootSec(self):
        # Needs user input for max iter.
        f = self.funcInpRoot.text()
        if not f:
            QMessageBox.warning(self, "User Warning","Enter an equation.")
        else:
            approxOne = self.lowerBound.value()
            approxTwo = self.upperBound.value()
            if self.precisionRF.text():
                preci = float(self.precisionRF.text())
                x,niter,xval = roots.secant(f,approxOne,approxTwo,tol=preci)
            else:
                x,niter,xval = roots.secant(f,approxOne,approxTwo)
            self.outTextRoot.append("<b> Secant Method </b><br> \
             For the function " + self.funcInpRoot.text())
            self.outTextRoot.append("The root is approximately " + repr(x))
            if niter < 100:
                self.outTextRoot.append("After " + str(niter) + " iterations.")
            else:
                self.outTextRoot.append("After the maximum allowed iterations.")
            self.outTextRoot.append("At the approximate root, the function is " \
             + repr(xval))

    def calcLASMenu(self):
        try:
            if self.inpGE.isChecked() == true:
                # self.label_22.setEnabled(False)
                # self.upperBound.setEnabled(False)
                self.calcLASGEP()
            if self.inpGJ.isChecked() == true:
                self.calcLASGJ()
            if self.inpGS.isChecked() == true:
                self.calcLASGS()
            if self.btnGrpLAS.checkedId() == -1:
                QMessageBox.warning(self, "User Warning","Choose a method.")
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass
            

    def calcLASGEP(self):
       A = np.matrix(np.loadtxt(StringIO(self.inpTextLA.toPlainText())))
       b = np.fromstring(self.inpVecB.text(),sep=' ')
       classAns = las.gaussElim(A,b)
       self.outTextLA.append("<b> Gauss Elimination Method </b><br>")
       self.outTextLA.append("The matrix A is \n" + str(A))
       self.outTextLA.append("\nThe vector b is \n" + str(b.reshape((-1, 1))))
       self.outTextLA.append("\nThe X vector is \n" + str(classAns.x.reshape((-1,1))))

    def calcLASGJ(self):
       A = np.matrix(np.loadtxt(StringIO(self.inpTextLA.toPlainText())))
       b = np.fromstring(self.inpVecB.text(),sep=' ')
       classAns = las.gaussJordan(A,b)
       self.outTextLA.append("<b> Gauss Jordan Method </b><br>")
       self.outTextLA.append("The matrix A is \n" + str(A))
       self.outTextLA.append("\nThe vector b is \n" + str(b.reshape((-1, 1))))
       self.outTextLA.append("\nThe X vector is \n" + str(classAns.reshape((-1,1))))

    def calcLASGS(self):
       A = np.matrix(np.loadtxt(StringIO(self.inpTextLA.toPlainText())))
       b = np.fromstring(self.inpVecB.text(),sep=' ')
       if self.inpLASMaxItr.text():
           maxIter = int(self.inpLASMaxItr.text())
           x,itr = las.gaussSeidel(A,b, itrMax = maxIter)
       else:
           x,itr = las.gaussSeidel(A,b)
       x,itr = las.gaussSeidel(A,b)
       self.outTextLA.append("<b> Gauss Seidel Method </b><br>")
       self.outTextLA.append("The matrix A is \n" + str(A))
       self.outTextLA.append("\nThe vector b is \n" + str(b.reshape((-1, 1))))
       self.outTextLA.append("\nThe X vector is \n" + str(x.reshape((-1,1))))
       self.outTextLA.append("\nObtained in \n" + str(itr) + " iterations.")

    def calcODEMenu(self):
        try:
            if self.inpEu.isChecked() == true:
                self.calcODERK1()
            if self.inpRK2.isChecked() == true:
                self.calcODERK2()
            if self.inpRK3.isChecked() == true:
                self.calcODERK3()
            if self.inpRK4.isChecked() == true:
                self.calcODERK4()
            if self.inpMP.isChecked() == true:
                self.calcODEMP()
            if self.btnGrpRF.checkedId() == -1:
                QMessageBox.warning(self, "User Warning","Choose a method.")
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass

    def calcODERK1(self):
        # Needs to be modularized
        f = self.funcInpODE.text()
        if not f:
            QMessageBox.warning(self, "User Warning","Enter an equation.")
        else:
            startX = self.startX.value()
            startY = self.startY.value()
            endX = self.endX.value()
            if self.stepSize.text():
                stepSize = float(self.stepSize.text())
                MRKOde.rk1(f,startX,startY,endX,h=stepSize)
            else:
                self.outTextRoot.append("<b> Euler's Method </b><br> \
                    For the function " + self.funcInpRoot.text())
                MRKOde.rk1(f,startX,startY,endX)
            self.outTextRoot.append("The root is approximately " + repr(x))
            if niter < 100:
                self.outTextRoot.append("After " + str(niter) + " iterations.")
            else:
                self.outTextRoot.append("After the maximum allowed iterations.")
            self.outTextRoot.append("At the approximate root, the function is " \
             + repr(xval))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())