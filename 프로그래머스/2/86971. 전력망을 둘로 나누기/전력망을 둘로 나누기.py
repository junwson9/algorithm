from collections import deque

def solution(n, wires):
    tree = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        a,b = wires[i]
        tree[a].append(b)
        tree[b].append(a)
        
    
    def bfs(start):
        q = deque([start])
        visited = [0]*(n+1)
        visited[start] = 1
        cnt = 1
        while q:
            cur = q.popleft()
            for nxt in tree[cur]:
                if visited[nxt] == 0:
                    q.append(nxt)
                    visited[nxt] = 1
                    cnt += 1
        return cnt
    
    answer = n
    
    for i in range(n-1):
        a,b = wires[i]
        tree[a].remove(b)
        tree[b].remove(a)
        answer = min(answer,abs(bfs(a)-bfs(b)))
        tree[a].append(b)
        tree[b].append(a)
                    
                
            

    

        

    return answer