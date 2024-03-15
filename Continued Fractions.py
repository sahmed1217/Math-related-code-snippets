# -*- coding: utf-8 -*-
"""
Takes the first n elements of a continued fraction as a list, and returns the
rational approximation based on those n elements in the form of a two element
list with [numerator, denominator]
"""

def cont_frac_rational(num_list):
    #First check if the list is empty
    if len(num_list)==0:
        return 0
    
    top=1
    bottom=num_list.pop()
    
    while len(num_list)>0:
        
        #We go backwards through the continued fraction
        whole=num_list.pop()
        
        #Assuming we are not at the end of the continued fraction, we'll
        #have to flip it to add the next element.
        new_b=(whole*bottom)+top
        new_t=bottom
        
        bottom=new_b
        top=new_t
    
    #once we reach the end, we just flip the fraction over correctly.
    return([bottom, top])
        

