import sys
sys.stdin = open('bus.txt')

def bus (i,cnt):
    global min_cnt
    if cnt > min_cnt:
        return
    if i >= N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return


    # print(lst[i])
    for k in range(1,new_lst[i]+1):
        bus(i+k,cnt+1)



for tc in range(1,int(input())+1):
    N, *new_lst = list(map(int,input().split()))
    # print(new_lst)

    min_cnt=float('inf')
    bus(0,0)

    print(f'#{tc} {min_cnt-1}')


