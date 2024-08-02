import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for test_case in range(1, 1+T):

    lst = [list(input()) for _ in range(5)]
    print(lst)
    max_len = 0
    for lst in lst:
        if max_len < len(lst):
            max_len = len(lst)

    print(max_len)

    zero_matrix = [[0] * max_len for _ in range(max_len)]
    print(zero_matrix)
    # 전치
    for i in range(max_len):
        for j in range(max_len):
            zero_matrix[i][j] = lst[j][i]

    # 전치2

    # max(len())
    # for i in range()
    print()
