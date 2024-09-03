import sys
sys.stdin = open('pole.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    lst=[]
    for _ in range(N):
        lst.append(list(map(int,input().split())))
    # print(lst)
    matrix=[[0] *N for _ in range(N)]
    # print(matrix)

    for i in range(N):
        for j in range(N):
            if i!=j:
                if (lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]) or (lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]):
                    matrix[i][j] = 1
    cnt=0
    for i in range(N):
        for j in range(i,N):
            # print(i,j)
            if matrix[i][j] == 1:
                cnt+=1
    print(f'#{tc} {cnt}')


