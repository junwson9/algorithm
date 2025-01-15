import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
adjL = [[] for _ in range(n+1)]



for _ in range(m):
    s,e = map(int,input().split())
    adjL[s].append(e)
    adjL[e].append(s)

q = int(input())
for _ in range(q):
    def bfs():
        v = [-1]*(n+1)
        q = deque()
        q.append(1)
        v[1] = 0
        while q:
            t = q.popleft()
            for i in adjL[t]:
                if v[i] == -1:
                    v[i] = v[t] + 1
                    q.append(i)
        return v


    s,e = map(int,input().split())
    adjL[s].append(e)
    adjL[e].append(s)


    rlt = bfs()
    ans = rlt[1::]

    print(*ans)






