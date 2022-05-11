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
# python3 problem_c.py

# 3 9 5
# 1
# 2
# 3
# Answer: 7

import sys

def main():
    info = input().split(' ')
    studentNum = int(info[0])
    hallDur = int(info[1])
    totalDays = int(info[2])

    times = {}
    for i in range(0, studentNum):
        times[i] = int(input())

    passes = 0
    currentStu = 0
    currentDay = 0
    currentDur = 0
    timeLeft = True

    while currentDay <= totalDays-1:
        while timeLeft:
            if currentDur + times[currentStu] <= hallDur:
                currentDur += times[currentStu]
                if currentStu == studentNum-1:
                    currentStu = 0
                    passes += 1
                else:
                    currentStu += 1
            else:
                timeLeft = False

        currentDay += 1
        timeLeft = True
        currentDur = 0

    print(passes)

    sys.exit(0)


if __name__ == '__main__':
   main()
