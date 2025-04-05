from collections import deque
import sys
input = sys.stdin.readline
n,w,l = map(int,input().split())
q = deque(map(int,input().split()))

bridge = deque([0]*w)
weight = 0
time = 0
while bridge:
    out = bridge.popleft()
    weight -= out

    if q:
        if q[0]+weight <= l:
            bridge.append(q[0])
            weight += q[0]
            q.popleft()
        else:
            bridge.append(0)
    time += 1
print(time)







