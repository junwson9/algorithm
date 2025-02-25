import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
adjL = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    adjL[s].append([e,w])

s,e = map(int,input().split())
q = []
dist = [int(1e9)]*(n+1)
def dijkstra(start):
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        x_dist,x = heapq.heappop(q)
        if x_dist != dist[x]:
            continue

        for v,weight in adjL[x]:
            if dist[v] > dist[x]+weight:
                dist[v] = dist[x]+weight
                heapq.heappush(q,(dist[v],v))
    return dist


dijkstra(s)

print(dist[e])