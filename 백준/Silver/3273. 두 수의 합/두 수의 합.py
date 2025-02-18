import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
x = int(input())
lst.sort()

s = 0
e = n-1
ans = 0
while s<e:
    if lst[s]+lst[e] > x:
        e -= 1
    elif lst[s]+lst[e] < x:
        s += 1
    else:
        s += 1
        e -= 1
        ans += 1
print(ans)
