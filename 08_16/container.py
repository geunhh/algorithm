

'''
1
3 2
1 5 3
8 3
'''

T = int(input())
for tc in range(1, T+1):
    N,M =map(int,input().split())
    # N 컨테이너 수
    # M 트럭 수
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    print(truck)
    print(container)
    truck.sort(reverse=True)
    container.sort(reverse=True)


    print(truck)
    print(container)
    sum =0
    for truck_i in range(M):
        for con_i in range(len(container)):
            if truck[truck_i] - container[con_i] >=0:                
                sum += container[con_i]
                container.pop(0)
    print(sum)

    break