import sys

input = sys.stdin.readline
a,b = map(int,input().split())


def gcd(a,b):
    if a > b:
        while b:
            a,b = b, a%b
        return a
    elif b > a:
        while a:
            b,a = a, b%a
        return b
    else:
        return a

def lcd(a,b):
    return a*b//gcd(a,b)



print(gcd(a,b))
print(lcd(a,b))
