import sys
input = sys.stdin.readline
N = int(input())
lst = [1,5,10,50]
ans = []
tmp = []
def dfs(n,idx):
    global ans,tmp
    if n == N:
        ans.append(sum(tmp))
        return
    for i in range(idx,4):
        tmp.append(lst[i])
        dfs(n+1,i)
        tmp.pop()
dfs(0,0)
print(len(set(ans)))



