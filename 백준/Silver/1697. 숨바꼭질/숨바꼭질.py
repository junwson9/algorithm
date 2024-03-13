from  collections import deque
def bfs(s):
    global ans
    q = deque()
    q.append(s)
    while q:
        t = q.popleft()
        if t == K:
            ans = v[t]
            break
        else:
            for i in (t-1,t+1,t*2):
                if (0<=i<=100000) and v[i] == 0:
                    v[i] = v[t]+1
                    q.append(i)


N, K = map(int, input().split())
v = [0]*100001
v[N] = 0
ans = 0
bfs(N)
print(ans)