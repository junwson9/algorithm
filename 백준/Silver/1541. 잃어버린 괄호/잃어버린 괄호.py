st = input()
lst = st.split('-')
nums = []
for i in lst:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    nums.append(cnt)
start = nums[0]
for i in range(1,len(nums)):
    start -= nums[i]
print(start)
