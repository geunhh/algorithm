def make_set(n):
    p = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
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

    # 다른 집합이라면 더 작은 루트노트에 합친다. (index가 작은)
    # 문제에 따라 다르다.
    if root_x < root_y:
        parents[y] = root_x  # y 가 바라보는 부모는 x 의 대표자
    else:
        parents[x] = root_y
n = 7
parents = make_set(n)
print(parents)

union(1,3)
print(parents)
union(2,3)
print(parents)
union(2,5)
print(parents)

print('find_set(6) = ', find(3))


