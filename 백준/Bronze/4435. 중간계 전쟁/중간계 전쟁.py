import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    hobit,human,elf,dwaf,eagle,wizard = map(int, input().split())
    ok,badman,wag,goblin,hi,troil,badwiz = map(int, input().split())
    gandalf = hobit+2*human+3*elf+3*dwaf+4*eagle+10*wizard
    sawron = ok+2*badman+2*wag+2*goblin+3*hi+5*troil+10*badwiz

    if gandalf > sawron:
        print(f'Battle {tc}: Good triumphs over Evil')
    elif gandalf < sawron:
        print(f'Battle {tc}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {tc}: No victor on this battle field')
