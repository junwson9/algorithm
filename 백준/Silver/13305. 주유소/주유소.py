import sys

input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
total = sum(road)
price = list(map(int,input().split()))
ans = 0
i = 0
for j in range(i+1,len(price)-1):
    if price[i] <= price[j]:
        ans += price[i]*road[j-1]
        continue
    ans += sum(road[i:j])*price[i]
    i = j

print(ans + price[i]*road[-1])