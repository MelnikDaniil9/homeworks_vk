import socket
import threading

COUNT_TH = 5
c_res = 0


def thread(data):
    data = data.strip().split(",")
    count_url = (len(data) + COUNT_TH - 1) // COUNT_TH
    threads = [
        threading.Thread(
            target=send_data,
            name=f"thread_{i}",
            args=(
                data[i * count_url: count_url * (i + 1)],
            ),
        )
        for i in range(COUNT_TH)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def send_data(data):
    global c_res
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
                c_res += 1
                print(res)
            except Exception as e:
                print(e)
    print(c_res)
    client_socket.close()


def run_client(file):
    with open(file, "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    thread(run_client("urls.txt"))
