import socket
import random
from _thread import *

HOST = '192.168.212.40'  # 호스트
PORT = 1111        # 포트
success_num = 0
MAX_NUM = 100000000 #1억
answer = random.randint(1, MAX_NUM)

def handle_client(client_socket, answer):
    global success_num
    
    client_socket.sendall("Welcome to Up & Down game!".encode('utf-8'))
    while True:
        # client_socket.sendall("Guess the number: ".encode('utf-8'))
        guess = client_socket.recv(1024).decode('utf-8').strip().strip()
        try :
            guess = int(guess)
            if guess == answer:
                success_num += 1
                client_socket.sendall(f"{success_num}번째 정답!".encode('utf-8'))
                print(f"{success_num}번째 정답!")
            elif guess < answer:
                client_socket.sendall("UP~! 다시 입력하세요.".encode('utf-8'))
            elif guess > answer :
                client_socket.sendall("Down~! 다시 입력하세요.".encode('utf-8'))
        except :
            if '종료' in guess :
                break
        

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server started, listening on port", PORT)
        while True:
            client_socket, _ = server_socket.accept()
            print("Client connected")
            
            start_new_thread(handle_client, (client_socket, answer))
       
if __name__ == "__main__":
    main()