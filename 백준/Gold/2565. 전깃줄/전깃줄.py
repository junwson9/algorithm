N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0]) # A전봇대 순서대로 전깃줄 정렬
dp = [1]*N
for i in range(1,N):
    for j in range(i):
        if arr[j][1] < arr[i][1]: # 지금보고 있는 전깃줄의 B전봇대 보다 번호가 작은 B전봇대들을 카운트
            dp[i] = max(dp[i], dp[j]+1) #전깃줄이 안꼬인 경우가 가장많은 값을 갱신
print(N-max(dp))    #제거해주어야 하는 전깃줄 수는 전체에서 전깃줄이 안꼬이는 가장 많은경우를 빼준다