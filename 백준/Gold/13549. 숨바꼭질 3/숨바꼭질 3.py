import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int, input().split())
v = [False]*(100001)
dist = [-1]*(100001)
def bfs(n):
    q = deque()
    q.append(n)
    dist[n] = 0
    v[n] = True
    while q:
        t = q.popleft()
        for i in (t*2,t-1,t+1):
            if 0 <= i <= 100000:
                if not v[i] and i == t*2:
                    q.appendleft(i)
                    v[i] = True
                    dist[i] = dist[t]
                if not v[i] and i != t*2:
                    q.append(i)
                    v[i] = True
                    dist[i] = dist[t]+1



bfs(N)
print(dist[K])