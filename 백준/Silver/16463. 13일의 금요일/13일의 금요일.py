import sys

input = sys.stdin.readline

N = int(input())

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isleap(n):
    if n%400 != 0 and n%100 == 0:
        return False

    if n%400 == 0:
        return True

    if n%100 != 0 and n%4 == 0:
        return True
    return False

start = 1
ans = 0
for y in range(2019,N+1):
    for m in range(1,13):
        if (start+12)%7 == 4:
            ans += 1

        if m == 2 and isleap(y):
            start += 29
        else:
            start += days[m]


print(ans)