import sys
input = sys.stdin.readline

n = int(input())
tmp = n//3
cnt = 0
for i in range(1,tmp):
    for j in range(1,tmp):
        for k in range(1,tmp):
            if 3*i+3*j+3*k == n:
                cnt += 1
print(cnt)