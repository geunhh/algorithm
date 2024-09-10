import sys
sys.stdin = open('cook.txt')

# 1부터 N까지 중에 N//2 개를 골라야 함. + 나머지는 B음식에 쓸겨
# 조합한 친구들의 [row][col] 값을 total에 더하자
# A음식과 B음식의 차이의 절대값이 가장 작은 것이 정답.



from itertools import combinations

for tc in range(1,int(input())+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    min_total = float('inf')

    # 1. 조합 구하기
    combs = list(combinations(range(N),N//2))           # 식재료 index의 조합 구하기.

    # 2. 조합 순회
    for comb in combs[:len(combs)//2]:      # 조합을 순회하는데
        total_A = 0         # A의 시너지 총합
        total_B = 0         # B의 시너지 총합
        for i in range(N):
            for j in range(N):
                if i in comb and j in comb:             # comb i,j 가 조합에 포함될 때만
                    total_A += foods[i][j]              # 시너지에 더해준다.
                elif i not in comb and j not in comb:   # 위와 동
                    total_B += foods[i][j]              #
        # 3. min값 갱신
        min_total = min(min_total,abs(total_A - total_B)) # minimum 값 갱신.
    # 4. 출력
    print(f'#{tc} {min_total}')
