# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:37:10 2022

@author: Hu, I-Hsuan
"""

target = int(input('Enter a number '))
fibo = [0,1]

def fibofinder(target, fibo):
    while True:
        if target == fibo[-1]:
            return True
        elif target < fibo[-1]:
            return False
        fibo.append(fibo[-1]+fibo[-2])
        
print(fibofinder(target, fibo))