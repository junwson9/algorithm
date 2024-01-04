import sys
from math import sqrt
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
def prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
ans = 0
for j in range(len(lst)):
    if prime(lst[j]):
        ans += 1
print(ans)