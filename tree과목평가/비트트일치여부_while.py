T = int(input())
for tc in range(1,T+1):
    N= int(input()) # 비트의 길이
    bits = input()
    max_len = 1
    
    # 각 비트를 순회
    for center in range(N):
        left = center - 1
        right = center + 1
        cur_len = 1
        while left >=0 and right < N and bits[left] == bits[right]:
            left-=1
            right+=1
            cur_len+=2
        max_len = max(max_len, cur_len)
    print(f'#{tc} {max_len}')
        