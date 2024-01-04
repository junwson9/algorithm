import sys
from itertools import combinations
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    def gcd(a,b):
        while b > 0:
            a,b = b, a%b
        return a

    tmp = list(combinations(lst,2))
    ans = 1
    for i in range(len(tmp)):
        if gcd(tmp[i][0],tmp[i][1]) > ans:
            ans = gcd(tmp[i][0],tmp[i][1])

    print(ans)