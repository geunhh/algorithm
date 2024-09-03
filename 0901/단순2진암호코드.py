import sys
sys.stdin= open('11.txt')

my_code = {
    '0001101':0, '0011001':1, '0010011':2,'0111101':3,'0100011':4,
    '0110001':5, '0101111':6, '0111011':7,'0110111':8,'0001011':9
}

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())

    # 1. 암호 코드 찾기
    for _ in range(N):
        lst = input()
        if '1' in lst:
            code = lst

    # 1-1 암호 코드 찾기 2
    for i in range(M-1,-1,-1):
        if code[i] == '1':
            start_ind = i-55
            end_ind=i
            break

    # 2 암호 코드 변환해서 리스트 넣기
    result=[]
    for j in range(start_ind,start_ind+50,7):
        result.append(my_code[code[j:j+7]])

    # 3 연산
    total=0
    for k in range(8):
        if k%2 ==0:             # 짝수지만 여기서는 홀수로 취급 (인덱스가 1부터 시작하기 때문)
           total += 3*result[k]
        else:
            total += result[k]

    # 옳은 암호코드인가?
    if total%10 == 0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')




