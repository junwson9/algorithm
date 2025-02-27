import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == '.':
        break

    stk = []
    is_balance = True

    for s in S:
        if s == '(':
            stk.append('(')
        elif s == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                is_balance = False
                break

        elif s == '[':
            stk.append('[')
        elif s == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                is_balance = False
                break

    if is_balance and not stk:
        print('yes')
    else:
        print('no')


