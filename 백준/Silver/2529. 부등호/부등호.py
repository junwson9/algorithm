import sys
input = sys.stdin.readline
k = int(input())
lst = list(map(str,input().split()))
v = [0]*(10)
num = [0,1,2,3,4,5,6,7,8,9]
tmp = []
mx = '0'
mn = '9'*10
def dfs(n):
    global mx,mn
    if n >= 2:
        if lst[n-2] == '<':
            if tmp[n-2] > tmp[n-1]:
                return

        if lst[n-2] == '>':
            if tmp[n-2] < tmp[n-1]:
                return


    if n == k+1:
        rlt = ''.join(map(str,tmp))
        if rlt > mx:
            mx = rlt
        if rlt < mn:
            mn = rlt
        return

    for i in range(10):
        if v[i] == 0:
            v[i] = 1
            tmp.append(i)
            dfs(n+1)
            v[i] = 0
            tmp.pop()


dfs(0)
print(mx)
print(mn)