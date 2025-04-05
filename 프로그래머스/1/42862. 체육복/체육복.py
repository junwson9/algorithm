def solution(n, lost, reserve):
    answer = 0
    answer += n-len(lost)
    new_lost = []
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        else:
            new_lost.append(i)


    lost = new_lost
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
                
    
    
    return answer