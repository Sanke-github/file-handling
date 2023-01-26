'''modify the program so that the lines are printed in reverse order'''
file = open('sarojinipoem.txt','r')
text = file.readlines()
text.reverse()
print('reversed text : \n',text)
file.close()