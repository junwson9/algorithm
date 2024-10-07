import sys

input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]



exc = set(lst)
mx = 0

for ex in exc:
    rlt = []
    for j in range(n):
        if lst[j] == ex:
            continue
        rlt.append(lst[j])

    cnt = 1
    for x in range(1,len(rlt)):
        if rlt[x-1] == rlt[x]:
            cnt += 1
        else:
            mx = max(cnt,mx)
            cnt = 1
    mx = max(cnt,mx)


print(mx)



