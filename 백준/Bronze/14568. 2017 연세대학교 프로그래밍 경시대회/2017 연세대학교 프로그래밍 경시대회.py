import sys

input = sys.stdin.readline
n = int(input())
ans = 0
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if i+j+k == n:
                    if k%2 == 0 and i >= j+2:
                        ans += 1
print(ans)












