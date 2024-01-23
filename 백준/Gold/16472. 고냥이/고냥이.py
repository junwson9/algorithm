import sys
input = sys.stdin.readline
N = int(input())
lst = list(input().strip())
s = 0
e = 0
ans = 0
word = {}
while True:
    if e >= len(lst):
        break
    if lst[e] not in word:
        word[lst[e]] = 1
    else:
        word[lst[e]] += 1
    while True:
        if len(word) <= N:
            break
        word[lst[s]] -= 1
        if word[lst[s]] == 0:
            word.pop(lst[s])
        s += 1
    ans = max(ans, e-s+1)
    e += 1
print(ans)


