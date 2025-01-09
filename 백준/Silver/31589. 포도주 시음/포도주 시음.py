import sys
input = sys.stdin.readline

N,K = map(int,input().split())
lst = [0]+list(map(int,input().split()))
lst.sort()

s = 0
e = len(lst)-1
cnt = 0
rlt = 0
while cnt < K:

    if cnt%2 == 0:
        rlt += lst[e] - lst[s]
        e -= 1
        cnt += 1

    else:
        s += 1
        cnt += 1

print(rlt)