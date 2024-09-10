import sys
sys.stdin = open('virsu.txt')
def make_set(n):
    p = [i for i in range(n+1)]  # 각 원소의 부모를 자신으로 초기화
    return p


def find(x):
    if parents[x] == x:  # x 자기자신이 x 를 바라본다 == 해당 집합의 대표자를 찾았다
        return x
        # x의 부모가 가리키고 있는 정점부터 다시 대표자를 탐색
    return find(parents[x])

def union(x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    elif root_x < root_y:
        parents[root_y] = root_x  # y 가 바라보는 부모는 x 의 대표자
    else:
        parents[root_x] = root_y


N = int(input()) # 컴퓨터의 수
E = int(input()) # 간선의 수

parents = make_set(N)
# print(parents)

# print(parents)
for _ in range(E):
    x, y = map(int,input().split())
    union(x,y)

cnt=0
for i in range(N+1):
    if find(1) == find(i):
        cnt += 1
print(cnt-1)

for item in parents:
    if item == 1:
        cnt+=1
print(parents)