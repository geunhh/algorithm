import sys
sys.stdin = open('airstrip.txt')

'''
경사로는 x 길이, 1의 높이
높이차가 1이고, 낮은 지형으 ㅣ높이가 동일하게 연속되는 곳에 설치 가능.

j값을 먼저 검사. 

같으면 continue해주는데, cnt+1, cnt로 시작점 알아볼겨.

다르면 cnt에 따라서 경사로가 설치될 수 없는지 확인.
1. mapp[j]와 mapp[j-1]의 높이차가 2이상이면 애초에 불가능 바로 return

2. mapp[j]와 mapp[j-1]이 같은 높이다? 그럼 cnt하나 올려주고, 한칸 이동
3. mapp[j]와 mapp[j-1]이 다른 높이다? 
    1) j가 j-1보다 높을 때
        cnt 가 k보다 작으면 -> 설치 못하니까 return
        cnt 가 k 보다 높다? -> 설치가능하니까 j+=1 하고 cnt 1로 continue
    2) j가 j-1보다 낮을 때
        1. 뒷 구간에 충분한 공간이 있는지 확인.
          1-1 있다면 설치하고 다음 구간 탐색
          1-2 없다면 return
    
    
while이 무사히 끝나면, result +=1
'''
def check(mapp,X):
    global result
    j = 1
    before_val = mapp[0]
    cnt=1

    while j < N:
        # 두칸의 높이 차가 2 이상이면 연결 불가.
        if abs(mapp[j] - mapp[j-1]) > 1:
            return

        # 같은 높이일 때
        if mapp[j] == mapp[j-1]:
            cnt+=1
            j+=1
            continue

        # 다른 값이 나오면 현재가 더 높을 떄 -> 이전에 활주로 설치 가능한가?
        elif mapp[j] == mapp[j-1]+1:
            if cnt < X:
                return
            cnt = 1
            j+=1
            continue
        # 현재가 낮아졌을 때 -> 다음에 올 수 있는가?
        elif mapp[j] == mapp[j-1]-1:
            # 이후에 공간 확인
            for k in range(j,j+X):  # 활주로 올 구간까지 사악 검사하는데,
                if k >= N or mapp[k] != mapp[j]: # 구간을 넘어가거나, 다른 애가 나오면 컷.
                    return
            # 그렇지 않으면 계속 검사.
            j+=X    # 근데 이번엔 X만큼 옮겨서 고고싱
            cnt=0   # 0 or 1
            continue
    # break 없이 끝났을 때
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
    # 전치행렬 만들어줘야지.
    col_map=[[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            col_map[i].append(row_map[j][i])    # 세로로 입력되게 따로 만들어버림

    for j in range(N):
        check(col_map[j],X)

    print(f'#{tc} {result}')
