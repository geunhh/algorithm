import sys
sys.stdin = open("snail/input.txt", "r")
sys.stdout = open("snail/output.txt", "w")

def sort():
    pass


def snail(new_arr, N):
    add = 0
    num_list = new_arr  # 넣은 숫자 list
    # print(num_list)
    z = 0
    a, b, c, d = 0, 0, 0, 0  # i,j

    new_list = [[0] * N for _ in range(N)]
    for index in range(2 * N - 1):
        # ->
        if index % 4 == 0:  # y축 고정 a
            for i in range(add, N - add):
                new_list[a][i] = num_list[z]
                z += 1  # 넣을 숫자 index 올리기.
            a += 1

        # 아래
        elif index % 4 == 1:  # x축 고정 b
            for j in range(add + 1, N - add):
                new_list[j][N - 1 - b] = num_list[z]
                z += 1  # 넣을 숫자 index 올리기.
            b += 1

        # <-
        elif index % 4 == 2:  # y 축 고정 c
            for i in range(N - 2 - add, add - 1, -1):
                new_list[c - 1][i] = num_list[z]
                z += 1  # 넣을 숫자 index 올리기.
            c -= 1
        # 위
        elif index % 4 == 3:  # y축만 바뀜
            for j in range(N - 1 - add, add + 1, -1):
                new_list[j - 1][d] = num_list[z]
                z += 1  # 넣을 숫자 index 올리기.
            add += 1
            d += 1
        #####

    return new_list


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    # arr 병합.
    new_arr = []
    for i in range(len(arr)):
        new_arr.extend(arr[i])
    new_arr.sort()

    result = snail(new_arr, N)

    print(f'#{test_case}')
    for row in result:
        for num in row:
            print(num, end=' ')
        print()

# print(result)