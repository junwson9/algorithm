import sys

input = sys.stdin.readline
N = int(input())
ans = N
for _ in range(N):
    S = list(input().strip())
    lst = []
    i = 1
    tmp = S[0]
    while True:
        if i == len(S):
            if tmp not in lst:
                lst.append(tmp)
            else:
                ans -= 1
            break
        if S[i] != tmp:
            if tmp not in lst:
                lst.append(tmp)
            else:
                ans -= 1
                break
            tmp = S[i]


        i += 1


print(ans)







