M,A = 20, 3
A = [2, 2, 3, 2, 2, 2, 2, 3, 3, 4, 4, 3, 2, 2, 3, 3, 3, 2, 2, 3]
B = [4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 1, 4, 1, 4, 3, 3, 3, 3, 3, 3]
AP1 = [4, 4, 1, 100] # (4,4), C1(충전범위)=1, P1=100
AP2 = [7, 10, 3, 40]
AP3 = [6, 3, 2, 70]

'''
1. BC 범위(좌표 지정) // BC 개수 1~8
2. A, B의 T 별 좌표 만들기 // 
    + A 는 1,1 부터   
    + B 는 10,10부터
3. A,B 좌표 순회하면서 BC 범위에 속하는지?? [T,BC1,BC2] 이런식으로 저장.
    + 거리 D = |Xa-Xb| + |Ya-Yb|
4. T 순회하면서 계산
    + BC 겹치는지 확인. -> 
    1) 겹치면 
        + 반띵 or A,B 중 두개에 속하는 친구가 있는지 확인.

'''


# 이동 dir 변환 dict
dir_dict = {
    0:[0,0], 1:[0,-1], 2:[1,0], 3: [0,1], 4:[-1,0]
}

# AP 변환
AP1 = [AP1[1],AP1[0],AP1[2],AP1[3]]
AP2 = [AP2[1],AP2[0],AP2[2],AP2[3]]
AP3 = [AP3[1],AP3[0],AP3[2],AP3[3]]
AP_lst = [AP1,AP2,AP3]
print('ap',AP_lst)

# A,B의 T별 좌표 만들기.
A_pos = [[1,1,0]]
B_pos = [[10,10,0]]
ta,tb=1,1
for dir in A:
    dx,dy = dir_dict[dir][0], dir_dict[dir][1]
    A_pos.append([A_pos[-1][0]+dx,A_pos[-1][1]+dy,ta])
    ta+=1
for dir in B:
    dx,dy = dir_dict[dir][0], dir_dict[dir][1]
    B_pos.append([B_pos[-1][0]+dx,B_pos[-1][1]+dy,tb])
    tb+=1
print(A_pos)
print(B_pos)

# 3. A,B 좌표 순회하면서 BC 범위에 속하는지?? [T,BC1,BC2] 이런식으로 저장.
    #    + 거리 D = |Xa-Xb| + |Ya-Yb|
A_energy=[]
for ap in AP_lst:
    ap_x,ap_y =ap[0],ap[1]
    for ax,ay,ta in A_pos:
        if abs(ax-ap_x) + abs(ay-ap_y) <= ap[2]:
            A_energy.append([ax,ay,ap[3],ta])

print('A energy : ',A_energy)





<<<<<<< HEAD
=======

>>>>>>> fa34ca0088ef9cfbd0ddc6a9d3525c66aed24ddc
