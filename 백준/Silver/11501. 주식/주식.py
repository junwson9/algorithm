T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    cur = N-1
    ans = 0
    for i in range(N-2,-1,-1):
        if lst[cur] > lst[i]:
            ans += (lst[cur]-lst[i])
        else:
            cur = i
    print(ans)
