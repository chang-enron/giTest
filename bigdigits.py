#/usr/bin/env python3
# print("Hello", "World")
'''
a = 1;
if  a:
    print("a is smaller than 0")
else:
    print("bad")
'''
'''
a = -1
while a < 10:
    a = a + 1
    print(a)
'''
'''
a = ['a','b','c','d']
for data in "enron":
    print(data)
for word in a:
    print(word)
'''

'''
s = input("enter the integer: ")
try:
    i = int(s)
    print("valid interger entered:", i)
except ValueError as err:
    print(err)
'''
import sys

def myname(number):
    digit =[ ["  ***  ", " *   * ","*     *","*     *","*     *"," *   * ","  ***  "],[] ]
    for num in number:
        realnum = int(num)
        printDig = digit[realnum]
        for start in printDig:
            print start + '\n'

myname (sys.argv[1])

