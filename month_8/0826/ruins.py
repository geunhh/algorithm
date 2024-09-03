import sys
sys.stdin=open('ruin.txt')

for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) # N개 줄에 M개씩
    lst = [list(map(int,input().split())) for _ in range(N)]
    # for row in lst:
    #     print(row)
    max_cnt=0
    #가로 세기
    for i in range(N):
        cnt = 0
        for j in range(M):
            if lst[i][j] == 1:
                cnt+=1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt=0

        if cnt > max_cnt:
            max_cnt = cnt
        # print(max_cnt)
    #세로 세기
    for j in range(M):
        cnt = 0
        for i in range(N):
            # print(i,j)
            if lst[i][j] == 1:
                cnt+=1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt=0
        if cnt > max_cnt:
            max_cnt = cnt
    if max_cnt ==1:
        max_cnt=0
    print(f'#{tc} {max_cnt}')







