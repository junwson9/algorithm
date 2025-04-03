from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    usdict = defaultdict(set)
    numdict = defaultdict(int)
    
    for i in range(len(report)):
        ke,v = report[i].split()
        usdict[ke].add(v)
        numdict[v] += 1

    
    for name in id_list:
        rlt = 0
        for nm in usdict[name]:
            if numdict[nm] >= k:
                rlt += 1
        answer.append(rlt)
        
            
            


    
    return answer