
from collections import deque



def bfs(s,n):
    visited= [0] * n
    print(visited)
    q = deque([0])
    visited[0]=1
    print(visited)

    while q:

        cur_node = q.popleft()
        print(cur_node)

        for i in range(n):
            if computers[i]

        for next_node in computers[cur_node]:
            if computers[cur_node][next_node] == 1 and visited[next_node]!=1: #다음 경로가 있고, visitied
                print(cur_node,next_node)
                q.append(next_node)
                visited[next_node] = 1
            else :
                print('이미옴')









computers = [[1,1,0],[1,1,0],[0,0,1]]
n = 3


bfs(0,n)
