import sys
sys.stdin = open('suyeol.txt')

N=int(input())
lst = list(map(int,input().split()))
print(lst)
inc_cnt=1
dec_cnt=1
max_cnt=1
for num in lst:
    if up :
        if num >= prev_num:
            cnt+=1
            prev_num = num
            up=True
    else:
        if cnt > max_cnt:
            max_cnt=cnt
        prev_num = num
        cnt=0
print(max_cnt)