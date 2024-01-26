import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = []
for i in range(M):
    lst.append(int(input()))
def ok(n):
    cnt = 0
    for i in range(M):
        cnt += lst[i]//n
        if lst[i]%n:
            cnt += 1
    if cnt <= N:
        return n
    return False

s = 1
e = max(lst)
ans = e
while s<=e:
    mid = (s+e)//2
    if ok(mid):
        if ok(mid) < ans:
            ans = ok(mid)
        e = mid-1

    else:
        s = mid+1
print(ans)





