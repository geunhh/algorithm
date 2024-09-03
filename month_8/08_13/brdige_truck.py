from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()                 # deque객체를 만들고
    sum_q =0                    # 다리 위의 트럭들 무게 합을 할당할 친구를 만들고
    cnt=0                       # 전체 시간 기록할 친구도 만듭니다.


    while True:        
        # q가 비었을 때를 먼저 확인. [다리 위 트럭]
        if not q:                                       # 비었으면                              
            q.appendleft([truck_weights.pop(0), 0])     # [트럭무게 첫번째 요소 pop한 값, 0초] 리스트로 묶어서 append
            sum_q += q[0][0]                            # 다리 위 무게 += 방금 추가한 트럭무게

        # 트럭 도착
        elif q[-1][1] >= bridge_length:                 # 가장 먼저들어온 친구, 즉 먼저 나갈 친구의 시간이 length와 같다?
            sum_q -= q[-1][0]                           # 무게 합에서 도착한 트럭 무게 빼줌
            q.pop()                                     # 다리 위 트럭 queue에서 도착한 친구 pop



        # 트럭 출발
        if truck_weights and sum_q+truck_weights[0] <= weight:      # 출발할 트럭이 남아있고, 다리 위 트럭의 무게가 10 이하
            q.appendleft([truck_weights.pop(0),0])                  
                                                        # 남은 트럭 리스트에서 pop한 친구를 q(다리 위 트럭 리스트)에 append
                                                        # [1,2,3,4] 일 때 1부터 빼야하기 때문에 pop(0), 시간 0 을 list로 append.
            sum_q += q[0][0]                            # 방금 append한 친구 무게 추가.

        # 시간 증가 
        for i in range(len(q)):                         # 다리위 친구들 모두 시간 1 씩 증가           
            q[i][1] +=1
        cnt+=1                                          # 전체 시간은 흘러 째깍깍.
        
        if not q :                                      # 큐가 비었을 때 리턴.
            return cnt

bridge_length = 100
weight = 100                 # 견딜 수 있는 최대 중량
truck_weights = [7,4,5,6]   # 트럭 무게
truck_weights = [10,10,10,10,10,10,10,10,10,10]	   # 트럭 무게
truck_weights = [10]	   # 트럭 무게
result = solution(bridge_length,weight,truck_weights)
print(result)