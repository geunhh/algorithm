import sys
sys.stdin = open('heap.txt')
from heapq import heappush, heappop

for tc in range(1,int(input())+1):
    N=int(input())
    arr = list(map(int,input().split()))

    heap = []

    for num in arr:
        heappush(heap,num)
    result = 0
    i=N-1
    while i>=1:
        print(i)
        if i // 2 >= 1 :
            result += heap[i//2]
            i//=2






    # while heap:
    #     print(heappop(heap), end = ' ')
    print(result)

    break