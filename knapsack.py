# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:31:02 2019

@author: Long
"""

def knapsack(W,wt,val,num):
    pairList = [[0 for w in range(W + 1)] 
                   for v in range(num + 1)] 

    for m in range(num + 1): 
        for n in range(W + 1): 
            #base case
            if m == 0 or n == 0:
                pairList[m][n] = 0
            elif wt[m - 1] <= n: 
                pairList[m][n] = max(val[m - 1] + pairList[m - 1][n - wt[m - 1]], 
                               pairList[m - 1][n]) 
            else: 
                pairList[m][n] = pairList[m - 1][n] 
    result = pairList[num][W]
    print(result)
    w = W 
    for i in range(num, 0, -1): 
        if result <= 0: 
            break
        # either the result comes from the 
        # top (pairList[i-1][w]) or from (val[i-1] 
        # + pairList[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if result == pairList[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            print(wt[i - 1], end = " ")
            print(val[i - 1])  
            # Since this weight is included 
            # its value is deducted 
            result = result - val[i - 1] 
            w = w - wt[i - 1] 
#    return (pairList[m][n],m,n)
#v = [ 60, 100, 120 ] 
#w = [ 10, 20, 30 ] 
#W = 50

w = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 7, 7, 8, 9, 10, 11, 15]
v = [2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6,10, 11, 13, 12, 15, 11, 20]
W = 30
num = len(v) 
      
knapsack(W, w, v, num)