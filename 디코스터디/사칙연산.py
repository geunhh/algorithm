import sys
sys.stdin= open('2.txt')
from _collections import defaultdict

def order(node):

    if tree[node][1] == '+':
        return order(tree[node][0][0]) + order(tree[node][0][1])
    elif tree[node][1] == '-':
        return order(tree[node][0][0]) - order(tree[node][0][1])
    elif tree[node][1] == '*':
        return order(tree[node][0][0]) * order(tree[node][0][1])
    elif tree[node][1] == '/':
        return order(tree[node][0][0]) // order(tree[node][0][1])
    else :
        return int(tree[node][1])



for tc in range(1,11):
    N = int(input())
    tree = defaultdict(lambda : [ [None,None], 0])
                                # 이거 해봤는데 지저분해서 그렇지 좋아여

    # 1. 이쁘게 tree 만들기.
    for _ in range(N):
        lst = list(input().split())
        par = int(lst[0])               # 엄빠
        val = lst[1]                    # 값

        tree[par][1] = val              # 넣어주기

        if len(lst) ==4:                # 자식 노드도 같이 줬다?
            c1,c2 = int(lst[2]), int(lst[3])
            tree[par][0][0] = c1        # 넣어주기
            tree[par][0][1] = c2
    print(tree)

    result = order(1)
    print(f'#{tc} {result}')


