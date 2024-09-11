# 복구시간이 이동시간에 비해 아주 길기 때문에 이동시간은 계산X
# 0인 곳은 복구가 불필요한 곳이다.

import sys
sys.stdin = open('supply.txt')


import heapq
def dij(si,sj):     # start_i, start_j : 0,0

    # 1. 우선순위 큐 선언.
    pq = []

    # 1-1. heappush로 큐에 저장
    heapq.heappush(pq, (0,(si,sj))) # 가중치(복구시간)

    # 2. 우선순위 큐가 빌 때까지 반복
    while pq:
        # 2-1. 최단 시간을 기준으로 time, (i,j) 꺼내기
        now_time, (cur_i,cur_j) = heapq.heappop(pq)


        # 3. 현재 노드의 상하좌우 노드 확인
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            # 3-1. 우하상좌 순으로 다음 node의 i,j를 선택한다.
            next_i,next_j = cur_i+di, cur_j+dj

            # 3-2. 다음 i,j가 범위 밖으로 나가면, continue
            if next_i >= N or next_i < 0 or next_j >= N or next_j <0:
                continue

            # 3-3. 아니라면,
            # 이전 노드의 누적시간 + 현 노드의 복구시간을 new_time에 저장
            new_time = now_time+lst[next_i][next_j]

            # 3.4
            # 다음 노드에 (이전에) 저장된 시간이 지금 경로의 누적시간 보다 작으면, continue
            if new_time >= times[next_i][next_j]:
                continue

            # 3.5 아니라면,
            # 갱신~~
            times[next_i][next_j] = new_time
            # 우선순위큐에 push~~~~
            heapq.heappush(pq, (new_time,(next_i,next_j)))

for tc in range(1, int(input())+1):
    # input 받기
    N = int(input())
    lst = [list(map(int,input().strip())) for _ in range(N)]
    # 아주 큰 값이 저장된 N x N array 선언. -> 누적합이 저장될 겨.
    times = [[999999] * N for _ in range(N)]

    # 함수 호출
    dij(0,0)
    # 우측하단 끝에 저장된 값 호출
    print(f'#{tc} {times[N-1][N-1]}')
