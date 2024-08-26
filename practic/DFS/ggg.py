
import sys
sys.stdin=open('input.txt')

def dfs(N,row,cur_sum):
    if row == N:
        global min_val
        if min_val > cur_sum:
            min_val = cur_sum
        return

    if min_val < cur_sum:
        return

    for col in range(N):            # col 순회
        if visited[col] == 0:       # visited[col]에 없으면
            visited[col] = 1        # 1로 바꿔주고
            dfs(N,row+1,cur_sum+matrix[row][col])   # 다음 row로 넘겨줌.
            visited[col] = 0



for tc in range(1,int(input())+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N    # 각 행별로 같은 열을 방문하지 못하게 체크.
    min_val=999

    dfs(N,0,0)
    print(min_val)








