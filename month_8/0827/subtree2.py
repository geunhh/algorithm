import sys
sys.stdin= open('subtree.txt')

def subtree(node):
    global cnt
    if node == 0:
        return
    else :
        cnt+=1

    subtree(left[node])
    subtree(right[node])


for tc in range(1,int(input())+1):
    E,S = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(arr)
    cnt=0
    length = max(arr)
    left = [0] * (length+1)
    right = [0] * (length+1)

    for i in range(E):
        p,c = arr[i*2],arr[i*2+1]

        if left[p] == 0:
            left[p]=c
        else:
            right[p] =c

    print(left)
    print(right)

    subtree(S)
    print(f'#{tc} {cnt}')