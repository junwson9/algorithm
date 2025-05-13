function solution(numbers) {
    var answer = -1;
    const sm = numbers.reduce((acc,cur) => acc+cur,0)
    answer = 45-sm
    return answer;
}