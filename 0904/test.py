import sys

sys.stdin = open('paper.txt')


def check(start_row, end_row, start_col, end_col):
    # 종료조건: 구역의 크기가 1x1일 때
    if end_col - start_col == 1 and end_row - start_row == 1:
        global cnt1, cnt0, cnt_minus1
        if arr[start_row][start_col] == 1:
            cnt1 += 1
        elif arr[start_row][start_col] == 0:
            cnt0 += 1
        else:
            cnt_minus1 += 1
        return

    # 같은 수인지 검사
    cur_val = arr[start_row][start_col]
    same = True
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if arr[i][j] != cur_val:
                same = False
                break
        if not same:
            break

    if same:
        # 구역이 모두 동일한 값이라면 그 값을 카운트
        if cur_val == 1:
            cnt1 += 1
        elif cur_val == 0:
            cnt0 += 1
        else:
            cnt_minus1 += 1
    else:
        # 구역이 동일한 값이 아니면 9개로 분할하여 재귀적으로 검사
        seg_row = (end_row - start_row) // 3
        seg_col = (end_col - start_col) // 3

        for i in range(3):
            for j in range(3):
                new_start_row = start_row + i * seg_row
                new_end_row = new_start_row + seg_row
                new_start_col = start_col + j * seg_col
                new_end_col = new_start_col + seg_col
                check(new_start_row, new_end_row, new_start_col, new_end_col)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt1, cnt0, cnt_minus1 = 0, 0, 0
check(0, N, 0, N)

print(cnt1)
print(cnt0)
print(cnt_minus1)
