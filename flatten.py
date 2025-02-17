# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:42:29 2018

@author: Bec
"""
aList=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    def flat(L):
        for i in L:
            if type(i)!=list:
                ans.append(i)
            else: 
                ans.append(flat(i))
        return ans
    ans=[]
    x=flat(aList)
    for i in x:
        if type(i)==list:
            x.remove(i)
    for i in x:
        if type(i)==list:
            x.remove(i)
    return x
    
print(flatten(aList))