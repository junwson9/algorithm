N,M = map(int, input().split())
listen = []
see = []
for _ in range(N):
    listen.append(input())
for _ in range(M):
    see.append(input())
ans = sorted(list(set(listen)&set(see)))
print(len(ans))
for st in ans:
    print(st)
