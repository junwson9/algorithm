import sys
from collections import deque

input = sys.stdin.readline

def bfs(n):

    q = deque()
    q.append(n)
    while q:
        t = q.popleft()
        if t == K:
            break
        for i in (t+1,t-1,t*2):
            if i < 0 or i > 100000:
                continue
            if v[i] != 0:
                continue
            q.append(i)
            v[i] = v[t]+1


N,K = map(int, input().split())
v = [0]*100001
bfs(N)
print(v[K])
