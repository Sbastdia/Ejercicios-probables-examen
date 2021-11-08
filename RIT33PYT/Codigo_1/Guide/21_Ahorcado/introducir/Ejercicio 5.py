import math
import os
import random
import re
import sys


def gameOfStones(n):
    for i in range (m):
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
        fptr.close()
