import sys
input = sys.stdin.readline
a,d = map(int, input().split())
q = int(input())
for _ in range(q):
    check,l,r = map(int, input().split())
    if check == 1:
        print((r-l+1)*(a+(l-1)*d+a+(r-1)*d)//2)
    else:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        if l == r:
            print(a+(l-1)*d)
        else:
            print(gcd(a,d))

