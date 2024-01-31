import sys
input = sys.stdin.readline
n,k = map(int, input().split())
ans = []
def dfs(n,tmp):
    global ans
    if n < 0:
        return
    if n == 0:
        ans.append(''.join(map(str,tmp)))
        return

    dfs(n-1,tmp+[1])
    dfs(n-2,tmp+[2])
    dfs(n-3,tmp+[3])
dfs(n,[])
if k > len(ans):
    print(-1)
else:
    rlt = ans[k-1]
    for i in range(len(rlt)):
        if i == len(rlt)-1:
            print(rlt[i], end= '')
        else:
            print(rlt[i]+'+', end = '')
