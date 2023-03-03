N = int(input())
lst = list(map(int, input().split()))
lst.sort()
sm = 0
for i in range(N,-1,-1):
    for j in range(i):
        sm += lst[j]
print(sm)