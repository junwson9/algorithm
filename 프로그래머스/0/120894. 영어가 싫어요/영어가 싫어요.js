function solution(numbers) {
    var answer = '';
    var alpha = {'one': 1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
    var alp = ''
    for (const s of numbers){
        alp += s
        if (alp in alpha){
            answer += alpha[alp]
            alp = ''
        }
    }
    return Number(answer);
}