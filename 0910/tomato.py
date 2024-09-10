# 상하 좌우로 익기 때문에 dir 쓰기.
# 익은 토마토가 다시 접근되지 않게 하기 위해 visited 를 사용.
# 인접한 곳에 있는 토마토들이 익는다 -> BFS
# tomatos의 default는 0 익었으면(방문했으면)로 설정

import sys
sys.stdin = open('tomato.txt')
from _collections import deque

def bfs():
    q = deque([])
    # 농장 순회
    for i in range(N):
        for j in range(M):
            # 익은 토마토가 있다면,
            if tomatos[i][j] ==1:
                q.append([i,j,0]) # i,j,day

    # q가 남아 있으면,
    while q:

        cur_i,cur_j,day = q.popleft()

        if cur_i + 1 < N and tomatos[cur_i+1][cur_j] == 0:
            tomatos[cur_i+1][cur_j] = -1
            q.append([cur_i+1, cur_j, day+1])
        if cur_i - 1 >= 0 and tomatos[cur_i-1][cur_j] == 0:
            tomatos[cur_i-1][cur_j] = -1
            q.append([cur_i-1, cur_j, day+1])
        if cur_j + 1 < M and tomatos[cur_i][cur_j+1] == 0:
            tomatos[cur_i][cur_j+1] = -1
            q.append([cur_i, cur_j+1, day+1])
        if cur_j - 1 >= 0 and tomatos[cur_i][cur_j-1] == 0:
            tomatos[cur_i][cur_j-1] = -1
            q.append([cur_i, cur_j-1, day+1])

    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                return -1
    return day

M, N = map(int,input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

result = bfs()

print(result)
