import sys
sys.stdin = open('why.txt')

def order(node):
    if node > N:
        return 0

    if tree[node] == 0:
        tree[node] = order(2*node)+order(2*node+1)
    return tree[node]


for tc in range(1,int(input())+1):
    N,M,out = map(int,input().strip().split())
    tree = [0] * (N+1)
    for _ in range(M):
        lst = list(map(int,input().split()))
        tree[lst[0]] = lst[1]

    order(1)
    print(tree)



    break