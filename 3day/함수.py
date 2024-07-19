#%%
# 독스트링 호출
print(help(int))
#%%
# list 타입에서 사용 가능한 메서드 및 변수 목록
print(dir(list))

# %%
# 타입 체크
# isinstance()

print(isinstance(10, float))
print(isinstance(10, int))
# %%
# 재귀함수
# 1) 리스트의 요소를 모두 더하는 함수

def sum_list(nums):
    # list 요소가 비어있는 경우
    if len(nums)==0:
        return 0
    # 이렇게도 할 수 있음. (위와 동)
    if not nums:
        return 0

    return nums[0] +sum_list(nums[1:])

nums = [1,2,3,4,5,6]
sum_list(nums)
# %%
nums = [1,2,3,4,5]

print(nums[0:10]) # python은 slicing의 경우 인덱스 범위를 벗어나도 최대한 가져온다
print(nums[8])    # 그러나 인덱스를 벗어나고, slicing이 아닌 경우 error
# %%
def sum_list(nums,idx):
    if idx >= len(nums):
        return 0
    return nums[idx] + sum_list(nums, idx+1)
    # 위의 코드와 같은 기능을 하지만, list 재할당이 없이 인덱스만 참조하기 때문에 시간적으로 매우 효율적
nums = [1,2,3,4,5]
sum_list(nums, 0)
# %%
# 2) 재귀함수를 이용해서 문자열 뒤집어서 출력
#"hello" => "olleh"

def olleh(str_hi):
    i = len(str_hi)
    str_olleh =''
    str_olleh = str_hi[0] + olleh(str_hi[1:])
    if len(str_hi) >= len(str_hi):
        return str_olleh   


olleh('hello')
# %%
#"hello" => "olleh"
# 함수(알고리즘) 설계
# 입력 : 문자열
# 출력 : 문자열
# 문제풀이 : 재귀함수 이용
#           문자열 더하기 활용
#+ recur(다음 문자 인덱스) + 현재 문자
#+ 종료 조건 : 인덱스 문자열 길이보다 같거나 클때

def reverse_string(s, idx):

    if idx >= len(s):
        return ""

    return reverse_string(s, idx+1) + s[idx]

reverse_string("hello", 0)

# %%
# 람다 활용

radius = [1,2,5,4,3] # 반지름 리스트
print(sorted(radius))
print(sorted(radius, reverse=True))

# 원의 넓이 순으로 정렬
print(sorted(radius, key = lambda r:r**2*3.14))

# 사각형 예제
rects = [(1,2),(3,3),(1,17),(10,9)] # 가로 세로
print(sorted(rects)) #가로 길이 순으로 오름차순
print(sorted(rects, key=lambda rect:rect[1])) # 세로 길이 순으로 오름차순 정렬.
print(sorted(rects, key=lambda rect:rect[0]*rect[1])) # 사각형 넓이 순
print()
# 정렬 조건 세분화
# 정렬 값이 동일한 경우 그 다음 정렬 조건으로 정렬
# ex) 가로 길이 순으로 오름차순 정렬 -> 가로 길이가 동일하면 세로 길이 내림차순 정렬
print(sorted(rects, key=lambda rect:-rect[0])) 
print(sorted(rects, key=lambda rect:-rect[1])) 
print(sorted(rects, key=lambda rect:(rect[0],-rect[1])))
# %%
# map : iterable(리스트)한 객체를 통해 새로운 iterable(리스트)를 만들 때.

names = ['홍길동','임꺽정','김현수']
ages= [20,30,40]
no =0
# 딕셔너리 형태로 바꿔서 리스트로 저장.
def create_user(name,age):
    global no
    no +=1
    return {        
        '번호' : no,
        '이름':name,
        '나이':age
    }

members = list(map(create_user, names, ages))
print(members)

# %%
# filter : 값은 변경하지 않고, 원하는 요소만 가져오고 싶은 경우.

print(list(filter(lambda m:m['나이']>20, members)))

radius = [1,2,5,3,2,7]
#원의 넓이가 10 이상인 반지름의 리스트만 얻기
print(list(filter( lambda r:(r**2)*3.1415 > 10, radius)))