# 시간초과
import sys
sys.stdin = open('1.txt')
from itertools import combinations

def func(res_list):
    # print(type(res_list))
    # print(res_list)
    min_num, max_num = min(res_list), max(res_list)
    # print(min_num, max_num)
    cnt_min = res_list.count(min_num)
    cnt_max = res_list.count(max_num)
    # print(cnt_max,cnt_min)
    if cnt_min+cnt_max >= 3:
        return False
    return True
def func2(N):
    for n in range(0, len(res_list_list),N):
        # print(n,len(res_list_list),N)
        res_list = res_list_list[n]
        print(res_list)
        # print(res_list)
        check = func(res_list)
        if check == False:
            return False
    else:
        return



for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    for length in range(3,N+1):
        # print(length)
        res = combinations(lst,length)
        res_list_list = list(res)
        print(res_list_list)
        # [(3, 2, 4), (3, 2, 3), (3, 4, 3), (2, 4, 3)]
        check_main = func2(N)
        if check_main == False:
            print(f'#{tc} NO')
            break
    else:
        print(f'#{tc} YES')

    # print(list(res))
    # print(lst)



