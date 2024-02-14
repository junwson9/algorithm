import sys
input = sys.stdin.readline
n = 1000001
is_prime = [True]*(n+1)
is_prime[1] = False

for i in range(2,int(n**0.5)+1):
    if is_prime[i] == False:
        continue
    for j in range(i*i,n+1,i):
        is_prime[j] = False


T = int(input())
for _ in range(T):
    ans = 0
    N = int(input())
    for n in range(2,N):
        if is_prime[n]:
            if is_prime[N-n]:
                if n == N-n:
                    ans += 1
                else:
                    ans += 1/2

    print(int(ans))


