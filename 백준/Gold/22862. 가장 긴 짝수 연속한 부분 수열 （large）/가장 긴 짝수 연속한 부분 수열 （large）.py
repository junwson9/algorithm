import sys
input = sys.stdin.readline
N,K = map(int,input().split())
lst = list(map(int, input().split()))
s = 0
e = 0
odd = l = 0
while True:
    if e >= N:
        break
    if odd > K:
        if lst[s] % 2 == 1:
            odd -= 1
        s += 1

    else:
        if lst[e] % 2 == 1:
            odd += 1
        e += 1
    l = max(l,e-s-odd)
print(l)


