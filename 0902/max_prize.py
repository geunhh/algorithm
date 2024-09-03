import sys
sys.stdin = open('prize.txt')



# 바꿔줄 인덱스 정보 구하는 함수
def cost_index():
    for i in range(len(cost_list)):
        for j in range(i+1,len(cost_list)): # 중복되지 않게
            if i != j:
                perm_index.append([i,j])
    return perm_index

# 교환
def exchange(level,N):
    global max_cost
    if level==N:
        cost = int(''.join(cost_list))
        if cost > max_cost:
            max_cost = cost
        return

    cur_state =''.join(cost_list)           # 현 상태를 저장.

    # 가지치기
    if [cur_state,level] in visited:        # 방문정보 있으면
        return
    else:
        visited.append([cur_state,level])
###############################################
    for ind in perm_index:
        x,y = ind[0],ind[1]

        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]
        exchange(level+1,N)
        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]
    return

for tc in range(1,int(input())+1):
    cost, N = input().split()
    N = int(N)
    cost_list=[]
    visited = []
    perm_index=[]
    max_cost = 0

    for c in cost:
        cost_list.append(c)

    # 인덱스 구해줌
    perm_index = cost_index() # 인덱스 목록 (순열)

    # 교환해줌.
    exchange(0,N)

    # print(visited)
    print(f'#{tc} {max_cost}')