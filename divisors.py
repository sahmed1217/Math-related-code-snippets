# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:07:43 2024

@author: sa066
"""

import math
import numpy
import itertools

"""
Check whether a positive integer is a perfect square by asking if 
the square root is an integer.
"""
def is_square(n):
    return (math.sqrt(n)==round(math.sqrt(n)))


"""
Given a positive integer n, returns the non-zero divisors of n
that are strictly less than n.
"""

def divisors_of(n):
    # Return the empty list for n=1
    if n==1:
        return ([])
    #Otherwise, we start with a list that goes up to the ceiling of the square root
    div_list=list(range(2, math.ceil(math.sqrt(n))))
    k=2
    
    """
    Start with k=2, and ask whether or not it divides n. If k does not divide n, 
    then we know that all multiples of k certainly do not divide n so we eliminate 
    them from the list. Proceed up to the square root of n, and then toss in the
    remainder of the list by simply dividing n by the elements of the original list.
    """
    while k<math.ceil(math.sqrt(n)):
        if n%k!=0:
            div_list=list(filter(lambda x : not((x%k==0)), div_list))
        
        """
        When we move to the next k value, it may very well be possible that we
        eliminated all higher values of k below the square root of n. So, we
        just catch the ValueError exception and set k equal to the square root
        to end the loop.
        """
        try:
            k=min(y for y in div_list if y>k)
        except ValueError:
            k=math.ceil(math.sqrt(n))
    #Adding remaining values to the divisor list 
    div_list=div_list+[int(n/div) for div in div_list]+[1]
    
    #Also toss in the square root of n if it's a square.
    if is_square(n):
        return(div_list+[int(math.sqrt(n))])
    else:
        return(div_list)
        