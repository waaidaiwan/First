# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:14:38 2017

@author: Papa
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    ans = 0
    for i in range(len(listA)):
        ans = ans + listA[i]*listB[i]
        i += 1 
    #print(i)
    return ans
    
dotProduct([2,3,4], [5,6,7])