## CLIENT ##

import socket
from _thread import *

HOST = '192.168.212.40' ## server에 출력되는 ip를 입력해주세요 ##
PORT = 9999 #서버의 port번호
NAME = 'Geunhh' #클라이언트 이름
MAX_LEN = 1024 #입력 받을 최대 길이(byte)

client_socket = socket.py(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
client_socket.connect((HOST, PORT)) #서버에 연결

#서버로부터 받은 데이터 출력
def recv_data(client_socket):
    while True:
        data = client_socket.recv(MAX_LEN)
        print(data.decode('utf-8'))

start_new_thread(recv_data, (client_socket,))
print(f'>> 서버에 연결 IP:{HOST}, PORT:{PORT}')

#서버로 데이터 전송
while True:
    inStr = input()
    message = f'[{NAME}]\\'+inStr
    if inStr == 'quit': 
        close_data = message
        break

    client_socket.send(message.encode('utf-8'))

client_socket.close()
