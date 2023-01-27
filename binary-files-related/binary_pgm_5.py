#A binary file “discovery.dat” has a structure:
#[scien_name,discovery,yearofDiscovery,yearofbirth]
#Write a function display(scien_name) in python that accepts the name of a scientist as scientist_name and
# returns the discovery with the year of discovery

import pickle
def display():
    file = open('discovery.dat','rb')
    try:
        while True:
            fin = pickle.load(file)
            print(fin)
    except EOFError:
        pass

def create():
    file = open('discovery.dat','wb')
    ans = 'y'
    while ans == 'y':
        scientist_name = input("enter scientist name : ")
        discovery= input("discovery : ")
        year= int(input("year of discovery : "))
        yearofbirth = int(input("year of birth: "))
        lst = ([scientist_name,discovery,year,yearofbirth])
        ans = input('more records ? [y/n]: ')
        pickle.dump(lst,file)
    
    file.close()

def display(science_name):
    file = open('discovery.dat','rb')
    try:
        while True:
            fin = pickle.load(file)
            if fin[0] == science_name:
                print(fin[1])
                print(fin[2])
            
    except EOFError:
        file.close()
while True:
    print('1.add records')
    print('2.Display')
    print('3.exit')
    choice = int(input('enter your choice : '))
    if choice == 1:
        create()
    elif choice == 2:
        sci = input('enter the scientists name to display : ')
        display(sci)
    else:
        break
