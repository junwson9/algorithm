import sys
from itertools import combinations
input = sys.stdin.readline
lst = []
for _ in range(9):
    n = int(input())
    lst.append(n)

seven = list(combinations(lst,7))
for l in seven:
    if sum(l) == 100:
        l_lst = list(l)
        l_lst.sort()
for ans in l_lst:
    print(ans)



