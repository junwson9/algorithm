import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    st = input().split()
    if st[0] == 'push_front':
        q.appendleft(st[1])
    elif st[0] == 'push_back':
        q.append(st[1])
    elif st[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            t = q.popleft()
            print(t)
    elif st[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            t = q.pop()
            print(t)
    elif st[0] == 'size':
        print(len(q))
    elif st[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif st[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif st[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])




