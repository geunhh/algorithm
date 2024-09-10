import sys
sys.stdin = open('home.txt')

'''
M : 집당 지불비용/
 - K = 1 일 때, 운영 비용은 1 이다.
 - K = 2 일 때, 운영 비용은 5 이다.  i : -1 0 1, // j 0, -1 0 1, 0
 - K = 3 일 때, 운영 비용은 13 이다. i : -2 -1 0 1 2 // j 0,-1 0 1, -2 -1 0 1 2 ....
 - K = 4 일 때, 운영 비용은 25 이다.
 - K * K + (K - 1) * (K - 1)
 
 1. 집을 찾는다. 집 좌표를 저장해둠. -> 집 좌표를 기준으로 검색 -> edge case가 있음
 2. K를 키워가면서 완전탐색한다. 
    -> 상하좌우 -> 기준 상하좌우
    이득을 보는 경우가 나오고, 다음 k에서 본 이득이 max_이득보다 작으면 탐색 종료.
 
'''

'''
포문으로 마름모 탐색하는 함수. 이거 생각하는 게 조금 힘들었음.

'''
def check(K, ci, cj): # k, 중심이 될 i,j
    global max_profit,result
    k1 = 0
    k = ci+K
    cur_cnt=0
    # k가 2 이상일 때
    for i in range(ci-K, ci+K + 1):             # 행
        if i >= 0 and i < N :                   # 범위 내에 들어가면
            for j in range(-k1, k1 + 1):        # j를 돌려
                if 0 <= cj+j < N and lst[i][cj+j] == 1:
                    # print(cj + j, end=' ')
                    cur_cnt+=1
        if i < ci:
            k1 += 1
        else:
            k1 -= 1
    # print()
    # print()

    # profit 계산
    K=K+1
    cur_cost = M*cur_cnt - (K * K + (K - 1) * (K - 1))
    # print('cur cnt :', cur_cnt, cur_cost)
    if cur_cost >= 0 and cur_cnt > result:
        result = cur_cnt


for tc in range(1,int(input())+1):
    N,M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]
    # for row in lst:
    #     print(row)
    max_profit = 0 # 최대값.
    result =0


    # 1. 집 찾기.
    home_lst = []
    # map을 쫙 순회할겨.
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                home_lst.append((i, j))
    # print(home_lst)

    # 집이 하나라도 있으면 k가 1일 때는
    if home_lst:
        max_profit = M-1
        result=1


    # k를 키워가며 완전탐색. 근데 k는 2부터
    # for k in range(1, N+1): # k 순회
    #     for x,y in home_lst:
    #         # print('cur_pos :',x, y,'k',k )
    #         check(k, x, y)
    # -> 집 찾고 집을 중심으로 마름모 그려서 탐색하려 했는데, 이러면 안대여

    for k in range(1, N+1): # k 순회
        for x in range(N):
            for y in range(N):
                # print('cur_pos :',x, y,'k',k )
                check(k, x, y)

    print(f'#{tc} {result}')

    # break