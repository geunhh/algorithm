'''
첫번째 수는 1감수 후 맨뒤
두번째 수는 2감소 후 맨뒤
n번째 수는 n감소 후 맨뒤
숫자 감소할 때 : 0 -> 뒤로 보내고 프로그램 종료.
'''
from collections import deque
for tc in range(1,11):
    # deque 생성
    # lst = [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]  # 6 2 2 9 4 1 3 0
    # lst = [10,6,12,8,9,4,1,3]
    N= input()
    lst = list(map(int, input().split()))
    d = deque(lst)
    i=1
    go=True
    while go:
        for i in range(1,6):
        #덱 순회
            pop_val = d.popleft()
            if pop_val - i <= 0:
                go = False
                d.append(0)
                break
            else:
                d.append(pop_val-i)
    print(f'#{tc}',*d)