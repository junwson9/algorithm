import sys
input = sys.stdin.readline
K,N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))

def ok(n):
    cnt = 0
    for i in range(len(lst)):
        cnt += lst[i]//n
    if cnt >= N:
        return n
    return False

s = 1
e = max(lst)
ans = 0
while s<=e:
    mid = (s+e)//2
    if ok(mid):
        if ok(mid) > ans:
            ans = ok(mid)
        s = mid + 1
    else:
        e = mid - 1
print(ans)


