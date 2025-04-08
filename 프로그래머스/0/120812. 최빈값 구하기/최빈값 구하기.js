function solution(array) {
    var answer = 0;
    const obj = {}
    for (let i =0; i<array.length; i++){
        const num = array[i];
        obj[num] = (obj[num] || 0) + 1;
    }
    
    let mx = 0;
    let arr = [];
    
    for (const key in obj){
        if (obj[key] > mx) {
            mx = obj[key]
        }
    }
    
    for (const key in obj) {
        if (obj[key] === mx){
            arr.push(key)
        }
    }
    if (arr.length > 1){
        answer = -1
    }
    else {
        answer = Number(arr[0])
    }
    return answer;
}