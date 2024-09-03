import sys
sys.stdin = open('nodesum')

def calc(node):

    if graph[node] == [] or graph[node][0] == 0:
        return value[node]

    return calc(graph[node][0]) + calc(graph[node][1])


    # [[],[2,3],[4,5],[],[],[]]

for tc in range(1,int(input())+1):
    N, M, L = map(int, input().split())
    # 노드 개수, 리프 노드 개수, 답 노드 번호
    arr=[]
    for _ in range(M):
        arr.append(list(map(int,input().split())))
    # [node num, value]
    # print(arr)
    value = [0] * (N+1)
    # value list 만들기
    for i in range(N+1):
        for lst in arr:
            if lst[0] == i:
                value[i] = lst[1]
                break
            else:
                value[i] = 0
    # print(value)

    graph = [[] for _ in range(N+1)]
    # print(graph)
    for i in range(1, N//2+1):
        if 2*i <=N:
            graph[i].append(2*i)
        if 2*i+1 <= N :
            graph[i].append(2*i+1)
    # print(graph)

    for i in range(1,len(graph)):
        while len(graph[i]) < 2:
            graph[i].append(0)
    # print(graph)
    result = calc(L)
    print(f'#{tc} {result}')
    # break




