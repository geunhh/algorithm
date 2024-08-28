import sys
sys.stdin = open('binary')

def inorder(node):
    global cnt
    if node ==0:
        cnt+=1
        return

    inorder(left[node])
    result[node]=cnt
    inorder(right[node])

    # print('reulst',result)


T=int(input())
for tc in range(1,T+1):
    n= int(input())

    left = [0] * (n+1)
    right = [0] * (n+1)
    result = [0] * (n+1)


    cnt=0
    for i in range(2,n+1):
        if not left[i//2]:
            left[i//2] = i
        else:
            right[i//2] = i
    cnt=0
    inorder(1)
    print(f'#{tc} {result[1]} {result[n//2]}')

    # break


