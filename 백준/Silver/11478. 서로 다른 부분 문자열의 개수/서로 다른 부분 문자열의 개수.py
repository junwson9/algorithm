import sys
input = sys.stdin.readline
S = input().strip()
cnt = set()

for i in range(len(S)):
    for j in range(i,len(S)):
        cnt.add(S[i:j+1])
print(len(cnt))



