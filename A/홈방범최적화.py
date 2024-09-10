import sys

sys.stdin = open('home.txt')

'''
M : 집당 지불비용/
 - K = 1 일 때, 운영 비용은 1 이다.
 - K = 2 일 때, 운영 비용은 5 이다.  i : -1 0 1, // j 0, -1 0 1, 0
 - K = 3 일 때, 운영 비용은 13 이다. i : -2 -1 0 1 2 // j 0,-1 0 1, -2 -1 0 1 2 ....
 - K = 4 일 때, 운영 비용은 25 이다.
 - K * K + (K - 1) * (K - 1)

# 1번 아이디어.
 1. 집을 찾는다. 집 좌표를 저장해둠. -> 집 좌표를 기준으로 검색 
 2. K를 키워가면서 완전탐색한다.
    ** 마름모 탐색 구현만 잘해보자 ** 
    -> 실패. 집 tc 2번만 미리 봤어도 이런 생각은 안했음 
 
# 2번 아이디어.
 1. 집을 찾는다.
 2. K를 키워가며 완전탐색한다.
 # -> M==1 일 때 처리를 안 해줌. ->cnt가 0이 나올 수 있음.
 ==> 처리하고 패스. 

 
    
 
 
 '''
    
    



def check(K, ci, cj):  # k, 중심이 될 i,j
    global result
    k1 = 0          # 열 탐색할 때 개수 범위조절 해주기 위한 변수
    cur_cnt = 0     # 현재 범위에서의 집 개수
    # k가 2 이상일 때
    for i in range(ci - K, ci + K + 1):                 # 행은 자신을 기준으로 -k부터 +k 까지 탐색
        if i >= 0 and i < N:                            # 범위 내에 들어가면
            for j in range(-k1, k1 + 1):
            # column을 k1만큼 돌리는데 => [0],[-1,0,1],[-2,-1,0,1,2],[-1,0,1]... 이런식으로 돌아야함
            # 그래서 k1이라는 변수를 0으로 설정하고,
            #   i가 ci(인풋받은 i)가 되는 순간부터 -=1 해주면서 마름모를 그림.
                if 0 <= cj + j < N and lst[i][cj + j] == 1:
                    cur_cnt += 1

        # 열을 마름모로 만들기 위해 아래 처리 해줌.
        if i < ci:
            k1 += 1
        else:
            k1 -= 1

    # profit 계산
    K = K + 1       # K가 -1 된 상태로 루프를 돌렸기 때문에 +1 해서 이득 계산
    cur_cost = M * cur_cnt - (K * K + (K - 1) * (K - 1))    # 계산

    # 손해가 아니고, 집 개수가 result(max_cnt)보다 클 때 갱신.
    if cur_cost >= 0 and cur_cnt > result:
        result = cur_cnt


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 1  # 최대 집 개수 -> default

    for k in range(1, N + 1):  # k 순회 1이지만, 2부터 순회
        prev_result = result    # k 갱신할 때마다 prev_result도 갱신
        for x in range(N):
            for y in range(N):
                check(k, x, y)
                # print(prev_result,result)
        # print(prev_result,result)
        if prev_result > result:
            # print(k)
            break

    print(f'#{tc} {result}')

    # break