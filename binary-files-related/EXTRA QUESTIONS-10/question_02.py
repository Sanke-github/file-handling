'''2. Write a Program in Python that defines and calls the following user defined functions:
INSERT() – To create the “data.dat” file in your system and add the student’s Roll number, Name and Age in it. 
READ() – To search and display the data of the students whose age is above 16.
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
            if reader['age'] >= 16:
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