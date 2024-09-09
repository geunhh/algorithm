# 게임은 핀볼이 출발 위치로 돌아오거나, 블랙홀에 빠질 때 종료
# 점수는 벽이나 블록에 부딪힌 횟수 (웜홀 포함 x)

# 게임판 위에서의 출발위치나 진행방향은 임의 설정 가능

# 1,2,3,4 블록의 접근방향별 실행을 다르게 해야 함.
# 5번 블록은 반대로 가게
# 6~10번은 웜홀

import sys
sys.stdin = open('pin.txt')

dir = [[0,-1],[0,1],[1,0],[-1,0]] # 상하좌우


for tc in range(1,int(input())+1):
    N= int(input())
    board = [list(map(int,input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if board[i][j] == 0: