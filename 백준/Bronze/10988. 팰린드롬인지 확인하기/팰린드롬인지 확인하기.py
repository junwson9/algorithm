import sys

input = sys.stdin.readline
S = list(input().strip())
s =0
e = len(S)-1
ans = 1
while s<e:
    if S[s] != S[e]:
        ans = 0
        break
    s += 1
    e -= 1

print(ans)







