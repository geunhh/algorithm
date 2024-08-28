import sys
sys.stdin = open('heap.txt')
import heapq

for tc in range(1,int(input())+1):
    N= int(input())
    arr = list(map(int, input().split()))
    # heapq.heapify(arr)
    heap=[]
    for num in arr:
        heapq.heappush(heap,num)

    # print(arr)

    result = 0
    i = N-1 # n-1 ~ -1
    while i > 0:
        i = (i-1)//2
        # print(i, arr[i])
        result += heap[i]

    print(f'#{tc} {result}')
