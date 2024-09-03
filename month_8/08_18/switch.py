import sys
sys.stdin = open('switch.txt')
'''
켜져있음 1
꺼져있음 0
남자 1
- 스위치 번호가 자기가 받은 수의 배수이면, 그 수위치 상태를 바꿈
- 3이면 3,6,9... 번호 바꿈.
여자 2
- 받은 수의 번호 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아 전체 바꿈.
- N//2 만큼하면 될듯.
'''
def male(num,N):
    for i in range(N):
        if (i+1)%num==0 :
            switch[i] = 1- switch[i]

def female(num,N):
    switch[num] = 1 - switch[num]
    # 좌우 살펴
    j = 1
    while num - j >= 0 and num+j <N:
        if switch[num+j] != switch[num-j] :
            break
        else:
            switch[num-j]  = 1-switch[num-j]
            switch[num+j]  = 1-switch[num+j]
            j+=1

N = int(input())
switch = list(map(int,input().split()))

for _ in range(int(input())):
    sex, num = map(int, input().split())
    # 남자면
    if sex ==1:
        male(num,N)
    else:
        female(num-1,N)

for i in range(len(switch)):
    if i != 0 and i % 20 == 0:
        print()
    print(f'{switch[i]}',end=' ')

# for i in range(1, (N-num)//2):
    #     if switch[num-i] == switch[num+i] and switch[num-i]==1:
    #         switch[num-i], switch[num+i] = 0,0
    #     elif switch[num-i] == switch[num+i] and switch[num-i]==0:
    #         switch[num-i], switch[num+i] = 1,1
    #     else :
    #         break