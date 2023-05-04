N = int(input())
a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))
ans = 0
for _ in range(N):
    ans += min(a_lst)*max(b_lst)
    a_lst.remove(min(a_lst))
    b_lst.remove(max(b_lst))
print(ans)