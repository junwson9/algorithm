L = int(input())
N = int(input())
mx = 0
pk = [list(map(int, input().split())) for _ in range(N)]
cake = [0]*(L+1)
mx_person = 0
real = 0
real_person = 0
for i in range(N):
    if pk[i][1]-pk[i][0] > mx:
        mx = pk[i][1]-pk[i][0]
        mx_person = i+1
for i in range(N-1, -1, -1):
    for j in range(pk[i][0], pk[i][1]+1):
        cake[j] = i+1
for i in range(1,N+1):
    if cake.count(i) > real:
        real = cake.count(i)
        real_person = i
print(mx_person)
print(real_person)