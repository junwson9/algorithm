N, M, L = map(int, input().split())
lst = [1]+[0]*(N-1) # 인덱스 = 자리 - 1
i = 0
cnt = 0
while True:
    if lst[i] == M:
        break
    if lst[i] % 2:
        i = (i+L) % N
    else:
        i = i-L
        if i < -N:
            i = i+N
    lst[i] += 1
    cnt += 1
print(cnt)
