'''Write a function in Python PUSH(Arr),where Arr is a list of numbers, From this list 
push all numbers divisible by 5 in to a stack implemented by using a list. Display the stack 
if it has at least one element, otherwise display appropriate error message. 
>>> li=[10,2,5,6,15,30] 
>>> push(li) 
Stack elements: [30, 15, 5, 10]'''
def push(arr):
    stk = []
    empty = True
    for i in arr:
        if i%5 == 0:
            stk.append(i)
            empty = False
        else:
            continue
    stk.reverse()
    print(f'Stack elements: \n{str(stk)}')
    if empty == True:
        print('\nUNDERFLOW ERROR\n')

li=[10,2,5,6,15,30]
push(li)