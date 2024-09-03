import sys
sys.stdin= open('4.txt')
from collections import defaultdict

def order(node):
    global cnt
    if node > N :
        return
    order(node*2)
    cnt += 1
    value[node] = cnt
    order(node*2+1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0

    # 순회하면서 값을 할당할 딕셔너리
    value = defaultdict(int)

    # 중위 순회 시작
    order(1)

    # 결과 출력
    print(f'#{tc} {value[1]} {value[N // 2]}')