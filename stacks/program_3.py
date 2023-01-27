'''Write a function in Python PUSH(Arr),where Arr is a list of numbers, from this list 
push all even numbers into a stack implemented by using a list. Display the stack if it has 
at least one element, otherwise display “stack empty” message. 
>>> li=[1,6,89,100,25,29] 
>>> push(li)  
Stack elements after push operation : [100, 6] '''
def push(arr):
    lst = []
    for i in arr:
        if i%2 == 0:
            lst.append(i)
        else:
            continue
    lst.reverse()
    print(f'Stack elements after push operation :\n{str(lst)}')

list=[1,6,89,100,25,29]             
push(list)