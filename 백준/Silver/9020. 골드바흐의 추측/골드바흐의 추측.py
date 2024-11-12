import sys
from math import sqrt

input = sys.stdin.readline
T = int(input())
def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

for _ in range(T):
    a = b = 0
    diff = 1e9
    n = int(input())
    for i in range(2,n+1):
        if is_prime(i):
            if is_prime(n-i):
                if abs(i-(n-i)) < diff:
                    diff = abs(i-(n-i))
                    a = i
                    b = n-i
    print(a,b)


