import sys
sys.stdin = open('contact.txt')
from collections import deque

def bfs(start,N):

    # 초기화
    visited = [0] * 101     # 방문 기록을 위한 list
    q = deque([start])      # deque 호출
    visited[start] = 1      # start 기록.

    while q:                # q가 있으면 진행
        t = q.popleft()     # q << pop

        for w in arr_go[t]:         # pop한 t를 기준으로 인접 노드들을 순회
            if visited[w] == 0:     # 노드가 visited에 속하지 않았다면(방문하지 않았다면)
                q.append(w)         # 큐에 append
                visited[w] = visited[t] +1      # visited에 넣어주고 (이전 노드에서 수를 1씩 증가시켜)
                                                # 거리 계산을 편하게 하기 위해 : 이전노드의 거리 + 1
                max_visit = visited[w]          # 마지막 노드의 값을 할당 (갱신

    for i in range(len(visited)-1,-1,-1):       # 역순회 하면서 가장 큰 숫자를 찾는다.
        if visited[i] == max_visit:             # max_visit과 같은 경우 index 반환
            return i




for tc in range(1,11):
    N, start = map(int, input().split())        # 데이터의 길이, 시작점
    arr = list(map(int, input().split()))       #


    ## 인접리스트 구하기.####
    arr_go = [[] for _ in range(101)]         # 번호가 100번까지 -> 101

    for i in range(N//2):                       # 데이터의 길이 N -> 간선의 수는 N//2
        v1, v2 = arr[i*2], arr[i*2+1]
        arr_go[v1].append(v2)

    result = bfs(start,N)
    print(f'#{tc} {result}')



