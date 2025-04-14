function solution(n)
{
    var answer = 0;
    str = n.toString()
    for (let n of str){
        answer += Number(n)
    }

    return answer;
}