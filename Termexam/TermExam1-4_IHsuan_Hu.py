# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:53:27 2022

@author: Hu, I-Hsuan
"""
from collections import defaultdict
import random
student = input('Enter stuent\'s name with space to seperate ')
name = [i for i in student.split()]

stuDict = defaultdict(int)

for i in name:
    stuDict[i] = random.randint(1,100) 

for i, j in stuDict.items():
    if j == max(stuDict.values()):
        
        break
for i, j in stuDict.items():
    if j == max(stuDict.values()):
        print('The second high student\'s name is', i +', and the grade is', j)
        break
