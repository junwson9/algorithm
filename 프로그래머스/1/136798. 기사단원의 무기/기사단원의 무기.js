function solution(number, limit, power) {
    var answer = 0;
    let lst = []
    
    function div(n){
        let tmp = 0
        for (let i=1; i < parseInt(Math.sqrt(n))+1; i++){
            if (n%i === 0) {
                if (i === n/i){
                    tmp += 1

                }
                else {
                    tmp += 2
                }
            }
        }
        
        return tmp > limit ? power : tmp
    }
    
    for (let i=1; i<number+1;i++){
        lst.push(div(i))
    }
    
    for (let n of lst){
        answer += n
    }
    
    return answer;
}