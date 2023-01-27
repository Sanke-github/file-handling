'''Write a function in python to perform Pop Operation in a stack implemented by 
using list. Print the element deleted, top position and also display the stack elements 
before and after the pop operation? 
>>> li=[20,5,4,3] 
>>> pop(li) 
Original stack [3, 4, 5, 20] 
Top position: 3 
Deleted element 3 
stack after Pop Operation: [4, 5, 20] 
'''
def pop(li):
    if len(li) == 0:
        print("Error: Stack is empty.")
        return
    top_pos = len(li) - 1
    print("Original stack:", li[::-1])
    print("Top position:", top_pos)
    deleted_element = li.pop(top_pos)
    print("Deleted element:", deleted_element)
    print("Stack after Pop Operation:", li)

list=[20,5,4,3]
pop(list)     