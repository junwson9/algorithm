import sys
input = sys.stdin.readline
N,K = map(int,input().split())
lst = list(map(int,input().split()))
tmp_lst = []
for i in range(N-K+1):
    tmp = 0
    for j in range(i,i+K):
        tmp += lst[j]
    tmp_lst.append(tmp)
print(max(tmp_lst))







