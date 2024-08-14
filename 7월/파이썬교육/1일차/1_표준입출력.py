
#%%
# 1. 표준 출력
# print()

name = '홍길동'
age = 20
print('내 소개:', name,age) #변수마다 띄어쓰기
print(f'내 소개: {name} {age}') #f-string.
copyy = f'내 소개: {name} {age}'
copyy = f'내 소개: {name} {age}'
print(copyy)
#실행 : ctrl + Enter (단축키)
#실행 후 새로운 블락 생선 : Shift + Enter

# %%

print('hihi',end='')
print('byebye',end='\n\n')
print('내 소개:', name,age,sep="---") #변수마다 띄어쓰기

# %%
# {}-포맷팅
name,age = 'ghh', 29
text = "my name is %s, my age is %d" %(name,age)
text1 = "my name is {}, my age is {}".format(name,age)
print(text1)

# f-포맷팅

text2 = f"my name is {name}, my age is {age}"
print(text2)

# f-포맷팅 장점
# {} 안에 표현식<함수, 연산자, 변수 등의 처리결과>를 넣을 수 있음.
text3 = f"my name is {name+'님'}, my age is {age+5}"
print(text3)
# %%
# 자리수 및 정렬 지정
# 정렬 `>`:오른쪽, `<`:왼쪽, `^``:가운데
text4 = f"my name is {name+'님':^20}, my age is {age+5:>10}"
text5 = f"my name is {name+'님':_^30}, my age is {age+5:a>10}"
print(text4)
print(text5)
# %%
# 소숫점 자리수 지정

float_num = 3.141592
# 최소 10글자, 소숫점 3자리 까지 출력.
print(f'소숫점 자리수 지정{float_num:^10.3f}') 
# %%

text = "my name is {0}{0}{0}, my age is {1}".format(name,age)
print(text)

# %%
# 문자열의 덧셈과 곱셈

fruit1 = '사과'
fruit2 = '포도'
fruit3 = fruit2*5 +' '+ fruit1*2
print(fruit3)
# %%
# 표준 입력
# input()
print("문자열을 입력하세요 > ", end='')
text = input() # 키보드로 부터 입력받아 문자열로 반환
print(text)
# %%
text = input("문자열을 입력하세요 : ")
print(text)
# %%

text = input("정수를 입력하세요 : ")
print(int(text)+33)
# %%

text = input("실수를 입력하세요 : ")
print(float(text)+4)
# 다른 타입끼리 계산이 안 되지만, float + int -> 명시적으로 변경해서 계산.
# %%
# 실습
# 섭씨 온도를 입력받아서 화씨 온도로 출력하는 프로그램
# 화씨 온도 = 섭씨 *1.8 +32
# 소숫점 2째 자리까지만 표시
# 출력 예시 ) 섭씨 온도 26.31은 화씨온도 98.21입니다.

temp = input("섭씨온도를 입력해주세요 : ")
temp = float(temp)
print(f"섭씨온도 {temp}은 화씨온도 {temp*1.8+32:.2f}입니다.")
