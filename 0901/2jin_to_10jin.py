
import sys
sys.stdin = open('8.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    print(f'#{tc}',end='')
    input_all=''
    for _ in range(N):
        input_all += input().strip()
    # print(input_all)
    for i in range(0, len(input_all),7):
        print(f'',int(input_all[i:i+7],2),end='')
    print()



