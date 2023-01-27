'''Write a Program in Python that defines and calls the following user
defined functions:
(i) add() – To accept and add data of an employee to a CSV
file ‘furdata.csv’. Each record consists of a list with field
elements as fid, fname and fprice to store furniture
id, furniture name and furniture price respectively.
(ii) search()- To display the records of the furniture whose
price is more than 10000.'''

import csv
def add():
    file = open('furdata.csv','w')
    writer = csv.writer(file)
    ans = 'y'
    writer.writerow(['furniture id','furniture name','furniture price'])
    
    while ans == 'y':
        fid = int(input('enter the the furniture id : '))
        fname = input('enter the furniture name : ')
        fprice = int(input('enter the furiture price : '))
        lst = ([fid,fname,fprice])
        writer.writerow(lst)
        ans = input('more records? [y/n]')
    file.close()
def search():
    file = open('furdata.csv','r',newline = '\n')
    reader = csv.reader(file)
    next(reader,None)
    for i in reader:
        if int(i[2]) >= 10000:
    print(f'furnitures costing more than 10k is {i}')
    file.close()
def display():
    file = open('furdata.csv','r',newline = '\n')
    reader = csv.reader(file)
    for i in reader:
        print(i)
    file.close()
    
while True:
    print('1.add records')
    print('2.search records')
    print('3.display')
    print('4.exit')
    choice = int(input('enter choice 1-3 : '))
    if choice == 1:
        add()
    elif choice == 2:
        search()
    elif choice == 3:
        display()
    else:
        break
    
