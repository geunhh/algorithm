import sys
sys.stdin = open('yeon.txt')

from collections import deque,defaultdict

def calc(N,target):
    # 1-1. deque에 value와 cnt(depth)를 list로 넣어줌
    q = deque([[N,0]])  # value, cnt
    # 1-2. visited를 1로 표시해줌.
    #      -> 이미 연산한 값에 대해서는 동일한 4개 연산을 하지 않기 위함
    visited[N] = 1

    # 2. 시작
    while q:                            # 덱에 요소가 존재할 때
        val,cur_cnt = q.popleft()       # 가장 먼저 들어간 [val, cnt] 가져옴

        # 종료 조건
        if val == target:               # val과 target이 일치하면
            return cur_cnt              # cnt return

        # 2-1 조건을 만족할 경우 deque에 append 해주기
        # + 1                                           # 연산의 중간 결과도 항상 백만 이하의 자연수
        if val + 1 <= 1000000 and not visited[val + 1]: # 연산한 값이 위 조건을 만족하고, 아직 방문하지 않았다면,
            visited[val+1] = 1                          # 방문처리 후
            q.append([val+1,cur_cnt+1])                 # 덱에 넣어줌.
        # -1
        if val -1 > 0 and not visited[val - 1]:
            visited[val-1] = 1
            q.append([val-1,cur_cnt+1])
        # *2
        if val * 2 <= 1000000 and not visited[val * 2]:
            visited[val*2] = 1
            q.append([val*2,cur_cnt+1])
        # -10
        if val -10 > 0 and not visited[val - 10]:
            visited[val-10] = 1
            q.append([val-10,cur_cnt+1])

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    visited = defaultdict(int)      # 해당 값을 방문했는가?
    result = calc(N,M)
    print(f'#{tc} {result}')



