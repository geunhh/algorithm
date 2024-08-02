import sys
sys.stdin = open("input.txt", "r")

def comp_str(str1, str2):
    str1 = (list(set(str1)))
    max_cnt=0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2 :
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = comp_str(str1,str2)
    print(f'#{test_case} {result}')
