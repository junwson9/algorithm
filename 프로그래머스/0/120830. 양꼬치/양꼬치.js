function solution(n, k) {
    var answer = 0;
    var sheep = n*12000
    var can = 0
    if (n < 10){
        can = k*2000
    }
    else {
        var n = Math.floor(n/10)
        can = (k-n)*2000
    }
    answer = sheep+can
    return answer;
}