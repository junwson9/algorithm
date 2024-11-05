function solution(balls, share) {
    var answer = 0;
    if (balls === share){
        return 1
    }
    else {
    function fact(n) {
        if (n < 2) return BigInt(1)
        return BigInt(n)*fact(n-1)
    }

    
    answer = fact(balls)/(fact(balls-share)*fact(share))
    return answer;
    }
}