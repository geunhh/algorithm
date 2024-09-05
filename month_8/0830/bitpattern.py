import sys
sys.stdin = open('input1.txt')

patter ={'001101': 0,'010011': 1,'111011':2, '110001':3,
         '100011': 4,'110111': 5,'001011':6, '111101':7,
         '011001': 8,'101111': 9}

for tc in range(1,int(input())+1):
    N = input().strip()
    result=''
    for num in N:
        num = bin(int(num,16))[2:]
        while len(num)<4:
            num ='0'+num
        result += num
    print(f'#{tc}',end=' ')
    i=0
    while i <len(result)-5:
        if result[i:i+6] in patter:
            print(patter[result[i:i+6]],end=' ')
            i+=6
            continue
        i+=1
    print()
