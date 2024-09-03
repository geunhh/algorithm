import sys
sys.stdin=open('mag.txt')

for tc in range(1,11):
    N=int(input()) # 항상 100
    board = [list(map(int,input().split())) for _ in range(N)]
    # print(board)


    # for row in board[:15]:
    #     print(row[:15])
    cnt =0
    for j in range(100): # column 별로 처리 및 계산
        start = 0 # 아무것도 없음, N극부터 시작
        '''
             ####  1  ####
           1 : N극, 아래로
           2 : S극, 위로
             ####  2  ####
        '''
        for i in range(100):
            # if board[i][j] !=0:           # 요건 디버깅하려고
            #     # print(i,j,board[i][j])
            # 나는 S 극 = 2
            if board[i][j] == 2:
                # 근데 바로 위가 N극(시작점)임
                if start == 0:
                    board[i][j] = 0 # 0으로 바꿔줌 N극으로 슈루룩 빨려들어감.
                # 바로 위가 N극이야 -> N극 친구는 밑으로 나는 위로 가고 싶어. 교착
                elif start == 1:
                    cnt += 1  # 교착 +1
                    start = 2
                    # print('1증가 총:', cnt)
                # 나는 S인데 S를 만났어. -> NSS인 경우
                elif start == 2:
                    pass            # NSS는 어차피 교착상태 1로 치고, start는 여전히 S

            # 나는 N 극 = 1
            elif board[i][j] == 1:
                # 바로 위가 S극 = 0이야
                if start == 0:
                    start = 1
                elif start == 2 :
                    start = 1 # 이전 교착은 끝나고 새로운 교착 가능성이 열려
                # 바로 위가 N이야 -> 넘어가
                elif start == 1:
                    pass

    print(f'{tc} {cnt}')


