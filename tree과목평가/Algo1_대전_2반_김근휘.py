for tc in range(1,int(input())+1):
    N = int(input())
    lst = input()
    max_cnt = 1
    for i in range(1, N-1):
        # 대칭 확인
        k   = 1     # 좌우 하나씩 늘려서 확인할 용도
        cnt = 1     # 대칭 하는 거리 저장하는 용도
        while i-k >=0 and i+k<N:            # index가 유효한가??
            if lst[i-k] == lst[i+k]:        # 좌우가 대칭이라면
                k += 1                      # 한칸 더 옮기고
                cnt += 2                    # 좌우 대칭이니까 거리 2 올리기
                if max_cnt < cnt :          # max_cnt 갱신해주기
                    max_cnt = cnt
                continue
            else:
                break

    print(f'#{tc} {max_cnt}')

