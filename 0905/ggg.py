import sys
sys.stdin = open('bus.txt')

def get_mincnt(idx,arr:list,cnt):
    global min_val
    # 가지치기
    if cnt >= min_val:
        return
    if idx >= N-1:
        if min_val > cnt:
            min_val = cnt
        return


    # 못 가는 경우

    # 종료 조건

    for i in range(arr[idx],0,-1):
        get_mincnt(idx+i,arr,cnt+1)

T = int(input())
for tc in range(1,1+T):
    check = list(map(int,input().split()))
    N, *arr = check
    min_val = float('inf')

    get_mincnt(0, arr, 0)
    print(min_val)