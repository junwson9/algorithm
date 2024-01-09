import sys
input = sys.stdin.readline
N,K,A,B = map(int,input().split())
plant= [K]*N
ans = 0
while True:
    if 0 in plant:
        break
    for i in range(A):
        plant[i] += B
    
    for i in range(len(plant)):
        plant[i] -= 1
    
    plant.sort()

    ans +=1
print(ans)
