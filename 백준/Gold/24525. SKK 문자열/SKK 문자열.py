from collections import defaultdict
S = list(input())
prefix_sum = [0]*(len(S)+1)
cnt = [0]*(len(S)+1)
idx = defaultdict(int)
ans = -1
for i in range(len(S)):
    tmp = 0
    if S[i] == 'S':
        tmp = 2
    elif S[i] == 'K':
        tmp = -1
    prefix_sum[i+1] = prefix_sum[i] + tmp
    if tmp == 0:
        cnt[i+1] = cnt[i]
    else:
        cnt[i+1] = cnt[i]+1
for i in range(len(S)+1):
    if prefix_sum[i] not in idx:
        idx[prefix_sum[i]] = i
    else:
        midx = idx[prefix_sum[i]]
        if cnt[midx] == cnt[i]:
            continue
        ans = max(ans, i - midx)
print(ans)

