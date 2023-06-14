N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
ans = []
for r in range(N-7):
    for c in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for i in range(r,r+8):
            for j in range(c,c+8):
                if (i+j)%2 == 0:
                    if arr[i][j] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if arr[i][j] != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
        ans.append(w_cnt)
        ans.append(b_cnt)

print(min(ans))



