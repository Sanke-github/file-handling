#Write a program to read contents from the text file diary.txt and count number of lines with Starting letter “T” or “M”.
file = open('diary.txt','r')
lines = file.readlines()
print(lines)
count = 0
for line in lines:
    if line.startswith('T') or line.startswith('M') or line.startswith('t') or line.startswith('m'):
        count += 1
print(count)
# Print the result
print(f'There are {count} lines in the file that start with "T" or "M".')
