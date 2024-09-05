T = int(input())
for tc in range(1,T+1):
    N= int(input()) # 비트의 길이
    bits = input()
    max_len = 1
    
    # 각 비트를 순회
    for i in range(N):
        cnt=0   #일치 여부 cnt 개수
        # i 를 중심으로 j번 째 떨어진 bit 일치 여부
        for j in range(1,N):
            if 0<=i-j and i+j <N and bits[i-j] == bit[i+j]:
                cnt+=1
            else:
                break
        max_len = max(max_len, cnt*2+1)
    print(f'#{tc} {max_len}')
        