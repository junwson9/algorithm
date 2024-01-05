import sys
input = sys.stdin.readline
N,A = map(int, input().split())
ans = 0
while N != 0:
    ans += N // A
    N = N//A

print(ans)
