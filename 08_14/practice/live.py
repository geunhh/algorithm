import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(s,V): # 시작점, 정점수
    # 준비
    cnt=1
    visited = [False]*(V+1)
    q = deque([s]) # 한번에 씀.
    visited[s] = True

    while q:
        if visited[5] == True:
            return cnt
        t = q.popleft()
        print(t)
        for w in adj_list[t]:
            if visited[w] ==False:
                q.append(w) # 인큐
                visited[w] = True
                print(w,'방문')
                cnt+=1


V,E = map(int,input().split()) # v 마지막 정점, E : 간선 수
arr = list(map(int, input().split()))
# 인접 리스트
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v1,v2 = arr[i*2], arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)
print(adj_list)
for i in range(len(adj_list)):
    adj_list[i].sort()


result = bfs(2,V)
print(result)