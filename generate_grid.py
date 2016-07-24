#/usr/bin/env python3
# print("Hello", "World")
import sys
import random
def myname(number):
    digit =[ ["  ***  ", " *   * ","*     *","*     *","*     *"," *   * ","  ***  "],[] ]
    for num in number:
        realnum = int(num)
        printDig = digit[realnum]
        for start in printDig:
            print start + '\n'

def gen_grid(row, col, maximum, minimum):
    for i in range(0,row):
        line = ""
        for j in range(0,col):
            num = random.randint(minimum, maximum);
            line +=  str(num) + " " 
            #print(str(num) + " ")
        print(line)
        #print('\n')

row = input("row: ")
col = input("col: ")
#myname (sys.argv[1])
maximum = input("Max: ")
minimum = input("Min: ")
gen_grid(row, col, maximum, minimum)





