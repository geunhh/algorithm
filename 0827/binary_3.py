import sys
sys.stdin = open('binary')

def inorder(node,N):
    global cnt

    if node <= N:
        inorder(node*2,N)
        tree[node] = cnt
        cnt+=1
        inorder(node*2+1, N)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N+1)
    cnt=1
    inorder(1,N)
    print(tree)
    print(f"#{t} {tree[1]} {tree[N//2]}")

