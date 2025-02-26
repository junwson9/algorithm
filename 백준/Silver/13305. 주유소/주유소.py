import sys

input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
total = sum(road)
price = list(map(int,input().split()))
ans = 0
i = 0
for j in range(i+1,len(price)):

    if price[i] <= price[j]:
        ans += price[i]*road[j-1]
    else:
        ans += price[i]*road[j-1]
        i = j

print(ans )