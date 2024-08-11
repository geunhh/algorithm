import sys
sys.stdin = open('4875_input.txt','r')

def find_start(maze , N):        #시작점 찾기 2.
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                return i, j
    return -1,-1

def dfs(maze, N, si, sj, visited):
    stack = [(si,sj)] # 스택 초기화 -> 시작점.

    while stack:
        i,j =stack.pop()    #현재 위치 스택에서 꺼냄

        if visited[i][j]:
            continue

        if maze[i][j] == 3:
            print(f'찾음 {i, j}')
            return 1

        visited[i][j] =1    #방문함

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((ni,nj))
                print(stack)

    return 0




T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]  # maze matrix가져오기.
    print(maze)
    si, sj = find_start(maze,N)
    print(si, sj)
    visited = [[0]*N for _ in range(N)]
    print(visited)
    result = dfs(maze,N,si,sj,visited)



    break
