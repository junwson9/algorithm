import sys
input = sys.stdin.readline
N,X = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for n in lst:
    if n == X:
        ans += 1
for _ in range(ans):
    lst.pop()
s = 0
e = N-1-ans
bottle = N-ans
while True:
    if s >= e:
        break
    if lst[s]+lst[e] >= X/2:
        s += 1
        e -= 1
        ans += 1
        bottle -= 2
    else:
        s += 1
ans += bottle//3
print(ans)