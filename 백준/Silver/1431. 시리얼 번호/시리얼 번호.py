import sys
input = sys.stdin.readline
N = int(input())
lst = []
def sum_num(input):
    cnt = 0
    for s in input:
        if s.isdigit():
            cnt += int(s)
    return cnt


for _ in range(N):
    lst.append(input().strip())

lst.sort(key=lambda x:(len(x), sum_num(x), x))
for i in range(N):
    print(lst[i])