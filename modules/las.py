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


''' X = nGaussElim(a,b)
	Solves [a]{b} = {x} by the Naive Gauss Eliminiation method.
	Uses https://gist.github.com/jgcastro89/49090cc69a499a129413597433b9baab
	Basically, Ax = b --> Ux = c
'''

import numpy as np
from scipy import linalg as LA
import copy

def nGaussElim():
	n = len(b)
	# Elimination Phase
	for k in range(n-1):
		for i in range(k+1,n):
			if a[i,k] != 0.0:
				lam = a[i,k]/a[k,k]
				a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
				b[i] = b[i] - lam*b[k]
	# Back Substitution
	for k in range(n-1,-1,1):
		b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
	return b 

class gaussElim():
    """
    Gaussian elimination with partial pivoting.
    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b
            with the entries permuted in
            accordance with the pivoting
            done by the algorithm
    post-condition: A and b have been modified.
    :return
    """

    def __init__(self, A, b, doPricing=True):
        #super(gaussElim, self).__init__()

        self.A = A                      # input: A is an n x n numpy matrix
        self.b = b                      # b is an n x 1 numpy array
        self.doPricing = doPricing

        self.n = None                   # n is the length of A
        self.x = None                   # x is the solution of Ax=b

        self._validate_input()          # method that validates input
        self._elimination()             # method that conducts elimination
        self._backsub()                 # method that conducts back-substitution

    def _validate_input(self):
        self.n = len(self.A)
        if self.b.size != self.n:
            raise ValueError("Invalid argument: incompatible sizes between" +
                             "A & b.", self.b.size, self.n)

    def _elimination(self):
        """
        k represents the current pivot row. Since GE traverses the matrix in the
        upper right triangle, we also use k for indicating the k-th diagonal
        column index.
        :return
        """

        # Elimination
        for k in range(self.n - 1):
            if self.doPricing:
                # Pivot
                maxindex = abs(self.A[k:, k]).argmax() + k
                if self.A[maxindex, k] == 0:
                    raise ValueError("Matrix is singular.")
                # Swap
                if maxindex != k:
                    self.A[[k, maxindex]] = self.A[[maxindex, k]]
                    self.b[[k, maxindex]] = self.b[[maxindex, k]]
            else:
                if self.A[k, k] == 0:
                    raise ValueError("Pivot element is zero. Try setting doPricing to True.")
            # Eliminate
            for row in range(k + 1, self.n):
                multiplier = self.A[row, k] / self.A[k, k]
                self.A[row, k:] = self.A[row, k:] - multiplier * self.A[k, k:]
                self.b[row] = self.b[row] - multiplier * self.b[k]

    def _backsub(self):
        # Back Substitution
        self.x = np.zeros(self.n)
        for k in range(self.n - 1, -1, -1):
            self.x[k] = (self.b[k] - np.dot(self.A[k, k + 1:], self.x[k + 1:])) / self.A[k, k]


def gaussSeidel(A, b, itrMax = 1000):
	# From https://gist.github.com/szknbyk/07542a8cca549fd1315aedba53c6511c
	# Check https://www.wikiwand.com/en/Gauss%E2%80%93Seidel_method too.	
    if A.shape[1] != b.shape[0]:
        return 0
    
    n = b.shape[0]
    
    x = np.zeros(n)
    old_x = np.zeros(n)
    
    for k in range(itrMax):
        for i in range(n):
            x[i] = b[i]
            
            for j in range(n):
                if i != j:
                    x[i] -= A[i, j] * x[j]
                    
            x[i] = x[i] / A[i, i]
        
        if LA.norm(x - old_x) < 1.0e-20:
            break
        
        old_x = copy.deepcopy(x)
    
    return x,k


def gaussJordan(A,b):
    """
    Returns the vector x such that Ax=b.
    
    A is assumed to be an n by n matrix and b an n-element vector.
    """
    n,m = A.shape
    # should put in some checks of our assumptions, e.g. n == m
    C = np.zeros((n,m+1),float)
    C[:,0:n],C[:,n] = A, b

    for j in range(n):
        # First, do partial pivoting.
        p = j # the current diagonal element is pivot by default
        # look for alternate pivot by searching for largest element in column
        for i in range(j+1,n):
            if abs(C[i,j]) > abs(C[p,j]): p = i
        if abs(C[p,j]) < 1.0e-16:
            print("matrix is (likely) singular")
            return b 
        # swap rows to get largest magnitude element on the diagonal (BROKEN)
        # C[p,:],C[j,:] = copy(C[j,:]),copy(C[p,:])
        # Now, do scaling and elimination.
        pivot = C[j,j]
        C[j,:] = C[j,:] / pivot
        for i in range(n):
            if i == j: continue
            C[i,:] = C[i,:] - C[i,j]*C[j,:]
    I,x = C[:,0:n],C[:,n]
    return x