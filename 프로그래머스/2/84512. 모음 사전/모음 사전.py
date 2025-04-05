def solution(word):

    alpha = ['A','E','I','O','U']
    dict = []
    def dfs(st,n):
        if n == 5:
            return
        
        for w in alpha:
            dict.append(st+w)
            dfs(st+w,n+1)
    
    dfs('',0)

    return dict.index(word)+1