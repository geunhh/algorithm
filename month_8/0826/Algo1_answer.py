T= int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int, input().split()))

    #1 현재 위치로부터 k범위 내에 가장 멀리 있는 먹이로 이동 계속 반복

    #   1.1 K범위 내에 먹이가 없다면, K까지 이동하고 멈춤 (끝)

    #2. 배열의 크기를 벗어나 이동하면 벗어나면 배열의 크기에서 멈춤 (끝)

    cur_pos = 0
    #인덱스를 변화시키면서 탐색.
    while True:
        last = cur_pos + K
        if last >= N:
            cur_pos = N-1
            break

        #1번 아이디어 탐색
        for i in range(last,cur_pos,-1):
            if arr[i] :
                cur_pos = i
                break
        else:
            cur_pos = last
            break

    print(f'#{tc} {cur_pos+1}')