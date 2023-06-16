import sys
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    order = sys.stdin.readline()
    if 'push' in order:
        p,n = order.split()
        queue.append(n)
    if 'pop' in order:
        if queue:
            pn = queue.pop(0)
            print(pn)
        else:
            print(-1)
            continue
    if 'size' in order:
        print(len(queue))
    if 'empty' in order:
        if queue:
            print(0)
        else:
            print(1)
    if 'front' in order:
        if queue:
            print(queue[0])
        else:
            print(-1)
    if 'back' in order:
        if queue:
            print(queue[-1])
        else:
            print(-1)