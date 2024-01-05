import sys
from math import sqrt
input = sys.stdin.readline
g,l = map(int, input().split())
tmp = l//g
ans = 200000000
def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a
for a in range(1,int(sqrt(tmp))+1):
    b = tmp//a
    if gcd(a,b) == 1 and tmp % a == 0:
        sm = (a+b)*g
        if sm < ans:
            ans = sm
            ans_lst = [a*g,b*g]

print(*ans_lst)

