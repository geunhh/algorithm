import sys

sys.stdin = open('3.txt')
from collections import defaultdict

def order(node):
    global cnt
    if node == None:
        return
    # cnt+=1             # 어디 넣어도 노상관
    order(graph[node][0])
    # cnt+=1             # 어디 넣어도 노상관
    order(graph[node][1])
    cnt+=1               # 어디 넣어도 노상관
    return


for tc in range(1, int(input()) + 1):
    E, node = map(int, input().split()) # 간선 개수, 시작 노드
    lst = list(map(int,input().split()))
    graph = defaultdict(lambda : [None,None])

    cnt =0
    for i in range(E):
        par,chi = lst[2*i],lst[2*i+1]
        if graph[par][0] == None:
            graph[par][0] = chi
        else:
            graph[par][1] = chi
    order(node)
    print(f'#{tc} {cnt}')





