# 1-3, 1-2 같은 조가 되고 싶다? -> 1-2-3이 같은 조가 됨.

import sys
sys.stdin = open('group.txt')

def make_set(n):
    p = [i for i in range(n)]
    return p

def findd(x):
    if parents[x] == x:
        return x
    parents[x] = findd(parents[x])
    return parents[x]

def union(x,y):
    root_x = findd(x)
    root_y = findd(y)

    if root_x == root_y:
        return

    if root_x <root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    in_lst = list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]

    # print(graph)
    parents = make_set(N+1)
    for i in range(0,len(in_lst),2):
        s,e = in_lst[i], in_lst[i+1]
        union(s,e)
    # print(parents)
    result_set=set()
    for j in range(1, N+1):
        result_set.add(findd(parents[j]))
    print(f'#{tc} {len(result_set)}')



