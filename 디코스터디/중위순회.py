import sys
from _collections import defaultdict
sys.stdin = open('1.txt')
def order(node):
    if graph[node][1] == None:
        return
    # print(graph[node][1])
    order(graph[node][0][0])        # W??
    print(graph[node][1],end='')    # 나는 join도 result=''도 귀찮아서 그냥
                                    # print 해버려 -> 런타임 오래걸림..
    # result += graph[nod]
    order(graph[node][0][1])

for tc in range(1,11):
    N = int(input())

    graph = defaultdict(lambda: [[None,None],None]) # [[left,right],value]

    # input 처리
    for _ in range(N):
        lst = list(input().split())

        graph[int(lst[0])][1] = lst[1]

        if len(lst) == 3:                         # 3개면 왼쪽 자식만 추가
            graph[int(lst[0])][0][0] = int(lst[2])
        elif len(lst) == 4:                         # 4개면 좌우 둘 다  추가
            graph[int(lst[0])][0][0] = int(lst[2])
            graph[int(lst[0])][0][1] = int(lst[3])
        # int 처리 잘해줘야 한다링 하하하하하하하ㅏ하하하하하하하하ㅏ하하하하ㅏㅎ
        # 아까도 같은 실수 했는데
    # print(graph)
    print(f'#{tc}',end=' ')
    order(1)
    print()             #