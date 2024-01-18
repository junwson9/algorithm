import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
s = 0
e = n-1
ans = abs(lst[s] + lst[e])
left = lst[s]
right = lst[e]
while s < e:
    tmp = lst[s]+lst[e]
    if abs(tmp) < ans:
        left = lst[s]
        right = lst[e]
        ans = abs(tmp)

        if ans == 0:
            break
    if tmp < 0:
        s += 1
    else:
        e -= 1
print(left, right)