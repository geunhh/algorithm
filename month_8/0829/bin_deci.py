import sys
sys.stdin = open('bin_deci.txt')


for tc in range(1,int(input())+1):
    input_data=''
    for _ in range(int(input())):
        input_data += input().strip()
    # print(input_data)
    N = len(input_data)//7
    lst=[]
    for i in range(N):
        lst.append(input_data[7*i:7*i+7])
    print(f'#{tc}',end=' ')
    for data in lst:
        # print(data)
        result=0
        if data[0] == '1':
            result+=64
        if data[1]=='1':
            result += 32
        if data[2]=='1':
            result += 16
        if data[3]=='1':
            result += 8
        if data[4]=='1':
            result += 4
        if data[5]=='1':
            result += 2
        if data[6]=='1':
            result += 1
        print(result,end =' ')
# 1 2 4 8 16 32 64 128