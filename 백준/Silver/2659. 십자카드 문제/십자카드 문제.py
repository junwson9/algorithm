import sys
from collections import deque
input = sys.stdin.readline
lst = list(map(int,input().split()))
tmp = int(''.join(map(str,lst)))
rlt = [0]*10001
def check(n):
    q = deque()
    for i in range(4):
        q.append(n//10**(3-i))
        n %= 10**(3-i)

    ans = int(''.join(map(str,q)))
    for _ in range(3):
        t = q.popleft()
        q.append(t)
        tmp = int(''.join(map(str,q)))
        if tmp < ans:
            ans = tmp
    return ans

for i in range(1111,10000):
    rlt[check(i)] = 1

cnt = 0

for i in range(1111,10000):
    if rlt[i] == 1:
        cnt += 1
    if i == check(tmp):
        break
print(cnt)


