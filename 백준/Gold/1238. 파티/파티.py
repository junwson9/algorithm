import sys
import heapq

input = sys.stdin.readline
n,m,x = map(int,input().split())
adjL = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    adjL[s].append([e,w])

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist = [int(1e9)]*(n+1)
    dist[start] = 0
    while q:
        dist_x, x = heapq.heappop(q)
        if dist_x != dist[x]:
            continue
        for v,weight in adjL[x]:
            if dist[v] > dist[x]+weight:
                dist[v] = dist[x]+weight
                heapq.heappush(q,(dist[v],v))
    return dist

ans = 0
for i in range(1,n+1):
    if i == x:
        continue
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans,go[x]+back[i])

print(ans)






