import sys

input = sys.stdin.readline
lst = list(input().strip())
stack = []
ans = 0
for s in lst:
    if s == '(':
        stack.append(s)
    else:
        if stack:
            stack.pop()
        else:
            ans += 1
print(ans + len(stack))