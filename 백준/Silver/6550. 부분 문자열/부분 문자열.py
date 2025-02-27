import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == '':
        break
    s,t = S.split()

    s_str = 0
    cnt = 0

    for t_str in t:
        if s_str == len(s):
            break

        if t_str == s[s_str]:
            cnt += 1
            s_str += 1

    if cnt == len(s):
        print('Yes')
    else:
        print('No')
