function solution(a, b, n) {
    let answer = 0;
    while (n >= a) {
        const change = Math.floor(n/a)*b;
        answer += change;
        n = Math.floor(n/a)*b+(n%a);
    }
    return answer;
}
