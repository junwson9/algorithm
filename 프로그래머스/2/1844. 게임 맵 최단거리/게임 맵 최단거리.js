function solution(maps) {
    var answer = 0;
    const n = maps.length
    const m = maps[0].length
    const visited = Array(n).fill().map(e => Array(m).fill(0))
    const si = 0
    const sj = 0
    const di = [1,0,-1,0]
    const dj = [0,-1,0,1]
    
    const bfs = (si,sj) => {
        const q = [[si,sj]]
        visited[si][sj] = 1
        while (q.length > 0){
            const [ci,cj] = q.shift()
            for (let dr = 0; dr < 4; dr++){
                let ni = ci+di[dr]
                let nj = cj+dj[dr]
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue
                if (maps[ni][nj] === 1 && visited[ni][nj] === 0){
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.push([ni,nj])
                }
            }
        }
        return visited[n-1][m-1]
    }
    const rlt = bfs(0,0)
    return rlt === 0 ? -1 : rlt
}