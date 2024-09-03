# N개의 피자를 동시에 굽기 가능
# M번 pizza 까지 구워야 함.
# [, , , , , ]
# lst rotate 하면서 한바퀴 돌때마다, c // 2 해서 넣어줌

import sys
sys.stdin = open('5099_input.txt', 'r')
from collections import deque

T= int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split()) # N : maxlen, M 피자 개수
    pizza_lst = list(map(int, input().split()))
    # print('N,M :',N,M)
    # print('pizza_list', pizza_lst)

    cnt=0
    oven = deque(maxlen=N)

    ##### oven 처음에 넣기 ####
    i=0
    for _ in range(N):
        oven.appendleft([i,pizza_lst.pop(0)])
        i+=1

    while len(oven)>1:

        if oven[-1][1] // 2 == 0 :   # 뺐는데, c//2 한게 0이다. pop +append
            oven.pop()
            if pizza_lst:
                oven.appendleft([i,pizza_lst.pop(0)])
                i+=1
            # print('투입 후 피자리스트', pizza_lst)
            # print()
            # print(oven)

        else :
            val = oven.pop()
            oven.appendleft([val[0],val[1]//2])
            # print(oven)

    else :
        print(f'#{tc} {oven[0][0]+1}')



