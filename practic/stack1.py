import sys
sys.stdin = open('stack1.txt')
from collections import deque

def dfs(start):
    need_visited=deque([start])
    # print(need_visited)

    while need_visited:
        node = need_visited.pop()
        if node == 99:
            return 1

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            # print(need_visited)
    return 0

def dfs_recur(start,visited):
    if start == 99:
        return 1

    visited.append(start)
    # print(visited)

    for node in graph[start]:
        if node not in visited:
            if dfs_recur(node,visited):
                return 1
    return 0



for tc in range(1,11):
    tcc, N = map(int,input().split())
    lst = list(map(int,input().split()))
    start = 0
    end = 99
    visited = []
    # 길 만들기.
    graph=[[] for _ in range(100+1)]
    for i in range(N):
        v1,v2 = lst[2*i],lst[2*i+1]
        graph[v1].append(v2)
    # print(graph)

    result = dfs_recur(start,visited)
    print(f'#{tc} {result}')

    # break
