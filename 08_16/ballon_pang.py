import sys
sys.stdin = open('ballon.txt')





for tc in range(1, 1+int(input())):
    M,N = map(int,input().split())      #M개씩 N줄
    ballon_list = [list(map(int,input().split())) for _ in range(M)]
    # print(M,N)
    # print(ballon_list)
    max_sum = ballon_list[0][0]
    for i in range(M):
        for j in range(N):
            # print('#',i,j)

            cur_sum=ballon_list[i][j]
            for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                for k in range(1, ballon_list[i][j]+1):
                    ni = i+di*k
                    nj = j+dj*k
                    # print(ni,nj)
                    if 0<=ni<M and 0<=nj<N :
                        cur_sum+=ballon_list[ni][nj]
            if max_sum < cur_sum:
                max_sum = cur_sum
    print(f'#{tc} {max_sum}')





