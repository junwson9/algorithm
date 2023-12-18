import sys
input = sys.stdin.readline

N = int(input())
a = 1
b = 1
ans = 0
while True:
    N = N-2*a
    if N < 3:
        break
    while True:
        if N < 2*b+2:
            break
        ans += 1
        b += 1
    N = N+2*a
    a += 1
    b = 1
print(ans)
