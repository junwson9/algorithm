def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        
        limit = (schedules[i]//100)*100+(schedules[i]%100+10)%60+((schedules[i]%100+10)//60)*100
        
        flag = 0
        for j in range(7):
            weekend = (startday+j)%7
            if weekend == 6 or weekend == 0:
                continue
            else:
                if timelogs[i][j] > limit:
                    flag = 1
                    break
        if flag == 0:
            answer += 1
            
                    
                
        
    return answer