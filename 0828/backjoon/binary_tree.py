import sys
from collections import defaultdict

def post_order(node):
    if value[node] != 0:        # 현재 노드가 0이 아닐 때 후위순회 할겨        #
        # 왼쪽
        if value[node*2] !=0 :  # 왼쪽이 0이 아니다? 다시 왼쪽 확인.
            post_order(node*2)
        # 오른쪽
        if value[node*2+1] !=0: # 오른쪽이 0이 아니다? 다시 오른쪽 확인.
            post_order(node*2+1)
        print(value[node])      # 좌우 둘다 0이면 출력.


def insert(node,cur_v):
    # 값이 없으면 삽입
    if value[node] == 0:
        value[node] = cur_v
        return
    # 루트와 비교해서 작으면 왼쪽
    elif cur_v < value[node]:
        insert(node*2,cur_v)
    # 루트와 비교해서 크면 오른쪽
    elif cur_v > value[node]:
        insert(node*2+1,cur_v)


# 파일을 읽기 모드로 열기
with open('binary_tree.txt', 'r') as f:
    # 여러 줄의 입력을 리스트로 받아오기
    input_data = f.read().strip().split()
# 입력값을 정수형으로 변환
data = list(map(int, input_data))
# print(data)  # 결과 출력

graph=defaultdict(list) # 경로 -> 필요 없었음.
value=defaultdict(int)  # value 값 저장을 위함
# print(graph)



for num in data:
    insert(1, num)

# print(value)
post_order(1)