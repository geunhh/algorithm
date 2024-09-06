import sys
sys.stdin = open('airstrip.txt')

'''
경사로는 x 길이, 1의 높이
높이차가 1이고, 낮은 지형으 ㅣ높이가 동일하게 연속되는 곳에 설치 가능.

j값을 먼저 검사. 
같으면 continue해주는데, cnt+1, cnt로 시작점 알아볼겨.
다르면 cnt에 따라서 경사로가 설치될 수 있는지 확인.
1. cnt >= k 
    1) cnt >= 2*k : 무조건 설치 가능
    2) 그게 아니라면, 양 옆의 값이 하나는 크고 하나는 작아야 함.
        + 만약 cur_v가 bef_v보다 크면, 반대쪽이 작아야함. 
                                (cur_j-cnt-1)
        + 둘 다 작으면 cnt=1,j+=1 continue
2. cnt < k:
    1) 다시 시작. cnt=1,j+=1
    
마지막에 while문이 끝나버리면,
저장된 cnt값과 -cnt-1 을 이용해서 경사로 설치할 수 있는지 다시 확인.
 


'''
def check(mapp,X):
    global result
    j = 1
    before_val = mapp[0]
    cnt=1
    while j < N:
        # 같은 값이 나오면
        if mapp[j] == mapp[j-1]:
            cnt+=1
            j+=1
            continue
        # 다른 값이 나오면
        else:
            # cnt가 k이상이다?
            if cnt >= X:
                # cnt가 k의 2배일 때 + mapp의 좌우에 더 높은 곳이 한 곳이라고 있다면
                if cnt >= 2*X and (mapp[j] < mapp[j-1] or mapp[j-cnt-1] > mapp[j-1]):
                    result += 1
                    break
                # cnt가 k보다 크거나 같을 때
                else:
                    # 시작이 벽
                    if j-cnt == 0 :
                        if mapp[j]>mapp[0]:
                            result += 1
                            break
                        else:
                            cnt=1
                            j+=1
                            continue

                    # cnt 구간 좌우 중 한쪽은 높고 한쪽은 낮으면,
                    elif (mapp[j] > mapp[j-1] and mapp[j-cnt-1] < mapp[j-1]) or\
                       (mapp[j] < mapp[j-1] and mapp[j-cnt-1] > mapp[j-1]):
                        result +=1
                        break
                    else:
                        cnt=1
                        j+=1
                        continue
            # cnt가 k보다 작을 때
            else:
                cnt=1
                j+=1
                continue
    # break 없이 끝났을 때
    else:
        if cnt >=X and mapp[N-1] < mapp[N-cnt-1]:
            result+=1

    return







for tc in range(1,int(input())+1):
    N,X = map(int,input().split())
    row_map = [list(map(int,input().split())) for _ in range(N)]

    result=0

    # 가로
    for i in range(N):
        check(row_map[i],X)


    # 세로
    col_map=[[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            col_map[i].append(row_map[j][i])

    for j in range(N):
        check(col_map[j],X)

    print(result)

    break