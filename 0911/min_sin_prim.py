import sys
sys.stdin = open('mi_sin.txt')
from heapq import heappush, heappop

def prim(start):
    heap = list()       # 힙 리스트를 만들고.
    MST = [0] *(V+1)

    sum_weight = 0

    heappush(heap, (0,start))   # list, (가중치, node번호)

    while heap:
        weight, v = heappop(heap)   # 가중치와 vertex(정점)
        print(weight, v, MST,'힙',heap)

        if MST[v]:
            continue

        MST[v] = 1
        sum_weight += weight

        for next in range(V+1):
            if graph[v][next] == 0:
                continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))
    return sum_weight


for tc in range(1, int(input())+1):
    V,E = map(int,input().split()) # 마지막 노드 번호, 간선 개수
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1,n2,w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w
    for row in graph:
       print(row)

    result = prim(0)
    print(f'#{tc} {result}')

    # break


