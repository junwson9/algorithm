import sys
st = sys.stdin.readline()
word = st.lower()
cnt = []
word_list = []
mx_cnt = 0
for i in word:
    if i not in word_list and i != '\n':
        word_list.append(i)
for w in word_list:
    count = word.count(w)
    cnt.append(count)
mx = max(cnt)
for n in cnt:
    if n == mx:
        mx_cnt += 1
if mx_cnt >= 2:
    print('?')
else:
    print(word_list[cnt.index(mx)].upper())
