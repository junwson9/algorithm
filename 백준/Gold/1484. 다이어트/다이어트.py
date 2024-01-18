import sys
input = sys.stdin.readline
G = int(input())
s = 2
e = 1
ans = []
while True:
    if s+e > G:
        if len(ans) == 0:
            ans.append(-1)
        break
    if e >= s:
        if len(ans) == 0:
            ans.append(-1)
        break
    tmp = (s+e)*(s-e)
    if tmp < G:
        s += 1
        e = 1
    elif tmp > G:
        e += 1
    else:
        ans.append(s)
        s += 1
        e = 1
for n in ans:
    print(n)