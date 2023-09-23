import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    lst.append((int(age),name, i))
lst.sort(key=lambda x: (x[0],x[2]))
for i in range(N):
    print(f'{lst[i][0]} {lst[i][1]}')