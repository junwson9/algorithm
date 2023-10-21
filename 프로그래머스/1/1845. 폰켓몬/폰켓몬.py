def solution(nums):
    n = len(nums)//2
    nums = list(set(nums))
    tmp = []
    for i in nums:
        if i not in tmp:
            tmp.append(i)
    if len(tmp) > n:
        answer = n
    else:
        answer = len(tmp)
    return answer
    