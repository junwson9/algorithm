function solution(N, computers) {

    let visited = Array(N).fill(0)
    const dfs = (cur) => {
        visited[cur] = 1
        for (let i=0; i<N; i++){
            if (i === cur) continue
            if (visited[i]) continue
            if (computers[cur][i]) dfs(i)
        }
    }
    let ans = 0
    for (let i=0; i<N; i++) {
        if (visited[i]) continue
        dfs(i)
        ans += 1
    }
    
    return ans;
}