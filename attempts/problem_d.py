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
# python3 problem_d.py

# 3 4
# 1 2 1 1
# 2 2 1 2
# 1 2 2 2

# Answer 8

import sys

def main():
    [rows, columns] = input().split(' ')

    values = []
    for i in range(0, int(rows)):
        temp = input().split(' ')
        for j in range(0, int(columns)):
            values.append(int(temp[j]))

    middle = int(rows)*int(columns)/2
    firstHalf = values[0:middle]
    secondHalf = values[middle+1:-1]

    print(firstHalf)
    print(secondHalf)

    print(values)
    sys.exit(0)


if __name__ == '__main__':
   main()
