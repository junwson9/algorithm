def solution(brown, yellow):
    s = 1
    e = yellow
    answer = []
    rlt = []
    while True:
        if s > e:
            break
        if yellow % s == 0:
            tmp = (s+2)*2 + e*2
            if tmp == brown:
                answer += [s+2,e+2]
                break
        s += 1
        e = yellow//s
    answer.sort(reverse=True)
    return answer