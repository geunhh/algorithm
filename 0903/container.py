'''
화물이 실려 있는 M대의 트럭
N개의 컨테이너.

트럭당 한 개의 컨테이너
A도시에서 B도시로 최대 M대의 트럭이 편도로 한 번만 운행.
이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출
'''
import sys
sys.stdin = open('container.txt')
from _collections import deque

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    w = list(map(int,input().split())) # 화물의무게 W
    t = list(map(int,input().split())) # 적재 용량  T
    weight = deque(sorted(w))
    truck  = deque(sorted(t))
    # print(weight)
    # print(truck)
    total = 0
    while truck and weight:
        if truck[-1] >= weight[-1]:
            total += weight.pop()
            truck.pop()
        else:
            weight.pop()
    print(f'#{tc} {total}')



