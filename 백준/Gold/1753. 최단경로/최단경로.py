import heapq
import sys
input = sys.stdin.readline
V,E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V+1)]
dist = [int(1e9)]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
q = []
heapq.heappush(q,(0,K))
dist[K] = 0
while q:
    dist_x,x = heapq.heappop(q)
    if dist_x != dist[x]:
        continue
    for u,w in arr[x]:
        if dist[u] > dist[x]+w:
            dist[u] = dist[x]+w
            heapq.heappush(q,[dist[u],u])

for i in range(1,V+1):
    if dist[i] != int(1e9):
        print(dist[i])
    else:
        print("INF")