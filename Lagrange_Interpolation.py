# -*- coding: utf-8 -*-
"""
Takes a sequence of (x,y) points and returns a vector of coefficients for
the Lagrange Interpolating polynomial in degree order starting with the
constant term. 
"""
import numpy as np

def poly_interp(points):
    
    n=len(points)
    coef_mat=np.empty((n,n))
    
    #Set aside the y-values as a vector
    y_vect=np.asarray([p[1] for p in points])
    i=0
    
    #Create the Vandermonde matrix from the given x-values
    for (x,y) in points:
        coef=[]
        for k in range(n):
            coef.append(x**k)
        
        coef_mat[i]=coef
        i+=1
    
    #Solve Ax=b where A is the Vandermonde matrix and b is the y-values
    return(np.linalg.solve(coef_mat, y_vect))
