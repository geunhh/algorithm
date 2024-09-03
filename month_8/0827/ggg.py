import sys
sys.stdin = open('binary')
import math

def dfs(node):
    global cnt

    if len(road[node]) == 0:
        bst[node] = cnt
        cnt += 1
        return
    dfs(road[node][0])
    bst[node] = cnt
    cnt+=1
    dfs(road[node][1])




def make_graph(n):
    h = int((math.log2(n+1) -1))
    print(h)
    num = 2**(h+1)-1
    print(num)
    graph = [[] for _ in range(num)]
    print(graph)

    # 빈 트리, 인접 행렬 만들기.
    for i in range(n+1):
        while len(graph[i]) < 2:
            graph[i].append(0)
    print(graph)

    road = [[] for _ in range(num+1)]
    for j in range(1, n//2+1):
        road[j].extend([2*j,2*j+1])

    bst = [0] * (num+1)


    return graph,road,bst # 트리, 행렬


for tc in range(1, int(input())+1):
    N = int(input())
    graph,road,bst = make_graph(N)
    cnt=1
    print(road)


    # dfs(1)
    print(bst)
    print(f'#{tc} {bst[1]} {bst[N//2]}')