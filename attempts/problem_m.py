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
# python3 problem_m.py

# 5
# 1 1
# 3 2
# 4 5
# 4 3
# 5 4

# Answer: 1

import sys

def main():
    packetCount = int(input())

    times = {}
    timeArrived = []
    packet = {}
    for i in range(0, packetCount):
        [arrived, packet] = input().split(' ')
        timeArrived.append(arrived)

        # times[packet] = timeArrived


        # tempInput = input().split(' ')
        # times[int(tempInput[1])] = int(tempInput[0])

    # print(times)
    print(timeArrived)
    print(packet)

    tempTimes = {}

    buffer = []
    timeElapsed = 0


    sys.exit(0)


if __name__ == '__main__':
   main()
