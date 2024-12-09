import socket

HOST = '127.0.0.1'  # Локальный адрес (localhost)
PORT = 65432  # Порт для прослушивания


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Сервер слушает на {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Подключено к {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Получено от {addr}: {data.decode()}")
                    conn.sendall(data)


if __name__ == "__main__":
    start_server()
