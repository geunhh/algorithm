from collections import defaultdict
import math
def check(node,graph):
    # print(graph[])
    if graph[1] == '0':
        return 0

    while node < len(graph)//2:
        if graph[node] == '0' and (graph[node*2] == '1' or graph[node*2+1] == '1'):
            return 0
        node+=1
    else:
        return 1

def insert(node,graph):
    global index
    if graph[node]==0:
        return

    insert(2*node,graph)
    graph[node] = binary_num[index]
    index+=1
    insert(2*node+1,graph)

numbers=[7,95,5]
answer = []
for N in numbers:
    index = 0
    binary_num=bin(N)[2:]
    graph = defaultdict(int)
    # 높이 및 생성 노드수 구하기
    cur_y = len(binary_num)
    h = math.floor(math.log2(cur_y))    # 높이수
    y = 2**(h+1)-1                      # 노드수
    while len(binary_num) <y:
        binary_num = '0'+binary_num
    for i in range(y):
        graph[i+1] = -1

    insert(1,graph)
    result = check(1,graph)
    answer.append(result)
print(answer)
