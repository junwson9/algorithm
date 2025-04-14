import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
lst = list(map(int,input().split()))
photo = []
time = 0
for student in lst:
    flag = 0
    for candi in photo:
        if student == candi[0]:
            candi[1] += 1
            flag = 1
            break
    if flag:
        continue

    if len(photo) < n:
        photo.append([student,1,time])
    else:
        photo.sort(key=lambda x:(x[1],x[2]))
        photo.pop(0)
        photo.append([student,1,time])
    time += 1
rlt = []
photo.sort(key=lambda x:x[0])
for i in range(len(photo)):
    rlt.append(photo[i][0])
print(*rlt)