import sys
sys.stdin = open('fly.txt')
'''
NxN 배열 M칸 파리 잡기.

분사하면 + 또는 X 중에 많이 잡는 방향으로 분사.
'''


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]
    zero_mat = [[0]*N for _ in range(N)]            # 이건 첨에 답이 안 나와서 디버깅 하려고 만들었음.
    # print(flies)
    dir1=[[1,0],[0,1],[-1,0],[0,-1]]            # + 방향 델타
    dir2=[[1,1],[1,-1],[-1,1],[-1,-1]]          # x 방향 델타
    # 하나씩 순회
    max_sum =0
    for i in range(N):                          # 전구간 순회해야겠지?
        for j in range(N):
            cur_sum1 = flies[i][j]   # i,j 파리 +
            cur_sum2 = flies[i][j]   # i,j 파리 +

            for k in range(1,M):      # M만큼 가서 확인
                # 가로 세로
                for dir in dir1:
                    cur_i, cur_j = i + dir[0]*k, j + dir[1]*k
                    if 0<=cur_i<N and 0<=cur_j<N:
                        cur_sum1 += flies[cur_i][cur_j]
                # 대각선 방향
                for dir0 in dir2:
                    cur_i, cur_j = i + dir0[0]*k, j + dir0[1]*k
                    if 0<=cur_i<N and 0<=cur_j<N:
                        cur_sum2 += flies[cur_i][cur_j]

                max_sum = max(max_sum, cur_sum1, cur_sum2)
    print(f'#{tc} {max_sum}')



