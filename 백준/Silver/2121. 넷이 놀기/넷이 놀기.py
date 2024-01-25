import sys
input = sys.stdin.readline
N = int(input())
A,B = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0],x[1]))
ans = 0
def ok(find):
    s = 0
    e = N-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < find:
            s = mid+1
        elif arr[mid] > find:
            e = mid-1
        else:
            return True
    return False

for x,y in arr:
    find1 = [x+A,y]
    find2 = [x, y+B]
    find3 = [x+A, y+B]

    if ok(find1) and ok(find2) and ok(find3):
        ans += 1

print(ans)



