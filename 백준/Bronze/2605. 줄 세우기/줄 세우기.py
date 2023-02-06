import sys
N = int(sys.stdin.readline())
idx = list(map(int, sys.stdin.readline().split()))
ans = [1]
for i in range(1,N):
    ans.insert(idx[i], i+1)
reverse_ans = ans[::-1]
print(*reverse_ans)