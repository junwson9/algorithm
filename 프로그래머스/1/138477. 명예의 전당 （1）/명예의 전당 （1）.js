function solution(k, score) {
    var answer = [];
    var scores = [];
    
    for (let i=0; i< score.length; i++){
        if (scores.length < k){
            scores.push(score[i])
        }
        else {
            const tmp = Math.min(...scores)
            if (score[i] > tmp){
                scores.sort((a,b) => b-a)
                scores.pop()
                scores.push(score[i])
            }
        }

        const mn = Math.min(...scores)
        answer.push(mn)
        
    }
    
    return answer;
}