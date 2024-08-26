# 깊이 우선 탐색
from collections import defaultdict
import sys
sys.stdin=open('graph.txt')
from collections import defaultdict
def dfs(start):
    visited[start] = 1
    stack.append(start)

    for next in graph[start]:
        if visited[next] != 1:
            dfs(next)


V,E = map(int,input().split())
input_list = list(map(int,input().split()))
visited=[0]*(V+1)   # 정점의 개수만큼이니까.
stack=[]

graph = defaultdict(list)
for i in range(E):
    v1, v2 = input_list[2*i],input_list[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)
dfs(1)
print(f'#1',end=' ')
for num in stack[:-1]:
    print(num,end='-')
print(stack[-1])


