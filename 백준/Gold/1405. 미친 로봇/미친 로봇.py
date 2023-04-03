def dfs(n,si,sj,sm):
    global ans
    if sm == 0: # 가지치기 -> 0나온다는건 아예그방향으로 못가는 0 확률을 곱한거라 걍 바로 리턴
        return
    if n == N:
        ans += sm   #0거르고 자리중복 없는 확률들만 더한다
        return

    for d in range(4):
        ni,nj = si+dr[d][0], sj+dr[d][1]
        if v[ni][nj] == 0:
            v[ni][nj] = 1
            dfs(n+1,ni,nj,sm*p[d]*0.01)
            v[ni][nj] = 0
lst = list(map(int, input().split()))
N = lst[0]  #로봇 작동횟수
p = lst[1:] #확률들
ans = 0
dr = [(0,1),(0,-1),(1,0),(-1,0)]    #동서남북
v = [[0]*(2*N+1) for _ in range(2*N+1)] #14번다 똑같은데로 가도 인덱스에러 안나는 크기 v 만들고
v[N][N] = 1 # 정가운데 시작
dfs(0,N,N,1)
print(ans)
