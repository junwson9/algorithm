import sys
input = sys.stdin.readline
N,M,K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
skill = []
ans = 0
def dfs(n,idx):
    global ans
    if n == N:
        cnt = 0
        for lst in arr:
            cnt2 = 0
            for s in skill:
                if s in lst:
                    cnt2 += 1
            if cnt2 == K:
                cnt += 1
        if cnt > ans:
            ans = cnt
        return


    for i in range(idx,2*N+1):
        skill.append(i)
        dfs(n+1,i+1)
        skill.pop()

dfs(0,1)
print(ans)