N = int(input())
person = []
for _ in range(N):
    w,h = map(int, input().split())
    person.append((w,h))
rank = [1]*N
for i in range(N):
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank[i] += 1
print(*rank)