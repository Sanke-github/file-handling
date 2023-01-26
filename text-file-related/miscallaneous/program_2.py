#write a program to contents from a text file myfile.txt and find word count in it
file = open('myfile.txt','r')
file_in_text = file.read()
file_in_list = file_in_text.split()
print(file_in_list)
count = len(file_in_list)
print(count)
