import sys
sys.stdin = open("input.txt", "r")

my_dict = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9
}


T = int(input())
for test_case in range(1, T + 1):
    counts=[0]*10 # [0~9] 각 0씩 할당
    my_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    tc, length= map(str,input().split())
    lst = list(map(str, input().split()))
    # counts 숫자 증가.
    for c in lst:
        counts[my_dict[c]] += 1

    # 출력
    print(f'#{test_case}')
    for i in range(len(counts)):
        for _ in range(counts[i]):
            print(f'{my_list[i]}', end=' ')





