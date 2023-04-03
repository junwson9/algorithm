def dfs(n,a_lst,b_lst):
    global ans
    if n == N:
        if len(a_lst) == M:
            a_sum = b_sum = 0
            for i in range(M):
                for j in range(M):
                    a_sum += arr[a_lst[i]][a_lst[j]]
                    b_sum += arr[b_lst[i]][b_lst[j]]
            ans = min(ans,abs(a_sum-b_sum))
        return


    dfs(n+1,a_lst+[n],b_lst)
    dfs(n+1,a_lst,b_lst+[n])



N = int(input())
M = N//2
arr = [list(map(int, input().split())) for _ in range(N)]
a_lst = []
b_lst = []
ans = 100*M
dfs(0,a_lst,b_lst)
print(ans)