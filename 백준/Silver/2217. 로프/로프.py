N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
mx = 0
for i in range(len(lst),0,-1):
    if lst[len(lst)-i]*i >= mx:
        mx = lst[len(lst)-i]*i
print(mx)