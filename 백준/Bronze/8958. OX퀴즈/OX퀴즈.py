T = int(input())
for _ in range(T):
    st = input()
    ans = 0
    score = 0
    for s in st:
        if s == 'O':
            score += 1
            ans += score
        else:
            score = 0
    print(ans)