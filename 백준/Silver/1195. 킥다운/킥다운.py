import sys
input = sys.stdin.readline


gear1 = input().strip()
gear2 = input().strip()


if len(gear1) < len(gear2):
    gear1,gear2 = gear2,gear1

rlt = 0


for i in range(len(gear2)):
    for j in range(i+1):
        if gear2[-i+j-1] == '2' and gear1[j] == '2':
            break
    else: rlt = max(rlt, i+1)

    for j in range(i+1):
        if gear2[j] == '2' and gear1[-i+j-1] == '2':
            break
    else: rlt = max(rlt, i+1)


for i in range(len(gear1)-len(gear2)+1):
    for j in range(len(gear2)):
        if gear2[j] == '2' and gear1[i+j] == '2':
            break
    else:
        rlt = max(rlt, len(gear2))
        break

print(len(gear1)+len(gear2)-rlt)