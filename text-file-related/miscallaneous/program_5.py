'''create a function AMcount() that counts the number of A and Z in a text file'''
def AMcount():
    file = open('story.txt','r')
    a = file.read()
    b = a.split()
    print(b)
    count = 0
    for i in b:
        for l in b:
            z = l.count('A')
            y = l.count('Z')
            count += z+y
    print(count)
AMcount()
