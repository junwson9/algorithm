def solution(sizes):
    answer = 0
    w = sizes[0][0]
    h = sizes[0][1]
    
    for i in range(1,len(sizes)):
        tmp1 = max(w,sizes[i][0])*max(h,sizes[i][1])
        tmp2 = max(w,sizes[i][1])*max(h,sizes[i][0])
        
        if tmp1 >= tmp2:
            w = max(w,sizes[i][1])
            h = max(h,sizes[i][0])
        
        if tmp1 < tmp2:
            w = max(w,sizes[i][0])
            h = max(h,sizes[i][1])
    
    answer = w*h

            
    
    return answer