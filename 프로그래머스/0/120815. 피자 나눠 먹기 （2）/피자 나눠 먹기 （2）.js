function solution(n) {
    var answer = 0;
    var lcd = 0;
    for (let i = Math.max(6,n); i <= 6*n; i++){
        if (i%6 === 0 && i%n === 0){
            lcd = i
            break
        }
    }
    answer = lcd/6
    return answer;
}