
import sys
sys.stdin = open('maze1.txt')
from collections import deque

def bfs(si,sj):
    visited=[[0 for _ in range(16)] for _ in range(16)]
    N=16
    q = deque([[si,sj]])


    # for row in visited:
    #     print(row)
    print(q)

    while q:
        ti, tj = q.popleft()

        if maze[ti][tj] == 3:
            return 1

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
            print(q)
    return 0


# 탐색

# 시작점 찾기
def start_where():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i,j

for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]

    # for row in maze:
    #     print(row)

    si, sj = start_where()
    # print(si,sj)
    result = bfs(si,sj)
    print(f'#{tc} {result}')
    break
