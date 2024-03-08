import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
adjL = [[] for _ in range(N+1)]

for i in range(1,N+1):
    j = int(input())
    adjL[j].append(i)
rlt = set()
def dfs(n,tmp):
    for i in adjL[n]:
        if not v[i]:
            v[i] = True
            dfs(i,tmp+[i])
        else:
            while tmp:
                a = tmp.pop()
                rlt.add(a)
                if i == a:
                    break
    return

for i in range(1,N+1):
    v = [False]*(N+1)
    dfs(i,[])
rlt = sorted(list(rlt))
print(len(rlt))
for n in rlt:
    print(n)




