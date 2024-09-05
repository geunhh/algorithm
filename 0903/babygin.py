'''
# 9 5 5 1 4 2
# 9 6 6 1 2 1

# 5 2 1 2 9 0
# 3 9 5 0 2 0

sort
'''
import sys
sys.stdin = open('2.txt')
from collections import deque

def triple(player):
    # print(player)
    for num in player:
        if player.count(num) >= 3:
            return 1
    return

3445
def runn(player):
    player =list(set(player))
    player.sort()
    # print(player)
    for i in range(1, len(player)-1):
        # print(i)
        #3 4 4 5
        if player[i] - 1 == player[i-1] and player[i] + 1 == player[i+1]:
            return 1
    return



for tc in range(1,int(input())+1):
    lst = list(map(int, input().split()))
    # print(lst)
    deq = deque(lst)
    # print(deq)
    player1 = []
    player2 = []
    #########
    while deq:
        player1.append(deq.popleft())
        player2.append(deq.popleft())
        # print(player1)
        # print(player2)
        if len(player1) >= 4:
            # print(player1, player2)
            if triple(player1):
                print(f'#{tc} 1')
                break
            if runn(player1):
                print(f'#{tc} 1')
                break
            if triple(player2):
                print(f'#{tc} 2')
                break
            if runn(player2):
                print(f'#{tc} 2')
                break
    else:
        print(f'#{tc} 0')

