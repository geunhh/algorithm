# N개의 원자들이 [x,y] 위치, 이동방향, 보유 에너지가 주어질 때 소멸되면서 방출하는 에너지 총합.
# 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)

# 0.5초 단위로 움직이는데, x,y 둘다 같은 친구들의 에너지값을 total에 더하고, remove로 제거.
# 무한루프가 걸리지 않으려면. 1000초만 움직이자. 첫위치가 -1000~1000

import sys
sys.stdin = open('atom.txt')

dir_dict = {
    #  상 하 좌 우
    0 : (0.5, 0),
    1 : (-0.5, 0),
    2 : (0, -0.5),
    3 : (0, 0.5)
}

for tc in range(1,int(input())+1):
    N = int(input()) # 원자 개수

    atom_lst=[]

    for ind in range(N):
        x,y,dir_a,E = map(int,input().split())
        atom_lst.append(([x,y],dir_a,E))              # 좌, 표, 방향, 에너지

    total_energy = 0    # 결과값
    t = 0               # 시간

    while t <= 4000 : # 초당 0.5 씩 움직일겨
        # 1. atom list를 순회하면서 각각의 위치 정보를 업데이트
        for atom in atom_lst:
            atom[0][1] += dir_dict[atom[1]][0] # x,y와 i,j에 맞게 꼬아줌
            atom[0][0] += dir_dict[atom[1]][1]

        # 2. x,y가 겹치는 친구들이 있으면, 에너지값 total에 더해주고, 소멸 remove.
        # 조합을 순회하면서 좌표가 같으면, 처리.

        pos_lst    = set()             # 길이 비교할 set
        remove_lst = set()             # 제거 대상

        for atom in atom_lst:
            # print(atom)
            if (atom[0][0],atom[0][1]) in pos_lst:          # set에 이미 있으면
                remove_lst.add((atom[0][0],atom[0][1]))  # 제거 대상이니까 넣어줌.
            else:
                pos_lst.add((atom[0][0],atom[0][1]))

        # remove list가 비었다?
        if not remove_lst:
            t+=1
            continue
        # 아니라면
        else :
            for remove_pos in remove_lst:
                for i in range(len(atom_lst)-1,-1,-1):
                    if (atom_lst[i][0][0],atom_lst[i][0][1]) == remove_pos:
                        total_energy += atom_lst[i][2]
                        del atom_lst[i]

    print(f'#{tc} {total_energy}')