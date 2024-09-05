import sys
sys.stdin = open('cart.txt')

def patrol(i, N, used, cur_sum):
    global min_sum
    if cur_sum > min_sum:
        return

    if used == check:
        cur_sum += cost[i][0]
        min_sum = min(cur_sum,min_sum)
        return

    for j in range(N):

        if not used[j] and i!=j:
            used[j] = 1
            patrol(j, N, used, cur_sum+ cost[i][j])
            used[j] = 0
    return


for tc in range(1,int(input())+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    # print(cost)

    used = [0] * N # 방문여부
    check = [1] *N
    used[0] = 1
    # print(used)
    min_sum=float('inf')
    patrol(0,N,used,0)
    print(f'#{tc} {min_sum}')


    # break