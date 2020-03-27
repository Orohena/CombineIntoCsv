#Import all library that will be needed
import os
import glob
import csv
import pandas as pd


#Change directory to the one with the results // Will need to ask user instead of hard coding
dir1 = os.chdir('/Users/Orohena/Desktop/Data_CombineIntoCsv/Results_csv/Folder1')
#print(os.getcwd())
file_list = [i for i in glob.glob('*.{}'.format('csv'))]
#print(file_list)

filename1 = file_list[0]
filename2 = file_list[1]
filename3 = file_list[2]

with open(filename1) as f1:
    datalist1 = f1.readlines()

with open(filename2) as f2:
    datalist2 = f2.readlines()

with open(filename3) as f3:
    datalist3 = f3.readlines()

print(datalist1)
print(datalist2)
print(datalist3)

df1 = pd.DataFrame({
    filename1: datalist1,
    filename2: datalist2,
    filename3: datalist3
})
print(df1)

df1.to_csv ('combined.csv', sep='\n')


