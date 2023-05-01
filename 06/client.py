import socket
import threading
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thread", type=int, default=5, help="Count th")
parser.add_argument(
    "urls_file",
    type=str,
    nargs="?",
    default="urls.txt",
    help="Path to urls",
)
args = parser.parse_args()
COUNT_THREADS = args.thread
COUNT_RES = 0


def create_threads(data):
    data = data.strip().split(",")
    count_url = (len(data) + COUNT_THREADS - 1) // COUNT_THREADS
    threads = [
        threading.Thread(
            target=send_data,
            name=f"thread_{i}",
            args=(data[i * count_url: count_url * (i + 1)],),
        )
        for i in range(COUNT_THREADS)
        if len(data[i * count_url: count_url * (i + 1)])
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def send_data(data):
    global COUNT_RES
    host = "localhost"
    port = 1489
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(bytes(",".join(data).encode()))
    while True:
        response = client_socket.recv(1024)
        if not response:
            break
        else:
            try:
                res = response.decode()
                COUNT_RES += 1
                print(f"CLIENT OUTPUT: {res}")
            except Exception as e:
                print(e)
    print(f"CLIENT OUTPUT: {COUNT_RES}")
    client_socket.close()


def run_client(file):
    with open(file, "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    create_threads(run_client(args.urls_file))
