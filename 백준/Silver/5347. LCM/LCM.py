import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    def gcd(a,b):
        while b > 0:
            a,b = b, a%b
        return a
    ans = a*b//gcd(a,b)
    print(ans)



