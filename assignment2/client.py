from socket import *
import json

def create_list(): # 클라이언트에서 전송할 리스트를 생성하는 함수
    name = "김형민"
    major = "소프트웨어학부"
    student_number = "20243047"
    return [name, major, student_number]


if __name__ == "__main__":
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    
    # json 형식으로 바꿔서 server_socket에 리스트 전송
    client_list = create_list()
    client_socket.sendall(json.dumps(client_list).encode("utf-8"))
    print("Send", client_list)


    # 소켓을 닫아야 누수가 생기지 않는다
    client_socket.close()


    