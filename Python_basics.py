# -*- coding: utf-8 -*-
"""Pyhton_Basics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gru_fzZZMaNlqKeaQtqQyHPGpTnekhoc

# **Python_basics**
"""

#Q1 Program to calculate the length of the string without using function

a = input()
#print(type(a))
count=0
for i in a:
  count = count + 1
print(count)

#Q2 To display which letter is there in first string but not in second string

a = input()
b = input()
#bucket=0
for i in a:
  if i not in b:
    print(i)

#Q3 Write a program to swap two numbers

a = int(input())
b = int(input())
'''
c=a
a=b
b=c
print(a,b)
'''
a,b=b,a
print(a,b)

#Q4 Write a program to map 2 list into a dictionary

a = ["Apple", "Football", "Books"]
b = ["Fruit", "Sport", "Study"]

c = {}
count=0
for i in a:
  count = count + 1

for i in range(0,count):
  c.update({a[i]:b[i]})

print(c)

#Q5 write a program to count the number of times a letter has appears in the text file

Data = open("newfile.txt","w")
Data.write("Daipayan Chakroborty")
Data.close()

a= input()
count=0

Data = open("newfile.txt","r")
for i in Data.read():
  if i==a:
    count=count+1
print(count)

#Q6 To find th valid email_id and 10 digit number in the given string

import re

email = '^([A-Z|a-z])+\d*[^.]@[a-z]+.[a-z]+'
mobile_no = '^[0-9]{10}$'

user_mail = input()
user_mobile_number = input()

if(re.search(email,user_mail)):
  print("Valid email")
else:
  print("Invalid email")

if(re.search(mobile_no,user_mobile_number)):
  print("Valid number")
else:
  print("Invalid number")

#Q7 To find the sum of square of even numbers in the given list

'''
find the even numbers
do square of the even numbers
and then add the numbers 
'''

user = list(map(int,(input().split())))
#even_numbers = []
#sq_even_numbers = []
#count = 0
sum = 0
'''
for i in user:
  if i % 2 == 0:
    sum = sum + i**2
    even_numbers.append(i)

for i in even_numbers:
  count = i**2
  sq_even_numbers.append(count)

for i in sq_even_numbers:
  sum = sum + i
'''

for i in user:
  if i % 2 == 0:
    sum = sum + i**2
print(sum)

#Q8 Create a pickle file to store your dictionary

import pickle
# initializing data to be stored in db
record = {'key' : 'Omkar', 'pay' : 40000}
  
# database
#db = {}
#db['Omkar'] = Omkar
#db['Jagdish'] = Jagdish


# Its important to use binary mode
dbfile = open('examplePickle', 'wb')
pickle.dump(record, dbfile)                     
dbfile.close()

dbfile = open('examplePickle', 'rb')
db= pickle.load(dbfile) 
dbfile.close()

print(db)


#print(myEntry)
