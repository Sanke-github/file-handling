'''Write a function in Python PUSH(mydict,maxsize=5),where mydict is a dictionary 
of phone book(name and mobile numbers), from this dictionary push all phone numbers 
to a stack implemented by using list and also the display the numbers that Display the 
stack if it has at least one element, otherwise display “stack empty” message 
>>>mydict={1234567890:"Shyam",94567892:"Ram",8657456789012: 
"Karun",9674123789:"Tharun"} 
>>> push(mydict) 
Stack elements after push operation : 
[[1234567890, 94567892, 8657456789012, 9674123789]] '''
def create():
    mydict = {}
    ans = 'y'
    while ans == 'y':
        name = input('enter name : ')
        mobile_no = int(input('enter mobile number : '))
        mydict[mobile_no] = name
        ans = input('more records? [y/n]: ')
    print(f'dictionary is: \n{mydict}')
    return mydict

def push():
    stk = []
    dict = create()
    for i in dict.keys():
        stk.append(i)
    print(f'Stack elements after push operation : \n{stk}')



push()