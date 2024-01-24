import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    ans = 0
    def ok(s,e,tmp):
        while s<=e:
            mid = (s+e)//2
            if lst[mid] > tmp:
                e = mid-1
            elif lst[mid] < tmp:
                s = mid+1
            else:
                return True
        return False
    for s in range(N-2):
        for e in range(s+2,N):
            tmp = (lst[s]+lst[e])/2
            if ok(s,e,tmp):
                ans += 1
    print(ans)