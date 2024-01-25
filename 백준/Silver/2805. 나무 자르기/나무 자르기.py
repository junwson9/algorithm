import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
mx = max(lst)
def ok(n):
    sm = 0
    for i in range(len(lst)):
        if lst[i]-n <= 0:
            continue
        else:
            sm += lst[i]-n
    return sm >= M
r = 0
s = 0
e = mx
while s<=e:
    mid = (s+e)//2
    if ok(mid):
        r = mid
        s = mid+1
    else:
        e = mid-1
print(r)




