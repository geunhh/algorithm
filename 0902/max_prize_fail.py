import sys
sys.stdin = open('prize.txt')


# 바꿔줄 인덱스 정보 구하는 함수
def cost_index():
    for i in range(len(cost_list)):
        for j in range(i+1,len(cost_list)): # 중복되지 않게 i+1부터 [0,1] ~
            if i != j:                      # 같은 인덱스끼리 교환할 순 없으니!
                perm_index.append([i,j])
    return perm_index

# 순
def exchange(level,N):
    global max_cost

    # 종료 조건
    if level == N:                          # 교환 끝나면
        cost = int(''.join(cost_list))      # join하고 int로 바꿔줌
        if cost > max_cost:                 # max_cost랑 비교해서 갱신
            max_cost = cost
        return

    for ind in perm_index:
        x,y = ind[0],ind[1]

        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]   # 교환
        exchange(level+1,N)                                     # 다음레벨로
        cost_list[x],cost_list[y] = cost_list[y],cost_list[x]   # 복구
    return

for tc in range(1,int(input())+1):
    cost, N = input().split()
    N = int(N)
    cost_list=[]

    for c in cost:
        cost_list.append(c)

    # 인덱스 구해줌
    perm_index=[]
    perm_index = cost_index()

    max_cost = 0
    exchange(0,N)
    print(f'#{tc} {max_cost}')


