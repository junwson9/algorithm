import sys

input = sys.stdin.readline
N = int(input())
ans = 0
v = [0]*N

def check(n):
    for i in range(n):
        if v[i] == v[n] or abs(v[i]-v[n]) == n-i:
            return False
    return True


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        v[n] = i
        if check(n):
            dfs(n+1)
dfs(0)
print(ans)
