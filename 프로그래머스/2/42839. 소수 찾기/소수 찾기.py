import math
def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    
    v = [0]*len(numbers)
    num = []
    arr = list(numbers)
    print(arr)
    def dfs(n,tmp):

        
        if n == len(numbers):
            if tmp == '':
                return
            if int(tmp) not in num:
                    num.append(int(tmp))
            return
        
        for i in range(len(numbers)):
            if v[i] == 0:
                v[i] = 1
                dfs(n+1,tmp+arr[i])
                dfs(n+1,tmp)
                v[i] = 0
            
    dfs(0,'')
    answer = 0
    for n in num:
        if is_prime(n):
            answer += 1
        
    
    
    return answer