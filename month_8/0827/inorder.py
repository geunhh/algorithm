import sys
from collections import defaultdict
sys.stdin = open('inorder.txt')

def dfs(node):
    if node == -1:
        return

    dfs(graph[node][0])
    inorder.append(node)
    dfs(graph[node][1])

for tc in range(1,11):
    N = int(input()) # 정점의 개수

    word=[]
    arr = []
    for _ in range(N):
        lst = input().split()
        # print(lst)
        word.append(lst[1])
        if len(lst) >=3:
            arr.append(lst[0])
            arr.append(lst[2])
        if len(lst) >=4:
            arr.append(lst[0])
            arr.append(lst[3])
    E = len(arr)//2

    # graph 만들기.
    graph = [[] for _ in range(N+1)]
    for i in range(E):
        v1,v2 = arr[i*2], arr[i*2+1]
        graph[int(v1)].append(int(v2))

    # 이진트리 -> 빈 곳 -1로 채워주기
    for i in range(N+1):
        while len(graph[i]) < 2:
            graph[i].append(-1)


    inorder=[]

    dfs(1)
    print(f'#{tc}',end=' ')
    for i in inorder:
        print(word[i-1], end='')
    print()



