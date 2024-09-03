import sys
sys.stdin = open('passw.txt')

# 암호해독에 필요한 dictonary 선언.
password = {'1011000':0, '1001100':1,'1100100':2,'1011110':3,
            '1100010':4, '1000110':5,'1111010':6,'1101110':7,
            '1110110':8, '1101000':9}


for tc in range(1,int(input())+1):
    N,M = map(int,input().split())          # input 받아오기
    arr = [input() for _ in range(N)]       # input 받아오기

    # 암호 해독에 필요한 한 줄 가져오기.
    for row in arr:
        if '1' in row:
            pw = row
            break
    # 암호 끝이 무조건 1이기 때문에 역순회해서 1이 되는 친구부터 암호 찾기.
    pw_list=[]
    for i in range(len(pw)-1,-1,-1):
        if pw[i] == '1':                                # 1이 나오면 암호 시작.
            for j in range(8):                          # 총 8개
                pw_list.append(pw[i-7*j:i-7-7*j:-1])    #
            break
    # ['1101110', '1100100', '1011000', '1000110', '1000110', '1101110', '1000110', '1101110']
    pw_list.reverse()
    # ['1101110', '1000110', '1101110', '1000110', '1000110', '1011000', '1100100', '1101110']
    real_pw = [] # 찐 암호.
    for pw1 in pw_list:
        real_pw.append(password[pw1]) # dictionary 이용해서 암호!
    # [7, 5, 7, 5, 5, 0, 2, 7]


    # 암호 계산
    odd_v=0     # 홀
    even_v=0    # 짝
    for i in range(8):  # 8개 암호 순회
        if i%2==0:               # 짝수일 때
            even_v+=real_pw[i]   # 짝수에 넣기
        else:                    # 홀수일 때
            odd_v+=real_pw[i]    # 홀수에 넣기
    result = odd_v+even_v*3

    # output
    if result % 10 == 0:
        print(f'#{tc} {even_v+odd_v}')
    else:
        print(f'#{tc} 0')

    break