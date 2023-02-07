'''
3. A binary file “Book.dat” has structure [BookNo, Book_Name, Author, Price]. 
Write a Program in Python that defines and calls the following user defined functions: 
(i) CreateFile() – To input data of books and add to ‘Book.dat’. 
(ii) CountRec(Author) – To accept the Author name as parameter. Count and return number of books by the given Author 
that are stored in the binary file “Book.dat”.
'''
import pickle
def Createfile():
    file = open('Book.dat','wb')
    ans = 'y'
    while ans == 'y':
        bookno = int(input('enter the book number: '))
        book_name = input('enter the book name: ')
        author = input('enter the author: ')
        price = int(input('enter the price: '))
        lst = ([bookno,book_name,author,price])
        ans = input('more records?[y/n] : ')
        pickle.dump(lst,file)
    file.close()

def Countrec(author):
    file = open('Book.dat','rb')
    try:
        count = 0
        while True:
            reader = pickle.load(file)
            if str(reader[2]) == author:
                count += 1
                print(reader)
    except EOFError:
        file.close()
        print(f'number of books by author is {count}')

def start():
    print('1.add')
    print('2.display')
    print('3.exit')
    ch = int(input('enter your choice: '))
    if ch == 1:
        Createfile()
    elif ch == 2:
        Countrec('rick')
    else:
        exit()
    
    start()
start()