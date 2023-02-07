'''
5. Write a Program in Python that defines and calls the following user defined functions: 
(i) ADD() – To accept and add data of an item to a binary file ‘events.dat’. Each record of the file 
    is a list [Event_id, Description, Venue, Guests, Cost]. Event_Id, Description, and venue are of str type, 
    Guests and Cost are of int type. /;
(ii)COUNTR() – To read the data from the file events.dat, calculate and display the average number of
    guests and average cost
'''
import pickle
def ADD():
    file = open('events.dat','wb')
    ans = 'y'
    while ans == 'y':
        event_id = int(input('enter the id: '))
        description = input('enter the description: ')
        venue = input('enter the venue: ')
        guests = int(input('enter the number of guests: '))
        cost = int(input('enter the cost: '))
        lst = ([event_id,description,venue,guests,cost])
        pickle.dump(lst,file)
        ans = input('more records? [y/n]: ')

    file.close()

def COUNTR():
    file = open('events.dat','rb')
    try:
        t_cost = 0
        t_guest = 0
        records = 0
        while True:
            reader = pickle.load(file)
            t_cost += reader[4]
            t_guest += reader[3]
            records += 1       
    except EOFError:
        print(f'average cost is: {t_cost/records}')
        print(f'average number of guests: {t_guest/records}')
        file.close()

def display():
    file = open('events.dat','rb')
    try:
        while True:
            reader = pickle.load(file)
            print(reader)

    except EOFError:
        file.close()
while True:
    print('1.add records')
    print('2.count the AVERAGE of GUESTS AND COST')
    print('3.Display')
    print('4.exit')
    choice = int(input('enter your choice : '))
    if choice == 1:
        ADD()
    elif choice == 2:
        COUNTR()
    elif choice == 3:
        display()
    else:
        break