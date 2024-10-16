function solution(money) {
    var answer = [];
    let coffee = Math.floor(money/5500)
    answer.push(coffee)
    let rest = money%5500
    answer.push(rest)
    return answer;
}