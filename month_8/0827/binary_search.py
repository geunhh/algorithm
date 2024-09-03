import sys
sys.stdin = open('binary')
import math

def dfs(node):
    global cnt

    if node > N or len(road[node]) == 0:
        bst[node] = cnt
        cnt += 1
        return
    dfs(road[node][0])
    bst[node] = cnt
    cnt+=1
    if len(road[node])> 1:
        dfs(road[node][1])




def make_graph(n):
    h = int((math.log2(n+1) -1)+0.9999999999999999)
    num = 2**(h+1)-1
    graph = [[] for _ in range(num)]

    # 빈 트리, 인접 행렬 만들기.
    for i in range(n+1):
        while len(graph[i]) < 2:
            graph[i].append(0)

    road = [[] for _ in range(num+1)]
    for j in range(1, n//2+1):
        if 2 * j <= n:
            road[j].append(2 * j)
        if 2 * j + 1 <= n:
            road[j].append(2 * j + 1)

    bst = [0] * (num+1)


    return graph,road,bst # 트리, 행렬


for tc in range(1, int(input())+1):
    N = int(input())
    graph,road,bst = make_graph(N)
    # print('ggg',road)
    cnt=1

    dfs(1)
    # print(bst)
    print(f'#{tc} {bst[1]} {bst[N//2]}')