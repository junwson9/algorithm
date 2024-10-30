function solution(array) {
    var answer = [];
    var mx = -Infinity;
    var idx;
    
    for (let i=0; i <array.length; i++){
        if (array[i] > mx) {
            mx = array[i]
            idx = i
        }
    }
    answer.push(mx,idx)
    return answer;
}