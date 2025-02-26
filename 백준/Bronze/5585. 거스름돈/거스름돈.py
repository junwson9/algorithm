import sys

input = sys.stdin.readline
N = 1000 - int(input())

ans = 0
for money in (500,100,50,10,5,1):
    while True:
        if N < money:
            break
        N -= money
        ans += 1
print(ans)

