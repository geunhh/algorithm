import sys
sys.stdin = open('byeonghap.txt')
def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr

    mid = len(arr) //2
    left = arr[:mid]
    right= arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt+=1

    return merge(left,right)

def merge(left,right):
    result = [0] *(len(left)+len(right))
    l=r=0

    while l <len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l+=1
        else :
            result[l+r] = right[r]
            r+=1
    while l< len(left):
        result[l+r] = left[l]
        l+=1

    while r< len(right):
        result[l+r] = right[r]
        r+=1

    return result

for tc in range(1,int(input())+1):
    N= int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    cnt = 0
    arr = merge_sort(arr)
    # print(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')