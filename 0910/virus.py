import sys
sys.stdin = open('virsu.txt')

def make_set(n):
    p = [i for i in range(n+1)]  # 각 원소의 부모를 자신으로 초기화
    r = [0] * (n+1)
    return p,r

def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y]:
        parents[root_x] = root_y  # y 가 바라보는 부모는 x 의 대표자
    else:
        parents[root_y] = root_x
        ranks[root_x] += 1


N = int(input()) # 컴퓨터의 수
E = int(input()) # 간선의 수

parents,ranks = make_set(N)

for _ in range(E):
    x, y = map(int,input().split())
    union(x,y)
# print(parents)
# print(ranks)
cnt=0
for i in range(N+1):
    if find(1) == find(i):
        cnt += 1

print(cnt-1)

