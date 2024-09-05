'''

꿀통의 꿀 최대 양은 1~9
내가 채취할 수 있는 C 최대값은 30
벌통 NxN : 3~10
선택할 수 있는 벌통의 수 : M <=5
'''

import sys
sys.stdin = open('hoeny.txt')
from itertools import combinations


'''
profit을 계산할 함수.
'''
def clac_profit(honey_comb):
    max_profit =0
    for com_len in range(1, M+1):                           # 1~M 사이로 조합의 길이를 정해서 포문
        honeys = list(combinations(honey_comb, com_len))    # 조합을 만들고 list로 변환해줌
        for honey in honeys:                                # 부분조합 하나씩 뜯어봄
            if c >= sum(honey):                             # 총합이 c보다 작으면
                cur_profit = 0
                for hony in honey:                          # 부분조합의 요소 제곱을 cur_profit에 더함
                    cur_profit += hony ** 2

                if max_profit < cur_profit:                 # 부부조합 중에서 가장 큰 친구 갱신
                    max_profit = cur_profit
    return max_profit




for tc in range(1, int(input())+1):
    N, M, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_total_profit = 0

    for i in range(0,N):
        for j in range(N-M+1):

            '''
            1 번 친구 먼저 진행.
            '''
            honey_comb1 = lst[i][j:j+M]         # 범위에 따른 list 생성
            cur_honey=sum(honey_comb1)          # 꿀통들의 합
            profit1 = 0

            # 만약 profit이 c 미만이다?
            if cur_honey <= c:
                for honey in honey_comb1:       # 바로 계산
                    profit1 += honey ** 2
            # 초과한다??
            else :
                profit1 = clac_profit(honey_comb1)  # 부분집합 속에서 가장 큰 값 구해야함

            #2. 이제 player 2 검사해볼까

            for i2 in range(i,N):
                # 1번 친구와 같은 행에 있다면,
                if i2 == i:
                    for j2 in range(j+M, N-M+1):                     # 해당 열 이후로
                        profit2 = clac_profit(lst[i2][j2:j2+M])      # 함수 호출
                        max_total_profit = max(max_total_profit, profit1 + profit2) # 결과값 맥스 갱신.

                # 같은 행이 아니라면, 다 검사
                else:
                    for j2 in range(N-M+1):
                        profit2 = clac_profit(lst[i2][j2:j2+M])
                        max_total_profit = max(max_total_profit, profit1 + profit2)


    print(f'#{tc} {max_total_profit}')




