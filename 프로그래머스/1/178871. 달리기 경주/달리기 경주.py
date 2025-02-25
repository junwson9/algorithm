def solution(players, callings):
    answer = {}
    for i in range(len(players)):
        answer[players[i]] = i
        
        
    for call in callings:
        cur = answer[call]
        front = players[cur-1]
        
        players[cur-1], players[cur] = players[cur], players[cur-1]
        answer[front] += 1
        answer[call] -= 1
        
    

    
    return players