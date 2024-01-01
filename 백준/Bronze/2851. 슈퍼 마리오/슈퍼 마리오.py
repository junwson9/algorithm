lst = [int(input()) for _ in range(10)]
sm = 0
check = 0
sm2 = 0
for i in range(len(lst)):
    sm += lst[i]
    if sm > 100:
        check = i
        break
sm2 = sm - lst[check]
if sm-100 <= 100-sm2:
    print(sm)
else:
    print(sm2)