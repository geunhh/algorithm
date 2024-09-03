'''
지나간 곳을 1로 바꿔버리기.
하나를 만들어 지나간 곳을 따로 표기하기. -> visited
1 3 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 0 2 1
'''
import sys
sys.stdin = open('4875_input.txt', 'r')


def fstart(N):          # 출발 지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def dfs2(i, j, N):      # 재귀
    visited[i][j] = 1
    if maze[i][j] ==3:
        return 1
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
            if dfs2(ni, nj, N):
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]


    # 출발위치 찾기
    sti, stj = fstart(N)
    visited = [[0]*N for _ in range(N)] # dfs2 용
    # 미로 탐색
    ans = dfs2(sti, stj, N)     # stack을 사용한 dfs1 구현해보기
    #print(f'#{tc} {ans}')

    print(f'#{tc} {ans}')
