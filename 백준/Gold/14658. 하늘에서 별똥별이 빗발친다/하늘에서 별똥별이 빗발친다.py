import sys
input = sys.stdin.readline
n,m,l,k = map(int,input().split())
stars = []

for _ in range(k):
    r,c = map(int,input().split())
    stars.append([r,c])

mx = 0
for i in range(k):
    for j in range(k):
        cnt = 0
        for cur in stars:

            if stars[i][0] <= cur[0] <= stars[i][0]+l and stars[j][1] <= cur[1] <= stars[j][1]+l:
                cnt += 1

        if cnt > mx:
            mx = cnt
print(k-mx)