import sys
sys.stdin=open('flog.txt')

def jump(K):
    index=0
    total=0
    back=0
    cnt=1

    index =lst[index]
    print('#0',index)

    while cnt < K:
        # 이전 점프에 후진했다면,
        if back != 0:
            index = index+lst[index]+abs(back)    # 후진한만큼을 index에 더해주고
            back = 0          # back을 다시 0으로 만듬
        else:
            index = index + lst[index] # 아니라면, 현재 위치에서 해당 num만큼을 index에 더해줌.
        print(f'#{cnt} {index}')

        if index < 0 or index >=N:
            break

        total += lst[index]
        cnt+=1

        # 새로운 인덱스의 값이 음수(후진)면 back에 저장해줌.
        if lst[index] < 0:
            back = lst[index]

    return total



for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    lst = list(map(int, input().split()))

    print(lst)
    result = jump(K)
    print(result)

    break