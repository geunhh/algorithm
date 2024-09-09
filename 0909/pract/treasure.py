import sys
sys.stdin = open('treasure.txt')
# 답 : K번째로 큰 수를 10진수로 만든 수.
# 1. 서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다.
#    크기 순서를 셀 때 중복을 주의하라. -> set에 넣자.
# N은 4의 배수, 8이상 28이하. 2*4, 3*4,4*4,5*4,6*4,7*4
# 숫자는 0~F

# 회전 : rotate -> deque
# 결과 : list(set) -> sort

# N을 4로 나눈만큼만 rotate 해주면 되네요.
from collections import deque

def find_value():
    for j in range(0, N, N//4):
        word=''
        for k in range(j,j+N//4):
            word += deq[k]
        result.add(int(word,16))

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    deq = deque()
    lst = input()
    # 1. 입력 받아오기.
    for i in range(N):
        deq.append(lst[i])
    result = set()

    # rotate하면서 값 찾기.
    for _ in range(N//4):
        find_value()        # 찾고
        deq.rotate()        # rotate

    result = list(result)
    result.sort(reverse=True)
    print(f'#{tc} {result[K-1]}')



