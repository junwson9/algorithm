def solution(board, skill):
    cnt = 0
    sum_arr = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    #구간합 구할거 세팅
    for tp, r1, c1, r2, c2, dg in skill:
        if tp == 1:
            sum_arr[r1][c1] -= dg
            sum_arr[r1][c2+1] += dg
            sum_arr[r2+1][c1] += dg
            sum_arr[r2+1][c2+1] -= dg
        else:
            sum_arr[r1][c1] += dg
            sum_arr[r1][c2+1] -= dg
            sum_arr[r2+1][c1] -= dg
            sum_arr[r2+1][c2+1] += dg
    #행으로 더하기
    for i in range(len(board)+1):
        for j in range(1,len(board[0])+1):
            sum_arr[i][j] += sum_arr[i][j-1]
    #열로 더하기
    for j in range(len(board)+1):
        for i in range(1, len(board)+1):
            sum_arr[i][j] += sum_arr[i-1][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sum_arr[i][j]
            if board[i][j] >= 1:
                cnt += 1
            
    return cnt