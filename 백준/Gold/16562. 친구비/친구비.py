import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M,k = map(int,input().split())
lst = [0]+list(map(int,input().split()))
arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(n):
    global tmp
    tmp.append(n)
    visited[n] = True
    for i in arr[n]:
        if visited[i] == True:
            continue
        dfs(i)

for _ in range(M):
    v,w = map(int,input().split())
    arr[v].append(w)
    arr[w].append(v)

rlt = []
for i in range(1,N+1):
    if visited[i] == True:
        continue
    tmp = []
    dfs(i)
    rlt.append(tmp)
ans = 0
for group in rlt:
    money = 1e9
    for i in group:
        if money > lst[i]:
            money = lst[i]
    ans += money
if ans <= k:
    print(ans)
else:
    print('Oh no')


