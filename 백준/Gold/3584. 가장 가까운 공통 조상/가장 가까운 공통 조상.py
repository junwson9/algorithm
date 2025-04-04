import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0]*(N+1)
    for _ in range(N-1):
        a,b = map(int,input().split())
        parent[b] = a

    ta , tb=map(int,input().split())

    Aparent = []

    while True:
        if ta == 0:
            break
        Aparent.append(ta)
        ta = parent[ta]


    while True:
        if tb in Aparent:
            print(tb)
            break
        tb=parent[tb]


