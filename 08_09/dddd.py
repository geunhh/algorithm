def recur(idx, cur_sum, N):
    cnt=0
    # 종료조건
    print('index ',idx)
    if idx == N :               # 다 돌았을 때
        if cur_sum == 10 :
            print('ddd')
            return 1
        else:
            return 0
    
    # 가지치기
    if cur_sum + sum(num_lst[idx:]) < 10: # 남은 친구들에 지금 친구를 더했을 때 타겟보다 작으면,
        return 0
    
    # 다음 인덱스
    cnt = recur(idx+1, cur_sum + num_lst[idx], N)
    return cnt


num_lst = list(map(int,input().split()))
print(num_lst)

N = len(num_lst)
result = recur(0,0,N)
print(result)
