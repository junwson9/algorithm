N = int(input())
lst = [int(input()) for _ in range(N)]
ans = 0
for n in range(N-2,-1,-1):
    while lst[n] >= lst[n+1]:
        lst[n] -= 1
        ans += 1
print(ans)