import sys
input = sys.stdin.readline
N = int(input())
lst = [0]*N
ans = 0

def check(row):
    for n in range(row):
        if lst[row] == lst[n] or abs(lst[n]-lst[row]) == row-n:
            return False
    return True



def dfs(row):
    global ans
    if row == N:
        ans += 1
        return

    for col in range(N):
        lst[row] = col
        if check(row):
            dfs(row+1)

dfs(0)
print(ans)