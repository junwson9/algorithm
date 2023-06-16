T = int(input())
for tc in range(T):
    stack = []
    st = input()
    ans = 'YES'
    for s in st:
            if s == '(':
                stack.append(s)
            if s == ')':
                if stack:
                    stack.pop()
                else:
                    ans = 'NO'
                    break
    if stack:
        ans = 'NO'
    print(ans)