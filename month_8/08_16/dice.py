

import sys
sys.stdin = open('dice.txt')

# 초기화

N = int(input())                            # 주사위 개수(층수)
dice_arr = [list(map(int,input().split())) for _ in range(N)]   # 주사위 array 받기.

my_dict = {0: 5, 5: 0, 1: 3, 3: 1, 2: 4, 4: 2}  # 다음 루프에 주사위 개체의 윗면 숫자를 리턴하기 위한.
# A B C D E F 순으로 입력되고
# A:F, C:E, B:D 각 반대면의 짝이이 된다.

max_sum=0           # 옆면 합의 최대값을 위한 변수.

######### start ##########
"""
1. 가장 아래 주사위 윗면의 시작 숫자를 1부터 6까지 루프하며 최대값을 찾는다.
2. 주사위 옆면의 합을 계산할 때 주사위의 아래 윗면만 고정되고, 회전은 자유롭기 때문에 max값을 찾아 더해줌.
3. 

dice_arr : ABCDEF 순으로 받아온 각 층의 리스트 
my_dict  : n+1 층 주사위의 밑면에 n층 주사위 윗면 숫자를 리턴하기 위한 dict
cur_sum  : 1층 주사위 밑(윗)면의 숫자를 n으로 했을 때 옆면의 합의 최대값 
max_sum  : cur_sum 중 max 값
add_num  : 각 층에서 위 아래 면을 제외한 숫자 중에서 max 값을 할당해 cur_sum에 더하기 위한 변수
start    : 다음 층 주사위의 밑면이 될 숫자를 할당할 변수
index    : start의 인덱스를 할당할 변수 
"""
for i in range(6):          # 가장 아래 주사위 숫자 루프 -> 즉 시작 숫자
    cur_sum =0              # 각각 루프마다 sum을 초기화
    # 1층 주사위의 합은 계산하고 시작
    if i == 0 or i == 5:                    # 아래 윗면이 0,5 인 경우
        # 둘 빼고 나머지 중에서 찾아서 할당
        add_num = max([ dice_arr[0][1],dice_arr[0][2],dice_arr[0][3],dice_arr[0][4]])
    elif i == 1 or i == 3:                  # 아래 윗면이 1,3 인 경우
        add_num = max([ dice_arr[0][0],dice_arr[0][5],dice_arr[0][2],dice_arr[0][4]])
    elif i == 2 or i == 4:                  # 아래 윗면이 2,4 인 경우
        add_num = max([ dice_arr[0][0],dice_arr[0][1],dice_arr[0][3],dice_arr[0][5]])
    # 더해줌
    cur_sum+=add_num

    # 다음 주사위의 밑면이 될 숫자를 정해줌
    start = dice_arr[0][my_dict[i]]

    ###### 2번째 줄부터 GO ######
    for i in range(1,N):
        # 먼저 밑면 숫자인 start의 인덱스를 찾아줌.
        index = dice_arr[i].index(start)

        # 위와 마찬가지로 해당 인덱스와 dictonary에 저장된 반대편 인덱스를 제외하고
        # 나머지 면의 숫자 중 max 값을 더해줌.
        if index == 0 or index == 5:
            # 둘 빼고 나머지 중에서 찾아서 더함
            add_num = max([dice_arr[i][1], dice_arr[i][2], dice_arr[i][3], dice_arr[i][4]])
        elif index == 1 or index == 3:
            add_num = max([dice_arr[i][0], dice_arr[i][2], dice_arr[i][5], dice_arr[i][4]])
        elif index == 2 or index == 4:
            add_num = max([dice_arr[i][0], dice_arr[i][1], dice_arr[i][3], dice_arr[i][5]])

        cur_sum +=add_num

        # 다음 스타트(주사위의 밑면 숫자) 갱신
        start = dice_arr[i][my_dict[index]]     # index가 0(밑면)이면 0과 대비되는 5번(윗면)의 숫자
        # -> 밑면 index를 key로 활용해 dictonary에서 윗면 index(value)를 찾아 i층의 윗면숫자, i+1층의 밑면숫자를 찾음.

    ####### 1층 주사위의 n번 루프 종료 #######
    # max 값 갱신
    if cur_sum > max_sum:
        max_sum = cur_sum

print(max_sum)