import sys
sys.stdin = open('input.txt')
def preorder(node):
    if node != 0:
        preorder(left[node])
        print(node, end =' ')
        preorder(right[node])


V= int(input())
E = list(map(int,input().split()))

left = [0] * (V+1)
right = [0] * (V+1)

for i in range(len(E)//2):
    p,c = E[2*i],E[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)

