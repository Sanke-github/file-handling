'''Write a Program in Python that defines and calls the following user defined functions:
(a) ADD() – To accept and add data of an employee to a CSV file ‘record.csv’. Each record
consists of a list with field elements as empid, name and salary to store employee id, employee
name and employee salary respectively.
(ii) (b) COUNTR() – To count the number of records present in the CSV file ‘record.csv’.'''

import csv
def add():
    file = open('record.csv','w')
    writer = csv.writer(file)
    writer.writerow(['emp_id','emp_name','salary'])
    ans = 'y'
    while ans == 'y':
        emp_id = int(input('enter employee id : '))
        emp_name = input('enter employee name : ')
        salary = int(input('enter the salary : '))
        lst = ([emp_id,emp_name,salary])
        writer.writerow(lst)
        ans = input('more records? [y/n] : ')
    file.close()
def countr():
    file = open('record.csv','r',newline = '\n')
    reader = csv.reader(file)
    count = 0
    next(reader,None)
    for i in reader:
        print(i)
        count += 1
    print(f'number of records in record.csv : {count}')

while True:
    print('1.add records')
    print('2.count the number of records')
    print('3.exit')
    choice = int(input('enter choice : '))
    if choice == 1:
        add()
    elif choice == 2:
        countr()
    else:
        break