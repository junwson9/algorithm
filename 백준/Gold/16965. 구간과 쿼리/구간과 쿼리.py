import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
lst = []
def dfs(sx,sy):
    v.append([sx,sy])
    if sx == ex and sy == ey:
        return True
    for x2,y2 in lst:
        if [x2,y2] in v:
            continue
        if x2<sx<y2 or x2<sy<y2:
            if dfs(x2,y2):
                return True
    return False


for _ in range(N):
    t,s,e = map(int,input().split())
    if t == 1:
        lst.append([s,e])

    elif t == 2:
        v = []
        sx,sy = lst[s-1]
        ex,ey = lst[e-1]
        if dfs(sx,sy):
            print(1)
        else:
            print(0)

