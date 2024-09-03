import sys
sys.stdin = open('tree.txt')
from collections import defaultdict

def inorder(node):
    if value[node] == 0:
        return

    inorder(tree[node][0])
    print(value[node],end='')
    inorder(tree[node][1])


for tc in range(1,11):
    N = int(input())
    value = defaultdict(int)
    tree = defaultdict(lambda :[None,None])

    # tree와 value 구성
    for i in range(N):
        lst = input().split()

        value[int(lst[0])] = lst[1]

        if len(lst) ==3:
            tree[int(lst[0])][0] = int(lst[2])
        if len(lst) ==4:
            tree[int(lst[0])][0] = int(lst[2])
            tree[int(lst[0])][1] = int(lst[3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()


