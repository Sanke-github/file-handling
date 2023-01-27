'''write a function to search and display details of all trains, whose destination is "delhi" from a binary 
'TRAIN.DAT'. Assuming the binary file is containing the objects in the following format : 
Train = {'Tno':____,'from':_____,'to':______}
'''
import pickle
def create():
    file = open('TRAIN.dat','ab')
    d = {}
    ans = 'y'
    try:
        while ans == 'y':
            d['Tno'] = int(input('enter train number : '))
            d['From'] = input('enter the starting point : ')
            d['destination'] = input('enter the destination of the train : ')
            pickle.dump(d,file)
            ans = input('more records [y/n] : ')
    except EOFError:
        file.close()

def search():
    file = open('TRAIN.dat','rb')
    found = False
    try:
        while True:
            d = pickle.load(file)
            pos = file.tell()
            if d['destination'] == 'delhi':
                print(d)
                found = True
    except EOFError:
        file.close()
    if found == True:
        print('the details of the delhi train is printed')
    else:
        print('not found')

create()
search()
