import sys
sys.stdin = open("input.txt", "r")

def find_road(j, arr): # x : 99
    i = 99
    left, right = None, None
    while i >= 0:
        # 좌
        if j !=0 and arr[i][j-1] == 1 and right==False:
            # print(i, j)
            j -= 1
            left=True
            continue
        # 우
        if j!= 99 and arr[i][j+1] == 1 and left==False:
            j += 1
            right = True
            continue

        # 좌우에 없으면 한 칸 위로
        right = False
        left = False
        i -= 1

    return j


for test_case in range(1, 11):
    N = int(input()) # 배열의 크기
    arr = []
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)
    # print(arr[99][57]) #i,j
    # print(arr[95][58])

    for j in range(100):
        if arr[99][j] == 2:
            # print(j)
            result = find_road(j, arr)
            print(f'#{test_case} {result}')



