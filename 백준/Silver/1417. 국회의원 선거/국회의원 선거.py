import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
cnt = int(input())
lst = []
for _ in range(N-1):
    lst.append(int(input()))
people = 0
if len(lst) == 0:
    print(people)
else:
    while True:
        lst.sort(reverse=True)
        if lst[0] < cnt and max(lst) < cnt:
            break
        cnt += 1
        people += 1
        lst[0] -= 1
    print(people)