def solution(lst, k):
    answer = [0,len(lst)]
    s = 0
    e = 0
    sm = lst[0]
    while True:
        if sm < k:
            e += 1
            if e >= len(lst):
                break
            sm += lst[e]
        else:
            if sm == k:
                if e-s < answer[1]-answer[0]:
                    answer = [s,e]
            sm -= lst[s]
            s += 1
                

    return answer