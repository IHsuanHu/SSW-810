'''
Problem 1 
The German mathematician Gottfried Leibniz developed the following method 
to approximate the value of π: 
𝜋/4 = 1-1/3+1/5-1/7.... 
 
Write a program that allows the user to specify the number of 
iterations used in this approximation and that displays the 
resulting value of 𝜋. 
'''


iterations = int(input('The number of iterations: '))
if iterations <= 0: # edge case
    print('Error')
else:
    
    sign = 1        # To determine plus or minus sign
    start = 1       # The first iteration number
    value = 0       # Value of 𝜋/4
    for i in range(iterations):
        value += ((start/(2*(i+1)-1))*sign) # Make denominator become 1 3 5 7
        sign = -sign
        
    print('The approximate value of 𝜋 is', value*4)


'''
Problem 2 
Write a program that receives a series of numbers from the user and allows 
the user to press the Enter key to indicate that he or she is finished 
providing inputs. After the user presses the Enter key, the program should 
print the sum of the numbers and their average. 
'''

seriesnumber = input('Please input the numbers with period or whitespace to split: ')
temp = ''                                            # store a number
result = []
for item in seriesnumber:
    if item.isdigit() or item == '.' or item == '-': # remove all the alphabet 
        temp += item
    else:
        if temp:                                     # before going to next number add to result
            result.append(float(temp))
            temp = ''
if temp:                                             # add the last number
    result.append(float(temp))

print('The sum of the numbers is', sum(result))
print('The average is', sum(result)/len(result))




'''
Problem 3 
Teachers in most school districts are paid on a schedule that provides a 
salary based on their number of years of teaching experience. 
For example, a beginning teacher in the Lexington School District might be 
paid $30,000 the first year. For each year of experience after this first 
year, up to 10 years, the teacher receives a 2% increase over the preceding 
value. Write a program that displays a salary schedule, in tabular format, 
for teachers in a school district. The inputs are the starting salary, 
the percentage increase, and the number of years in the schedule. Each row 
in the schedule should contain the year number and the salary for that year. 
'''


from tabulate import tabulate
startupsalary = input('Please enter your startup salary:')
startupsalary = [i for i in startupsalary if i.isdigit()] # remove all non-digit
startupsalary = int(''.join(startupsalary))    # make all the digits in list become a number
setofyearsalary = []                           # collect the group of year & salary
for i in range(1, 11):                         # execute 10 tiimes because of 10 years
    result = list(str(startupsalary))          # for adding ','
    if len(result) > 3:                        # if digit < 3 no need to add ','
       for j in range(len(result)-3, -1, -3):  # insert ',' from back to front
           if j == 0:                          # don't let ',' become first charactor
               break
           result.insert(j, ',')
    result.insert(0,'$')
    result = ''.join(result)
    setofyearsalary.append([i,result])
    startupsalary = int(startupsalary*1.02)
print(tabulate(setofyearsalary, headers = ['Year', 'Salary'])) # make in tabular format


'''
Problem 4 
In the game of Lucky Sevens, the player rolls a pair of dice. If the dots 
add up to 7, the player wins $4; otherwise, the player loses $1. Suppose that,
to entice the gullible, a casino tells players that there are lots of ways 
to win: (1,6), (2,5), and so on. A little mathematical analysis reveals that 
there are not enough ways to win to make the game worthwhile; however, because
many people’s eyes glaze over at the first mention of mathematics, your 
challenge is to write a program that demonstrates the futility of playing 
the game. Your program should take as input the amount of money that the 
player wants to put into the pot and play the game until the pot is empty. 
At that point, the program should print the number of rolls it took to break 
the player, as well as maximum amount of money in the pot. 
'''

import random
money = input('Please input your money: ')
money = [i for i in money if i.isdigit()]   # remove all the non-digit element
money = int(''.join(money))
maxmoney = money 
count = 0                                   # count the rolls
while money > 0:                            # keep playing while player has money
    dice = (random.randint(1,6),random.randint(1,6))
    if sum(dice) == 7:
        money += 4
    else:
        money -= 1
    count += 1
    maxmoney = max(maxmoney, money)          # get maximum money in the pot
print('The time of rolls is', count, 'times')
print('The maximum amount of money in the pot is $'+ str(maxmoney))




