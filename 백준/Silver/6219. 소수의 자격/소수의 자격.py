import sys
from math import sqrt
input = sys.stdin.readline
A,B,D = map(int, input().split())
ans = 0
def prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
for j in range(A,B+1):
    if prime(j):
        tmp = list(str(j))
        if str(D) in tmp:
            ans += 1
print(ans)

