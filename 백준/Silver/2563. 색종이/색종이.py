import sys
N = int(sys.stdin.readline())
paper = [[0]*100 for _ in range(100)]
for _ in range(N):
    L,B = map(int, sys.stdin.readline().split())
    for i in range(L,L+10):
        for j in range(B,B+10):
                paper[i][j] = 1
ans = 0
for k in paper:
    ans += sum(k)
print(ans)