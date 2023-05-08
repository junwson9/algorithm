N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))
arr.sort()
start = arr[0][0]
end = arr[0][1]
ans = 0
for i in range(1,N):
    if arr[i][0] <= end:
        end = max(end, arr[i][1])
    else:
        ans += (end-start)
        start, end = arr[i][0], arr[i][1]
ans += (end-start)
print(ans)