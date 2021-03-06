#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Copyright (C) 2017  Rohit Goswami

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import math
from numpy import sign
from sympy import *

''' root = bisection(f,x1,x2,switch=0,tol=1.0e-9)
	Finds a root of f(x)=0 by the bisection method.
	Root is bracketed by (x1,x2).
	Switch is set to 1 for the root, else 0 for instability.
'''

def bisection(f,x1,x2,tol=1.0e-9,switch=1):
	# Variable Definition
	sym_x = Symbol('x')

	# Conversion attempt
	try:
		fx = S(f)
	except:
		sys.exit('Unable to convert function to symbolic expression.')

	f1 = fx.subs({sym_x : x1})
	if f1 == 0.0 : return x1	

	f2 = fx.subs({sym_x : x2})
	if f2 == 0.0 : return x2

	if not (f1*f2 < 0):
		print('Root is not bracketed')

	n = int(math.ceil(math.log(abs(x2-x1)/tol)/math.log(2)))

	for _ in range(n):
		x3 = 0.5*(x1+x2); f3 = fx.subs({sym_x : x3})
		if (switch == 1) and (abs(f3) > abs(f1)) \
		and (abs(f3) > abs(f2)):
			return None
		if f3 == 0.0: return x3
		if sign(f2) != sign(f3):
			x1 = x3; f1 = f3
		else: x2 = x3; f2 = f3
	# Get the value at the root	
	# Declare a result tuple
	r = 0.5*(x1 + x2)
	xval = fx.subs({sym_x : r},)
	return r, n, xval


''' root = newtonRaphson(f,guessX,precision=1.0e-9)
	Finds a root of f(x)=0 by the Newton Raphson method.
	Uses symbolic differentiation to get to the root from the initial guess.
'''

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


''' root = secant(f,x1,x2,tol=1.0e-9,maxIter=1.0e4)
	Finds a root of f(x)=0 by the secant method.
	Root approximations are x1 and x2.
'''

def secant(f,x1,x2,tol=1.0e-9,maxIter=1000):
	# Variable Definition
	sym_x = Symbol('x')
	
	# Conversion attempt
	try:
		fx = S(f)
	except:
		sys.exit('Unable to convert function to symbolic expression.')


	# e is the relative error between consecutive approximations
	e = 1
	niter = 0

	f1 = fx.subs({sym_x : x1})
	if f1 == 0.0 : return x1	
	
	f2 = fx.subs({sym_x : x2})
	if f2 == 0.0 : return x2
	
	while ( e > tol ):
		# Get a new approximation
		try:
			f1 = fx.subs({sym_x : x1})
			f2 = fx.subs({sym_x : x2})
			x3 = x2 - (f2*(x2-x1))/(f2-f1); f3 = fx.subs({sym_x : x3})
		except ZeroDivisionError:
			print("Division by Zero. Terminate")
			sys.exit()
		# Update the error
		e = abs((x3-x2)/x3)
		niter += 1
		x1 = x3
		if niter > maxIter:
			break

	# Get the value at the root	
	xval = fx.subs({sym_x : x3},)
	itr = niter - 1
	# Declare a result tuple
	result = (x3,itr,xval)
	return result


''' root = regulaF(f,x1,x2,tol=1.0e-9,maxIter=1.0e4)
	Finds a root of f(x)=0 by the secant method.
	Root approximations are x1 and x2.
	Switch is set to 1 for the root, else 0 for instability.
'''

def regulaFalsi(f,x1,x2,tol=1.0e-9,maxIter=1000):
	# Variable Definition
	sym_x = Symbol('x')
	
	# Conversion attempt
	try:
		fx = S(f)
	except:
		sys.exit('Unable to convert function to symbolic expression.')


	# e is the relative error between consecutive approximations
	e = 1
	niter = 0

	f1 = fx.subs({sym_x : x1})
	if f1 == 0.0 : return x1	
	
	f2 = fx.subs({sym_x : x2})
	if f2 == 0.0 : return x2
	
	while ( e > tol ):
		# Get a new approximation
		try:
			f1 = fx.subs({sym_x : x1})
			f2 = fx.subs({sym_x : x2})
			x3 = x2 - (f2*(x2-x1))/(f2-f1); f3 = fx.subs({sym_x : x3})
		except ZeroDivisionError:
			print("Division by Zero. Terminate")
			sys.exit()
		# Update the error
		e = abs((x3-x2)/x3)
		niter += 1
		if sign(f2) != sign(f3):
			x1 = x3
		else: 
			x2 = x3
		if niter > maxIter:
			break

	# Get the value at the root	
	xval = fx.subs({sym_x : x3},)
	itr = niter - 1
	# Declare a result tuple
	result = (x3,itr,xval)
	return result
