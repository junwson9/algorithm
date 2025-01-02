
def solution(k, dungeons):
    cnt_arr = [n for n in range(len(dungeons))]
    v = [0]*len(cnt_arr)
    global mx
    mx = -1
    def dfs(n,tmp):
        global mx
        if n == len(dungeons):
            tmp_k = k
            cnt = 0
            for i in range(len(dungeons)):
                if tmp_k < dungeons[tmp[i]][0]:
                    break
                tmp_k -= dungeons[tmp[i]][1]
                cnt += 1
                
            if cnt >= mx:
                mx = cnt
            return
        
        for i in range(len(cnt_arr)):
            if v[i] == 0:
                v[i] = 1
                dfs(n+1,tmp+[cnt_arr[i]])
                v[i] = 0
    
    dfs(0,[])
    
    return mx