import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = e = 0
ans = 0
total = lst[0]
while True:
    if total < M:
        e += 1
        if e >= N:
            break
        total += lst[e]
    elif total == M:
        ans += 1
        total -= lst[s]
        s += 1
    else:
        total -= lst[s]
        s += 1
print(ans)
