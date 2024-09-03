import sys
sys.stdin = open('16jin.txt')
hex_digits = "0123456789ABCDEF"

for tc in range(1,int(input())+1):
    N, hexa = input().split()
    # print(N,hexa)
    answer=''
    # 10진수로
    for hex in hexa:
        jin10 = hex_digits.index(hex)
        # print(hex, jin10)
        #2진수로
        result =''
        for _ in range(4):
            result = str(jin10 % 2) + result
            jin10//=2
        answer+=result
    print(f'#{tc} {answer}')


