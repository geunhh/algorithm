'''
4
3 7 왼쪽 변과 종이 왼쪽변 사이의 거리, 아래쪽과 아래쪽 사이의 거리.
5 2
15 7
13 14
'''

import sys
sys.stdin = open('paper.txt')
width=10    # 가로세로 10의 사각형
N= int(input())
rects = [list(map(int,input().split())) for _ in range(N)]
# print(rects)

# 도화지 만들기
board = [[0]*100 for _ in range(100)]
# 도화지 색칠하기
for rect in rects:
    for i in range(rect[0],rect[0]+10):
        for j in range(rect[1], rect[1]+10):
            board[i][j] += 1
# 도화지 둘레 확인하기. -> 주변 모든 친구를 확인해요. 꽉차 있다면 면, 아니라면 둘레+1
cnt=0 # 둘레값.
dirs = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(100):
    for j in range(100):
        # i,j의 전 방향을 확인해
        if board[i][j] != 0:
            for dir in dirs:
                di, dj = i+dir[0], j+dir[1]
                # 만약 범위 밖으로 벗어나면 무조건 둘레.
                if di<0 or di >= 100 or dj<0 or dj>= 100 :
                    cnt+=1
                # 범위 안에 있지만 상하좌우에 0이 있으면 그 경계면은 둘레가 됨.
                elif 0<=di<100 and 0<=dj<100 and board[di][dj] == 0:
                    cnt+=1

print(cnt)





