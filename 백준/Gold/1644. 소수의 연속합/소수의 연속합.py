import sys
input = sys.stdin.readline
N = int(input())
ans = 0
if N == 1:
    print(ans)
else:
    is_prime = [True]*(N+1)
    is_prime[1] = False
    for i in range(2,N+1):
        if not is_prime: continue
        for j in range(i*i,N+1,i):
            is_prime[j] = False
    p_lst = []
    for i in range(2,N+1):
        if is_prime[i] == True:
            p_lst.append(i)
    if len(p_lst) == 1 and p_lst[0] == 2:
        print(1)
    else:
        s = 0
        e = 1
        total = p_lst[e]+p_lst[s]
        while True:
            if total < N:
                e += 1
                if e >= len(p_lst):
                    break
                total += p_lst[e]
            elif total > N:
                total -= p_lst[s]
                s += 1
            else:
                total -= p_lst[s]
                s += 1
                ans += 1
        print(ans)
