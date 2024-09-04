import sys
sys.stdin = open('paper.txt')

def check(start_row, end_row, start_col, end_col):

    # 종료 조건 : 하나만 남았을 때 그 값 +1 해주기.
    if end_col-start_col == 1 and end_row - start_row == 1:
        global cnt1, cnt0,cnt_minus1
        if arr[start_row][start_col] == 1:
            cnt1 += 1
        elif arr[start_row][start_col] == 0:
            cnt0 += 1
        else:
            cnt_minus1 += 1
        return

    # 1. 같은 수인지 검사하기
    cur_val = arr[start_row][start_col]     # 기준점이 될 값
    same = True                             # 구역 안의 친구들이 같은 값인지 확인하려고 씀.
    for i in range(start_row,end_row):      # row 순회
        for j in range(start_col,end_col):  # col 순회
            if arr[i][j] != cur_val:        # 기준값이랑 다른 친구가 있다?
                same = False                # same = False 주고
                break                       # break
        if not same:                        # 포문 하나 더 break
            break

    # 2. 후처리
    if same:                                   # 모두 같은 값이면 수행.
        if arr[start_row][start_col] == 1:
            cnt1 += 1
        elif arr[start_row][start_col] == 0:
            cnt0 += 1
        else:
            cnt_minus1 += 1

    # 2-1. 후처리2
    else:                                       # 다른 값이 있었다면
        seg_row = (end_row-start_row)//3        # 구간의 길이를 새로 구해줌.
        seg_col = (end_col-start_col)//3        # column 도

        # 요런식으로 나눠줄겨
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # 총 9 구역 호출 이게 맞나? 돌아 가긴 하나.
        check(start_row, start_row+seg_row, start_col, start_col+seg_col)                          # 1번 구역
        check(start_row, start_row+seg_row, start_col+seg_col, start_col+2*seg_col)                # 2번 구역
        check(start_row, start_row+seg_row, start_col+2*seg_col, start_col+3*seg_col)              # 3번 구역
        check(start_row+seg_row, start_row+2*seg_row, start_col, start_col+seg_col)                # 4번 구역
        check(start_row+seg_row, start_row+2*seg_row, start_col+seg_col, start_col+2*seg_col)      # 5번 구역
        check(start_row+seg_row, start_row+2*seg_row, start_col+2*seg_col, start_col+3*seg_col)    # 6번 구역
        check(start_row+2*seg_row, start_row+3*seg_row, start_col, start_col+seg_col)              # 7번 구역
        check(start_row+2*seg_row, start_row+3*seg_row, start_col+seg_col, start_col+2*seg_col)    # 8번 구역
        check(start_row+2*seg_row, start_row+3*seg_row, start_col+2*seg_col, start_col+3*seg_col)  # 9번 구역

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt1, cnt0, cnt_minus1 = 0, 0, 0
check(0,N,0,N)
print(cnt_minus1)
print(cnt0)
print(cnt1)