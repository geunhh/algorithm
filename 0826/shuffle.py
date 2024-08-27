import sys
sys.stdin = open('shuffle.txt')

def shuffle(N):
    print(f'#{tc}',end = '')
    if N==1:
        print(' '+lst[0],end='')
    elif N%2==1:
        for i in range(N//2):
            print(' '+lst[i]+' '+ lst[i+N//2+1],end='')
        print(' '+lst[N//2],end ='')
    else:
        for i in range(N//2):
            print(' '+lst[i]+' '+ lst[i+N//2],end='')

for tc in range(1,int(input())+1):
    N = int(input())
    lst = list(input().split())
    # print(lst)
    shuffle(N)
    print()
