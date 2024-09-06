import sys
sys.stdin = open('trail.txt')

'''
순회하면서 가장 긴 루트 찾는 함수.
'''
def recur(si,sj,cnt):
    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni = di + si
        nj = dj + sj
        if 0 <= ni < N and 0 <= nj < N and heights[ni][nj] < heights[si][sj]:
            recur(ni,nj,cnt+1)

        else :
            global max_cnt
            if cnt > max_cnt:
                max_cnt = cnt
                # print(max_cnt,si,sj)
    return

'''
가장 높은 봉우리를 찾을 함수.
return max_val, max_lst -> max_lst만 쓸겨
'''
def where_start():
    max_val = 0
    max_lst=[]
    for ii in range(N):
        for jj in range(N):      # 순회
            if heights[ii][jj] > max_val:
                max_val = heights[ii][jj]
                max_lst = [[ii,jj]]
            elif heights[ii][jj] == max_val:
                max_lst.append([ii,jj])
    return max_val, max_lst

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0      # result

    start_val, start_lst = where_start()     # 탐색시작 좌표 구하기. start_lst

    # 1. k 만큼 깎고 탐색할겨
    for k in range(1,K+1):                  # k만큼 깎을 겨
        for i in range(N):
            for j in range(N):              # 순회
                heights[i][j] -= k          # k만큼 깎고

                # 2. 탐색
                for si,sj in start_lst:
                    recur(si,sj,cnt=1)

                # 3. 원복
                heights[i][j] += k


    print(f'#{tc} {max_cnt}')
    # break




