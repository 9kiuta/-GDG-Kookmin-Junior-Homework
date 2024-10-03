def generate_hello_world_str():
    name = "김형민"
    return "Hello World "+name # 이름 입력받고 Hello World랑 같이 반환

def print_console():
    print(generate_hello_world_str()) # Hello World `이름` 출력 

if __name__ == "__main__":
    print_console()

# 파이썬이 실행될 때 해당 스크립트가 직접 실행되면 
# 내부적으로 __name__ 변수가 "__main__"으로 설정
# 만약 다른 모듈을 import 하면 __name__변수가 `파일명`으로 설정됨