def solution(cards1, cards2, goal):
    answer = 'Yes'
    for word in goal:
        if word in cards1 and cards1[0] == word:
            cards1 = cards1[1:]
        
        elif word in cards2 and cards2[0] == word:
            cards2 = cards2[1:]
            
        
        else:
            answer = 'No'
            break
            
        
        
    return answer