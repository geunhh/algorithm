# CLI (Command Line Inteface)
+ 터미널을 통해 사용자가 컴퓨터와 상호작용

## 경로
1. 루트 디렉터리(/)
  + 모든 파일과 폴더를 담고 있는 최상위 폴더
  + 윈도우의 경우 보통 `C드라이브`
2. 홈 디렉터리 (`~`)
  + 현재 로그인 된 사용자의 홈 폴더
  + 윈도우 : `C:/사용자(Users)/현재 사용자 계정`
  + MAC : `Users/현재 사용자 계정`
3. 절대 경로 : 루트 디렉터리로부터 목적 지점까지의 경로
  + ex) `C:/Users/사용자계정/Desktop`
4. 상대 경로 : 현재 작업하고 있는 디렉터리 기준으로 계산된 경로
  + `./` : 현재 작업하고 있는 폴더
  + `../` : 현재 작업하고 있는 폴더의 부모폴더
  + ex) `./SSAFY` : (현재 작업 폴더에 있는 SSAFY 폴더)

---
C:\Users\SSAFY\Desktop\스타트캠프실습\gpt-chatbot-program-problem\gpt-program-problem\index.html
+ 요건 절대 경로

gpt-chatbot-program-problem\gpt-program-problem\index.html
+ 상대경로(Relative Path) : 최상위 폴더 기준의 '상대경로'이다.
---

## 터미널 명령
1. touch : 파일 생성
  + 띄워쓰기로 구분하여 여러 파일 한꺼번에 생성 가능
  + 숨김 파일을 만들기 위해서는 `.`을 파일명 앞에 붙입니다.

```bash
touch text.txt
```

2. mkdir : 폴더 생성
  + 띄어쓰기 구분해서 여러 폴더를 한꺼번에 생성 가능
  + 폴더 이름에 공백을 넣고 싶은 경우 따옴표로 묶어서 입력
  + 

```bash
mkdir myFolder
mkdir 'ssafy start'
```

3. ls : 현재 디렉터리의 폴더 및 파일 목록 보여줌
  + `-a` : all 옵션. 숨김 파일까지 모두 보여줍니다.
  + `-l` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여줍니다.

```bash
#기본 사용
ls

#all 옵션
ls -a

#all과 long 옵션 함께 사용
ls -a -l

# 여러 옵션 축약
ls -al
```

4. mv 
  + 폴더 또는 파일을 다른 폴더로 이동할 때 사용
  + 폴더 및 파일 이름을 변경할 때 사용
  
```bash
# text.txt를 myFolder로 이동
mv text.txt myFolder

# myFolder를 testFolder로 이름 변경
mv myFolder testFolder
```

5. rm : 폴더 또는 파일 삭제
  + 휴지통 이동 없이 완전 삭제
  + `*`를 사용해서 `rm *.txt`입력 시 txt 파일 전체 삭제   
  + 와일드 카드 
    + `*` : 0개 이상의 문자를 대체할 수 있습니다.
    + `?` : 임의의 한 문자
    + `[abcd가` : 괄호 안의 문자 중 하나와 일치할 경우 
      + [abcd가].txt -> a.txt, b.txt, c.txt, d.txt, 가.txt 만 삭제

  + `-r` : 폴더 삭제 옵션

```bash
rm -r testFolder
```

6. start, open : 파일 또는 폴더 열기
+ `window`에서 start, `Mac` 에서 open

```bash
start test.txt
```

7. cd : 현재 작업 중인 디렉터리 변경
  + `cd ~` : 홈 디렉터리로 이동
  + `cd ..` : 부모 디렉터리로 이동
  + `cd -` : 이동 전 디렉터리로 이동 (뒤로가기)

```bash
cd testFolder
```

## bash의 유용한 단축키
+ `위, 아래 방향키` : 과거에 작성했던 명령어 조회
+ `tab` : 폴더 및 파일 이름 자동 완성
+ `ctrl + a` : 커서가 맨 앞으로 이동
+ `ctrl + e` : 커서가 맨 뒤로 이동
+ `ctrl + w` : 커서 앞 단어 삭제
+ `ctrl + l` : 터미널 화면 청소
+ `ctrl + insert` : 복사
+ `shift + insert` : 붙여넣기

 