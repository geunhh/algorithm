import sys
sys.stdin= open('1.txt')
from collections import defaultdict

def preorder(node):
    if node == None:
        return

    print(node, end=' ')
    preorder(graph[node][0])
    preorder(graph[node][1])


V = int(input())
lst = list(map(int,input().split()))

graph = defaultdict(lambda : [None,None])

for i in range(len(lst)//2):
    if graph[lst[2*i]][0] == None:
        graph[lst[2 * i]][0] = lst[2 * i + 1]
    else:
        graph[lst[2 * i]][1] = lst[2 * i + 1]

preorder(1)
