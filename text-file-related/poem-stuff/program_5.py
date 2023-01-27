'''write a program Show_Words() to read the contents of a text file 
    'sarojinipoem.txt' and display only such lines/sentences of the file which have EXACTLY 6 words in them '''
file = open('sarojinipoem.txt','r')
lst = file.readlines()
lst.remove('\n')
print(lst)
for i in lst:
    if len(i.split()) == 6:
        print(i)
