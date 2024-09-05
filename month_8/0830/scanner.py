import sys
sys.stdin=open('input11.txt')

pattern_miny ={'0001101': 0,'0011001': 1,'0010011':2, '0111101':3,
                '0100011': 4,'0110001': 5,'0101111':6, '0111011':7,
                '0110111': 8,'0001011': 9}

def pattern_make(length):
    k = length//56
    new_pattern={}
    for patt in pattern_miny:
        new_pat=''
        for pat in patt:
            # print(pat)
            for _ in range(k):
                new_pat+=pat
        new_pattern[new_pat]=pattern_miny[patt]

    print(new_pattern)
    return new_pattern

for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) # 가로 세로
    # print(N,M)
    board = [list(input().split()) for _ in range(N)]
    # print(board)
    check=''
    for _ in range(M):
        check+='0'
    # print(len(check))
    pw = []

    # 1. 암호 후보 찾아내기.
    for i in range(N): # 그 행에
        password = ''
        if [check] != board[i]: # 암호 코드가 있으면
            board_row = board[i][0]
            j = M-15 # 뒤에서부터 순회할겨
            # print(board_row[j+14])

            while j >= 0:                               # 애매한디용
                if board_row[j+14] == '0':
                    j -= 1
                    continue
                print(board_row[j:j+14])

                if board_row[j-1] == '0':
                    password += board_row[j:j+15]
                    pw.append(password)
                    password =''
                    print(pw)
                else :
                    password += board_row[j:j+15]
                j-=14
            # print(password)
            pw.append(password)
            # print(pw)
    # set해서 중복 제거하고 다시 list로 만들기.
    pw = list(set(pw))
    # print(pw)
    # for num in pw:
    #     result=''
    #     for numnum in num:
    #         numnum = bin(int(numnum,16))[2:]
    #         while len(numnum)<4:
    #             numnum ='0'+numnum
    #         # print(numnum)
    #         result += numnum
    #     print(result,len(result))
    #
    #     new_dict = pattern_make(len(result))


        # break



    break
