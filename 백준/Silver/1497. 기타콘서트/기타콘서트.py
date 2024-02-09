import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
ans = N
tmp3 = []
def dfs(n,tmp):
    if n == N:
        cnt = set()
        for check in tmp:
            for i in range(len(check)):
                if check[i] == 'Y':
                    cnt.add(i+1)

        if len(cnt) == 0:
            return
        else:
            tmp3.append((len(cnt),len(tmp)))
        return


    dfs(n+1,tmp+[arr[n][1]])
    dfs(n+1,tmp)

dfs(0,[])

if len(tmp3) == 0:
    print(-1)
else:
    tmp3.sort(key=lambda x: x[0], reverse=True)
    s = tmp3[0][0]
    for i in range(len(tmp3)):
        if tmp3[i][0] == s:
            if ans > tmp3[i][1]:
                ans = tmp3[i][1]
        else:
            break
    print(ans)