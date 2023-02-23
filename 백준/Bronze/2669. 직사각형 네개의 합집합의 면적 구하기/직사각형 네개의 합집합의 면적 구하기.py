arr = [[0]*101 for _ in range(101)]
ans = 0
for _ in range(4):
    sj,si,ej,ei = map(int, input().split())
    for i in range(si,ei):
        for j in range(sj, ej):
            arr[i][j] = 1
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            ans += 1
print(ans)