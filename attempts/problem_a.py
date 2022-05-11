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
# python3 problem_a.py

import re
import sys

def main():
    info = input().split(' ')
    orderNum = int(info[0])
    tank = int(info[1])
    # print(type(orderNum))
    # print(orderNum)
    # print(tank)

    orders = {}
    for i in range(0, orderNum):
        orders[i] = input()

    # print(orderNum)
    # # print(tank)
    # print(order)

    waterUsed(orders)

    tempTank = tank
    refills = 0
    for order in orders:
        # print("Temp-Tank:", tempTank)
        # print("Order:", orders[order])
        if tempTank-orders[order] >= 0:
            tempTank -= orders[order]
        else:
            # print("Refilled")
            tempTank = tank
            refills += 1
            tempTank -= orders[order]
    print(refills)

    # print(waterUsed)


    sys.exit(0)

def waterUsed(order):
    for item in order:
        # print(item)
        if isLatte(order[item]):
            # print("Is a latte", order[item])
            order[item] = int(order[item][:-1]) + 1
        else:
            # print("Is a espresso", order[item])
            order[item] = int(order[item])

def isLatte(input):
    for char in str(input):
        if char == 'L':
            return True
    return False


if __name__ == '__main__':
   main()
