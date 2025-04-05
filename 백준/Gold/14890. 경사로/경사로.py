import sys
input = sys.stdin.readline
n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0

def check(lst):
    v = [0]*n
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            continue

        elif abs(lst[i]-lst[i+1]) > 1:
            return False
        elif lst[i] > lst[i+1]:
            tmp = lst[i+1]
            for j in range(i+1,i+l+1):
                if 0 <= j < n:
                    if lst[j] != tmp:
                        return False

                    elif v[j]:
                        return False

                    v[j] = 1
                else:
                    return False
        else:
            tmp = lst[i]
            for j in range(i,i-l,-1):
                if 0 <= j < n:
                    if lst[j] != tmp:
                        return False
                    elif v[j]:
                        return False

                    v[j] = 1
                else:
                    return False
    return True

for row in arr:
    ans += check(row)

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    ans += check(tmp)

print(ans)