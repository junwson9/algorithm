import sys
input = sys.stdin.readline
n = 1000000
is_prime = [True]*(n+1)
is_prime[1] = False
M,N = map(int,input().split())

for i in range(2,int(n**0.5)+1):
    if not is_prime[i]:
        continue
    for j in range(i*i,n+1,i):
        is_prime[j] = False

for check in range(M,N+1):
    if is_prime[check]:
        print(check)

