import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n,k = map(int, input().split())
v = [-1]*100001
path = [-1]*100001
def bfs(cur):
    q = deque()
    q.append([cur,0,[n]])
    v[cur] = 0
    if n > k:
        return n-k,[x for x in range(n,k-1,-1)]
    while q:
        prev,cnt,path = q.popleft()
        if prev == k:
            return cnt,path
        for nxt in (prev*2,prev-1,prev+1):
            if not 0<= nxt <= 100000:
                continue
            if v[nxt] != -1:
                continue
            v[nxt] = 1
            q.append([nxt,cnt+1,path+[nxt]])

ans_c, ans_p = bfs(n)
print(ans_c)
print(*ans_p)


