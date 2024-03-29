import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
adjL = [set() for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adjL[a].add(b)
    adjL[b].add(a)
InF = 1e9
def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adjL[cur]:
            if v[nxt] > v[cur]+1:
                v[nxt] = v[cur]+1
                q.append(nxt)

mn = 1e9
ans = 0
for i in range(1,n+1):
    v = [InF]*(n+1)
    bfs(i)
    tmp = 0
    for j in range(len(v)):
        if v[j] != 1e9 and v[j] != 0:
            tmp += v[j]
    if tmp < mn:
        mn = tmp
        ans = i
print(ans)

