import heapq,sys
sys.stdin = open('7.txt')

for tc in range(1,int(input())+1):
    N=int(input())
    lst = list(map(int,input().split()))
    heap =[]
    for num in lst:
        heapq.heappush(heap,num)
    print(heap)

    result =0
    node = N-1
    while node >0:
        node = (node-1)//2
        result += heap[node]
    print(result)