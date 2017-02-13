# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:21:34 2017

@author: Papa
"""

def closest_power(base, num):
    """
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    """    
    z = {}
    i = 0
    lk=[]
    lv=[]
    for i in range ((num//base)+1):
        z.update({i:abs(base**int(i)-num)})
        i += 1
        for key, value in z.items():
            lk.append(key)
            lv.append(value)       
    return lk[lv.index(min(lv))]       