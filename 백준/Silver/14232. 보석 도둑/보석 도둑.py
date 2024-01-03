from math import sqrt,ceil
import sys
input = sys.stdin.readline
k = int(input())
lst = []
for i in range(2,ceil(sqrt(k))+1):
    while k % i == 0:
        lst.append(i)
        k//= i

if k != 1:
    lst.append(k)
print(len(lst))
print(*lst)


