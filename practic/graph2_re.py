import sys
sys.stdin = open('graph2.txt')
from collections import defaultdict

def dfs(s):
    visited[s]=1

    for next in graph[s]:
        if visited[next] != 1:
            dfs(next)


T=int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0] for _ in range(V+1)]
    visited=[0]*(V+1)

    for _ in range(E):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)

    s,g = map(int, input().split())
    dfs(s)



