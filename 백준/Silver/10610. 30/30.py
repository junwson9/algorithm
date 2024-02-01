import sys
input = sys.stdin.readline
N = input().strip()
if '0' not in N:
    print(-1)
else:
    sm = 0
    for s in N:
        sm += int(s)
    if sm % 3 != 0:
        print(-1)
    else:
        lst = sorted(list(N),reverse=True)
        rlt = ''.join(map(str,lst))
        print(rlt)



