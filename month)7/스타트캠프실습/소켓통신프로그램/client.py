import socket

HOST = '192.168.212.40'  # 호스트
PORT = 1111        # 포트

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(client_socket.recv(1024).decode('utf-8'))
        while True:
            ##코드 수정 부분##
            guess = input("Guess the number > ")
            client_socket.send(guess.encode('utf-8'))
            ##------------##
            
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            if "정답" in data:
                client_socket.send("종료".encode('utf-8'))
                break

if __name__ == "__main__":
    main()
