import sys
input = sys.stdin.readline
N = int(input())
stk = []

for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stk.append(order[1])
    if order[0] == 2:
        if len(stk) >= 1:
            tmp = stk.pop()
            print(tmp)
        else:
            print(-1)
    if order[0] == 3:
        print(len(stk))
    if order[0] == 4:
        if len(stk) >= 1:
            print(0)
        else:
            print(1)
    if order[0] == 5:
        if len(stk) >= 1:
            print(stk[-1])
        else:
            print(-1)

