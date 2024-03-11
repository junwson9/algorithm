import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,s1,s2 = map(int,input().split())
adjL = [[] for _ in range(N+1)]
for i in range(N-1):
    s,e,z = map(int, input().split())
    adjL[s].append([e,z])
    adjL[e].append([s,z])

v = [False]*(N+1)
rlt = []
def dfs(n,tmp,mx):
    v[n] = True
    if n == s2:
        print(tmp-mx)
    for i,z in adjL[n]:
        if v[i]:
            continue
        dfs(i,tmp+z,max(z,mx))

if s1 == s2:
    print(0)
else:
    dfs(s1,0,0)