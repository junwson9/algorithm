def solution(wallpaper):
    answer = []
    si = len(wallpaper)
    sj = len(wallpaper[0])
    ei = 0
    ej = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < si:
                    si = i
                if j < sj:
                    sj = j
                if i > ei:
                    ei = i
                if j > ej:
                    ej = j

    answer = [si,sj,ei+1,ej+1]
    return answer