import sys
sys.stdin = open('mincost.txt')

def calc(N,row,cur_sum):
    global min_val
    if row == N:
        if min_val > cur_sum:
            min_val=cur_sum
        return
    if cur_sum > min_val:
        return

    for col in range(N):
        if visited[col] == 0 and W[row][col] != 0:  # col에 방문을 안 했고, 해당 경로가 있다면
            visited[col]=1                          # visited 걸어주고
            calc(N,row+1,cur_sum+W[row][col])       # 다음row로 보냄
            visited[col]=0                          # 갔다오면 visited 풀어줌.



N= int(input())
W = [list(map(int,input().split())) for _ in range(N)]

min_val = float('inf')
visited=[0]*N               # 이전 row 에서 col 방문했는지?
calc(N,0,0)
print(min_val)