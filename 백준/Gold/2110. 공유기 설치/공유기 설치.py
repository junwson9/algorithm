import sys
input = sys.stdin.readline
N,C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input().strip()))
lst.sort()
s = 1
e = lst[-1]-lst[0]
ans = 0
while s<=e:
    c = lst[0]
    cnt = 1
    mid = (s+e)//2
    for i in range(1,len(lst)):
        if lst[i] >= mid+c:
            cnt += 1
            c = lst[i]
    if cnt >= C:
        ans = mid
        s = mid+1
    else:
        e = mid-1
print(ans)




