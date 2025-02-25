def solution(n, w, number):
    answer = 0
    
    if n%w:    
        arr = [[0]*w for _ in range(n//w+1)]
    else:
        arr = [[0]*w for _ in range(n//w)]
        
    N = len(arr)-1
    num = 1
    for x in range(N,-1,-1):
        if x%2 == N%2:
            for y in range(w):
                arr[x][y] = num
                num += 1
                

        else:
            for y in range(w-1,-1,-1):
                arr[x][y] = num
                num += 1
                
    
    for i in range(N):
        for j in range(w):
            if arr[i][j] > n:
                arr[i][j] = 0
    
    
    find_x = 0
    find_y = 0
    
    for i in range(len(arr)):
        for j in range(w):
            if arr[i][j] == number:
                find_x = i
                find_y = j
                
                
    for i in range(find_x,-1,-1):
        if arr[i][find_y] != 0:
            answer += 1
    
    
        
        
        
        
    print(find_x,find_y)
    print(arr)
    return answer