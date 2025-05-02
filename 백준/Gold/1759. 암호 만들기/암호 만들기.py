import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
L,C = map(int,input().split())
lst = list(input().split())
lst.sort()


def dfs(n,idx,tmp):
    if n == L:
        cnt1 = 0
        cnt2 = 0
        for s in tmp:
            if s == 'a' or s =='e' or s == 'i' or s == 'o' or s =='u':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print(tmp)
        return

    for i in range(idx,C):
        dfs(n+1,i+1,tmp+lst[i])

dfs(0,0,'')




