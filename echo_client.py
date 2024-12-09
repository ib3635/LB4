import socket

HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Порт, на котором работает сервер

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        message = input("Введите сообщение для отправки на сервер: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Ответ от сервера: {data.decode()}")

if __name__ == "__main__":
    start_client()
