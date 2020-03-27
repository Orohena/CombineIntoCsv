#Import all library that will be needed
import os
import glob
import csv
import pandas as pd


#Change directory to the one with the results // Will need to ask user instead of hard coding
dir1 = os.chdir('/Users/Orohena/Desktop/Data_CombineIntoCsv/Results_csv/Folder1')
print(os.getcwd())
file_list = [i for i in glob.glob('*.{}'.format('csv'))]
print(file_list)

filename1 = file_list[0]
filename2 = file_list[1]
filename3 = file_list[2]

data1 = pd.read_csv(file_list[0])
data2 = pd.read_csv(file_list[1])
data3 = pd.read_csv(file_list[2])

df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})
print(df1)
