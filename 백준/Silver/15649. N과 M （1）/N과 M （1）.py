def bt(n):
    if n == M:
        print(' '.join(map(str, stk)))
        return  #종료 조건 - 들어갔는데 M과 깊이가 같아지면 한칸띄우고 출력
    for i in range(1, N+1):
        if visit[i] == 0:
            visit[i] = 1    #방문한곳 표시
            stk.append(i) #1부터 방문안했으면  추가
            bt(n+1) #다음 깊이로 드감
            visit[i] = 0    #올라갈때 visit초기화 해주면서 올라감
            stk.pop()   #위 단계로 올라올때 pop임



N, M = map(int, input().split())
# 1부터 N까지 숫자들로 M길이 수열 출력하는 단순한문제
visit = [0]*(N+1)
stk = []
bt(0)