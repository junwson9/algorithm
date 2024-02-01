import sys
from collections import defaultdict
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))

lst.extend(lst)
s = 0
e = k-1
dic = defaultdict(int)
dic[c] = 1
mx = 0
while True:
    if e >= len(lst):
        break
    for i in range(k):
        dic[lst[s+i]] += 1
    ans = 0
    for key in dic:
        if dic[key] >= 1:
            ans += 1
    if ans > mx:
        mx = ans
    if lst[s] != c:
        dic.pop(lst[s])
    s += 1
    e += 1
print(mx)