import sys
sys.stdin = open('cost.txt')

def calc(i,visited,cur_sum):
    global min_sum
    if i==N and cur_sum < min_sum:
        min_sum = cur_sum
        return

    if cur_sum > min_sum:
        return

    for j in range(N):
        if not visited[j]:
            visited[j]=True
            calc(i+1,visited,cur_sum+lst[i][j])
            visited[j]=False


for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    # print(lst)
    min_sum= float('inf')
    visited = [False] * (N+1)
    calc(0,visited,0)
    print(f'#{tc} {min_sum}')