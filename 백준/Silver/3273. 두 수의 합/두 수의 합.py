import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
x = int(input())
s = 0
e = n-1
lst.sort()
ans = 0
while s<e:
    sm = lst[s]+lst[e]
    if sm > x:
        e -= 1
    elif sm < x:
        s += 1
    else:
        ans += 1
        e -= 1
        s += 1
print(ans)