import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

s=0
e=1
ans = 0
while s<=e and e<=n:
    sm = 0
    for i in range(s,e):
        sm += lst[i]
    if sm > m:
        s += 1
    elif sm < m:
        e += 1
    else:
        e += 1
        ans += 1

print(ans)