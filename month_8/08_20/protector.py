import sys
sys.stdin = open('input.txt')
'''
가로 세로
상점 개수
상점 방향 상점 위치
-> 1 북쪽 2 남쪽 3 서쪽 4 동쪽
-> 동 서 - 위쪽에서 거리
-> 남 북 - 서쪽에서 거리.
동근이 위치
'''
X,Y=map(int,input().split())
N=int(input())
shop = [list(map(int, input().split())) for _ in range(N)]
Home = list(map(int,input().split()))

shop_xy = []    # 상점 list를 xy축 정보로 바꿔서 넣어줄테야.

# 좌표로 바꿔줌. 각 상점의 방향과 위치를 이용해 좌표를 계산
for dir, loc in shop:
    if dir==1:                  # 북쪽일때
        shop_xy.append([loc,Y])
    elif dir==2:                # 남쪽
        shop_xy.append([loc,0])
    elif dir==3:                # 동
        shop_xy.append([0,Y-loc])
    elif dir ==4:               # 서쪽
        shop_xy.append([X,Y-loc])

# 동근이네도 따로 계산.
if Home[0]==1:      # 북쪽
    Home_xy = [Home[1],Y]
elif Home[0]==2:
    Home_xy = [Home[1],0]
elif Home[0]==3:
    Home_xy = [0,Y-Home[1]]
elif Home[0]==4:
    Home_xy = [X,Y-Home[1]]

dir_dict = { 1:2, 2:1, 3:4, 4:3}  # 반대 방향인가 체크하려고 만들어줌.
# 1 북쪽 2 남쪽 3 서쪽 4 동쪽

result =0                   # 총 거리

for i in range(N):
    cur_sum=0               # 상점 별 거리

    # 동근이네와 상점이 같은 방향일 때
    if Home[0] == shop[i][0] :
        cur_sum += abs(Home[1] - shop[i][1])
    # 반대 방향
    elif dir_dict[Home[0]] == shop[i][0]:
        if Home[0] == 1 or Home[0] == 2:        # 북쪽 또는 남쪽
            sum_1 = Home[1] + shop[i][1]
            sum_2 = (X - Home[1]) + (X - shop[i][1])
            cur_sum += Y + min(sum_1, sum_2)
        else:                                   # 서쪽 또는 동쪽
            sum_1 = Home[1] + shop[i][1]
            sum_2 = (Y - Home[1]) + (Y - shop[i][1])
            cur_sum += X + min(sum_1, sum_2)
    # 인접한 방향
    else:
        cur_sum += abs(Home_xy[0] - shop_xy[i][0])
        cur_sum += abs(Home_xy[1] - shop_xy[i][1])

    result+=cur_sum
print(result)

# 최소 거리를 구해야 해.
