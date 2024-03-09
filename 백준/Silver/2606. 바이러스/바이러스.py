import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    adjL[s].append(e)
    adjL[e].append(s)
v = [False]*(N+1)
def dfs(n):
    global cnt
    v[n] = True
    for i in adjL[n]:
        if v[i]:
            continue
        dfs(i)
        cnt += 1


cnt = 0
dfs(1)
print(cnt)



