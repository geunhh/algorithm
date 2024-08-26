import sys
sys.stdin = open('graph2.txt')
from collections import defaultdict

def dfs(s):
    visited[s]=1

    for next in graph[s]:
        if visited[next] != 1:
            dfs(next)

# input 받기 및 graph 만들기
for tc in range(1,int(input())+1):
    V,E = map(int,input().split())

    arr=[]
    for _ in range(E):
        d1,d2 = map(int,input().split())
        arr.append([d1,d2])
    graph = defaultdict(list)
    for lst in arr:
        v1,v2 = lst[0],lst[1]
        graph[v1].append(v2)
    ##############################
    S, G = map(int, input().split())
    visited = [0]*(V+1)

    dfs(S)
    print(f'#{tc} {visited[G]}')


