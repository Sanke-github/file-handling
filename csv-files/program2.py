'''Question: Write a menu-driven program to do the following:
(a) To create a csv file having employee details(name, id, and salary).
(b) Search the record of the employee with salary in the range of 10000-50000. Extract this data and add the value(s) to a new csv file created within the function.
(c) Display the old and the new file'''
import csv

def create():
    file = open("employees.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow(["Name", "ID", "Salary"])
    ans = 'y'
    while ans == 'y':
        name = input("Enter employee name : ")
        id = input("Enter employee ID: ")
        salary = input("Enter employee salary: ")
        writer.writerow([name, id, salary])
        ans = input("more records? [y/n] : ")
    print("Employee details saved to 'employees.csv'.")

def display_old():
    file =  open("employees.csv", "r") 
    new_file = open('results.csv','r')
    new_reader = csv.reader(new_file)
    reader = csv.reader(file)
    print("the old file is :")
    for row in reader:
        print(row)

def display_new():
    new_file = open('results.csv','r')
    new_reader = csv.reader(new_file)
    print("the new file is :")
    for row in new_reader:
        print(row)

def search():
    file =  open("employees.csv", "r")
    reader = csv.reader(file)
    new_file =  open("results.csv", "w", newline="")
    writer = csv.writer(new_file)
    writer.writerow(["Name", "ID", "Salary"])
    next(reader)
    count = 0
    for row in reader:
        if row[2] == '':
            continue
        if 10000 <= int(row[2]) <= 15000:
            print(row[2])
            count += 1
            writer.writerow(row)
    print(f"total number of employees with salary between 10k and 15k are {count}")
    print("Search results saved to 'results.csv'.")


while True:
    print("Menu:")
    print("1. Create employee file")
    print("2. Display employee file (new) ")
    print("3. Display employee file (old)")
    print("4. Search employee file")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create()
    elif choice == "2":
        display_new()
    elif choice == "3":
        display_old()
    elif choice == "4":
        search()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
