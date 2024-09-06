# 시간 초과

import sys

sys.stdin = open('rect.txt')

def move(si, sj, bef_val, cnt, start_num):
    # 범위

    cur_val = board[si][sj]
    if cur_val != bef_val+1:  # 현재 수가 이전 수보다 1 크지 않으면
        global max_cnt, max_cnt_num

        if cnt > max_cnt :
            max_cnt = cnt
            max_cnt_num = start_num
        elif cnt == max_cnt and start_num < max_cnt_num :
            max_cnt = cnt
            max_cnt_num = start_num
        return

    if cnt == 0:                                    # 첫 시도 전에
        for dij in [(0,1),(1,0),(-1,0),(0,-1)]:
            di,dj = si+dij[0],sj+dij[1]
            # 시작값 상하좌우에 자신보다 1 작은 값이 있다면? 그냥 pass
            # 다음번에 본인을 지나갈거임.
            if 0<=di<N and 0<=dj<N and board[si][sj]-1 == board[di][dj]:
                return

    for dij in [(0,1),(1,0),(-1,0),(0,-1)]:
        di,dj = si+dij[0],sj+dij[1]
        if 0<=di<N and 0<=dj<N :
            move(di, dj, cur_val, cnt+1, start_num)

for tc in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0
    max_cnt_num = 9999
    for i in range(N):
        for j in range(N):
            start_num = board[i][j]
            move(i, j, start_num-1, 0, start_num)
    print(f'#{tc} {max_cnt_num} {max_cnt}')

