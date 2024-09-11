# 각 지역의 높이를 기록한 표의 예로,
# 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래
# 높은 지역으로 이동할 때 차이만큼 연료 +

# 선택한 정점에서 고를 수 있는 가까운 + 연료가 같거나 낮은 곳으로

import sys
sys.stdin = open('cost.txt')
import heapq

def dijkstrat(si,sj):
    pq = []
    distance[si][sj] = 0
    heapq.heappush(pq, (distance[si][sj], (si,sj)))

    # print(pq)

    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, (cur_i,cur_j) = heapq.heappop(pq)
        # print(dist, cur_i,cur_j)
        if distance[cur_i][cur_j] < dist:
            continue

        for add_i,add_j in [[1,0],[0,1],[-1,0],[0,-1]]:
            next_i,next_j = cur_i+add_i,cur_j+add_j
            if next_i <0 or next_i >=N or next_j <0 or next_j >=N:
                continue

            # 다음 친구가 높을 경우?
            if heights[next_i][next_j] > heights[cur_i][cur_j]:
                cost = distance[cur_i][cur_j]+ heights[next_i][next_j] - heights[cur_i][cur_j] + 1
            else:
                cost = distance[cur_i][cur_j] + 1
            # print(distance)
            # print(cost,'g')

            if cost >= distance[next_i][next_j]:
                continue
            distance[next_i][next_j] = cost
            heapq.heappush(pq, (cost, (next_i,next_j)))



for tc in range(1, int(input())+1):
    N = int(input())
    heights = [list(map(int,input().split())) for _ in range(N)]
    distance = [[99999999] * N for _ in range(N)]
    # print(distance)
    # for height in heights:
    #     print(height)

    dijkstrat(0,0)
    for dis in distance:
        print(dis)
    print(f'#{tc} {distance[N-1][N-1]}')







