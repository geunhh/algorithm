for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    i=0         # 0부터 시작
    can_move=0
    # print(N,K)
    # print(lst)

    while i<N:              # N-1 칸까지만 이동.
        # 첫칸부터 먹이가 없다.
        if lst[0]==0:
            break

        # index에 먹이가 있으면
        if lst[i] == 1:
            can_move = K    # 이동 거리 K만큼 리필.
            i+=1            # 이동 +1.
            continue

        # 이동 가능한 거리 -1
        can_move-=1
        # 더이상 이동할 수 없고 먹이도 없을 때
        if can_move == 0 and lst[i] ==0 :
            break

        i+=1                # 이동 +1.

    if i > N-1:               # 범위를 넘어선다면
        i=N-1



    print(f'#{tc} {i+1}')
