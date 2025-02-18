import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
M = int(input())
find = list(map(int,input().split()))


for num in find:
    s = 0
    e = N-1
    ans = 0
    while s<=e:
        mid = (s+e)//2
        if lst[mid] < num:
            s = mid+1
        elif lst[mid] > num:
            e = mid-1
        else:
            ans = 1
            break
    print(ans,end=" ")


