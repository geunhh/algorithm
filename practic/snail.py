
N=4

board = [[0]*N for _ in range(N)]
print(board)

# 우 하 좌 상
dir = [[0,1],[1,0],[0,-1],[-1,0]]
i,j=0,0
dir_index=0
dir_i=0
dir_j=1

for num in range(1,N*N+1):

    if  0<=i<N and 0<=j<N and board[i][j] == 0:
        board[i][j] = num
    else:   # 범위를 벗어나거나 이미 숫자가 들어갔다?
        i -= dir_i
        j -= dir_j

        # 방향벡터 바꿔줌
        dir_index = (dir_index+1) %4
        dir_i = dir[dir_index][0]
        dir_j = dir[dir_index][1]

        # 방향 이동.
        i += dir_i
        j += dir_j

        # 값넣어줌
        board[i][j] = num
    #일단 진행
    i += dir_i
    j += dir_j
for row in board:
    print(row)




