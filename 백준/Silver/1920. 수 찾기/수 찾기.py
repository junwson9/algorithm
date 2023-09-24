import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst.sort()
target = list(map(int,input().split()))
def binary(target):
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == target:
            return True

        if target < lst[mid]:
            right = mid-1
        elif target > lst[mid]:
            left = mid+1

for i in range(M):
    if binary(target[i]):
        print(1)
    else:
        print(0)
