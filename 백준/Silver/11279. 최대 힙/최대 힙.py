import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0 and len(heap) == 0:
        print(0)
        continue
    if x != 0:
        heapq.heappush(heap, (-x,x))
    if x == 0:
        rlt = heapq.heappop(heap)[1]
        print(rlt)


