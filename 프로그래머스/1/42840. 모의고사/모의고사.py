def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            cnt1 += 1
        if answers[i] == two[i%8]:
            cnt2 += 1
        if answers[i] == three[i%10]:
            cnt3 += 1

    cnt = [cnt1,cnt2,cnt3]
    
    mx = max(cnt)
    if cnt1 == mx:
        answer.append(1)
    if cnt2 == mx:
        answer.append(2)
    if cnt3 == mx:
        answer.append(3)

        
    return answer