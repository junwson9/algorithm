import sys

input = sys.stdin.readline
T = int(input())
def palin(st):
    s = 0
    e = len(st)-1
    while s<e:
        if st[s] != st[e]:
            return False
        s += 1
        e -= 1
    return True

def like_palin(st):
    s = 0
    e = len(st)-1
    while s<e:
        if st[s] != st[e]:
            if palin(st[s+1:e+1]) or palin(st[s:e]):
                return True
            return False
        s += 1
        e -= 1


for _ in range(T):
    S = list(input().strip())
    if palin(S):
        print(0)
    else:
        if like_palin(S):
            print(1)
        else:
            print(2)
