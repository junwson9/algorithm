while True:
    word = input()
    if word == '0':
        break
    reword = word[::-1]
    if word == reword:
        print('yes')
    else:
        print('no')