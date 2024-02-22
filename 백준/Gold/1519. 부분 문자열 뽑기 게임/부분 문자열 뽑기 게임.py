import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
dp = [-1]*1000001
InF = 1e9
def dfs(number):
    if number < 10:
        dp[number] = 0
        return 0

    if dp[number] != -1:
        return dp[number]

    n_str = str(number)
    flag = 0
    for i in range(1,len(n_str)+1):
        for j in range(i):
            sb_num = number % 10**i // 10**j
            if not 0<sb_num<number:
                continue
            nx_num = number-sb_num
            if dfs(nx_num) == 0:
                flag = 1
                break
        if flag:
            break
    dp[number] = flag
    return dp[number]

dfs(N)
if dp[N] == 0:
    print(-1)
else:
    n_str = str(N)
    for i in range(10):
        dp[i] = 0
    ans = InF
    for i in range(1,len(n_str)+1):
        for j in range(i):
            sb_num = N % 10 ** i // 10 ** j
            if not 0<sb_num<N:
                continue
            nx_num = N-sb_num
            if dfs(nx_num) == 0:
                ans = min(ans, sb_num)
    print(ans)