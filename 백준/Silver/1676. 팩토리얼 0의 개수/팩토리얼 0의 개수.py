def fact(N):
    if N < 2:
        return 1

    return N*fact(N-1)

N = int(input())
num = fact(N)
cnt = 0
while True:
    if num%10 != 0:
        break
    num = num//10
    cnt += 1
print(cnt)