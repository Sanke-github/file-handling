stk = []
def is_empty(stk):
    if len(stk) == 0:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk) -1

def pop(stk):
    if is_empty(stk):
        print('underflow')
    else:
        ele = stk.pop()
        print(f'popped element is {ele}')
def peek(stk):
    if is_empty(stk):
        print('underflow')
    else:
        top = len(stk) - 1
        print(f'topmost element is : {stk[top]}')
def display(stk):
    if is_empty(stk):
        print('underflow')
    else:
        top = len(stk) - 1
        print(stk[top],'<----top')
        for i in range(top-1,-1,-1):
            print(stk[i])
stack = []
while True:
    print('\n\tMENU BAR\n')
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display')
    choice = int(input('enter your choice : '))
    if choice == 1:
        item = int(input('enter an element : '))
        push(stack,item)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        peek(stack)
    elif choice == 4:
        display(stack)
    else:
        break