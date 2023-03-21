# -*- coding: utf-8 -*-
"""
Assignment #2

@author: I-Hsuan Hu
"""
'''
Problem 1 
Write a program to display the Fibonacci sequence up to n-th term. The program should 
prompt the user for the number of terms. 
Hint: a Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 
0 and 1. All other terms are obtained by adding the preceding two terms. 
'''

terms = int(input('Please input the number of Fibonacci sequence term:'))
fibolist = [0,1]            # making a Fibonacci list
if terms <= 0:              # edge case
    print('Error')
elif terms == 1:
    print(fibolist[terms-1])
elif terms == 2:
    print(fibolist[terms-1])
else:
    while terms > len(fibolist):        #keep executing when the length of list is less than the index
        fibolist.append(fibolist[-1]+fibolist[-2]) # summate the last two element in the list
    print(fibolist[-1])                



'''
Problem 2 
The payroll department keeps a list of employee information for each pay period in a text file 
named payroll.txt. The format of each line of the file is as follows: 
 
< name > < hourlywage > < hoursworked > 
 
Write a program that inputs the filename: payroll.txt from the user and prints to the terminal a 
report of the wages paid to the employees for the given period. The report should be in tabular 
format with the appropriate header. Each line should contain an employee’s name, the hours 
worked, and the wages paid for that period. You can find payroll.txt in Assignment #2 on 
Canvas.  
'''

from tabulate import tabulate
f = open('payroll.txt', 'r')
result = []
for i in f:
    result.append(i.split())            # split content in every lines to match headers
f.close()
print(tabulate(result, headers = ['name', 'hours worked', 'wages paid']))





''' 
Problem 3 
Write a program that prompts the user for the names of two text files including: myfile1.txt and 
myfile2.txt. The contents of the first file, myfile1.txt, should be input and written to the second 
file, myfile2.txt. You can find myfile1.txt in Assignment #2 on Canvas.  
'''

file = open('myfile1.txt', 'r')
file2 = open('myfile2.txt', 'w')

for i in file:
    file2.write(i)
file.close()
file2.close()



'''
Problem 4 
Write a program to populate an empty dictionary named myDict (see myDict sample below) 
and check if the values in myDict are prime or not. If a prime number is found, the program 
should print a text message including the corresponding key of the prime number. 
myDict sample: myDict = {“A”: 11, “B”: 4, “C”: 7, “D”: 15, “E”: 1} 
Hint: a natural number is called a prime number (or a prime) if it is greater than 1 and cannot 
be written as the product of two smaller natural numbers. For example, 2, 3, and 5 are prime 
numbers. 
'''
n = int(input('Enter number of elements:'))
myDict = dict()
for i in range(n):
    key = input('Enter key:')
    value = int(input('Enter value:'))
    myDict[key] = value
#myDict = {'A': 11, 'B': 4, 'C': 7, 'D': 15, 'E': 1, 'F': 3, 'G': 23} 
for k, i in myDict.items():
    if int(i) > 1:
        for j in range(2,int(i)):        # 1 is not a prime number, starting from 2 
            if int(i) % j == 0:          # the value divided by the numbers between 2 and the value
                break                    # if remainder is 0, the value is not prime number
            if int(i)-1 == j:            # when the for loop execute to value-1, the value is a prime number  
                print('The key of prime number', i, 'is', k)



'''
Problem 5 
Python’s pow function returns the result of raising a number to a given power. Define a 
function expo that performs this task. The first argument of this function is the number, and the 
second argument is the exponent (non-negative numbers only). You may use either a loop or a 
recursive function in your implementation.  
CAUTION: do not use Python’s ** operator or pow function in this exercise! 
''' 


#solution 1
def expo1(fnum, snum, total):           # (number, exponent, total = 1(base))
    if snum > 0:                        # total start from 1
        total *= fnum
        return expo1(fnum, snum-1, total)
    else:
        return total


#solution 2
def expo2(fnum, snum):              # (number, exponent)
    ret = 1                         # ret is base
    while snum > 0:
        
        if snum % 2 !=0:
            ret *= fnum
            snum -= 1
        else:
            fnum *= fnum
            snum //= 2
    return ret


