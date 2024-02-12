import sys
input = sys.stdin.readline

is_prime=[True]*(123456*2+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int((123456 * 2) ** 0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * i, 123456 * 2 + 1, i):
        is_prime[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,2*n+1):
        if is_prime[i] == True:
            cnt += 1
    print(cnt)


