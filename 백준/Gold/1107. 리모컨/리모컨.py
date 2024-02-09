import sys
input = sys.stdin.readline
num = input().strip()
number = int(num)
M = int(input())

if M == 0:
    if abs(100-number) > len(num):
        print(len(num))
    else:
        print(abs(100 - number))
else:
    lst = list(map(int, input().split()))
    ans = abs(100-number)
    tmp = []
    def dfs(n,N):
        global ans
        if n == N:
            tmp_int = int(''.join(map(str,tmp)))
            if N + abs(tmp_int-number) < ans:
                ans = N + abs(tmp_int-number)
            return

        for i in range(10):
            if i not in lst:
                tmp.append(i)
                dfs(n+1,N)
                tmp.pop()

    for i in range(1,7):
        dfs(0,i)
    print(ans)