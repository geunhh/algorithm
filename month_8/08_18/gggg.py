def ILLIT_Magnetic(matrix):
    cnt = 0
    N = len(matrix)  # 행렬의 크기
    for col_idx in range(len(matrix[0])):  # 열 인덱스를 기준으로 반복
        N_flag = False
        for row_idx in range(N):  # 각 열의 모든 행을 순회
            value = matrix[row_idx][col_idx]
            if value == 1:  # N극이 나오면
                N_flag = True
            elif N_flag and value == 2:  # S극이 나오면
                cnt += 1
                N_flag = False  # 다시 N극을 기다리기 위해 초기화
    return cnt

for testcase in range(1, 11):
    N = int(input())
    imatrix = [list(map(int, input().split())) for _ in range(N)]
    answer = ILLIT_Magnetic(imatrix)
    print(f"{testcase} {answer}")
