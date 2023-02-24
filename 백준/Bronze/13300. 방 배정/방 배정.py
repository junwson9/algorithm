N, K = map(int, input().split())
room = [[0]*2 for _ in range(6)]
cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    room[Y-1][S] += 1
for grade in room:
    for n in grade:
        if n != 0 and n > K:
            cnt += (n//K+1)
        elif n != 0:
            cnt += 1
print(cnt)
