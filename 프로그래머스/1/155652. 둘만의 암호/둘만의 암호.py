def solution(s, skip, index):
    answer = ''
    tmp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha = []
    for alp in tmp:
        if alp in skip:
            continue
        alpha.append(alp)
    print(alpha)
    for i in range(len(s)):
        compare = s[i]
        for j in range(len(alpha)):
            if compare == alpha[j]:
                answer += alpha[(j+index)%len(alpha)]
    return answer