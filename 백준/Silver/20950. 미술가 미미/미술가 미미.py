import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
gom = list(map(int, input().split()))

ans = float('inf')

def dfs(cnt, idx, r, g, b):
    global ans

    if cnt >= 2:
        r_avg = r//cnt
        g_avg = g//cnt
        b_avg = b//cnt
        diff = abs(r_avg - gom[0]) + abs(g_avg - gom[1]) + abs(b_avg - gom[2])
        ans = min(ans, diff)

    if cnt == 7:
        return

    for i in range(idx, N):
        dfs(cnt+1, i+1, r+arr[i][0], g+arr[i][1], b+arr[i][2])

# DFS 실행 (최초 호출)
dfs(0, 0, 0, 0, 0)

print(ans)
