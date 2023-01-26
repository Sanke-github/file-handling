#Write a program to read contents from the text file mydiary.txt and count number of lines with ending letter “r”.
file = open('diary.txt','r')
txt = file.read()
tzt = txt.split()

print(txt)
count = 0
for i in tzt:

    if i.endswith('r'):
        count += 1
print(f"number of lines ending with 'r' are {count}")
