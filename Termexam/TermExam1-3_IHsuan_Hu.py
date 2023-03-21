# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:47:48 2022

@author: Hu, I-Hsuan
"""

number = input('Enter a number ')

def rearrange(number):
    temp = sorted([int(i) for i in number])
    
    res = ''
    for i in temp:
        res += str(i)
    return res

print(rearrange(number))
