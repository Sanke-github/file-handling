'''write a program to read following details of sports performance(sports,competetion,prizes-won) of your school and store into a csv file delimited with a tab character'''
import csv
def create():
  file = open('sports.csv','w')
  writer = csv.writer(file,delimiter = '\t')
  writer.writerow(['sport','competitions','prizes won'])
  ans = 'y'
  i = 1
  while ans == 'y':
    print(f'{i} record/s added')
    sport = input('enter sport name: ')
    competition = int(input('number of competitions particapated : '))
    prizes = int(input('prizes won : '))
    lst = ([sport,competition,prizes])
    writer.writerow(lst)
    i += 1
    ans = input('more records? [y/n] : ')
  file.close()
  
 create()
