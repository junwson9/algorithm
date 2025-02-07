import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
M = int(input())
find = list(map(int,input().split()))

lst.sort()

answer = []

def binary_search (s,e,i):
    while s<=e:
        mid = (s+e)//2
        if lst[mid] < find[i]:
            s = mid+1
        elif lst[mid] > find[i]:
            e = mid-1
        else:
            return 1
    return 0



for i in range(len(find)):
    s = 0
    e = len(lst)-1
    answer.append(binary_search(s,e,i))


print(*answer)



