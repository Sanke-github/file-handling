'''
Q10. Dhirendra is a programmer, who has recently been given a task to write a python code to perform the following CSV
file operations with the help of two user defined functions/modules:
(i) CSVOpen() – To create a CSV file called BOOKS.CSV in append mode containing information of books: Title, Author
and Price.
(ii) CSVRead() – To display the records from the CSV file called BOOKS.CSV where the Book title starts with 'R'.
'''
import csv
def CSVOpen():
    file = open('BOOKS.csv','a')
    writer = csv.writer(file)
    writer.writerow(['Title','Author','Price'])
    ans = 'y'
    while ans == 'y':
        title= input('enter the name of the book: ')
        auth = input('enter the author: ')
        price = int(input('enter the price of the book: '))
        writer.writerow([title,auth,price])
        ans = input('more records? ')
    file.close()

def CSVRead():
    file = open('BOOKS.csv','r',newline = '\n')
    reader = csv.reader(file)               #DictReader is used to access files iterated through dictionaries
    next(reader)
    for i in reader:
        if i[0].startswith('R') or i[0].startswith('r'):
            print(i)
    file.close()

def start():
    print('1.add records')
    print('2.search')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        CSVOpen()
    elif ch == 2:
        CSVRead()
    else:
        exit()
    start()
start()