'''

꿀통의 꿀 최대 양은 1~9
내가 채취할 수 있는 C 최대값은 30
벌통 NxN : 3~10
선택할 수 있는 벌통의 수 : M <=5
'''

import sys
sys.stdin = open('hoeny.txt')

def honey(idx,jdx,honey_box,visited,level):
    if idx > N or jdx >= N-M+1:
        return

    # 종료조건
    if level >= 2:
        return

    # 꿀통에 넣어주기.
    for k in range(M):
        honey_box.append(lst[idx][jdx+k])
        visited.append((i,j+k))
    # 만약 꿀통에 넣은 애들 총량이 C를 넘는다면?
        # 꿀통 수정해주기.
    # print(honey_box)
    # print(visited)
    if level==1:
        for next_j in range(jdx, N - M + 1):
            print(idx, next_j)
            honey(idx, next_j, honey_box, visited, level + 1)
        print('세로')
    else:
        # j+1해준거(가로)
        for next_j in range(jdx+M,N-M+1):
            print(idx,next_j)
            honey(idx,next_j,honey_box,visited,level+1)
        print('세로')

    # # i+1해준거(세로)
    for next_i in range(N):
        print(next_i,0)
        honey(idx+next_i,0,honey_box,visited,level+1)

    print('먀먀먀')


    pass

for tc in range(1, int(input())+1):
    N, M, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # print(lst,M,c)
    result = 0

    # 채취한 꿀통의 위치를 저장.
    for i in range(0,N):
        for j in range(0,N-M+1):
            honey(i,j,[],[],0)

            break
            # 함수 호출.
    break