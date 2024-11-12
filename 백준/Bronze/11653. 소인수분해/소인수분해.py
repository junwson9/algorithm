import sys
from math import sqrt

input = sys.stdin.readline

N = int(input())

while True:

    if N < 2:
        break
    for i in range(2,N+1):
        if N%i == 0:
            print(i)
            N = N//i
            break