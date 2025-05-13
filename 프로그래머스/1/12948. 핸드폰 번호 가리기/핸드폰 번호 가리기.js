function solution(phone_number) {
    var answer = '';
    const star_cnt = phone_number.length-4
    answer += '*'.repeat(star_cnt)
    const non_star = phone_number.slice(phone_number.length-4,phone_number.length)
    answer += non_star
    return answer;
}