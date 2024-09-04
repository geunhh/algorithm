import sys
sys.stdin = open('q.txt')

def hoare_partition(left, right):
    pivot = arr[left]
    i = left+1
    j = right

    while i <= j :
        while i <= j and arr[i] <= pivot:
            i+=1
        while i<=j and arr[j] >= pivot:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j], arr[i]

    arr[left],arr[j] = arr[j],arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition(left,right)
        quick_sort(left,pivot-1)
        quick_sort(pivot+1,right)
for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(0,len(arr)-1)
    print(f'#{tc} {arr[N//2]}')


