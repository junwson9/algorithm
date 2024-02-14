import sys
input = sys.stdin.readline
S = input().strip()
lst = []
for i in range(len(S)):
    lst.append(S[i:])
lst.sort()

for s in lst:
    print(s)




