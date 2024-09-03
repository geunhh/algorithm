def calc(N,row,cur_sum):
    global min_sum

    # visited에 0이 없을 때 -> 모든 column 다 순회했을 때
    if 0 not in visited:
        if cur_sum < min_sum:   # 대소 비교
            min_sum = cur_sum
            return

    # 현재 위험도 합이 이미 min값을 넘었을 때
    if cur_sum > min_sum:
        return

    # 해당 row의 칼럼을 순회.
    for col in range(N):                            # N만큼의 column 값을 순회
        if visited[col] == 0 and A[row][col] !=0:   # 아직 방문 안했으면 & 나 자신이 아니면
            visited[row]=1                          # A->B일 경우 해당 row와 col 모두 다시 방문할 수 없음.
            visited[col]=1                          # 위와 동
            calc(N,col,cur_sum+A[row][col])         # (N,다음 row는 현재 col값으로 가야함, cur_sum 갱신)
            visited[col]=0                          # 복구
            visited[row]=0                          # 복구




for tc in range(1,int(input())+1):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]  # 외계인 위험도

    visited = [0]*N     # 방문한 col
    min_sum = 999       # min
    cur_sum = 0
    for row in range(N):
        calc(N,row,cur_sum)
    print(f'#{tc} {min_sum}')

