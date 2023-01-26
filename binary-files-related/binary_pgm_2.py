import pickle
d={}
def write_in_file():
    file=open("student.dat",'ab')
    no= int(input("enter number of student:"))
    for i in range(no):
        print("enter details of student",i+1)
        d["roll"]=int(input("enter roll number:"))
        d["name"]=input("enter the name:")
        pickle.dump(d,file)
    file.close()
def display():
    file=open("student.dat",'rb')
    try:
        while True:
            stud=pickle.load(file)
            print(stud)
    except EOFError:
        pass
    file.close()
def search():
    file=open("student.dat",'rb')
    r=int(input("enter the roll number to search:"))
    found=0
    try:
        while True:
            data=pickle.load(file)
            if data["roll"]==r:
                data['roll'] += 2
                print("the roll number=",r,"record found")
                print(data)
                found=1
                break
    except EOFError:
        pass
        file.close()
while True:
    print("Menu \n1.Write in file \n2.Display")
    print("3.Search\n4.Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        write_in_file()
    elif ch==2:
        display()
    elif ch==3:
        search()
    elif ch==4:
        print("Thank you")
        break