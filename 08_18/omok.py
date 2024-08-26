import sys
sys.stdin = open('omok.txt')
def check(i,j,dir):
    cur_cnt = 1
    # 양쪽으로 체크.
    for k in range(1, 5):
        di, dj = i + dir[0][0] * k, j + dir[0][1] * k
        if 0 <= di < N and 0 <= dj < N and omok[di][dj] == 'o':
            cur_cnt += 1
        else:
            break
    # 반대 방향 체크
    for k in range(1, 5):
        di, dj = i + dir[1][0] * k, j + dir[1][1] * k
        if 0 <= di < N and 0 <= dj < N and omok[di][dj] == 'o':
            cur_cnt += 1
        else:
            break
    if cur_cnt == 5:
        return True
    return False

def omokgame(N):
    # 각 방향 선언
    dir1 = [[1, 0], [-1, 0],[0, 1], [0, -1],[1, 1], [-1, -1],[1, -1], [-1, 1]]

    for i in range(N):
        for j in range(N):
            # 공이 있으면 확인 시작
            if omok[i][j] == 'o':
                if check(i,j,dir1[0:2]) == True or \
                    check(i, j, dir1[2:4]) == True or \
                    check(i, j, dir1[4:6]) == True or \
                    check(i, j, dir1[6:8]) == True :
                    return 'YES'
    return 'NO'

for tc in range(1, int(input())+1):
    N = int(input()) # NxN 판.
    omok = [input() for _ in range(N)]
    sol = omokgame(N)
    print(f'#{tc} {sol}')


