import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
dot = []
for _ in range(N):
    x,type = map(int,input().split())
    dot.append([x,type])

ans = 0
for i in range(len(dot)):
    dist = 1e9
    for j in range(len(dot)):
        if i == j:
            continue
        if dot[i][1] == dot[j][1]:
            if abs(dot[i][0] - dot[j][0]) < dist:
                dist = abs(dot[i][0] - dot[j][0])
    ans += dist
print(ans)