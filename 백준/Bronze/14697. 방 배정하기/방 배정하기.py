import sys
input = sys.stdin.readline
A,B,C,N = map(int,input().split())
ans = 0
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if A*i+B*j+C*k == N:
                ans = 1
print(ans)