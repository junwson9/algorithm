def dfs(n,tmp,idx):
    if n == L:
        cnt1 = 0
        cnt2 = 0
        for s in tmp:
            if s == 'a' or s =='e' or s=='i' or s=='o' or s=='u':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            rlt.append(tmp)
            return

    for i in range(idx,C):
        dfs(n+1, tmp+[lst[i]], i+1)

L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
tmp = []
arr = []
rlt = []
v = [0]*len(lst)
dfs(0,tmp,0)
for pwd in rlt:
    print(''.join(pwd))