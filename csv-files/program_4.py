'''write a program to write a nested list into a csv file in one go.After writing the csv file,
     read an display the content with pipe(|) as delimiter'''
import csv
def create():
    file = open('sample.csv','w')
    writer = csv.writer(file,delimiter='|')
    writer.writerow(['bookname','book_id','price'])
    lst = []
    ans = 'y'
    while ans == 'y':
        bookname = input('enter the book name : ')
        book_id = int(input('enter the book id : '))
        price = int(input('enter the price of the book : '))
        rec = ([bookname,book_id,price])
        lst.append(rec)
        ans = input('more records? [y/n] : ')

    print(f'writing the nested list: \n{lst}\ninto the file...')
    writer.writerows(lst)
    print(f'{len(lst)} records succesfully added\n')

    file.close()
def display():
    file = open('sample.csv','r',newline='\n')
    reader = csv.reader(file)
    for i in reader:
        print(i)
while True:
    print('1.create records')
    print('2.display')
    print('3.exit')
    choice = int(input('enter choice 1-3 : '))
    if choice == 1:
        create()
    elif choice == 2:
        display()
    else:
        break
        display()
    else:
        break
