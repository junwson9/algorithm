function solution(n) {
    var answer = [];
    let str = n+''
    for (let num of str){
        answer.push(parseInt(num))
    }
    answer.reverse()
    return answer;
}