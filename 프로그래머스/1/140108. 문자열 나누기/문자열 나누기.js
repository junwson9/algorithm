function solution(s) {
    var answer = 0;
    while (s.length > 0){
        const x = s[0]
        let same = 0
        let diff = 0
        for (let i=0; i<s.length; i++){
            if (s[i] === x){
                same += 1
            }
            else {
                diff += 1
            }
            if (same === diff){
                answer += 1
                s = s.slice(i+1)
                break
            }
            if (i === s.length-1){
                answer += 1
                s = ''
            }
        }

        
    }
    return answer;
}