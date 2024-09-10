import sys
sys.stdin = open('mag.txt')

# n번 자석이 회전하면, 회전하기 전의 상태에 따라 양옆의 자석의 회전이 결정됨.
#                    극이 다르더라도 주변 친구들이 회전하지 않으면, 회전 X
# 재귀.
#   n번 자석이면, 범위확인하고 ,n-1 n+1 -> n-1 n+1 이런식으로.
# 1. 회전시키기 전에 전체의 상태 확인. -> 돌릴 것인가??
# 2. 회전시키고,
# 각각의 2번, -2 ,2 가 접합부.

from collections import defaultdict
def mag_info(mag_i,r):
    rot_ind = set()
    rot_ind.add((mag_i,r))
    r = -r
    flag_r=1
    flag_l=1
    for n in range(4):
        # 오른쪽
        if flag_r and not visited[mag_i+n+1] and mag_i+n+1 < 4 and lst[mag_i+n][2] != lst[mag_i+n+1][-2]:
            rot_ind.add((mag_i+n+1,r))
            # print(n,rot_ind)
        else:
            flag_r =0
        # 왼쪽
        if flag_l and not visited[mag_i-n-1] and mag_i-n-1 >=0 and lst[mag_i-n][-2] != lst[mag_i-n-1][2] :
            rot_ind.add((mag_i-n-1,r))
            # print(n,rot_ind)
        else:
            flag_l =0
        r = -r

    # print('index', rot_ind)
    return rot_ind

def rotate(mag_i,r):

    # 이전 rotate 할 친구들 index를 미리 알자.
    rot_ind_r = mag_info(mag_i-1,r)

    # rotate 하기
    for ind,r in rot_ind_r:
        # print(ind,r)
        if r == 1:
            lst[ind].insert(0, lst[ind].pop())
        elif r== -1:
            lst[ind].append(lst[ind].pop(0))
    # print(lst)




for tc in range(1,int(input())+1):
    ###### 인풋 받아오기 ######
    K = int(input()) # 돌리기 횟수
    lst = [list(map(int,input().split())) for _ in range(4)]
    rot_lst = []
    for _ in range(K):
        rot_lst.append(list(map(int,input().split())))
    # print(lst)
    # print(rot_lst)
    ###########################

    for mag_i, r in rot_lst:
        visited=defaultdict(int)
        # print(mag_i,r)
        rotate(mag_i,r)
        # print()

    result = 0
    arr=[1,2,4,8]
    for i, multi in enumerate(arr):
        # print(i,multi)
        result += multi*lst[i][0]
    print(f'#{tc} {result}')




    # break