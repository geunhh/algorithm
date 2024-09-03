import sys

sys.stdin = open("input.txt", "r")


def Pali(lst, M, N):
    # 가로 체크
    for i in range(N):  # 한줄씩
        for j in range(N + 1 - M):  # 회문 길이에 따라 확인할 첫 인덱스 ~ 마지막 인덱스.
            word = lst[i][j:j + M]

            for index in range(M // 2):                 # index M//2
                if word[index] != word[-index - 1]:     # 확인.
                    break
            else:
                return ''.join(word)


    zero_matrix = [[0] * N for _ in range(N)]       # 전치행렬로 바꾸기.

    for i in range(N):
        for j in range(N):
            zero_matrix[i][j] = lst[j][i]
            # if i < j:
            #     lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

    # 가로 체크
    for i in range(N):  # 한줄씩
        for j in range(N + 1 - M):  # 회문 길이에 따라 확인할 첫 인덱스
            word = zero_matrix[i][j:j + M]
            # print(word)
            for index in range(M // 2):
                if word[index] != word[-index - 1]:
                    break
            else:
                return ''.join(word)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N : NxN, M : 회문의 길이

    # lst = [list(input().split()) for _ in range(N)]
    lst = [list(input()) for _ in range(N)]
    # print(lst)

    result = Pali(lst, M, N)
    print(f'#{test_case} {result}')


