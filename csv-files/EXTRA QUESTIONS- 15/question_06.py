'''
Q6. Write a Program in Python that defines and calls the following user defined functions:
(i) add() – To accept and add data of an employee to a CSV file ‘furdata.csv’. Each record consists of a list with field
elements as fid, fname and fprice to store furniture id, furniture name and furniture price respectively.
(ii) search()- To display the records of the furniture whose price is more than 10000.
'''

import csv 

def add():
    file = open('furdata.csv','w')
    writer = csv.writer(file)
    writer.writerow(['f_id','f_name','fprice'])
    ans = 'y'
    list = []
    while ans == 'y':
        eid = int(input('enter furniture id: '))
        name = input('enter furniture name: ')
        price = int(input('enter furniture price: '))
        ans = input('more records? ')
        lst = ([eid,name,price])
        list.append(lst)
    writer.writerows(list)
    file.close()

def search():
    file = open('furdata.csv','r',newline = '\n')
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        if int(i[2]) >= 10000:
            print(i)
    file.close()

def start():
    print('1.add records')
    print('2.search')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        add()
    elif ch == 2:
        search()
    else:
        'record not found'
    start()
start()