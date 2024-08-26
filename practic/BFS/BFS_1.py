import sys
sys.stdin=open('bfs1.txt')
from collections import deque

def bfs(s,N):
    visited = [0]*101       #visited 설정하기

    queue = deque([s])      #덱으로 큐 설정
    visited[s]=1            #visited[s] 1로 만듬
    max_num=0


    while queue:                            # 큐가 있다면 ㄱ
        node = queue.popleft()              # 선입된 친구를 노드로 빼줌.

        for neighbor in graph[node]:        # 주변 노드들을 슥 돌아봄
            if visited[neighbor] ==0 :      # 방문한 적이 없다?
                queue.append(neighbor)      # 그럼 큐에다가 넣어줌
                visited[neighbor] = visited[node] + 1
                # 그리고 visited에 0과 1이 아니라, 부모 노드의 +1로 넣어서 계산 쉽게 고고
                max_visit = visited[neighbor]

    for i in range(len(visited)-1,-1,-1):
        if visited[i] == max_visit:
            return i




N,s = map(int, input().split())
lst = list(map(int,input().split()))
print(lst)

graph = [[] for _ in range(101)]
# print(graph)
for i in range(N//2):
    v1,v2 = lst[2*i],lst[2*i+1]
    graph[v1].append(v2)
print(graph)
result = bfs(s,N)
print(result)