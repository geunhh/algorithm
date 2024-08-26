import sys
sys.stdin = open('miro.txt')

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j
    return -1,-10

def dfs(i,j,N):
    visited[i][j] = 1   # 방문 표시
    if maze[i][j] == 3: # 정답인가?
        return 1
    for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        ni, nj = i+di, j+dj
        # ni,nj가 벽이 아니고, 방문하지 않았을 때
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] != 1:
            if dfs(ni,nj,N):
                return 1
    return 0

for tc in range(1,int(input())+1):
    N= int(input())
    maze = [list(map(int,input().strip())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # print(visited)
    # print(maze)
    sti,stj = find_start(N)
    # print(sti,stj)
    result = dfs(sti,stj,N)
    # for row in visited:
    #     print(row)
    print(f'#{tc} {result}')

    # break
