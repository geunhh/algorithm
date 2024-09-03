import sys
sys.stdin = open('6.txt')

from collections import defaultdict

def order(node):

    # tree[node] -> [[2,3],value] or [[None,None],value] or [[None,None],0]

    # 연산자가 등장하면 left right 친구들 호출 -> return 받아서 연산 -> 결국 node 1까지 옴.
    if tree[node][1] == '+':
        return order(tree[node][0][0]) + order(tree[node][0][1])
    elif tree[node][1] == '-':
        return order(tree[node][0][0]) - order(tree[node][0][1])
    elif tree[node][1] == '*':
        return order(tree[node][0][0]) * order(tree[node][0][1])
    elif tree[node][1] == '/':
        return order(tree[node][0][0]) // order(tree[node][0][1])

    # 연산자가 아니면 리턴 해주기.
    else :
        return int(tree[node][1])


for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    tree = defaultdict(lambda: [[None, None],0])

    #list에 넣기
    for _ in range(N):
        lst = input().split()

        tree[int(lst[0])][1] = lst[1]                # 노드마다 value 넣어주기

        if len(lst) == 4:                            # 자식 노드를 함께 입력받으면
            tree[int(lst[0])][0][0] = int(lst[2])    # 넣어주기 [None,None] --> [a,b]
            tree[int(lst[0])][0][1] = int(lst[3])


    result = order(1)                                # 호출
    print(f'#{tc} {result}')

