import sys
from itertools import combinations
sys.stdin = open('hoeny.txt')

# 꿀통에서 최대 수익을 계산하는 함수
def clac_profit(honey_comb):
    max_profit = 0
    for com_len in range(1, M+1):  # M개의 조합까지 고려
        honeys = list(combinations(honey_comb, com_len))
        for honey in honeys:
            if c >= sum(honey):  # 채취할 수 있는 양을 넘지 않을 때
                cur_profit = sum(h**2 for h in honey)  # 수익은 제곱 합
                if max_profit < cur_profit:
                    max_profit = cur_profit
    return max_profit

for tc in range(1, int(input())+1):
    N, M, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_total_profit = 0  # 전체 최대 수익

    # 1번 일꾼의 꿀통 선택
    for i in range(N):
        for j in range(N-M+1):
            # 1번 일꾼의 꿀통 선택
            honey_comb1 = lst[i][j:j+M]
            cur_honey1 = sum(honey_comb1)  # 꿀의 양 계산
            if cur_honey1 <= c:
                profit1 = sum(h**2 for h in honey_comb1)  # 꿀이 C 이하일 때는 제곱합
            else:
                profit1 = clac_profit(honey_comb1)  # C 초과 시는 조합으로 최대 수익

            # 2번 일꾼의 꿀통 선택
            for i2 in range(i, N):
                if i2 == i:  # 같은 행에서 겹치지 않게
                    for j2 in range(j+M, N-M+1):  # 1번 일꾼의 범위 이후
                        honey_comb2 = lst[i2][j2:j2+M]
                        cur_honey2 = sum(honey_comb2)
                        if cur_honey2 <= c:
                            profit2 = sum(h**2 for h in honey_comb2)
                        else:
                            profit2 = clac_profit(honey_comb2)

                        max_total_profit = max(max_total_profit, profit1 + profit2)
                else:  # 다른 행은 자유롭게 선택 가능
                    for j2 in range(0, N-M+1):
                        honey_comb2 = lst[i2][j2:j2+M]
                        cur_honey2 = sum(honey_comb2)
                        if cur_honey2 <= c:
                            profit2 = sum(h**2 for h in honey_comb2)
                        else:
                            profit2 = clac_profit(honey_comb2)

                        max_total_profit = max(max_total_profit, profit1 + profit2)

    print(f"#{tc} {max_total_profit}")
