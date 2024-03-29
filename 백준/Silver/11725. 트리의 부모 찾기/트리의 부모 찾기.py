from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
adjL = [[] for _ in range(N+1)]
v = [0]*(N+1)
answer = [0]*(N+1)
for _ in range(N-1):
    s,e = map(int,input().split())
    adjL[s].append(e)
    adjL[e].append(s)
def bfs(adjL,v,node):
    q = deque()
    q.append(node)
    v[node] = 1
    while q:
        t = q.popleft()
        for i in adjL[t]:
            if v[i] == 0:
                q.append(i)
                answer[i] = t
                v[i] = 1
bfs(adjL,v,1)

for i in range(2,N+1):
    print(answer[i])
