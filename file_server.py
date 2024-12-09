import socket

HOST = '127.0.0.1'
PORT = 65432
SAVE_PATH = 'received_file.txt'  # Файл, в который будут сохраняться данные


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Сервер слушает на {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Подключено к {addr}")
            with open(SAVE_PATH, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"Файл сохранён как {SAVE_PATH}")


if __name__ == "__main__":
    start_server()
