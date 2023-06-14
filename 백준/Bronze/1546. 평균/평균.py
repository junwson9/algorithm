N = int(input())
lst = list(map(int, input().split()))
mx = max(lst)
ans = 0
for n in lst:
    ans += n/mx*100
ans = ans/N
print(ans)