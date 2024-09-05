import sys
sys.stdin = open('min.txt')

def move(i,j,cur_sum,N):
    if i >= N or j >= N:
        return
    # print(i,j,cur_sum)
    # (N,N)이면 종료.
    if i == N-1 and j == N-1 :
        global min_sum
        if min_sum > cur_sum:
            min_sum = cur_sum
        return

    # 오른쪽 이동
    move(i,j+1,cur_sum+lst[i][j],N)
    # 아래 이동
    move(i+1,j,cur_sum+lst[i][j],N)
    return

for tc in range(1,int(input())+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    # print(lst)
    min_sum= float("inf")

    move(0,0,0,N)
    min_sum += lst[N-1][N-1]
    print(f'#{tc} {min_sum}')

