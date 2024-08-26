from _collections import deque

def dfs(start,result):
    # 현재 노드 방문 처리

    visited[start] = 1
    need_visit = deque([start])

    for next in graph[start]:
        if not visited[next]:
            result+=(str(next)+'-')
            dfs(next,result)
    return result




V, E = 7,8
lst = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
visited=[0] * (V+1)
graph=[[] for _ in range(V+1)]
result=''
print(graph)

for i in range(E):
    v1,v2 = lst[2*i],lst[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)
result = dfs(1,result)
print(result)
