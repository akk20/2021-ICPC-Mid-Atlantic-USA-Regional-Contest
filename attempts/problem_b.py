#!/usr/bin/env python3

__author__ = ["Aidan Kelley"]
__copyright__ = "Copyright 2022"
__credits__ = ["Ryan Hirscher", "Ally Taylor"]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = ""
__email__ = ["akelley1@highpoint.edu", "rhirsche@highpoint.edu", "ataylor5@highpoint.edu"]
__status__ = ""

# To run:
# python3 problem_b.py



import sys

def main():
    time = input()
    thousands = int(time[0])
    hundreds = int(time[1])
    tens = int(time[2])
    ones = int(time[3])

    a = digitChars(thousands)
    b = digitChars(hundreds)
    c = digitChars(tens)
    d = digitChars(ones)

    for i in range(0, 4):
        print(a[i], b[i], ' ' ,c[i], d[i])

    sys.exit(0)

def digitChars(decimal):
    binValue = bin(decimal)
    binValue = binValue[2:]
    tempArray = []
    for bit in binValue:
        tempArray.append(int(bit))

    while len(tempArray) < 4:
        tempArray.insert(0, 0)

    chars = []
    for number in tempArray:
        if number == 0:
            chars.append('.')
        else:
            chars.append('*')
    return chars



if __name__ == '__main__':
   main()
