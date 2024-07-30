#%%
# 조건문
# month에 따라 계절 출력.
# 겨울 : 12~2
# 봄   : 3~5
# 여름 : 6~8
# 가을 : 9~11

month = 7
if month <=2 or month==12:
    season = '겨울'
elif month <=5 and month >=3:
    season = '봄'
elif 6<= month <=8:
    season = '여름'
elif month in [9,10,11]:
    season = '가을'
else:
    print('error')
print(month, season)
# %%
# 특정 범위의 값을 미리 정의된 카테고리로 매핑할 때
# 조건문을 대체할 수 있음.
# 코드도 간결해지고, 실행 속도도 빠름.
seasons = ['겨울']*2 + ['봄']*3 + ['여름']*3 +['가을']*3 + ['겨울']
print(f"{month}월의 계절은 {seasons[month-1]}입니다.")
# %%
# 학점 출력
# 90점 이상 : A
# 80점 이상 : B
# 70점 이상 : C
# 60점 이상 : D
# 50점 이상 : F

score = ['X']*5 + ['F'] + ['D'] + ['C']+['B']+['A']*2
score_c = 105
print(score)

print(f"{score_c}의 학점은 {score[score_c//10]}")
# %%
score = 77
check = ['F','D','C','B','A']
print(f'{score} 점수는 학점 {check[min(4, score//10-5)]}')
print(f'{score} 점수는 학점 {check[min(4, int((score//50.000000001/1/0)))]}')
# %%
humid_level = ['건조','적정','습함','매우 습함']
# 0~25 건조 -> 인덱스 0
# 25~50 건조 -> 인덱스 1
# 50~75 건조 -> 인덱스 2
# 75~100 건조 -> 인덱스 3

humidity = 75
level_index = humidity//25
print(f"습도 {humidity}% : {humid_level[level_index]}")
# %%
# 혈압
# 90 mmHg 미만   : 저혈압
# 90-110  미만   : 정상
# 110 -130  미만 : 주의
# 130-150  미만  : 높음
# 150 이상       : 위험

catergoires = ['저혈압','정상','주의','높음','위험']

bp = 150
level_index= max(0, min(4,(bp - 70)//20))

print(f"내 혈압 {bp} : {catergoires[level_index]}")
# %%
# 00:00:00 ~ 23:59:59 초 사이의
# 7이 몇번 출력되는지 개수를 구하시오.
"12:16:44".count('4')
num=0
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f"{i}:{j}:{k}")
            if ('7' in str(i)) or ('7' in str(j)) or ('7' in str(k)):                
                num+=1

print(num)
# %%
num=0
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f"{i}:{j}:{k}")
            time = f"{i}:{j}:{k}"
            if time.count('7'):                
                num+=1
print(num)
# %%
def count_sevens(hour=0,min=0,sec=0):
    time = f"{hour}:{min}:{sec}"
    cnt = time.count('0')
    sec+=1
    if sec>=60:
        sec =0
        min+=1
        if min >= 60:
            min=0
            hour+=1
    if hour<24:
        return cnt + count_sevens(hour,min,sec)
    else : 
        return cnt
    
print(count_sevens())
# 재귀함수는 너무 많이 호출되면 함수가 작동을 하지 않음.
# 숫자를 줄이면 가능

# %%
# 재귀함수 최대 호출 횟수 지정
import sys.setrecursionlimit(10000)
# %%
# 삼항 연산자 조건문
# 변수 = 참값 if 조건식 else 거짓인 경우 값.
# 1) 숫자의 짝수, 홀수 판별해서 타입을 얻음.
num = 5


num_type = "짝수" if num%2 ==0 else "홀수"
# 위 아래 같음.
def even_odd(num):
    if num%2==0:
        num_type = "짝수"
    else :
        num_type = "홀수"
    return num_type
# list 컴프리헨션
nums = list(range(10))
nums = ['짝수' if n%2==0 else"홀수" for n in nums]
print(nums)


print(num_type)
print(even_odd(6))
# %%

nums = list(range(10))
nums = ['짝수' if n%2==0 else"홀수" for n in nums]
print(nums)


nums = list(range(10))
nums = ['짝수' if n%2==0 else"홀수" for n in nums if n>=5] 
# 컴프리헨션 뒤쪽 if는 Filter 역할.
# 앞쪽 if는 값을 바꿀 조건.
print(nums)