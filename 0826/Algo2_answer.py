from itertools import permutations
for tc in range(1,int(input())+1):
    N= int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_val = float('inf')
    aliens = [i for i in range(N)]
    #import 쓸 수 있으면
    # aliens = list(permutations(aliens))

    for path in aliens:
        # 해당 줄 서기에 대한 위험도 값 얻기
        cur_val = sum(matrix[path[i]][path[i+1]] for i in range(N-1))
        min_val = min(min_val, cur_val)

    print(f'#{tc} {min_val}')