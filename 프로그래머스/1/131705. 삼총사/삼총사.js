function solution(number) {
    var answer = 0;
    
    const dfs = (n,idx,sm) => {
        if (n === 3){
            if (sm === 0){
                answer += 1
            }
            return
        }
        
        for (let i=idx; i < number.length; i++){
            dfs(n+1,i+1,sm+number[i])
        }
    }
    dfs(0,0,0)
    
    return answer;
}