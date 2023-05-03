N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.reverse()
i = 0
ans = 0
while True:
    if K == 0:
        break
    if lst[i] > K:
        i += 1
    else:
        K -= lst[i]
        ans += 1
print(ans)

