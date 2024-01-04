import sys
from math import sqrt
input = sys.stdin.readline
N = int(input())
cnt = 0
for i in range(1,int(sqrt(N)+1)):
    cnt += 1
print(cnt)
