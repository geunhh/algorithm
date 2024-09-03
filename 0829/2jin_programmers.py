from collections import defaultdict
import math
# 트리 검사
def check(node,graph):
    # print(graph[])
    if graph[1] == '0': # 루트노드가 0? 바로 리턴.
        return 0

    while node < len(graph)//2: # 노드를 순회를 해 루트(1)부터
        # 부모 노드가 0인데, 자식중에 1인 녀석이 하나라도 있다?
        if graph[node] == '0' and (graph[node*2] == '1' or graph[node*2+1] == '1'):
            return 0        # 0 리턴
        node+=1             # 아니면 node 하나 올려서 다시 검사.
    else:
        return 1

# 트리 만들기
def insert(node,graph):
    global index
    if graph[node]==0:
        return
    # 그림 보면 중위순회로 값 넣어줘야 함.
    insert(2*node,graph)        
    graph[node] = binary_num[index]     # 값 넣어주고
    index+=1                            # 이진수의 다음 인덱스 값 넣어줌.
    insert(2*node+1,graph)

### main #####
numbers=[7,95,5]                          # input을 얘로 줬구요
answer = []                               # list를 반환해야해서 만들었습니다.
for N in numbers:   
    index = 0                             # 이진수 0또는1을 graph에 넣어주기 위한 idnex
    binary_num=bin(N)[2:]                 # bin()을 쓰면 0x111 이런식으로 붙어서 제거해줌
    graph = defaultdict(int)    
    
    # 높이 및 생성 노드수 구하기 -> 포화 이진을 만들어야하기 때문.
    cur_y = len(binary_num)             
    h = math.floor(math.log2(cur_y))      # 높이수 구하고
    y = 2**(h+1)-1                        # 높이수로 포화 이진의 노드수 구하고
    # 포화 이진 만들기 위해 0 채워주기
    while len(binary_num) <y:           
        binary_num = '0'+binary_num     
        # 42의 경우에 101010 인데 포화이진이 되려면 0101010이 되야 함.
    for i in range(y):                    # 이건 왜했지
        graph[i+1] = -1

    insert(1,graph)
    result = check(1,graph)
    answer.append(result)
print(answer)
