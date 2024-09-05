# 시간초과
import sys
from itertools import combinations
sys.stdin = open('1.txt')

def func(N):
    for length in range(3,N+1):             # length 3 이상부터 최대 length(N)까지 검사
        for i in range(N-length+1):         # length 3 : index [0~3부터 1~4, N-3 ~ N],
                                            # length 4 :       [0~4,1~5,2~6 ...... 검사 진행.
            # min, max 값 구하기.
            min_num, max_num = min(set(lst[i:i+length])),max(set(lst[i:i+length]))
            # min,max 값이 몇 개 포함 되는가???
            cnt_min = lst[i:i+length].count(min_num)
            cnt_max = lst[i:i+length].count(max_num)

            if cnt_min+cnt_max >= 3:    # 두 cnt 합이 3 이상이라면
                print(f'#{tc} NO')      # NOPE
                return
    else:                               # 무사히 종료되면
        print(f'#{tc} YES')             # YES
        return

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    # print(lst)
    func(N)



