'''Write a program to create binary file Items.dat to store some details of items such as [itemno,name,price,category]
   write a program to append some records to the binary file  items.dat, created in the previous program
   write a program to modify the price the price of an item in the binary file Items.dat.Get the itemno of the item to be modified from the user

'''

import pickle

def create():
    file = open('Items.dat','wb')
    ans = 'y'
    while ans == 'y':
        itemno = int(input('enter item number : '))
        name = input("enter item name : ")
        price = int(input('enter price : '))
        category = input("enter category : ")
        lst = ([itemno,name,price,category])
        pickle.dump(lst,file)
        ans = input("more records? [y/n] : ")
    file.close()

def add():
    file = open('Items.dat','ab')
    ans = 'y'
    while ans == 'y':
        itemno = int(input('enter item number : '))
        name = input("enter item name : ")
        price = int(input('enter price : '))
        category = input("enter category : ")
        lst = ([itemno,name,price,category])
        pickle.dump(lst,file)
        ans = input("more records? [y/n] : ")
    file.close()


def modify():
    file_b = open('Items.dat','rb+')
    itemno = int(input('which item would you like to modify? : '))
    price = int(input('enter the new price of the modified item : '))
    found = False
    try:
        while True:
            pos = file_b.tell()
            file_t = pickle.load(file_b)
            if file_t[0] == itemno:
                file_t[2] = price
                file_b.seek(pos)
                found = True
                pickle.dump(file_t,file_b)

    except EOFError:
        file_b.close()
        if found == True:
            print('search succesful, record updated')
        else:
            print('vsad not found')

def display_old():
    file = open('Items.dat','rb')
    try:
        while True:
            fin = pickle.load(file)
            print(fin)
    except EOFError:
        file.close()

def delete_particular():
    file = open('Items.dat','rb')
    file_new = open('Itemsnew.dat','wb')
    Item_id = int(input('enter item id to be excluded: '))
    found = False
    try:
        while True:
            file_t = pickle.load(file)
            print(file_t)
            if file_t[0] != Item_id:
                pickle.dump(file_t,file_new)
            else:
                found = True
    except EOFError:
        file.close()
        if found == True:
            print(f'succesfully added records to the file except itemno - {Item_id}')
        else:
            print('item not found')

def display_new():
    file = open('Itemsnew.dat','rb')
    try:
        while True:
            file_t = pickle.load(file)
            print(file_t)
    except EOFError:
        file.close()

while True:
    print('\n\tMENU BAR\n')
    print('1. add records')
    print('2. append records')
    print('3. update and search')
    print('4. delete a particular record ')
    print('5. display records (old)')
    print('6. display records (new)')
    print('6. exit')
    ch = int(input('enter your choice : '))
    if ch == 1:
        create()
    elif ch == 2:
        add()
    elif ch == 3:
        modify()
    elif ch == 5:
        display_old()
    elif ch == 4:
        delete_particular()
    elif ch == 6:
        display_new()
    elif ch == 7:
        break
