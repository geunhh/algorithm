'''
[1, 1, 1, 1, 1]
[4, 1, 2, 1]
'''
def sol(numbers, target):
    if len(numbers) == 0:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return sol(numbers[1:], target - numbers[0]) + sol(numbers[1:], target + numbers[0])

def sol2(depth, target):
    if depth == len(numbers):
        if target == 0:
            return 1
        else :
            return 0
    else :
        return sol2(depth+1,target - numbers[depth]) + sol2(depth+1, target + numbers[depth])

if __name__ == '__main__':
    numbers = [4, 1, 2, 1]    # 숫자로 구성된 리스트가 문자열로 입력
    target = 4           # 타겟 숫자 입력
    print(target)
    print(numbers)

    result = sol(numbers, target)
    result2 = sol2(0, target)
    print(result)
    print(result2)


