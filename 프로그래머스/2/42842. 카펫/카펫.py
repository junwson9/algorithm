def solution(brown, yellow):
    # 조건은 (가로+2)*2+(세로*2) 브라운이되어야함
    
    answer = []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            if (i+2)*2+(yellow//i)*2 == brown:
                answer.append(i+2)
                answer.append(yellow//i+2)
                break
    answer.sort(reverse=True)

    return answer