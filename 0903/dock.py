import sys
sys.stdin = open('dock.txt')


for tc in range(1,int(input())+1):
    N= int(input())
    time_lst = []
    for _ in range(N):
        time_lst.append(list(map(int,input().split())))
    # print(time_lst)
    sorted_time = sorted(time_lst, key=lambda lst:lst[1])
    # print(sorted_time)

    time = 0
    cnt=0
    for start, end in sorted_time:
        if start >= time:
            cnt+=1
            time = end
    print(f'#{tc} {cnt}')
