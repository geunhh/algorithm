def order(node):
    global result
    if node == None:        # 다음 노드가 None이면 리턴.
        return

    order(tree[node][0])    # 좌측 자식 노드 호출
    result+=value[node]     # 중위순회하기 때문에 좌측 자식 노드 종료 후 result에 추가
    order(tree[node][1])    # 우측 자식 노드 호출
    return


for tc in range(1, int(input())+1):
    N = int(input())                # 문자열 길이
    word = input()                  # 문자열
    print(f'#{tc}',end ='')        # output.
    for w in word:                  # word내 문자 하나씩 순회

        code = bin(ord(w))[2:]      # 유효한 코드만 남김.
        if len(code) ==6:
            code='0'+code

        value =[0] * (len(code)+1)  # code의 길이만큼만 value list 생성.

        # 1. 트리 만들기
        tree = [[None,None] for _ in range(len(code)+1)] # default로 None,None을 가지는 tree 생성.

        # 1-1 root에 인접 노드와 value먼저 넣고
        tree[1] = [2,3]
        value[1] = code[0]

        # 1-2 나머지 처리
        for index, c in enumerate(code[1:]):
            ind = index+2               # 자식 노드가 기준이기 때문에 index+2
            if tree[ind//2][0] == None: # 부모노드 = 자식노드 // 2
                tree[ind//2][0] = ind   # 인접 노드 넣어줌
            else:
                tree[ind//2][1] = ind
            value[ind] = c              # value값도 넣어줌.

        # 2 호출
        result =''                      # 결과값을 저장.
        order(1)                        # 호출
        print(f' {result}',end='')
    print()



