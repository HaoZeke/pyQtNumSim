#!/usr/bin/python3
# -*- coding: utf-8 -*-


import math
from numpy import sign
from sympy import *
from PyQt5.QtWidgets import (QApplication, QWidget, qApp, QDesktopWidget, 
    QMessageBox, QPushButton, QToolTip, QMainWindow)

def rk1(f,startX,startY,endX,h=0.025):
	# Variable Definition
	sym_x = Symbol('x')
	sym_y = Symbol('y')

	# Conversion attempt
	try:
		fxy = S(f)
	except:
		sys.exit('Unable to convert function to symbolic expression.')

	# Differentiation attempt
	try:
		dfdx = diff(fxy, sym_x)
	except:
		print('Unable to differntiate.')

	itr = 0
	x = startX
	y = startY
	while startX < endX:
		itr += itr
		h = min(h,endX-startX)
		x = x + h
		if itr == 1:
			k1 = h * dfdx.evalf(subs={sym_x: startX, sym_y: startY})
		else:
			k1 = h * dfdx.evalf(subs={sym_x: x, sym_y: y})
		y = y + k1
		self.outTextODE.append("\n Iteration" + str(itr) + " : ")
		self.outTextODE.append("\nx is " + str(x) + " : ")
		self.outTextODE.append("\nk1 is " + str(k1) + " : ")
		self.outTextODE.append("\ny is " + str(y) + " : ")
			
