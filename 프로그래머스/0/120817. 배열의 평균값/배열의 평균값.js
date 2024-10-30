function solution(numbers) {
    var answer = 0;
    const sm = numbers.reduce((a,b)=> a+b)
    answer = sm/numbers.length
    return answer;
}