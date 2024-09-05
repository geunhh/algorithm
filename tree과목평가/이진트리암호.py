


def inorder(node):
    global inorder_expr
    if node > 7:
        return
    
    inorder(2*node) # 왼쪽
    inorder_expr+=tree[node]
    inorder(2*node+1) # 오른쪽
    

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    text = input()
    
    result=[]
    # 텍스트 한 글자씩 순회하면서 아스키코드로 변환 후 tree에 7비트 저장.
    for ch in text:
        asc = ord(ch)
        tree = [0] * 8
        bits = bin(asc)[2:].zfill(7)       # zfill : 빈 문자열 채우는 함수..
            # bits = '0'*(7-len(bin(asc)[2:])) + bin(asc)[2:]
            # bits = format(asc, '07b')
            # bits = f'{asc:0>7}'
        # 얘는 비트 연산으로 진행.
        for i  in range(1,8) :
            if asc & (1<<7-i) :
                tree[i] = 1
            else:
                tree[i] = 0
                
                
                    
            
            
        for i, n in enumerate(bits, start=1):
            tree[i] = n
            
        # 중위 순회까지~~
        inorder_expr = ""
        inorder(1)
        result.append(inorder_expr)
    print(f'#{tc}', *result)
        
        