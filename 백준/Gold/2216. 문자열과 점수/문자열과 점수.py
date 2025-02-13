import sys

input = sys.stdin.readline
A,B,C = map(int,input().split())

X = list(input().strip())
Y = list(input().strip())

dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]

for x in range(1,len(X)+1):
    dp[x][0] = x*B

for y in range(1,len(Y)+1):
    dp[0][y] = y*B


for x in range(1,len(X)+1):
    for y in range(1,len(Y)+1):
        if X[x-1] == Y[y-1]:
            tmp = A
        else:
            tmp = C

        dp[x][y] = max(dp[x-1][y-1]+tmp,dp[x-1][y]+B,dp[x][y-1]+B)

print(dp[len(X)][len(Y)])



# dp = [[-1]*(len(Y)+1) for _ in range(len(X)+1)]
#
# def dfs(x,y):
#
#     if x == 0:
#         return y*B
#
#     if y == 0:
#         return x*B
#
#
#     if dp[x][y] != -1:
#         return dp[x][y]
#
#     if X[x-1] == Y[y-1]:
#         tmp = A
#     else:
#         tmp = C
#
#     dp[x][y] = max(dfs(x-1,y-1)+tmp,dfs(x-1,y)+B,dfs(x,y-1)+B)
#     return dp[x][y]
#
#
# dfs(len(X),len(Y))
# print(dp[len(X)][len(Y)])


