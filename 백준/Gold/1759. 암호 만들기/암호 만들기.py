import sys
input = sys.stdin.readline
L,C = map(int, input().split())
lst = list(input().split())
lst.sort()
def dfs(n,idx,rlt):
    if n == L:
        cnt1 = 0
        cnt2 = 0
        for s in rlt:
            if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print(rlt)
        return

    for i in range(idx,C):
        dfs(n+1,i+1,rlt+lst[i])
dfs(0,0,'')
