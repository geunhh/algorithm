import sys
sys.stdin = open('dongchul.txt')
"""

"""
def  work_sep(i, visited, cur_p):
    global max_p

    # 2. 가지 치기
    # 이미 확률이 max 값보다 작다? 앞으로 나올 값의 최대는 1이라서 컷.
    if cur_p <= max_p:
        return

    # 3. 종료조건
    # 마지막 사람까지 확률을 곱했을 때
    if i == N:
        if cur_p > max_p:
            max_p = cur_p
        return


    # 1. 탐색
    for j in range(N):
        # 해당 일을 이미 했거나, 일을 성공할 확률이 0이 아닐 때
        if not visited[j] and lst[i][j] != 0:
            visited[j] = 1
            work_sep(i+1,visited,cur_p*lst[i][j]*0.01)
            visited[j] =0


for tc in range(1, int(input())+1):
    N=int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*(len(lst))
    max_p = 0

    work_sep(0,visited,1)

    print(f'#{tc} {max_p*100:.6f}')