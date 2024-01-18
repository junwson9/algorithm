import sys
input = sys.stdin.readline
N ,K, B = map(int,input().split())
lst = [int(input()) for _ in range(B)]
road = [0]*(N+1)
s = 1
e = K
total = 0
for i in range(B):
    road[lst[i]] = -1

for i in range(1,K+1):
    if road[i] == -1:
        total += 1

tmp = total
while True:
    total = min(total, tmp)
    if e >= N:
        break
    if road[s] == -1:
        tmp -= 1
    if road[e+1] == -1:
        tmp += 1
    s += 1
    e += 1
print(total)