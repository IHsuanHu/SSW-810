# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:32:45 2022

@author: user
"""

#1
filename = input('Input a file: ')
file = open(filename, 'r')
import pandas as pd
res = []
for i in file:
    res.append(i.split())
file.close()
df1 = pd.DataFrame(res, columns= ['Employee', 'Salary', 'Year', 'Gender'])
print(df1)

#2
malesalary = []
femalesalary = []
maleyears = []
femaleyears = []
for i in res:
    if i[3] == 'M':
        malesalary.append(int(i[1]))
        maleyears.append(int(i[2]))
    else:
        femalesalary.append(int(i[1]))
        femaleyears.append(int(i[2]))

import statistics as st

print('The maximum salary of male is', max(malesalary), 'thousand dollars, the mean is', 
      st.mean(malesalary), ', and the standard deviation is', st.stdev(malesalary))
print('The maximum salary of female is', max(femalesalary), 'thousand dollars, the mean is', 
      st.mean(femalesalary), ', and the standard deviation is', st.stdev(femalesalary))

#3
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'Gender': ['M']*len(malesalary) + ['F']*len(femalesalary),
                     'Salary': malesalary + femalesalary})

grouped = data.groupby('Gender')
print(grouped.describe())
grouped.boxplot()
plt.show()

#4
totalmalesalary = sum(malesalary)
totalfemalesalary = sum(femalesalary)


import seaborn as sns
import matplotlib.pyplot as plt
txtLabels = ['Male', 'Female']
fractions = [totalmalesalary, totalfemalesalary]
plt.pie(fractions, labels=txtLabels,autopct='%1.1f%%', shadow=True, startangle=90,
colors=sns.color_palette('muted') )
plt.axis('equal')
plt.show()

#5
import numpy as np
import matplotlib.pyplot as plt

plt.plot(malesalary, maleyears,".", color= 'blue')
plt.plot(femalesalary, femaleyears,".", color= 'red')
plt.title('Male & Female')
plt.xlabel('Salary')
plt.ylabel('Years')
plt.show()


#6
import matplotlib.pyplot as plt
salary = malesalary + femalesalary
plt.hist(salary, bins=5) 
plt.xlabel("Salary") 
plt.ylabel("Frequency") 
plt.show()
print('Based on the histogram, it is not a normal distrubution')

#7
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
x = malesalary + femalesalary
y = maleyears + femaleyears
df = pd.DataFrame({'Salary':x, 'Years':y})
sns.regplot('Salary', 'Years', data=df)
plt.show()

#8
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import statsmodels.api as sm 
model = sm.OLS(y,x).fit()    #OLS: Ordinary least square 
predictions = model.predict(x) #make the predictions by the model 
print (model.summary())

print('For the R-squared is 0.848, and it means that the salary is' 
      +' highly relative to the years of work. The company is right.')

