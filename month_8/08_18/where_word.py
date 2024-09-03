import sys
sys.stdin = open('word_txt')

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    # for row in array:
    #     print(row)
    cnt = 0

    # 가로 검사
    for i in range(N):
        for j in range(N-K+1):
            if (array[i][j:j+K] == [1]*K)  \
                    and (j+K==N or array[i][j+K] == 0) \
                    and (j-1<0  or array[i][j-1] == 0):
                cnt+=1
    # 세로 검사
    for j in range(N):
        for i in range(N - K+1):
            for k in range(K):
                if array[i+k][j] !=1:
                    break
            else:
                if (i + K == N or array[i+K][j] == 0) \
                        and (i - 1 < 0 or array[i-1][j] == 0):
                    cnt += 1

    print(f'#{tc} {cnt}')

