import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split())
ans1 = -a+math.sqrt(math.pow(a,2)-b)
ans2 = -a-math.sqrt(math.pow(a,2)-b)
ans1 = int(ans1)
ans2 = int(ans2)
if ans1 > ans2:
    print(f'{ans2} {ans1}')
elif ans1 < ans2:
    print(f'{ans1} {ans2}')
else:
    print(ans1)