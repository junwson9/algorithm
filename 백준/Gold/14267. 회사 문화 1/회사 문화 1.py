import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())
lst = list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
for i in range(2,n+1):
    tree[lst[i-1]].append(i)

arr = [0]*(n+1)

for _ in range(m):
    v,w = map(int,input().split())
    arr[v] += w

def dfs(cur):
    for nxt in tree[cur]:
        arr[nxt] += arr[cur]
        dfs(nxt)

dfs(1)
print(*arr[1:])
