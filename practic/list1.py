



import sys
sys.stdin = open('list.txt')

for tc in range(1,11):
    N=int(input())
    lst = list(map(int,input().split()))
    # print(lst)
    count=0
    for i in range(2,N-2):
        if lst[i] >lst[i-1] and lst[i]>lst[i-2] and lst[i]>lst[i+1] and lst[i]>lst[i+2]:
            lst_max = max(lst[i-1],lst[i-2],lst[i+1],lst[i+2])
            # print(lst[i],lst_max)
            count += (lst[i]-lst_max)
    print(f'#{tc} {count}')

