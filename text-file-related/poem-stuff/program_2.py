#modify the code so as to output to another file instead of the screen.
#Let your script overwrite the output file
file = open('sarojinipoem.txt','r')
text = file.readlines()
my_file = open('sarojinipoem_reversed','w')
text.reverse()
my_file.writelines(text)
