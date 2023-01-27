''' A list Customer contains n number of records in the format [Customer_name,Phone_number,City]
Write a Menu driven pgm that defines and calls the following user defined functions to perform given operations on stack named Stack:
(i) Push_element()- To push an object containing name and Phone number of customers who live in Goa into stack
(ii)Pop_element()- To pop objects from the stack and display them. Display "Stack Empty" when there are no element in stack'''

Customer=[]
Stack=[]
def Push_element():
    n = int(input("Enter number of customers:"))
    for i in range(n):
        Customer_name = input("Enter customer name:")
        Phone_number = int(input("Enter Phone number:"))
        City = input("Enter City:")
        Customer = [Customer_name,Phone_number,City]
        if Customer[2] == 'Goa':
            stk = [Customer[0],Customer[1]] 
            Stack.append(stk)  
    print("Stack is:", Stack)

def Pop_element():
    if Stack == []:
        print("STACK EMPTY")
    else:
        print('Popped elements are:')
        for i in range(len(Stack)):
            print(Stack.pop())
        print('Stack after pop:', Stack)

while True:
    print("MENU \n 1. Push \n 2. Pop \n 3. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1: 
        Push_element()
    elif ch == 2:
        Pop_element()
    elif ch == 3:
        break
    else:
        print("Invalid input")
        
       
    

