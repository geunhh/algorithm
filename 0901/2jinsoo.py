import sys
sys.stdin= open('9.txt')

for tc in range(1,int(input())+1):
    N, hex = input().split()
    result=''
    for hexa in hex:
        hexa = format(int(hexa,16),'b')
        while len(hexa) <4:
            hexa = '0'+hexa
        result+=hexa
    print(f"#{tc} {result}")

