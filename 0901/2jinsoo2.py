import sys
sys.stdin = open('10.txt')

for tc in range(1,int(input())+1):
    N=float(input())
    # print(N)
    div_num=0.5
    binary=''
    while N!=0:
        if len(binary) >=13:
            print(f'#{tc} overflow')
            break

        if N - div_num >=0:
            N -= div_num
            binary+='1'
        else:
            binary+='0'

        div_num *= 0.5
    else:
        print(f'#{tc} {binary}')

