Round = int(input())
for _ in range(Round):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = A[1:]
    B = B[1:]
    acnt = []
    bcnt = []
    for i in range(4,0,-1):
        acnt.append(A.count(i))
        bcnt.append(B.count(i))
    for c in range(4):
        if acnt[c] > bcnt[c]:
            winner = 'A'
            break
        elif acnt[c] < bcnt[c]:
            winner = 'B'
            break
        else:
            winner = 'D'
    print(f'{winner}')
