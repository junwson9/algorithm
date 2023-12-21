import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
ans = 0
for i in range(k+1):
    for j in range(k+1):
        if (n-i)//2 >= (m-j) and m-j > 0 and (n-i)//2 > 0:
            if m-j > ans and i+j == k:
                ans = m-j
        elif (n-i)//2 < m-j and (n-i)//2 > 0 and m-j > 0:
            if (n-i)//2 > ans and i+j == k:
                ans = (n-i)//2
print(ans)