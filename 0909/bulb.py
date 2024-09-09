import sys
sys.stdin = open('bulb.txt')

solution=[]
for tc in range(1,int(input())+1):

    x1, y1, x2, y2 = map(int, input().split())

    start = max(x1,x2)
    end = min(y1,y2)

    result = end - start
    if result <= 0 :
        result = 0
    solution.append(result)

for i, sol in enumerate(solution):
    print(f'#{i+1} {sol}')

# 입출력 시간도 오래걸림. testcase가 굉장히 많은 경우, 입력과 출력이 번갈아가며
# 하는 것이 굉장히 비효율적.
# 출력이 많으면 몰아서 하자.