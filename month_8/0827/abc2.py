from _collections import defaultdict

import sys
sys.stdin = open('inorder.txt')

def info(arr,graph):

    for lst in arr:
        graph[int(lst[0])] = lst[1:]
    print(len(graph))
    print(graph)
    #
    for i in range(1, len(graph)):
        while len(graph[i]) <3:
            graph[i].append('0')
    print(graph)

def inorder(node):
    if node == 0:
        return

    inorder(int(graph[node][1]))
    inorder_lst.append(graph[node][0])
    inorder(int(graph[node][2]))



for tc in range(1,11):
    N=int(input())

    name = [] * (N+1)
    arr = [input().split() for _ in range(N)]
    graph = [0] * (N+1)
    inorder_lst = []
    print(arr)
    print(graph)
    info(arr, graph) # graph 이쁘게 만들기
    inorder(1)

    print(*inorder_lst)
    break




