import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    ans = 'YES'
    s = int(input())
    for i in range(2,1000001):
        if s % i == 0:
            ans = 'NO'
    print(ans)







