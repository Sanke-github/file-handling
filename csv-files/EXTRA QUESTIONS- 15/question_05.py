'''
Q5. Write a Program in Python that defines and calls the following user defined functions:
(i) add() – To accept and add data of an employee to a CSV file ‘employee.csv’. Each record consists of a list with field
elements as eid, name and salary to store employee id, employee name and employee salary respectively.
(ii) search()- To display the records of the employee whose salary is more than 40000.
'''
import csv

def add():
    file = open('employee.csv','w')
    writer = csv.writer(file)
    writer.writerow(['e_id','e_name','salary'])
    ans = 'y'
    list = []
    while ans == 'y':
        eid = int(input('enter id: '))
        name = input('enter name: ')
        salary = int(input('enter salary: '))
        ans = input('more records? ')
    lst = ([eid,name,salary])
    list.append(lst)
    writer.writerows(list)
    file.close()

def search():
    file = open('employee.csv','r',newline = '\n')
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        if int(i[2]) >= 40000:
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