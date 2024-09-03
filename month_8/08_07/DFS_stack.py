V, E = 7, 8 # 노드수 , 간선수
edges = list(map(int, "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split())) # 연결된 엣지 정보
print(edges)    # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접 리스트
graph = [[] for _ in range(V+1)]        # 인덱스 0은 안 씀
# graph = {i+1:[] for i in range(V)}      # dict 으로도 표현 가능.
for i in range(E):
    v1, v2 = edges[2*i], edges[2*i+1] # 두 개가 한 묶음.
    # 무향 그래프 ( 양방향 이동 가능)
    graph[v1].append(v2)
    graph[v2].append(v1) # 유향 그래프이면, 지워야 함. 양방향이 아니기 때문.
print(graph)

def dfs_recursive(cur_node):
    #방문한 노드 처리 로직
    visited[cur_node] =1
    print(cur_node,end=' ')

    #현재 노드와 인접한 다음 노드 탐색
    for next_node in graph[cur_node]:
        # 방문하지 않은 것만 탐색
        if not visited[next_node]:
            dfs_recursive((next_node))

visited = [0] * (V+1) # 방문 노드 기록
dfs_recursive(1)

def dfs_stack(start_node) :
    stack = [start_node]
    while stack:       # 스택에 남은 것이 없을 때까지
        cur_node = stack.pop()
        # 방문한 적이 있다면
        if visited[cur_node]:
            continue

        # 방문 처리
        visited[cur_node]=1
        print(cur_node, end=' ')

        # 현재 노드와 연결된 노드 중 방문하지 않은 노드만 stack에 추가
        for next_node in graph(cur_node):
        #for next_node in sorted(graph(cur_node),reverse=True):
            if not visited[next_node]:
                stack.append(next_node)
print()
print()

visited = [0] * (V+1) # 방문 노드 기록
dfs_stack(1)