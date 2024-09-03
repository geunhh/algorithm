import sys
sys.stdin= open('3.txt')
from _collections import defaultdict

def insert(node):
    global cnt
    if node == None:                # 난 항상 이 조건이 까다롭다.
        return

    insert(tree[node][0])

    # 삽입.
    value[node] = cnt
    cnt+=1                          # 카운트 +1

    insert(tree[node][1])

for tc in range(1, int(input())+1):
    N= int(input())
    tree = defaultdict(lambda : [None,None])
    cnt=1

    '''
    부모 *2, 부모*2+1 = 자식,자식
    '''
    ### 1. tree 구성
    # root(=1)는 먼저 처리해줄게
    tree[1] = [2,3]
    # print(tree)

    value = [0]*(N+1) # value값은 따로 저장

    for i in range(2,N+1):              # 루트 제외하고 2부터 N까지 차례로 채워줬어.
                                        # i는 자식의 index로 설계함
        if tree[i//2] == [None,None]:
            tree[i//2][0] = i
        else:
            tree[i//2][1] = i

    print(tree)
    insert(1)
    print(value)

    print(f'#{tc} {value[1]} {value[N//2]}')


