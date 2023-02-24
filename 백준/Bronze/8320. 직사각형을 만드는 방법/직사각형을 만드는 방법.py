N = int(input())
if N < 4:
    print(N)
else:
    cnt = 0
    for i in range(1,N):
        for j in range(i,N//i+1):
            cnt += 1
    print(cnt)