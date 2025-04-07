def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for names in photo:
        rlt = 0
        for nm in names:
            if nm in dict:
                rlt += dict[nm]
        answer.append(rlt)
    return answer