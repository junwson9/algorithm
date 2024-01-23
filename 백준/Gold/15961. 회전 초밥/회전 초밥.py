import sys
from collections import defaultdict
input = sys.stdin.readline
N,d,k,c = map(int ,input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst = lst*2
s = 0
e = k-1
ans = 0
dic = defaultdict(int)
dic[c] += 1
for i in range(s,e+1):
    dic[lst[i]] += 1
while True:
    ans = max(ans, len(dic))
    if s >= N:
        break
    dic[lst[s]] -= 1
    if dic[lst[s]] == 0:
        dic.pop(lst[s])
    e += 1
    s += 1
    dic[lst[e%N]] += 1
print(ans)





