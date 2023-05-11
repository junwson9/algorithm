import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []
ans = 0
for _ in range(N):
    x = int(input())
    if len(heap) == 0 and x == 0:
        print(0)
        continue
    if x == 0:
        ans = heapq.heappop(heap)
        print(ans)
    else:
        heapq.heappush(heap, x)

