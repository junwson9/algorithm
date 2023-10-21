from itertools import permutations
def solution(k, dungeons):
    lst = [i for i in range(len(dungeons))]
    order_lst = list(permutations(lst,len(lst)))
    mx = 0
    for order in order_lst:
        tmp_k = k
        tmp = 0
        for n in order:
            if tmp_k >= dungeons[n][0]:
                tmp_k -= dungeons[n][1]
                tmp += 1
            else:
                continue
        if tmp >= mx:
            mx = tmp
            
    return mx