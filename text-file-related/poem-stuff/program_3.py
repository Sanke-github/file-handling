#modify the program so that each line is printed with a line number at the beginning 
file = open('sarojinipoem.txt','r')
text = file.readlines()
for number,line in enumerate(text):
    print(number,line)