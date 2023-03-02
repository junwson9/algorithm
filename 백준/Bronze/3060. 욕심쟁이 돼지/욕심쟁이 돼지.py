T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sm = 0
    ans = 1
    for n in lst:
        sm += n
    if sm <= N:
        sm = 0
        new = [0]*6
        while True:
            ans += 1
            for i in range(6):
                L = 1+i
                R = 5+i
                M = 3+i
                if L > 5:
                    L = L%6
                if R > 5:
                    R = R%6
                if M > 5:
                    M = M%6
                new[i] = lst[L]+lst[R]+lst[M]+lst[i]
            sm = sum(new)
            if sm > N:
                break
            lst = new
            new = [0]*6
    print(ans)