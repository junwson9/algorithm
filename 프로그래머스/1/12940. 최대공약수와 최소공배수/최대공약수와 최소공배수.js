function solution(n, m) {
    var answer = [];
    function gcd(a,b){
        while (b !== 0){
            let tmp = b
            b = a%b
            a = tmp
        }
        return a
    }
    if (n > m) {
        let g = gcd(n,m)
        let lcd = n*m/g
        answer.push(g,lcd)
        

    }
    else {
        let g = gcd(m,n)
        let lcd = n*m/g
        answer.push(g,lcd)
       
    }
    
    return answer;
}