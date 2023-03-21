# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:32:19 2022

@author: Hu, I-Hsuan
"""
from collections import defaultdict
import math
class solution:
    
   
    number = input('Enter a list of number ')
    
    numberList = [int(x) for x in number.split()]
    numberList.sort()
    n = len(numberList)
    
    
    def mean(self, n,numberList):
        if not numberList:
            return 0
        else:
            return sum(numberList)/n
    
    def median(self, n, numberList):
        if not numberList:
            return 0
        if n%2:
            return numberList[n//2]
        elif not n%2:
            n //= 2
            return sum(numberList[n-1:n+1])/2
      
        
    def mode(self, numberList):
        if not numberList:
            return 0
        numdict = defaultdict(int)
        for i in numberList:
            numdict[i] += 1
        res = []
        for i, j in numdict.items():
            if j == max(numdict.values()):
                res.append(i)
        if len(res) == 1:
            return res[0]
        else:
            return None
    
    def standard_deviation(self, n, numberList):
        
        if not numberList:
            return 0
        z = [i - self.mean(n, numberList) for i in numberList]
        temp = math.sqrt(sum(z)**2/(n-1)) 
        return temp
        
    
     
    print('The mean of the list of the integer is',mean(n, numberList))  
    
    print('The median of the list of the integer is',median(n, numberList))
    
    print('The mode of the list of the integer is',mode(numberList))
    
    print('The standard deviation of the list of the integer is',standard_deviation(n, numberList))

x = solution()
x