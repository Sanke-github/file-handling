'''Write a program to print following type of statistics:
16824  lines in the file
483    empty lines
53.7 average characters per line
65.9 average characters per non empty line
'''

file = open('sarojinipoem.txt','r')
txt = file.readlines()
empty_lines = 0
t = 0
for i in txt:
    for j in i:
        t += 1
    if i == '\n':
        empty_lines += 1
avg2 = t/len(txt)
lst = []
for i in txt:
    if i != '\n':
        lst.append(i)
tot = 0    
for i in lst:
    for j in i:
        tot += 1
avg = tot/len(lst)


print(f'"{len(txt)}" lines in the file \n{empty_lines} empty lines \n{round(avg2,2)} average charecters per line\n{round(avg,2)} average characters per non empty lines') 