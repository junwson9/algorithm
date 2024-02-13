import sys
input = sys.stdin.readline
lst = [0]*20000

for i in range(1,10001):
    tmp = i
    while True:
        if i == 0:
            break
        tmp += i%10
        i //= 10
    lst[tmp] = 1
for i in range(1,10001):
    if lst[i] == 0:
        print(i)