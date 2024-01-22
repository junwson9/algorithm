import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k,n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(4)]
    lst1 = []
    lst2 = []
    for i in range(n):
        for j in range(n):
            lst1.append(arr[0][i]+arr[1][j])
            lst2.append(arr[2][i]+arr[3][j])
    lst1.sort()
    lst2.sort()
    s = 0
    e = len(lst1)-1
    ans = 1e9
    tmp = abs(lst1[s]+lst2[e]-k)
    while True:
        if s >= len(lst1) or e < 0:
            break
        total = lst1[s] + lst2[e]
        if abs(total-k) < tmp:
            tmp = abs(total-k)
            ans = total
        if abs(total-k) == tmp and total < ans:
            ans = total

        if total-k > 0:
            e -= 1
        elif total-k < 0:
            s += 1
        else:
            e -= 1
            s += 1
    print(ans)

