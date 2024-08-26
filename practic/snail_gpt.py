N=4

board = [[0]*N for _ in range(N)]

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
i, j = 0, 0
dir_index = 0

for num in range(1,N*N+1):
    board[i][j] = num

    ni = i+dir[dir_index][0]
    nj = j+dir[dir_index][1]

    if ni <0 or ni >=N or nj<0 or nj>=N or board[ni][nj] != 0:
        dir_index = (dir_index+1)%4
        ni = i+dir[dir_index][0]
        nj = j+dir[dir_index][1]
    i,j = ni,nj


print(board)
