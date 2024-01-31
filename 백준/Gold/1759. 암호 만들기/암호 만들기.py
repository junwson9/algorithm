import sys
input = sys.stdin.readline
L,C = map(int, input().split())
lst = list(input().split())
lst.sort()
tmp = []
def dfs(n,idx):
    if n == L:
        cnt1 = 0
        cnt2 = 0
        for i in range(L):
            if tmp[i] == 'a' or tmp[i] == 'e' or tmp[i] == 'i' or tmp[i] == 'o' or tmp[i] == 'u':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            rlt = ''.join(map(str,tmp))
            print(rlt)
        return

    for i in range(idx,C):
        tmp.append(lst[i])
        dfs(n+1,i+1)
        tmp.pop()

dfs(0,0)
