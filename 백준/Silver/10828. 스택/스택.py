import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    order = sys.stdin.readline()
    if 'push' in order:
        pu,n = order.split()
        stack.append(n)
    if 'pop' in order:
        if stack:
            p = stack.pop()
            print(p)
        else:
            print(-1)
    if 'size' in order:
        print(len(stack))
    if 'empty' in order:
        if stack:
            print(0)
        else:
            print(1)
    if 'top' in order:
        if stack:
            print(stack[-1])
        else:
            print(-1)