H, W = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, W-1):
    if max(lst[:i]) > lst[i] and max(lst[i:W]) > lst[i]:
        cnt += min(max(lst[:i]), max(lst[i:W]))-lst[i]
print(cnt)