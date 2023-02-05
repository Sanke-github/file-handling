'''
Q8. Give any one point of difference between a binary file and a csv file. Write a Program in Python that defines and calls
the following user defined functions:
(i) add() – To accept and add data of a student to a CSV file ‘stud.csv’. Each record consists of a list with field elements as
admno, sname and per to store admission number, student name and percentage marks respectively.
(ii) search()- To display the records of the students whose percentage is more than 75.
'''

# 1. binary files are stored in binary format wheras csv is stored in plain text format
# 2. binary files requires specialised softwares to commit changes but in case of csv files, changes can take place
#    in the text editor itself

import csv 

def add():
    file = open('stud.csv','w')
    writer = csv.writer(file)
    writer.writerow(['f_id','f_name','fprice'])
    ans = 'y'
    list = []
    while ans == 'y':
        admid = int(input('enter admission id: '))
        name = input('enter student name: ')
        percentage = int(input('enter  percentage: '))
        ans = input('more records? ')
        lst = ([admid,name,percentage])
        list.append(lst)
    writer.writerows(list)
    file.close()

def search():
    file = open('stud.csv','r',newline = '\n')
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        if int(i[2]) >= 75:
            print(i)
    file.close()

while True:
    print('1.add records')
    print('2.search')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        add()
    elif ch == 2:
        search()
    else:
        break
