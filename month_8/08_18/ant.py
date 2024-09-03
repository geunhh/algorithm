'''
가로 길이가 w이고 세로 길이가 h인 2차원 격자 공간


'''
import sys
sys.stdin = open('ant.txt')

w,h = map(int, input().split())
start_point = list(map(int, input().split()))   # 시작점
t = int(input())


cur_dir = [1,1]
cur_point = start_point

for _ in range(t):
    # print(cur_point)
    # y축
    if cur_point[0] == w or cur_point[0] == 0 :
        cur_dir[0] *= -1
    if cur_point[1] == h or cur_point[1] == 0 :
        cur_dir[1] *= -1

    cur_point[0] += cur_dir[0]
    cur_point[1] += cur_dir[1]


print(cur_point)
