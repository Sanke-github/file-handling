'''Q2. Write a Program in Python that defines and calls the following user defined functions:
(i) ADDPROD() – To accept and add data of a product to a CSV file ‘product.csv’. Each record consists of a list with field
elements as prodid, name and price to store product id, employee name and product price respectively.
(ii) COUNTPROD() – To count the number of records present in the CSV file named ‘product.csv’.'''

import csv 
def ADD():
    file = open('products.csv','w')
    writer = csv.writer(file)
    writer.writerow(['prod_id','name','price'])
    ans = 'y'
    while ans ==  'y':
        id = int(input('enter the product id: '))
        name = input('enter the name of the employee: ')
        price = int(input('enter price: '))
        lst = ([id,name,price])
        writer.writerow(lst)
        ans = input('more records? ')
    file.close()
    
def COUNT():
    file = open('products.csv','r',newline = '\n')
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