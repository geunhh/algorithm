import sys
sys.stdin = open('prize.txt')
from itertools import permutations



def exchange(cost_list, N):
    max_cost = 0
    cost_str = ''.join(cost_list)

    for perm in permutations(range(N), 2):
        x, y = perm
        cost_list[x], cost_list[y] = cost_list[y], cost_list[x]
        new_cost = int(''.join(cost_list))
        if new_cost > max_cost:
            max_cost = new_cost
        cost_list[x], cost_list[y] = cost_list[y], cost_list[x]  # 원래 상태로 되돌리기

    return max_cost


for tc in range(1, int(input()) + 1):
    cost, N = input().split()
    N = int(N)
    cost_list = list(cost)

    max_cost = exchange(cost_list, N)

    print(f'#{tc} {max_cost}')
