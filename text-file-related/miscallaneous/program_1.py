'''program to count number of vowels in a text file(create a text file office.txt in the same folder as this program)'''
def countvowels():
    with open('office.txt', 'r') as f:
        a = f.read()
    l_v = 0
    u_v = 0
    for c in a:
      if c in 'aeiou':
        l_v += 1
      elif c in 'AEIOU':
        u_v += 1
    print(f'number of vowels = {l_v}+{u_v}')
    f.close()
countvowels()
