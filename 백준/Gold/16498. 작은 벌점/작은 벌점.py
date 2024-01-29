import sys
input = sys.stdin.readline
A,B,C = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))
a_lst.sort()
b_lst.sort()
c_lst.sort()
ans = 1e9
def ok(n,lst):
    s = 0
    e = len(lst)-1
    tmp = lst[s]
    while s<=e:
        mid = (s+e)//2
        if n == lst[mid]:
            return n
        elif n > lst[mid]:
            s = mid+1
        else:
            e = mid-1
        if abs(lst[mid]-n) < abs(tmp-n):
            tmp = lst[mid]
    return tmp

for i in range(len(a_lst)):
    tmp_b = ok(a_lst[i],b_lst)
    tmp_c1 = ok(tmp_b,c_lst)
    tmp_c2 = ok(a_lst[i],c_lst)
    mx1 = max(max(a_lst[i],tmp_b),tmp_c1)
    mn1 = min(min(a_lst[i],tmp_b),tmp_c1)
    rlt1 = mx1-mn1
    mx2 = max(max(a_lst[i],tmp_b),tmp_c2)
    mn2 = min(min(a_lst[i],tmp_b),tmp_c2)
    rlt2 = mx2-mn2
    ans = min(ans,min(rlt1,rlt2))
print(ans)



