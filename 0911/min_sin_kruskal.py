import sys
sys.stdin = open('mi_sin.txt')

def find_set(x):
    if parents[x] ==x :
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y



for tc in range(1, int(input())+1):
    cnt=0
    total=0
    V,E = map(int,input().split()) # 마지막 노드 번호, 간선 개수
    edge = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge.append([n1,n2,w])
    print(edge)
    edge.sort(key=lambda x:x[2])    # 가중치에 따라 sort.
    print(edge)
    parents = [i for i in range(V+1)]

    for u,v,w in edge:
        if find_set(u) != find_set(v):
            cnt+=1
            union(u,v)
            total += w
            if cnt == V:
                break
    print(f'#{tc} {total}')

    break


