import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a


a,b = map(int,input().split())
c,d = map(int,input().split())

s = a*d+c*b
m = b*d
tmp = gcd(s,m)
print(s//tmp,m//tmp)