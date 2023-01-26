#A binary file “STUDENT.DAT” has structure [admission_number, Name, Percentage].
#Write a function countrec() in Python that would read contents of the file “STUDENT.DAT” and
#display the details of those students whose percentage is above 75. Also display number of students
#scoring above 75%.
import pickle
file = open('student.dat','ab+')
stu = {}

def write():
    try:
        ans = 'y'
        while ans == 'y':
            stu['admission_no'] = int(input("enter admission number : "))
            stu['Name'] = input("enter name : ")
            stu['percentage'] = int(input('enter percentage : '))
            pickle.dump(stu,file)
            ans = input('more records? [y/n] : ')
    except EOFError:
        pass

def display():
    file = open('student.dat','rb')
    try:
        while True:
            fin = pickle.load(file)
            print(fin)

    except EOFError:
        pass

def countrec():
    file=open("student.dat",'rb')
    num = 0
    try:
      while True:
         rec=pickle.load(file)
         if rec['percentage'] >= 75:
            num = num + 1
            print(num)
    except EOFError:
        file.close()
    return num

while True:
    print('1.add records')
    print('2.count the number of students who scored above 75')
    print('3.Display')
    print('4.exit')
    choice = int(input('enter your choice : '))
    if choice == 1:
        write()
    elif choice == 2:
        countrec()
    elif choice == 3:
        display()
    else:
        break