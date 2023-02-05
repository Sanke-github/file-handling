'''
Q4. The scores and ranks of three students of a school level programming competition is given as:
[Name, Marks, 'Rank']
['Sheela', 450, 1]
['Rohan', 300, 2]
['Akash', 260, 3]
Write a program to do the following:
(i) Create a csv file (results.csv) and write the above data into it.
(ii) To display all the records present in the CSV file named 'results.csv'.
'''

import csv
def add():
    file = open('results.csv','w')
    first = ['Sheela', 450, 1]
    second = ['Rohan', 300, 2]
    third = ['Akash', 260, 3]
    lst = ([first,second,third])
    writer = csv.writer(file)
    writer.writerows(lst)
    file.close()
def read():
    file = open('results.csv','r',newline = '\n')
    reader = csv.reader(file)
    for i in reader:
        print(i)
    file.close()
add()
read()