from collections import deque
def bfs(n):
    v=[-1]*(N+1)
    q = deque()
    q.append(n)
    v[n] = 0
    while q:
        t = q.popleft()
        for i in adjL[t]:
            if v[i] == -1:
                v[i] = v[t]+1
                q.append(i)
    return max(v)


N = int(input())
adjL = [[] for _ in range(N+1)]
while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    adjL[s].append(e)
    adjL[e].append(s)

mx = 50
lst = []
for n in range(1,N+1):
    tmp = bfs(n)
    if tmp < mx:
        mx = tmp
        lst = [n]
    elif tmp == mx:
        lst.append(n)
print(mx, len(lst))
print(*lst)