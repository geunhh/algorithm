
import sys
sys.stdin = open('input.txt','r')

def dfs(start):

    visited[start] = 1
    # if start == 99:
        # return 1

    for next in graph[start]:
        if not visited[next]:
            dfs(next)



for tc in range(1,11):
    T, num = map(int, input().split()) # tc 번호, 총 길 개수.
    start=0
    end=99
    visited = [0] * (end+1)
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(end+1)]
    for i in range(num):
        v1, v2 = edges[2*i], edges[2*i+1]
        graph[v1].append(v2)
    # print(graph)

    dfs(start)

    print(f'#{T} {visited[end]}')

