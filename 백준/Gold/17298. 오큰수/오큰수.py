import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
ans = [-1]*n
stk = [0]

for i in range(1,n):
    while stk and lst[stk[-1]] < lst[i]:
        ans[stk.pop()] = lst[i]
    stk.append(i)
print(*ans)
