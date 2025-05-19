import sys

input = sys.stdin.readline

lst = list(map(int,input().split()))

ans = 0

def dfs(n,tmp):
    global ans
    if n >= 3:
        for i in range(len(tmp)-2):
            if tmp[i] == tmp[i+1] and tmp[i+1] == tmp[i+2]:
                return
    if n == 10:
        cnt = 0
        for i in range(10):
            if tmp[i] == lst[i]:
                cnt += 1
        if cnt >= 5:
            ans += 1
        return

    for i in range(1,6):
        dfs(n+1,tmp+[i])

dfs(0,[])
print(ans)