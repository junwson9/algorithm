import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
t = int(input())
for _ in range(t):
    hi = input()
    r,c = map(int, input().split())
    arr = [list(input().strip()) for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c-2):
            if ord(arr[i][j]) == 62 and ord(arr[i][j+1]) == 111 and ord(arr[i][j+2]) == 60:
                cnt += 1

    for j in range(c):
        for i in range(r-2):
            if ord(arr[i][j]) == 118 and ord(arr[i+1][j]) == 111 and ord(arr[i+2][j]) == 94:
                cnt += 1

    print(cnt)
