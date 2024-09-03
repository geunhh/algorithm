import sys
sys.stdin= open('subtree.txt')

def dfs(node):
    global cnt
    if node == -1:
        return

    cnt+=1
    dfs(graph[node][0])
    dfs(graph[node][1])



for tc in range(1, int(input())+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    E = len(arr)//2
    cnt=0
    graph = [[] for _ in range(N+2)]
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        graph[v1].append(v2)

    for node in range(N+2):
        while len(graph[node]) <2:
            graph[node].append(-1)
    dfs(start)
    print(f'#{tc} {cnt}')


