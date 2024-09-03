import sys

sys.stdin = open("input.txt", "r")

def check(str1) :

    for i in range(len(str1)//2):
        if str1[i] != str1[-i-1]:

            return 0
    return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = str(input())
    result = check(str1)
    # result = len(str1)
    print(f'#{test_case} {result}')


