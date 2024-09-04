import sys
sys.stdin = open('b.txt')
def binary_search(start, end, target,check):
    global cnt
    # 종료조건
    if start > end:
        return
    mid = (start+end) // 2

    if target == A[mid]:
        cnt+=1
        return

    elif target < A[mid] and check != 1:
        binary_search(start, mid-1, target, 1)
    elif target > A[mid] and check != 0:
        binary_search(mid+1, end, target, 0)
    else :
        return


for tc in range(1,int(input())+1):
    A_len,B_len = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt=0
    for target in B:
        # print(target)
        binary_search(0,len(A)-1,target,-1)

    print(f'#{tc} {cnt}')
    # break

