import sys
sys.stdin = open('prize.txt')
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
####################### 가지 치기 ########################
    cur_state =''.join(cost_list)           # 현재 상태

    # 가지치기
    if (cur_state,level) in visited:        # 동일한 레벨에서 같은 상태가 있었다면?
        return

    visited.add((cur_state,level))          # 현 상태와 레벨 저장
###############################################
    for ind in perm_index:
        x,y = ind[0],ind[1]
        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]   # 교환하기
        exchange(level+1,N)                                     # 다음 레벨 호출
        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]   # 되돌리기
    return





for tc in range(1,int(input())+1):
    cost, N = input().split()
    N = int(N)
    cost_list=[]

    for c in cost:
        cost_list.append(c)
    # print(cost_list,N)

    # 인덱스 구해줌
    perm_index=[]
    perm_index = cost_index()
    # print(perm_index)

    visited = set() # 방문 정보 저장

    max_cost = 0
    exchange(0,N)
    # print(visited)
    print(f'#{tc} {max_cost}')