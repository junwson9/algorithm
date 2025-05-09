function solution(nums) {
    var answer = 0;
    const monster = {}
    for (let i of nums) {
        monster[i] = (monster[i] || 0) + 1
    }
    
    const kind = Object.keys(monster).length
    if (kind >= nums.length/2) {
        answer = nums.length/2
    }
    else {
        answer = kind
    }
    
    return answer;
}