import sys
input = sys.stdin.readline

a,b,n,w = map(int, input().split())
ans = []
for sh in range(1,n):
    for go in range(1,n):
        if a*sh+b*go == w and sh+go == n:
            ans.append((sh,go))
if len(ans) == 0 or len(ans) > 1:
    print(-1)
if len(ans) == 1:
    print(' '.join(map(str, *ans)))