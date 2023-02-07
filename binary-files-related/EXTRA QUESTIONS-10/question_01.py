'''
1. A binary file data.dat needs to be created  with data written it in the form of Dictionaries.

Write the following functions in python to accommodate the data and manipulate it. 
a) A function insert() that creates the data.dat file in your system and writes the three dictionaries. 
b) A function read() that reads the data from the binary file and displays the dictionaries whose age is 16.
'''
import pickle
def insert():
    dict = {}
    file = open('data.dat','wb')
    for i in range(3):
        dict['Rollno'] = int(input('enter roll number: '))
        dict['name'] = input('enter name: ')
        dict['age'] = int(input('enter age: '))
        pickle.dump(dict,file)
    file.close()

def read():
    file = open('data.dat','rb')
    try:
        while True:
            reader = pickle.load(file)
            if reader['age'] == 16:
                print(reader)
    except EOFError:
        file.close()
    
def start():
    print('1.add')
    print('2.display')
    print('3.exit')
    ch = int(input('enter your choice: '))
    if ch == 1:
        insert()
    elif ch == 2:
        read()
    else:
        exit()
    
    start()
start()