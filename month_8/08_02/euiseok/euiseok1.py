import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, 1+T):

    arr=[]
    for _ in range(5):
        row = list(input().split())
        # print(row)
        arr += row
    # print()
    max_len=0
    for lst in arr:
        if max_len < len(lst):
            max_len = len(lst)


    # 전치 행렬 만들기
    zero_matrix = [[0] * max_len for _ in range(max_len)]
    # print(zero_matrix)
    # 전치
    for i in range(max_len):
        for j in range(max_len):
            # NxN이 아닌 경우 에러가 뜨기 때문에 예외처리 해줌
            try:
                zero_matrix[i][j] = arr[j][i]
            except IndexError:
                pass

    # print(zero_matrix)
    word =''
    for row in zero_matrix:
        for c in row:
            if c != 0:
                word += c
    print(f'#{test_case} {word}')









    # 전치2

    # max(len())
    # for i in range()
    # break
