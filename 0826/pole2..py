import sys
sys.stdin = open('pole.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    # print(ab)
    ab.sort() # 정렬해서 좌측 애들을 정렬해줌.
    # print(ab)
    cnt = 0  # 교차 수
    for i in range(1, N):   # 0층은 넘김
        for j in range(i):  # 나보다 있는 애들 중에
            if ab[j][1] > ab[i][1]:  # a가 더 아래있지만 b가 더 높으면 교차점
                cnt += 1

    print(f'#{tc} {cnt}')