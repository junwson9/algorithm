from collections import deque
def bfs(s,e):
    v[s] = 1
    q = deque()
    q.append(s)
    while q:
        t = q.popleft()
        if t == e:
            return v[t]-1
        for i in adjL[t]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[t]+1
    return -1





n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
adjL = [[] for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(m):
    p, c = map(int, input().split())
    adjL[p].append(c)
    adjL[c].append(p)
print(bfs(p1,p2))