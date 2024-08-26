import sys
sys.stdin=open('soin.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    result=''
    for i in [2,3,5,7,11]:
        count=0
        while N%i==0:
            count+=1
            N//=i
        result += (str(count)+' ')
    print(f'#{tc} {result[:-1]}')