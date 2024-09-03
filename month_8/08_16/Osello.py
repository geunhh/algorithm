import sys
sys.stdin = open('osello.txt')

board4 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,2,1,0],
    [0,0,1,2,0],
    [0,0,0,0,0]
]
board6 =[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,2,1,0,0],
    [0,0,0,1,2,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]
board8 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,2,1,0,0,0],
    [0,0,0,0,1,2,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
dir_check2 = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]



def placing_new(x,y,color):
    # 흑돌 : 1, 백돌 : 2
    if color ==1:
        BW = 2
    elif color ==2:
        BW = 1

    # 돌 놓기
    board[x][y] = color
    for row in board:
        print(*row)
    print()

    for x1, y1 in dir_check2:
        for ind in range(1,N):      # N?? 다 체크. (1,0),
            x_check1,y_check1 = x+x1*ind, y+y1*ind
            x_check2,y_check2 = x+x1*(ind+1), y+y1*(ind+1)
            # 범위 안에 들어가고 +1이 같은 색이면 바로 break
            if 1<=x_check1<len(board) and 1<=y_check1<len(board) and board[x_check1][y_check1] == color:

                break
            # 범위 안에 들어가고 +1이 다른색 +2가 같은색이면
            elif 1<=x_check1<len(board) and 1<=y_check1<len(board) and 1<=x_check2<len(board) and 1<=y_check2<len(board) \
                and board[x_check1][y_check1] == BW and board[x_check2][y_check2] == color:

                for put in range(1,ind+1):
                    x_put,y_put = x+x1*put, y+y1*put
                    board[x_put][y_put] = color
                break
            # 범위 안에 들어가고 +1이 다른색 +2도 다른색
            elif 1<=x_check1<len(board) and 1<=y_check1<len(board) and 1<=x_check2<len(board) and 1<=y_check2<len(board) \
                and board[x_check1][y_check1] == BW and board[x_check2][y_check2] == BW:
                continue



    for row in board:
        print(*row)
    print()




for tc in range(1,1+int(input())):
    N,M = map(int,input().split())  # N 오목판 nxn
                                    # M 돌 놓는 횟수
    # 보드판 선택 4 6 8

    if N==4:
        board = board4
    elif N==6:
        board = board6
    elif N==8:
        board = board8
    # print(board)
    for index in range(M):
        print(f'{index}번째 돌')
        y,x,color = map(int,input().split()) # x축,y축, 색
        placing_new(x,y,color)
        # 개수 세기

    cnt1=0
    cnt2=0
    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] ==1:
                cnt1+=1
            elif board[i][j] ==2:
                cnt2+=1
    print(f'#{tc} {cnt1} {cnt2}')


