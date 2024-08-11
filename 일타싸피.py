import math

def where_hole(hole, mokjeok_ball):
    min_d_2hole = 99999
    min_d_xy = [0,0]
    x1= mokjeok_ball[0]
    y1= mokjeok_ball[1]

    for x,y in hole:
        if min_d_2hole > math.sqrt((x1-x)**2 +(y1-y)**2):
            min_d_2hole = math.sqrt((x1-x)**2 +(y1-y)**2)
            min_d_xy = [x,y]
    return min_d_xy, min_d_2hole

cho_ball = (30,100)
mokjeok_ball = (50,30)
r = 5.73/2                      # 반지름 5.73 : 직경


hole = [
    (0,127),(127,127),(254,127),
    (0,127/2),(254,127/2),
    (0,0),(254//2,0),(254,0)
]

# 홀 좌표 찾기.
hole_xy,min_2d = where_hole(hole, mokjeok_ball)

# 홀 좌표 조정.
# 좌상
if cho_ball[0] > mokjeok_ball[0] and cho_ball[1] < mokjeok_ball[1]:
    hole_xy[0] +=r
    hole_xy[1] -=r
    print('좌상임')    
# 우상
elif cho_ball[0] < mokjeok_ball[0] and cho_ball[1] < mokjeok_ball[1]:
    hole_xy[0] -=r
    hole_xy[1] -=r 
    print('우상임')  
# 우하
elif cho_ball[0] < mokjeok_ball[0] and cho_ball[1] > mokjeok_ball[1]:
    hole_xy[0] -=r
    hole_xy[1] +=r  
    print('우하임')  
# 좌하
elif cho_ball[0] > mokjeok_ball[0] and cho_ball[1] > mokjeok_ball[1]:
    hole_xy[0] +=r
    hole_xy[1] +=r 
    print('좌\하임')  

print(hole_xy)

### 홀과 목적구 거리 구해서 -> 초구가 목적구를 타격하기 위해 도달해야할 곳 좌표 구하기. ###
dist_xy2hole = min_2d + 2*r 

