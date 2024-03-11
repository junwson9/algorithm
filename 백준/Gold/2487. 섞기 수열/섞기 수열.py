import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
mix = [0]+list(map(int, input().split()))
v = [False]*(N+1)
def dfs(n,cnt):
    v[n] = True
    if v[mix[n]]:
        return cnt
    else:
        return dfs(mix[n],cnt+1)


def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a//gcd(a,b)*b
ans = 1
for i in range(1,N+1):
    if v[i]:
        continue
    ans = lcm(ans,dfs(i,1))
print(ans)


