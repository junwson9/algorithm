from collections import deque
def bfs(adjL,v,start):
    q = deque()
    q.append(start)
    v[start] = 1
    cnt = 0
    while q:
        t = q.popleft()
        cnt += 1
        for i in adjL[t]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
    return cnt
    

def solution(n, wires):
    mn = n
    for i in range(len(wires)):
        v = [0]*(n+1)
        adjL = [[] for _ in range(n+1)]
        tmp = wires.copy()
        tmp.pop(i)
        start = 0
        for s,e in tmp:
            adjL[s].append(e)
            adjL[e].append(s)
        for s in range(len(adjL)):
            if adjL[s] != []:
                start = s
                break
        cnts = bfs(adjL,v,start)
        other_cnts = n-cnts
        if abs(cnts - other_cnts) < mn:
            mn = abs(cnts-other_cnts)
        
        
    return mn