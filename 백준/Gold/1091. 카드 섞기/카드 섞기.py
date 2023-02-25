N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
ans = 0
first = [0, 1, 2]*(N//3)    #맨처음 상태 카드 만들기
suffle = [0]*len(first)

i = 0
while True:
    if first == P:      #지민이가 원하는데로 보내면 끝
        break
    suffle[i] = first[S[i]] #셔플에다가 S에 적힌 순서대로 first에서 가져와 넣을거임
    i += 1
    if i == len(suffle):    #한번 다 돌리면 ans에 1추가, 섞인상태에서
                            #다시 S에 적힌순서로 돌려야 하기때문에 섞인 suffle을 first로, suffle 다시 초기화
        ans += 1
        if ans == 1:
            check = suffle
        first = suffle
        suffle = [0]*len(first)
        i = 0
        if ans != 1 and first == check:
            ans = -1
            break
print(ans)