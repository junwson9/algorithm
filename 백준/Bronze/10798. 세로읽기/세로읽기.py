import sys

input = sys.stdin.readline
arr = [list(input().strip()) for _ in range(5)]

mx_length = 0
for lst in arr:
    if len(lst) < 15:
        lst += [-1]*(15-len(lst))

rlt = ''

for j in range(15):
    for i in range(5):
        if arr[i][j] != -1:
            rlt += arr[i][j]
print(rlt)