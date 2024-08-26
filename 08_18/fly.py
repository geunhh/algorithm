import sys
sys.stdin = open('fly1.txt')

for tc in range(1,int(input())+1):
    N,M = map(int, input().split())
    # print(N,M)

    board = [list(map(int, input().split())) for _ in range(N)]
    # for row in board:
    #     print(row)
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cur_sum=0
            for x in range(M):
                for y in range(M):
                    cur_sum +=board[i+x][j+y]
            if cur_sum >max_sum:
                max_sum = cur_sum
    print(f'#{tc} {max_sum}')


