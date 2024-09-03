from collections import defaultdict
import sys
sys.stdin = open('tree.txt')

def order(node):
    if not tree[node]:
        return
    print(node, end=' ')

    # 조건을 안 달아주면 우측 자식이 없을 때 에러가 남.
    if len(tree[node]) >0:
        order(tree[node][0])

    if len(tree[node]) >1:
        order(tree[node][1])


N= int(input())
arr = list(map(int, input().split()))
tree = defaultdict(list)

for i in range(len(arr)//2):
    v1,v2 = arr[2*i],arr[2*i+1]
    tree[v1].append(v2)
print(tree)

order(1)