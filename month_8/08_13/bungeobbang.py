from collections import deque
import sys
sys.stdin = open('bbung.txt', 'r')

def bbung(M,K,cnt):
    for i in range(max(lst)+1):   # 손님이 오는 시간의 가장 늦은 시간까지 돌림

        if i/M >0 and i%M ==0:
            for _ in range(K):  # k개 만큼 목록에 추가
                cnt.append(1)

        if i in lst:
            for _ in range(lst.count(i)):
                try:
                    cnt.pop()
                except IndexError:
                    return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1,1+T):
    N, M, K = map(int,input().split())
    # 손님수, M초 -> K개
    lst = list(map(int, input().split()))
    # print(N,M,K)
    cnt = deque()
    # print(cnt)
    # print(max(lst))

    result = bbung(M,K,cnt)
    print(f'#{tc} {result}')




