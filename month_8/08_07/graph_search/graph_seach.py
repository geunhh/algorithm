import sys
sys.stdin = open('graph_input.txt', 'r')

def dfs(start):

    visited[start] = 1
    print(start, end ='-')
    lst.append(str(start))


    for next in graph[start]:
        if not visited[next]:
            dfs(next)




V, E = map(int, input().split())
edges = list(map(int, input().split()))
visited = [0] * (V+1)
lst=[]

# 인접 리스트 처리
graph =[[] for _ in range(V+1)]
# 그래프 만들기.
for i in range(E):
    v1, v2 = edges[2*i], edges[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)
dfs(1)
print()
print(f"#1 {'-'.join(lst)}")




