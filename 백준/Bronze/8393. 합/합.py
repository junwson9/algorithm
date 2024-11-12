import sys

input = sys.stdin.readline
n = int(input())
sm = 0
for i in range(1,n+1):
    sm += i
print(sm)