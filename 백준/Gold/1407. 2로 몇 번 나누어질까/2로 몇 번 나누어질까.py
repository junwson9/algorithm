import sys
input = sys.stdin.readline
A,B = map(int, input().split())
def calc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return n // 2 + 2*calc(n//2)
    elif n % 2 == 1:
        return n // 2 + 2*calc(n//2)+1
print(calc(B)-calc(A-1))


