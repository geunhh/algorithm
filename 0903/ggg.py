
import sys
sys.stdin = open('1.txt')
# 최댓값과 최솟값을 카운트할 check_subarrary 함수
def check_subarray(arr, max_val, min_val):
    count_max = 0  # max 카운트
    count_min = 0  # min 카운트

    for num in arr:
        if num == max_val:
            count_max += 1
        if num == min_val:
            count_min += 1
        # 최댓값이나 최솟값의 개수를 합친게 3이상이면 True로 반환 -> 'NO' 출력
        if count_max + count_min >= 3:
            return True


# 부분수열을 조회하는 함수
def max_min_find(N, arr):
    # 모든 가능한 부분 수열을 순회
    for i in range(N):
        for j in range(i + 1, N + 1):
            subarray = arr[i:j]  # 연속되는 부분수열 하나씩 증가
            print(i,j,subarray)

            max_val = max(subarray)  # subarray의 최댓값 선언
            min_val = min(subarray)
            if check_subarray(subarray, max_val, min_val):
                return "NO"

    return "YES"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = max_min_find(N, arr)
    print(f"#{tc} {result}")