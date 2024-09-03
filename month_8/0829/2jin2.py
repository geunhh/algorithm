import sys
sys.stdin = open('2jin2')

for tc in range(1,int(input())+1):
    num = float(input())
    num_div = 0.5
    # 1/2, 1/4, 1/8, 1/16
    i=1
    result=''
    while num != 0:
        if len(result) >= 13:
            print(f'#{tc} overflow')
            break

        if num - num_div >=0:
            num -= num_div
            num_div = num_div*0.5
            result+='1'
        else :
            num_div = num_div*0.5
            result+='0'

    else:
        print(f'#{tc} {result}')





