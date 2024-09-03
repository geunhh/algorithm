import sys
sys.stdin = open('4871_input.txt', 'r')
'''
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다. 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
'''
'''
6 5 V M  // V개 노드, E개 간선 
1 4      // E개만큼 경로수
1 3
2 3
2 5
4 6
1 6      // 경로.

'''
def dfs(start):

    visited[start] = 1


    for next in graph[start]:
        if not visited[next]:
            dfs(next)



T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # V개 노드, E개 경로.
    edge = []
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    # print(graph)
    # 단방향 경로 만들기
    for _ in range(E):
        edge += list(map(int,input().split()))
    # print(edge)                     # [1, 4, 1, 3, 2, 3, 2, 5, 4, 6]

    for i in range(E):
        v1,v2 = edge[2*i], edge[2*i+1]
        graph[v1].append(v2)
    # print(graph)                    # [ [], [4, 3], [3, 5], [], [6], [], [] ]

    start, end = map(int, input().split()) # 1,6
    dfs(start)

    print(f'{tc} {visited[end]}')




