import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
s = 0
e = N-1
ans = abs(lst[s]+lst[e])
l = lst[s]
r = lst[e]
while s<e:
    sm = lst[s]+lst[e]
    if abs(sm) < ans:
        ans = abs(sm)
        l = lst[s]
        r = lst[e]
        
        if ans == 0:
            break
    
    if sm < 0:
        s += 1
    else:
        e -= 1
print(l,r)




