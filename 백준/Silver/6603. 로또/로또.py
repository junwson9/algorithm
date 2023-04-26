def dfs(n,tmp,idx):
    if n == 6:
        print(*tmp)
        return

    for i in range(idx,len(lst)):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+[lst[i]], i+1)
            v[i] = 0

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break
    lst = lst[1:]
    tmp = []
    v = [0]*len(lst)
    dfs(0,tmp,0)
    print()