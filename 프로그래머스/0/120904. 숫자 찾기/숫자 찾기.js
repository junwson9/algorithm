function solution(num, k) {
    var answer = -1;
    num = num.toString()
    k = k.toString()
    num = [...num]
    for (let s=0;s<num.length;s++){
        if ( num[s] === k){
            answer = s+1
            break
        }
    }
    return answer;
}