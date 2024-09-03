import sys
sys.stdin = open('ant.txt')

w,h = map(int, input().split())
p,q = map(int, input().split())   # 시작점
t = int(input())

a = (p+t)//w
b = (q+t)//h

if a % 2 == 0:
    x = (p+t)%w # 처음 위치에서 시간만큼 이동하고, 총 길이에서 나머지
else :
    x = w - (p+t)%w

if b%2 == 0 :
    y = (q+t)%h
else :
    y = h - (q+t)%h
print(x,y)
