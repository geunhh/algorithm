import sys
sys.stdin= open('2.txt')
from collections import defaultdict

def inorder(node):
    if node == None:
        return

    inorder(graph[node][0])
    print(value[node], end='')
    inorder(graph[node][1])

for tc in range(1,11):
    N=int(input())

    graph = defaultdict(lambda : [None,None])
    value = [0] * (N+1)

    # input 길이에 따라 처리를 다르게 함
    for _ in range(N):
        input_1 = list(input().split())
        if len(input_1) == 2:
            value[int(input_1[0])] = input_1[1]
        elif len(input_1) == 3 :
            value[int(input_1[0])] = input_1[1]
            graph[int(input_1[0])][0] = int(input_1[2])
        else:
            value[int(input_1[0])] = input_1[1]
            graph[int(input_1[0])][0] = int(input_1[2])
            graph[int(input_1[0])][1] = int(input_1[3])
    print(f'#{tc}',end =' ')
    inorder(1)
    print()