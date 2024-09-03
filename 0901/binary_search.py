import sys
sys.stdin= open('4.txt')
from collections import defaultdict

def order(node,N):
    global cnt
    if node == None :
        return
    order(graph[node][0],N)
    cnt+=1
    value[node]= cnt
    order(graph[node][1],N)

for tc in range(1,int(input())+1):
    N = int(input())
    cnt=0
    # 이진 트리 만들기
    graph = defaultdict(lambda : [None,None])
    for i in range(0,N-1):
        if graph[i//2+1][0] == None:
            graph[i//2+1][0] = i+2
        else:
            graph[i//2+1][1] = i+2

    # 순회 하기
    value = defaultdict(int)
    order(1,N)
    print(f'#{tc} {value[1]} {value[N//2]}')

    # break




