from collections import defaultdict
import sys
sys.stdin = open('tree.txt')

def order(node):
    if node == None:
        return

    order(tree[node][0])

    order(tree[node][1])
    print(node, end=' ')


N= int(input())
arr = list(map(int, input().split()))
tree = defaultdict(lambda :[None,None])

for i in range(0,len(arr),2):
    p,c = arr[i], arr[i+1]
    if tree[p][0] == None:
        tree[p][0] = c
    else :
        tree[p][1] = c
print(tree)
order(1)
