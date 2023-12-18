import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for a in range(1,501):
    for b in range(1,501):
        if a <= b:
            break
        if (a-b)*(a+b) == N:
            ans += 1
print(ans)