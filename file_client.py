import socket

HOST = '127.0.0.1'
PORT = 65432
FILE_PATH = 'sample.txt'  # Файл для отправки

def send_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        with open(FILE_PATH, 'rb') as f:
            client_socket.sendfile(f)
        print(f"Файл {FILE_PATH} отправлен на сервер")

if __name__ == "__main__":
    send_file()
