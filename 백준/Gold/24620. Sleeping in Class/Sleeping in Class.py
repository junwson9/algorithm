import sys
input = sys.stdin.readline
def check(n):
    total = 0
    for i in range(N):
        if total > n:
            return False
        total += lst[i]
        if total == n:
            total = 0
    return True
T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    total = 0
    for i in range(N):
        if mx < lst[i]:
            mx = lst[i]
        total += lst[i]

    ans = 0
    for j in range(max(1,mx), total+1):
        if total % j == 0 and check(j):
            ans = N - total // j
            break
    print(ans)
