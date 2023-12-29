import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    x,y = map(int, input().split())
    lst.append((x,y))
ans = 0
for i in range(N-1):
    ans += abs(lst[i][0]-lst[i+1][0])+abs(lst[i][1]-lst[i+1][1])
mx = 0
for i in range(1,N-1):
    skip = abs(lst[i+1][0]-lst[i-1][0])+abs(lst[i+1][1]-lst[i-1][1])
    total = abs(lst[i][0]-lst[i-1][0])+abs(lst[i][1]-lst[i-1][1])+abs(lst[i][0]-lst[i+1][0])+abs(lst[i][1]-lst[i+1][1])
    mx = max(mx,total-skip)
print(ans-mx)






