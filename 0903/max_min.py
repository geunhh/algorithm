# 시간초과
import sys
sys.stdin = open('1.txt')

def func(N):
    for length in range(3,N+1):
        for i in range(N-length+1):
            # min, max 값 구하기.
            print(lst[i:i+length])
            if i==0:
                min_num, max_num = min(lst[i:i + length]), max(lst[i:i + length])
            else:
                # 새로 추가된 친구가 기존보다 큰가?
                if lst[i+length] > max_num:
                    max_num = max(lst[i:i + length])
                elff lst[i]

            cnt_min = lst[i:i+length].count(min_num)
            cnt_max = lst[i:i+length].count(max_num)
            if cnt_min+cnt_max >= 3:
                print(f'#{tc} NO')
                return
    else:
        print(f'#{tc} YES')
        return

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    func(N)



