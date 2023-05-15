def fibo(N):
    zero = [1,0,1]
    one = [0,1,1]
    if N >= 3:
        for i in range(2,N):
            zero.append(zero[i-1]+zero[i])
            one.append(one[i-1]+one[i])
    print(zero[N],one[N])

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)