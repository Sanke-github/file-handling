'''Q1. Write a Program in Python that defines and calls the following user defined functions:
ADD() – To accept and add data of a teacher to a CSV file ‘teacher.csv’. Each record consists of a list with field elements
as tid, name and mobile to store teacher id, teacher name and teacher mobile number respectively.
COUNT() – To count the number of records present in the CSV file named ‘teacher.csv’.
'''

import csv 
def ADD():
    file = open('teacher.csv','w')
    writer = csv.writer(file)
    writer.writerow(['t_id','name','mobile_number'])
    ans = 'y'
    while ans ==  'y':
        id = int(input('enter the teacher id: '))
        name = input('enter the name of the teacher: ')
        mob = int(input('enter mobile number: '))
        lst = ([id,name,mob])
        writer.writerow(lst)
        ans = input('more records? ')
    file.close()
    
def COUNT():
    file = open('teacher.csv','r',newline = '\n')
    reader = csv.reader(file)
    count = 0
    next(reader)
    for i in reader:
        count += 1
    print(f'the number of records : {count}')

while True:
    print('1.add records')
    print('2.count rows')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        ADD()
    elif ch == 2:
        COUNT()
    else:
        break