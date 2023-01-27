'''Write a function in Python PUSH(phonebook),where phonebook is a dictionary of phone 
book(name and mobile numbers), from this dictionary push only phone numbers having 
last digit is greater than 5 to a stack implemented by using list and also display the stack if 
it has at least one element, otherwise display “stack empty” message. 
>>> phonebook={9446789123:"Ram",8889912345:"Sam",7789012367:"Sree"} 
>>> push(phonebook) 
elements after push operation : [7789012367, 8889912345] 
'''

def create():
    phonebook = {}
    ans = 'y'
    while ans == 'y':
        name = input('enter name : ')
        mobile_no = input('enter mobile number : ')
        phonebook[mobile_no] = name
        ans = input('more records? [y/n]: ')
    print(f'dictionary is: \n{phonebook}')
    return phonebook

def push():
    stk = []
    empty = True
    dict = create()
    for i in dict.keys():
        if int(i[-1]) > 5:
            stk.append(i)
            empty = False
    print(f'Stack elements after push operation : \n{stk}')
    if empty == True:
        print('\nunderflow')
push()
