import sys
sys.stdin=open('queen.txt')

def chess(row,N):
    if row == N:
        global cnt
        cnt += 1
        return

    for col in range(N):
        if not used_col[col] and not used_up[row-col+(N-1)] and not used_down[row+col]:

            used_col[col] = True
            used_up[row-col+(N-1)] = True
            used_down[row+col] = True

            chess(row+1,N)
            used_col[col] = False
            used_up[row-col+(N-1)] = False
            used_down[row+col] = False

        '''
        used_up[row-col] 했는데, 3개만 맞아서 고민하다가 지선생님 도움 받음.
        우상향 대각선은 경우에 따라 음수가 나올 수도 있다.
        -> lst 인덱스로 음수가 들어갈 수 없어서 (N-1)만큼을 더해줘서 처리 + 구분
        
        '''

for tc in range(1,int(input())+1):
    N=int(input())
    cnt=0


    used_col = [False]*N
    # 우상향 그래프는 x,y 뺀값이 같음.
    used_up  = [False]*(2*N-1) # 표 그려서 대각선 그어보면 암
    # 우하향 그래프는 x+y 값이 같음.
    used_down  = [False]*(2*N-1) # 표 그려서 대각선 그어보면 암
    chess(0, N)

    print(f'#{tc} {cnt}')


