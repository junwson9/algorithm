def dfs(s):
    visit[s] = 1
    global ans
    while True:
        for e in adj[s]:
            if visit[e] == 0:
                stk.append(s)
                s = e
                visit[s] = 1
                ans += 1
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break


N = int(input())
P = int(input())
visit = [0]*(N+1)
stk = []
adj = [[] for _ in range(N+1)]
for _ in range(P):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

ans = 0
dfs(1)
print(ans)