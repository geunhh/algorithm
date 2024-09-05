T = int(input())
for tc in range(1,T+1):
    N= int(input()) # 비트의 길이
    bits = int(input(),2)
    max_len = 1
    
    # 각 비트를 순회
    for center in range(N):
        left = center - 1
        right = center + 1
        cur_len = 1
        while left >=0 and right < N :
            # 왼쪽 비트와 오른쪽 비트를 추출해서 XOR 연산으로 같은지 비교
            # XOR : 같으면 F, 다르면 T
            # 다른 경우 Break
            if ((bits >> left) & 1) ^ ((bits >> right) & 1) :
                break
            left-=1
            right+=1
            cur_len+=2
        max_len = max(max_len, cur_len)
    print(f'#{tc} {max_len}')
        