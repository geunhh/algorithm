import sys
sys.stdin = open('dist.txt')

import heapq

def dijkstrat(start):
    pq=[]
    heapq.heappush(pq, (0, start))

    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist :
            continue

        for next in graph[now]:
            next_node = next[1]
            cost = next[0]

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost,next_node))





for tc in range(1, int(input())+1):
    end,N = map(int,input().split())

    graph = [[] for _ in range(N)]
    for _ in range(N):
        s,e,w = map(int,input().split())
        graph[s].append((w,e))

    distance = [99999999 for _ in range(N)]
    dijkstrat(0)

    print(f'#{tc} {distance[end]}')

