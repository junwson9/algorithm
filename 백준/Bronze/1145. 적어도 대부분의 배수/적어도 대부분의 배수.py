import sys
input = sys.stdin.readline
lst = list(map(int, input().split()))
for i in range(1,1000001):
    cnt = 0
    for j in range(5):
        if i % lst[j] == 0:
           cnt += 1
    if cnt >= 3:
        print(i)
        break