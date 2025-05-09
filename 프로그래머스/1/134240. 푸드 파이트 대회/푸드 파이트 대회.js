function solution(food) {
    var answer = '';
    for (let i=1; i< food.length; i++){
        if (food[i] < 2) continue
        
        answer += i.toString().repeat(Math.floor(food[i]/2))
    }
    const back = answer.split('').reverse().join('')
    
    answer += '0'+back
    
    return answer;
}