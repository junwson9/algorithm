import sys

input = sys.stdin.readline

K = int(input())
lst = []
for _ in range(K):
    n = int(input())
    lst.append(n)
ans = 0
if len(lst) == 1:
    ans = lst[0]
else:
    tmp = []
    for i in range(K):
        if lst[i] == 0:
            tmp.pop()
        else:
            tmp.append(lst[i])

    ans = sum(tmp)

print(ans)
