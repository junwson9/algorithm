def dfs(n):
    global min_ans, max_ans

    if n >= 2:
        if lst[n-2] == '<':
            if tmp[n-2] > tmp[n-1]:
                return
        if lst[n-2] == '>':
            if tmp[n-2] < tmp[n-1]:
                return

    if n == N:
        for c in range(k):
            if lst[c] == '<':
                if tmp[c] > tmp[c+1]:
                    return
            if lst[c] == '>':
                if tmp[c] < tmp[c+1]:
                    return
        else:
            rlt = ''.join(map(str,tmp))
            if int(min_ans) > int(rlt):
                min_ans = rlt
            if int(max_ans) < int(rlt):
                max_ans = rlt
            return


    for i in range(10):
        if v[i] == 0:
            v[i] = 1
            tmp.append(i)
            dfs(n+1)
            tmp.pop()
            v[i] = 0

k = int(input())
lst = list(input().split())
tmp = []
min_ans = '9'*(k+1)
max_ans = '0'
v = [0]*10
N = k+1
dfs(0)
print(max_ans)
print(min_ans)
