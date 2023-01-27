'''a binary file emp.dat has structure [employee_id,emp_name]write a function 
    delrec(id) so that it would read the contents and delete the details of those whose employee id
    is passed as arguement'''
import pickle
def create():
    file = open('emp.dat','wb')
    try:
        ans = 'y'
        while ans == 'y':
            emp_id = int(input('enter the employee id : '))
            emp_name = input('enter the name of the employee : ')
            lst = ([emp_id,emp_name])
            pickle.dump(lst,file)
            ans = input('more records? [y/n] : ')

    except EOFError:
        file.close()

def delrec(id):
    file = open('emp.dat','rb')
    found = False
    try:
        while True:
            t_file = pickle.load(file)
            pos = file.tell()
            if t_file[0] == id:
                del t_file
                found = True
                file.seek(pos)
    except EOFError:
        file.close()
    if found == False:
        print('employee not found ')
    else:
        print('record succesfully deleted')
def display():
    file = open('emp.dat','rb')
    try:
        reader = pickle.load(file)
        print(reader)
    except EOFError:
        file.close()
while True:
    print('1.add records')
    print('2.delete records')
    print('3.display records')
    print('4.exit')
    choice = int(input('enter choice: '))
    if choice == 1:
        create()
    elif choice == 2:
        some_id = int(input('enter employee id: '))
        delrec(some_id)
    elif choice == 3:
        display()
    else:
        break