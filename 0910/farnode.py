
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque


def bfs(node, graph, visited):
    q = deque([(node, 1)])
    visited[node] = 1
    while q:
        cur_node, cur_depth = q.popleft()
        # print(cur_node)
        for next_node in graph[cur_node]:

            if visited[next_node] == 0:
                visited[next_node] = cur_depth+1
                q.append((next_node, cur_depth+1))
    return visited




def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for s, e in edge:
        v1, v2 = s, e
        graph[v1].append(v2)
        graph[v2].append(v1)


    bfs(1, graph, visited)
    max_num = max(visited)
    cnt=0
    for i in visited:
        if i == max_num:
            cnt+=1
    return cnt


solution(n, edge)