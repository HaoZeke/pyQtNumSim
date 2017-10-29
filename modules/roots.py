#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' root = bisection(f,x1,x2,switch=0,tol=1.0e-9)
	Finds a root of f(x)=0 by the bisection method.
	Root is bracketed by (x1,x2).
	Switch is set to 1 for the root, else 0 for instability.
'''

import math
from numpy import sign
from sympy import *

def bisection(f,x1,x2,switch=1,tol=1.0e-9):
	f1 = f(x1)
	if f1 == 0.0 : return x1	
	
	f2 = f(x2)
	if f2 == 0.0 : return x2

	if sign(f1) == sign(f2):
		print('Root is not bracketed')
	
	n = int(math.ceil(math.log(abs(x2-x1)/tol)/math.log(2)))

	for i in range(n):
		x3 = 0.5*(x1+x2); f3 = f(x3)
		if (switch == 1) and (abs(f3) > abs(f1)) \
		and (abs(f3) > abs(f2)):
			return None
		if f3 == 0.0: return x3
		if sign(f2) != sign(f3):
			x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	return (x1 + x2)/2.0

def newtonRaphson(f,guessX,precision=1.0e-9):
	''' Inspired by https://devopslog.wordpress.com/2012/12/23/newton-raphson-method-using-python-sympy/
	'''

	# Variable Definition
	sym_x = Symbol('x')

	# Conversion attempt
	try:
		fx = S(f)
	except:
		sys.exit('Unable to convert function to symbolic expression.')

	# Differentiation attempt
	try:
		dfdx = diff(fx, sym_x)
	except:
		print('Unable to differntiate.')

	# e is the relative error between consecutive approximations
	e = 1
	x0 = guessX
	niter = 0

	while ( e > precision ):
		# Get a new approximation
		try:
			r = x0 - fx.subs({sym_x : x0})/dfdx.subs({sym_x : x0})
		except ZeroDivisionError:
			print("Derivative is Zero. Terminate")
			# sys.exit()
		# Update the error
		e = abs((r-x0)/r)
		niter += 1
		x0 = r

	# Get the value at the root	
	xval = fx.subs({sym_x : r},)
	# Declare a result tuple
	result = (r,niter,xval)
	return result