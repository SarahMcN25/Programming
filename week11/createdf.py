# This program creates a data frame
# Then use functions to describe it, output to csv file, output to excel file, 
# add sheet to excel file and print out statical information
# Author: Sarah McNelis

import pandas as pd 

listdata = [
    ['John', 'math',        23],
    ['John', 'programming', 66],
    ['Mary', 'math',        45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM',        57],
    ['Mark', 'programming', 70],
    ['Mark', 'math',        73],
    ['John', 'Math', ],
    ['John', 'programming', 61],
    ['John', 'programming', 61],
]

df = pd.DataFrame(listdata, columns =['name', 'subject', 'grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))

# writing to csv file
csvFilename =  'grades.csv'
df.to_csv(csvFilename)

# if want to write to another depository set path
#path = "./data/"
#csvFilename = path + 'grades1.csv'
#df.to_csv(csvFilename)

# writing to excel file
excelFilename = 'grades.xlsx'       #path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

# writing new sheet in excel file
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name='summary')

mean = df.describe().loc['mean', 'grade']
print(mean)
mean = df['grade'].mean()
print(mean)