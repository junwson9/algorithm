import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
sort_lst = [[] for _ in range(5)]

for i in range(5):
    for j in range(N):
        sort_lst[i].append([arr[j][i],j])
    sort_lst[i].sort(reverse=True, key=lambda x:x[0])

v = [0]*N
rlt = 0

def dfs(n,sm):
    global rlt
    if n == 5:
        rlt = max(rlt,sm)
        return

    for score, idx in sort_lst[n][:5]:
        if not v[idx]:
            v[idx] = 1
            dfs(n+1,sm+score)
            v[idx] = 0

dfs(0,0)
print(rlt)
