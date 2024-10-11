from socket import *
import json

def list_to_dict(client_list): # 클라이언트로부터 받은 리스트를 딕셔너리로 변환하는 함수
    keys = ["이름", "학과", "학번"]
    return dict(zip(keys ,client_list))

if __name__ == "__main__":
    host = ""
    port = 8080

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(1) 

    # server_socket과 client_socket 연결
    # 내 경우 addr = (localhost(127.0.0.1), 8080)
    conn, addr = server_socket.accept() 

    # json 데이터를 python 형식의 리스트로 변환
    data_list = json.loads(conn.recv(1024).decode("utf-8"))

    # 리스트를 딕셔너리로 변환해서 출력
    print("Recv", list_to_dict(data_list))

    # 연결 종료
    conn.close()

