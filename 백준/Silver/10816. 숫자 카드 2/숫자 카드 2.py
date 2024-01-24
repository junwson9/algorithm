import sys
input = sys.stdin.readline
N = int(input())
lst = sorted(list(map(int , input().split())))
M = int(input())
find = list(map(int ,input().split()))
for i in range(M):
    tmp = find[i]
    s = 0
    e = N-1
    l = 0
    while s <= e:
        mid = (s+e)//2
        if lst[mid] > tmp:
            e = mid-1
        elif lst[mid] < tmp:
            s = mid+1
        else:
            l = mid
            e = mid-1


    s = 0
    e = N-1
    r = -1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] < tmp:
            s = mid+1
        elif lst[mid] > tmp:
            e = mid-1
        else:
            r = mid
            s = mid+1

    print(r-l+1, end= ' ')