def dfs(n,stack):
    for v in adjL[n]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v, stack+[v])
            visited[v] = 0
        else:
            while stack:
                a = stack.pop()
                ans.add(a)
                if v == a:
                    break
            return


ans = set()
N = int(input())
adjL = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(1,N+1):
    adjL[int(input())].append(i)
for n in range(1,N+1):
    dfs(n,[])
ans = sorted(list(ans))
print(len(ans))
print(*ans, sep='\n')