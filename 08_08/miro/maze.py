'''
지나간 곳을 1로 바꿔버리기.
하나를 만들어 지나간 곳을 따로 표기하기. -> visited
1 3 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 0 2 1
'''
def dfs2(i,j,N):
    visited[i][j] =1
    if maze[i][j] ==3 :
        return 1
    else:
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj] ==0:


def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j
    return -1,-1

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발위치 찾기.
    sti, stj = fstart(N)

    visited = [[0]*N for _ in range(N)]

