import sys
input = sys.stdin.readline

A,B = input().split()
B = int(B)
lst = list(A)
N = len(lst)
v= [0]*N
rlt = [-1]
def dfs(n,tmp):

    if n == N:
        if tmp[0] == '0':
            return

        if int(tmp) < B:

            rlt.append(int(tmp))
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tmp+lst[i])
            v[i] = 0

dfs(0,'')
print(max(rlt))

