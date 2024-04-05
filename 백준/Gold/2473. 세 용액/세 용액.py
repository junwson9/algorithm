import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
mn = 1e12
rlt = []
for i in range(n-2):
    s = i+1
    e = n-1
    while s < e:
        ans = lst[i]+lst[s]+lst[e]
        if abs(ans) < mn:
            mn = abs(ans)
            rlt = [lst[i],lst[s],lst[e]]
        if ans < 0:
            s += 1
        elif ans > 0:
            e -= 1
        else:
            break
print(*rlt)


