from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        t = q.popleft()
        for n in adjL[t]:
            if v[n] == 0:
                v[n] = 1
                q.append(n)





N, M = map(int, input().split())
peoples = list(map(int, input().split()))
v = [0]*(N+1)
adjL = [[] for _ in range(N+1)]
parties = []
ans = 0
for i in range(M):
    party = list(map(int, input().split()))
    party = party[1:]
    parties.append(party)
    for p in range(len(party)-1):
        for q in range(p+1,len(party)):
            adjL[party[p]].append(party[q])
            adjL[party[q]].append(party[p])


if len(peoples) == 1:
    ans = M
else:
    peoples = peoples[1:]
    for people in peoples:
        v[people] = 1
    for people in peoples:
        bfs(people)
    v = [x for x in range(1,len(v)) if v[x]]
    for party in parties:  # 각 파티별로
        if not (set(party) & set(v)):  # 아는 사람이 하나도 없다면
            ans += 1  # 과장된 이야기 할 수 있는 파티 개수 증가
print(ans)