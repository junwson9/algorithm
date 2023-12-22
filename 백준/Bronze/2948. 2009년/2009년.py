import sys
input = sys.stdin.readline
D, M = map(int, input().split())
date = ['Wednesday','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']
if M == 1:
    print(date[D%7])
elif M == 2:
    print(date[(D+31)%7])
elif M == 3:
    print(date[(D+59)%7])
elif M == 4:
    print(date[(D+90)%7])
elif M == 5:
    print(date[(D+120)%7])
elif M == 6:
    print(date[(D+151)%7])
elif M == 7:
    print(date[(D+181)%7])
elif M == 8:
    print(date[(D+212)%7])
elif M == 9:
    print(date[(D+243)%7])
elif M == 10:
    print(date[(D+273)%7])
elif M == 11:
    print(date[(D+304)%7])
elif M == 12:
    print(date[(D+334)%7])
