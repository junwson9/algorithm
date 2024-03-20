import heapq
import sys
from collections import deque
input = sys.stdin.readline
N,M,X = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,cost = map(int, input().split())
    adjL[s].append((e,cost))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist = [int(1e9)]*(N+1)
    dist[start] = 0
    while q:
        x_dist, x = heapq.heappop(q)
        if dist[x] < x_dist:
            continue
        for nxt, cost in adjL[x]:
            if dist[nxt] > x_dist + cost:
                dist[nxt] = x_dist + cost
                heapq.heappush(q, (dist[nxt], nxt))
    return dist

ans = 0
for i in range(1,N+1):
    if i == X:
        continue
    go = dijkstra(i)
    back = dijkstra(X)
    ans = max(ans,go[X]+back[i])


print(ans)

