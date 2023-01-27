'''write a menu driven program that has the following functions:
create() - add data to student.csv
search() search records whose fees is above 20k and below 40k and add them to a new file final.csv
display() - to dispay the old and new records '''


import csv
def create():
    # open file to write in
    file = open('Student.csv','w')
    writer = csv.writer(file) 
    writer.writerow(['Rollno','Name','Subjects','fees'])
    ans = 'y'
    count = 0
    # loop to add multiple records
    while ans == 'y':
        Rollno = int(input('enter your roll number : '))
        Name = input('enter your name : ')
        Subjects= int(input("enter the number of subjects : "))
        fees = int(input("enter your fees : "))
        lst = [Rollno,Name,Subjects,fees]
        writer.writerow(lst)
        count += 1
        print(f'\n{count} records added')
        # check if more records need to be added

        ans = input('\nmore records? [y/n] : ')
def Search():
    # open the file in read mode
    file = open('student.csv','r',newline = '\n')
    final_file = open('final.csv','w',newline = '\n')
    
    # open the file to write the filtered records
    writer = csv.writer(final_file,delimiter = ',')
    
    # write the header row
    writer.writerow(['Rollno','Name','Subjects','fees'])
    reader = csv.reader(file)
    count = 0
    count_new = 0
    sum_    = 0
    # skipping the header row
    next(reader,None)
    for row in reader:
        count += 1
        sum_  += int(row[3])
        if 20000 <= int(row[3]) <= 40000:
            record = row
            count_new += 1
            writer.writerow(record)
    final_file.close()
    print("average fee : ",round(sum_/count,2))
    print("total number of students with fees between 20k and 40k are :",count_new)
    file.close()
    
def display_old():
    file = open('student.csv','r',newline = '\n')
    reader = csv.reader(file)
    
    # loop through the records and display
    for records in reader:
        print(records)
    file.close()
    
def display_new():
    file = open('final.csv','r',newline = '\n')
    reader = csv.reader(file)
    for records in reader:
        print(records)
        
while True:
    print('\n\t MENU BAR\n')
    print('1. add new records ')
    print('2. search and update records')
    print('3. display old records')
    print('4. display new records')
    print('5. exit\n')
    choice = int(input("enter your choice 1-5: "))
    if choice == 1:
        create()
    if choice == 2:
        Search()
    if choice == 3:
        display_old()
    if choice == 4:
        display_new()
    if choice == 5:
        break
