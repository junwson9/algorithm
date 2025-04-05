import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
lst = list(map(int,input().split()))

cards.sort()


rlt = []

for i in range(M):
    s = 0
    e = N-1
    find = lst[i]
    answer = 0
    while s<=e:
        mid = (s+e)//2
        if cards[mid] < find:
            s = mid+1
        elif cards[mid] > find:
            e = mid-1
        else:
            answer = 1
            break
    rlt.append(answer)
print(*rlt)