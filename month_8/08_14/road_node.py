
import sys
sys.stdin = open('node.txt')
from collections import deque

def bfs(s,G,V):

    visited = [0] * (V+1)
    q = deque([s])
    # print(q)
    visited[s] = 1
    # print(visited,' 이러고 출발')


    while q:
        # G에 다녀왔으면
        if visited[G] != 0:
            return visited[G] -1
        t = q.popleft()


        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1 # cnt 쓰려다가 아까 라이브 때 배운거 써봄.
            # print(visited)
    return 0

for tc in range(1,int(input())+1):
    V, E = map(int,input().split())     # V: 노드 개수, E : 간선 수
    # print(V,E)
    # 경로 받기

    arr = []
    for _ in range(E):
        a,b = map(int,input().split())
        arr.append(a)
        arr.append(b)
    S,G = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    # print(adj_list)
    ###### 인접 리스트 만들기.
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    result = bfs(S,G,V)
    print(f'#{tc} {result}')
