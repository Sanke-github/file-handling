'''Q9. Write a Program in Python that defines and calls the following user defined functions:
(i) INSERTROW() – To accept and insert data of a student to a CSV file ‘class.csv’. Each record consists of a list with field
elements as rollno, name and marks to store roll number, student’s name and marks respectively.
(ii) COUNTD() – To count and return the number of students who scored marks greater than 75 in the CSV file named
‘class.csv’.
'''
import csv

import csv 

def INSERTROW():
    file = open('stud.csv','w')
    writer = csv.writer(file)
    writer.writerow(['student_id','student_name','pecentage'])
    ans = 'y'
    list = []
    while ans == 'y':
        admid = int(input('enter admission id: '))
        name = input('enter student name: ')
        marks = int(input('enter  marks: '))
        ans = input('more records? ')
        lst = ([admid,name,marks])
        list.append(lst)
    writer.writerows(list)
    file.close()

def COUNTD():
    file = open('stud.csv','r',newline = '\n')
    reader = csv.reader(file)
    next(reader)
    count = 0
    for i in reader:
        if int(i[2]) >= 75:
            count += 1
    file.close()
    print('number of students with percentage greater than 75 is:',count)
while True:
    print('1.add records')
    print('2.search')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        INSERTROW()
    elif ch == 2:
        COUNTD()
    else:
        break
