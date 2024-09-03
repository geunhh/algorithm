import sys
sys.stdin = open('input.txt', 'r')

def check(arr):
    for index in range(99,-1,-1): # 역순으로
        # 가로 확인
        for i in range(100):
            for j in range(100-index):
                word = arr[j][j:j+index]
                if word == word[::-1]:
                    return word

        # 세로 확인
        for j in range(100):
            for i in range(100-index):
                word = arr[i:i+index][j]
                if word == word[::-1]:
                    return word



for test_case in range(1,11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    result = check(arr)

    print(result)
