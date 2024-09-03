
import sys
sys.stdin = open('treasure.txt')
'''
보물상자에는 자물쇠가 걸려있는데, 
이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진 수로 만든 수

lst를 덱으로 받아서 
rotate를 돌리자. 그리고 rotate
'''
from _collections import deque
for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    lst = input()
    hex_set = set()     # 중복되지 않도록 주의하라! 라고 문제에 적혀있어서 set 써서 해결.
    deq = deque(lst)    # rotate 보자마자 생각나서 써봄

    for _ in range(N//4):
        meu = list(deq)                            # 덱은 index slicing이 안되더라구여?
        hex_set.add(''.join(meu[N//4*0 : N//4*1])) # 그래서 잠깐 list로 만들고 슬라이싱해서
        hex_set.add(''.join(meu[N//4*1 : N//4*2])) # hex_set에다가 넣어줬슴다.
        hex_set.add(''.join(meu[N//4*2 : N//4*3]))
        hex_set.add(''.join(meu[N//4*3 : N//4*4]))
        deq.rotate(1)                              # 그리고 한칸 >> 돌려줍니다.

    hex_lst = list(hex_set)     # 만들 수 있는 친구를 내림차순으로 정렬해야하는데요.
                                # set은 순서가 없죠? 리스트로 만들어요.
    result =[]                  # 어 아니네요. 얘가 순서를 고려할 list 입니다.
    for hex in hex_lst:
        result.append(int(hex,16))  # 16진수 10진수로 변환해서 던져요

    # print(result)
    result.sort(reverse=True)       # reverse sort 해서
    print(f'#{tc} {result[K-1]}')   # k번 째 출력


