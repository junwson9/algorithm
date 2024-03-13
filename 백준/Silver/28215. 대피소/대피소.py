import sys
from itertools import combinations
input = sys.stdin.readline
N,K = map(int,input().split())
home = []
for _ in range(N):
    i,j = map(int, input().split())
    home.append([i,j])

num = [i for i in range(N)]
lst = list(combinations(num,K))
ans = 1e9
for comb in lst:
    tmp = 0
    for hi,hj in home:
        rlt = 1e9
        for i in range(K):
            rlt = min(rlt,abs(home[comb[i]][0]-hi)+abs(home[comb[i]][1]-hj))
        tmp = max(tmp,rlt)
    ans = min(ans,tmp)
print(ans)

