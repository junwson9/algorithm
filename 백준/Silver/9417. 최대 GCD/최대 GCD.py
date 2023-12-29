import sys
import math
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    mx = 1
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            tmp = math.gcd(lst[i],lst[j])
            if tmp > mx:
                mx = tmp
    print(mx)



