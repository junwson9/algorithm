lst = list(input())
start = lst[0]
if lst[0] == '1':
    cnt_1 = 1
    cnt_2 = 0
else:
    cnt_2 = 1
    cnt_1 = 0
for i in range(1,len(lst)):
    if lst[i] != start:
        if start == '1':
            cnt_2 += 1
        if start == '0':
            cnt_1 += 1
        start = lst[i]
print(min(cnt_1, cnt_2))