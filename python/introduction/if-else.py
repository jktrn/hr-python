#!/bin/python

import math
import os
import random
import re
import sys

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input().strip())
    if not isEven(n):
        print("Weird")
    elif n >= 2 and n <= 5 or n > 20:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")