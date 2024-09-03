
'''
도착지부터 따라갈거임.
인접한 곳이 벽이 아니거나 방문한 곳이 아니면
큐에 넣음.

'''
import sys
sys.stdin = open('5105_input.txt')
from collections import deque

def bfs(i,j,N):
    # visited 생성
    visited = [[0]*N for _ in range(N)]
    # 큐 생성 및 시작점 큐인
    q = deque([[i,j]])
    # visited 시작점 표시.
    visited[i][j] = 1
    # print(q)

    #### 탐색 ####
    while q:
        ti,tj = q.popleft() # -> leftpop
        # print(ti,tj)

        if maze[ti][tj] == 3:
            return visited[ti][tj] -1 -1 # 경로의 빈칸 수,

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            # 인접이고 벽이 아니고, 미로를 벗어나지 않고, 방문한적 없고
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] ==0:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                # print(i,j)
                return i,j

for tc in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti,stj = find_start(N)
    ans = bfs(sti,stj,N)
    print(f'#{tc} {ans}')