import math
def solution(n):
    answer = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            if n//i != i:
                answer += n//i
                answer += i
            else:
                answer += i
    return answer