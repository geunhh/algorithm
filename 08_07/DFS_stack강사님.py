#%%
#그래프 자료 구조 표현하기
V, E = 7, 8
edges = list(map(int, "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
print(edges) #[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 무방향 그래프 만들기
from collections import defaultdict
graph = [[] for _ in range(V+1)]
graph = {i: [] for i in range(1, V + 1)} 
# graph = defaultdict(list)
for i in range(E): 
    v1, v2 = edges[2*i], edges[2*i+1]
    graph[v1].append(v2)
    # graph[v2].append(v1) #유향 그래프일 경우 주석 처리
print(graph)

#노드 번호 작은 순대로 방문 (graph가 딕셔너리로 표현한 경우)
for node, edges in graph.items() :
    graph[node] = sorted(edges)  # 재귀방식에서 작은 번호 순으로 방문
    #graph[node] = sorted(edges, reverse=True) #stack방식에서 작은 번호 순으로 방문

#노드 번호 작은 순대로 방문 (graph를 리스트로 표현한 경우)
# for node, edges in enumerate(graph):
#     graph[node] = sorted(edges)  # 재귀방식에서 작은 번호 순으로 방문
#     #graph[node] = sorted(edges, reverse=True) #stack방식에서 작은 번호 순으로 방문


#%%
def dfs_recursive(start):
    # 방문한 노드 처리
    visited[start] = 1
    print(start, end=' ')
    
    #현재 노드와 인접한 다음 노드 탐색
    for next in graph[start]:
        if not visited [next]: #방문 하지 않은 노드만 탐색
            dfs_recursive(next)

# 그래프 표현
N = 6 # 노드의 개수
graph = {0: [1, 2, 5],
        1: [2],
        2: [3, 4],
        3: [1, 2],
        4: [2],
        5: [0]} #인접 리스트

graph = [[1, 2, 5],
         [2],
         [3, 4],
         [1, 2],
         [2],
         [0]] #인접 리스트
# 방문 노드 기록
visited = [0]*N
# 노드 0에서 DFS수행
dfs_recursive(0)

#%%
def dfs_stack(start):
    stack = [start]
    while stack : #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # 현재 방문해야할 노드
        if visited[node] : #현재 방문할 노드가 방문했었다면 continue
            continue

        #방문 처리
        visited[node] = 1
        print(node, end=' ')

        #현재 노드와 연결된 노드 중 방문하지 않은 노드들만 stack에 추가
        for next_node in graph[node] :
            if not visited[next_node]:
                stack.append(next_node)

# 그래프 표현
N = 6 # 노드의 개수
graph = {0: [1, 2, 5],
        1: [2],
        2: [3, 4],
        3: [1, 2],
        4: [2],
        5: [0]} #인접 리스트

graph = [[1, 2, 5],
         [2],
         [3, 4],
         [1, 2],
         [2],
         [0]] #인접 리스트
# 방문 노드 기록
visited = [0]*N
# 노드 0에서 DFS수행
dfs_stack(0)

###
# 재귀와 스택의 차이:
# 재귀 DFS: 함수 호출 시점에 방문하지 않은 노드만 호출합니다.
# 스택 DFS: 모든 인접 노드를 스택에 넣고, 꺼낼 때 방문 여부를 확인합니다.

#%%
###그래프 인접 행렬
def dfs(start):
    # 방문한 노드 처리
    visited[start] = 1
    print(start, end=' ')
    
    #현재 노드와 인접한 다음 노드 탐색
    for i, conn in enumerate(graph[start]):
        if conn :
            if not visited[i]: #방문 하지 않은 노드만 탐색
                dfs(i)

# 그래프 표현
N = 6 # 노드의 개수
#         0,1,2,3,4,5  <= 노드 번호
graph = [[0,1,1,0,0,1], 
         [0,0,1,0,0,0],
         [0,0,0,1,1,0],
         [0,1,1,0,0,0],
         [0,0,0,0,1,0],
         [1,0,0,0,0,0]]

# 방문 노드 기록
visited = [0]*N
# 노드 0에서 DFS수행
dfs(0)