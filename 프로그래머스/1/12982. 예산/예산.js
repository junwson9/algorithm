function solution(d, budget) {
    var answer = 0;
    d.sort((a,b) => a-b)
    for (let i of d){
        if (budget-i >= 0) {
            answer += 1
            budget -= i
        }
    }

    return answer;
}