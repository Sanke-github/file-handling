#A binary file “employees.dat” has structure [empid, empname, age, department]
#a. Write a user defined function CreateEmployee() to input the data to a record and add to
#employee.dat
#b. Write a function CountRec(department) in Python which accepts the Department of the
#employee as the parameter and count and return the number of employees in that
#department
import pickle
def display():
    file = open('employee.dat','rb+')
    stu = {}
    try:
        while True:
            fin = pickle.load(file)
            print(fin)
    except EOFError:
        pass

def createEmployee():
    file = open('employee.dat','rb+')
    stu = {}
    ans = 'y'
    while ans == 'y':
        stu['empid'] = int(input("enter id : "))
        stu['empname'] = input("enter name : ")
        stu['age'] = int(input("enter age : "))
        stu['department'] = input("enter department")
        ans = input('more records ? : ')
        pickle.dump(stu,file)
    
    file.close()
    
def countrec():
    file = open('employee.dat','rb+')
    count = 0
    d = input("enter department : ")
    try:
        while True:
            fin = pickle.load(file)
            if fin['department'] == d:
                count += 1
    except EOFError:
        print("number of departments = ",count)
        file.close()


while True:
    print('1.add records')
    print('2.count the number of employees in each dept')
    print('3.Display')
    print('4.exit')
    choice = int(input('enter your choice : '))
    if choice == 1:
        createEmployee()
    elif choice == 2:
        countrec()
    elif choice == 3:
        display()
    else:
        break