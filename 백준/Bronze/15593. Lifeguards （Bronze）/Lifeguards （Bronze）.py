import sys
input = sys.stdin.readline
N = int(input())
lst = []
mx = 0
for _ in range(N):
    s,e = map(int, input().split())
    lst.append((s,e))
for i in range(N):
    work = [0]*1001
    ans = 0
    for j in range(N):
        if i == j:
            continue
        else:
            for k in range(lst[j][0],lst[j][1]):
                if work[k] == 0:
                    work[k] = 1
                    ans += 1
    if ans > mx:
        mx = ans
print(mx)







