from itertools import permutations
import math
def solution(numbers):
    answer = 0
    rlt = []
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    numb = [n for n in numbers]
    num_lst = []
    for i in range(1,len(numbers)+1):
        num_lst += (list(permutations(numb,i)))
    for n in num_lst:
        ans = int(''.join(n))
        if isPrime(ans):
            rlt.append(ans)
    answer = len(set(rlt))
           
    return answer