import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
cal_lst = list(map(int,input().split()))
ans = []
def dfs(n,rlt):
    global ans
    if n == N:
        ans.append(rlt)
        return


    for c in range(4):
        if cal_lst[c] != 0:
            cal_lst[c] -= 1
            if c == 0:
                dfs(n+1,rlt+lst[n])
            if c == 1:
                dfs(n+1,rlt-lst[n])
            if c == 2:
                dfs(n+1,rlt*lst[n])
            if c == 3:
                if rlt < 0:
                    dfs(n+1,-(-rlt//lst[n]))
                else:
                    dfs(n+1,rlt//lst[n])
            cal_lst[c] += 1
dfs(1,lst[0])
print(max(ans))
print(min(ans))