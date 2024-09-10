import sys
sys.stdin = open('brick.txt')
# 구슬은 N번 쏠 수 있다.
# 가장 위쪽에 위치한 벽돌만 깰 수 있으며,

# 1. 원본을 수정하고 복구시켜준다? -> 복구가 오래걸림.
# 2. 복사본을 수정하고 다음으로 전달.

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]


def shoot(level, remains, now_arr):
    global min_blocks
    # 기저 조건
    # 구슬을 모두 발사 or 남은 벽돌이 0
    if remains==0 or level==N:
        # 최소값 갱신
        min_blocks = min(min_blocks, remains)
        return

    # 1. 한 줄씩 쏘자
    for col in range(W):
        # 방법 1. (얘는 복구 시간이 너무 오래걸림)
        # 1. column 위치에 쏘기 전 상태를 복사
        # 2. 원본 리스트의 col 위치에 구슬을 쏜다.
        # 3. level+1 번 상태로 이동(다음 재귀 호출)
        # 4. col 위치에 쏘기 전 상태로 복구.

        # 방법 2.
        # 1. column 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 구술을 쏜다.
        # 3. level +1 번 상태로 이동(다음 재귀 호출) + col 위치에 쏘고 난 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬을 쏘자!
        # 1. 구슬을 쏘는 열에서 가장 위에 있는 벽돌을 찾자.
        row = -1        # 벽돌이 없다고 가정
        for r in range(H):
            if copy_arr[r][col]:    # r 위치에 벽돌이 있다면,
                row = r             # 가장 위로 갱신
                break
        if row == -1 :  # 벽돌이 없는 열이면 다음 열로 넘어감
            continue

        # 2. 벽돌이 연쇄적으로 깨짐
        # 행 열 숫자(파워)
        li = [(row,col,copy_arr[row][col])] # 앞으로 깨져야할 벽돌들을 저장.
        now_remains = remains-1 # 현재 남음 벽돌 -1
        copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 깨짐 처리.

        while li:
            r,c,p = li.pop()
            for k in range(1,p):    # 파워만큼 퍼지면서 깨진다.
                for i in range(4):  # 상하좌우
                    nr = r + (dy[i]*k)
                    nc = r + (dx[i]*k)

                    if nr<0 or nr >=H or nc<0 or nc>= W:    # 범위 계산
                        continue

                    if copy_arr[nr][nc] == 0 :  #벽돌이 없다면 통과
                        continue

                    li.append((nr,nc,copy_arr[nr][nc]))     # 후보 벽돌에 추가
                    copy_arr[nr][nc] = 0                    # 벽돌 깨짐짐
                    now_remains -=1                         # 은 벽돌 감소

            # 빈칸 메꾸기.
            for c in range(W):  # 전체 열들을 확인.
                idx = H - 1     # 벽돌이 위치할 인덱스
                for i in range(H-1,-1,-1):  #위에서 부터 확인
                    if copy_arr[r][c]:      # 벽돌이 있으면 무조건 swap하도록
                        # idx와 r이 같아도 바꾼다. -- 의미없는 교환이지만, 가독성을 위해서.
                        copy_arr[r][c], copy_arr[idx][c], copy_arr[idx][c], copy_arr[r][c]
                        idx-=1
            shoot(level+1, now_remains,copy_arr)







    # -> 벽돌이 깨진 상태
    # -> 중력을 받은 상태.






for tc in range(1,int(input())+1):
    N, W, H = map(int,input().split())

    # 1. 최소 벽돌 개수.
    # - 몇 개 남았을까? 계산해야 함. -> 2차원 리스트를 순회하며 매번 계산하면 느림.
    # 2. 남은 벽돌이 없다면, 더 이상 진행할 필요가 없다.
    # - 현재 남은 벽돌 수도 같이 저장하면 좋을 것 같다.
    # 3. N 번 구슬을 쏘자.
    # - 시작점 : 0번 / 하나도 안 깨진 벽돌 수.
    # - 끝점 : N번 쏘면 끝 / 벽돌이 다 깨지면 끝.

    arr = [list(map(int,input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el :
                blocks += 1
    print(blocks)

    shoot(0, blocks,arr)

    print(f'#{tc} {min_blocks}')
