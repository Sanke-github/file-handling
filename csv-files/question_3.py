'''
Q3. Rohan is making a software on "Countries & their Capitals" in which various records are to be stored/retrieved in
CAPITAL.CSV data file. It consists some records(Country & Capital). Help him to define and call the following user
defined functions:
(i) AddNewRec(Country, Capital) - To accept and add the records to a CSV file "CAPITAL.CSV". Each record consists of
a list with field elements as Country and Capital to store country name and capital name respectively.
(ii) ShowRec0 - To display all the records present in the CSV file named “CAPITAL.CSV”.
'''

import csv

def AddNeWRec(country,capital):
    file = open('CAPITAL.csv','a')
    writer = csv.writer(file)
    lst = ([country,capital])
    writer.writerow(['Country','Capital'])
    writer.writerow(lst)
    file.close()

def ShowRec():
    file = open('CAPITAL.csv','r',newline = '\n')
    reader = csv.reader(file)
    header = next(reader)
    for i in reader:
        if i != header:
            print(i)
    file.close()

while True:
    print('1.add records')
    print('2.display')
    print('3.exit')
    ch = int(input('enter choice: '))
    if ch == 1:
        lst = []
        country = input('enter country: ')
        capital = input('enter its capital: ')
        AddNeWRec(country,capital)
    elif ch == 2:
        ShowRec()
    else:
        break