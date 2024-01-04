import math
def prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


number = input()
lst = []
rev = {'0':0, '1':1, '2':2, '3': 'notnum', '4': 'notnum', '5':5,'6':9,'7': 'notnum','8':8,'9':6}

for n in range(len(number)-1,-1,-1):
    lst.append(rev[number[n]])
if 'notnum' in lst:
    print('no')
else:
    rlt = ''.join(map(str,lst))
    if prime(int(rlt)) and prime(int(number)):
        print('yes')
    else:
        print('no')


